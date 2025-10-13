
import tkinter as tk#as tk demek tkinter kütüphanesini tk olarak kullan demek silersen tkinter kütüphanesini tkinter olarak kullanır
from tkinter import messagebox
import os, base64, hashlib, hmac, secrets, re

FOLDER = "secret notes"

def sanitize_filename(title: str) -> str:
    name = re.sub(r'[\\/:*?"<>|]+', "_", title).strip().rstrip(".")
    return name or "untitled"

def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000, dklen=32)

def xor_keystream(data: bytes, key: bytes, nonce: bytes) -> bytes:
    out = bytearray()
    block_idx = 0
    i = 0
    while i < len(data):
        counter = block_idx.to_bytes(8, "big")
        stream_block = hmac.new(key, nonce + counter, hashlib.sha256).digest()
        take = min(len(data) - i, len(stream_block))
        for j in range(take):
            out.append(data[i + j] ^ stream_block[j])
        i += take
        block_idx += 1
    return bytes(out)

def encrypt_text(plain: str, password: str):
    salt = secrets.token_bytes(16)
    nonce = secrets.token_bytes(16)
    key = derive_key(password, salt)
    cipher = xor_keystream(plain.encode("utf-8"), key, nonce)
    return (
        base64.b64encode(salt).decode(),
        base64.b64encode(nonce).decode(),
        base64.b64encode(cipher).decode(),
    )

def decrypt_text(salt_b64: str, nonce_b64: str, data_b64: str, password: str) -> str:
    salt = base64.b64decode(salt_b64)
    nonce = base64.b64decode(nonce_b64)
    cipher = base64.b64decode(data_b64)
    key = derive_key(password, salt)
    plain = xor_keystream(cipher, key, nonce)
    return plain.decode("utf-8")

def parse_encrypted_blob(blob: str):
    lines = [ln.strip() for ln in blob.splitlines() if ln.strip()]
    if not lines:
        raise ValueError("Şifreli veri boş.")
    if len(lines) >= 3 and "|" in lines[-2]:
        salt_b64, nonce_b64 = lines[-2].split("|", 1)
        return salt_b64, nonce_b64, lines[-1]
    if len(lines) == 2 and "|" in lines[0]:
        salt_b64, nonce_b64 = lines[0].split("|", 1)
        return salt_b64, nonce_b64, lines[1]
    if len(lines) == 1 and lines[0].count("|") == 2:
        return lines[0].split("|", 2)
    raise ValueError("Biçim hatalı. 'salt|nonce|data' ya da 3 satırlı biçimi girin.")

def save_and_encrypt():
    title = entry_title.get().strip()
    content = text_content.get("1.0", "end-1c")
    password = entry_pass.get()
    if not title:
        messagebox.showwarning("Uyarı", "Başlık girin.")
        return
    if not content:
        messagebox.showwarning("Uyarı", "İçerik girin.")
        return
    if not password:
        messagebox.showwarning("Uyarı", "Şifre girin.")
        return
    try:
        salt_b64, nonce_b64, data_b64 = encrypt_text(content, password)
        os.makedirs(FOLDER, exist_ok=True)
        path = os.path.join(FOLDER, sanitize_filename(title) + ".txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(title + "\n")
            f.write(f"{salt_b64}|{nonce_b64}\n")
            f.write(data_b64 + "\n")
        # Kopyalamak isteyenler için şifreli içeriği göster
        text_content.delete("1.0", "end")
        text_content.insert("1.0", f"{title}\n{salt_b64}|{nonce_b64}\n{data_b64}")
        messagebox.showinfo("Başarılı", f"Not kaydedildi:\n{path}")
    except Exception as e:
        messagebox.showerror("Hata", f"Kaydetme/şifreleme başarısız.\n{e}")

def decrypt_from_text():
    blob = text_content.get("1.0", "end-1c").strip()
    password = entry_pass.get()
    if not blob:
        messagebox.showwarning("Uyarı", "Text alanına şifreli veriyi yapıştırın.")
        return
    if not password:
        messagebox.showwarning("Uyarı", "Şifre girin.")
        return
    try:
        salt_b64, nonce_b64, data_b64 = parse_encrypted_blob(blob)
        plain = decrypt_text(salt_b64, nonce_b64, data_b64, password)
        text_content.delete("1.0", "end")
        text_content.insert("1.0", plain)
        messagebox.showinfo("Tamam", "Şifre çözme başarılı.")
    except Exception as e:
        messagebox.showerror("Hata", f"Çözme başarısız. Şifre yanlış ya da veri bozuk/eksik.\n{e}")




# -------- UI  --------
root = tk.Tk()
root.title("Secret Notes")
root.configure(bg="#eaeaea")
root.minsize(340, 520)

container = tk.Frame(root, bg="#eaeaea")
container.pack(fill="both", expand=True, padx=16, pady=12)

# Logo
img_label = tk.Label(container, bg="#eaeaea")
img_label.pack(pady=(8, 8))
try:
    # 'top_secret.png' proje kökünde olmalı
    img_path = os.path.join(os.path.dirname(__file__), "top_secret.png")
    logo = tk.PhotoImage(file=img_path)
    img_label.configure(image=logo)
    img_label.image = logo  # referansı tut
except Exception:
    img_label.configure(text="")  # resim yoksa boş bırak

# Title
tk.Label(container, text="Enter your title", bg="#eaeaea",font=("Arial", 10, "bold")).pack(pady=(6, 2))
entry_title = tk.Entry(container, width=28, justify="center")
entry_title.pack(pady=(0, 10))

# Secret text
tk.Label(container, text="Enter your secret", bg="#eaeaea",font=("Arial", 10, "bold")).pack(pady=(0, 2))
text_content = tk.Text(container, width=34, height=12, wrap="word",relief="solid", borderwidth=1)
text_content.pack(pady=(0, 10))

# Master key
tk.Label(container, text="Enter master key", bg="#eaeaea",font=("Arial", 10, "bold")).pack(pady=(0, 2))
entry_pass = tk.Entry(container, width=28, justify="center", show="*")
entry_pass.pack(pady=(0, 10))

# Buttons
btn_save = tk.Button(container, text="Save & Encrypt", width=20, command=save_and_encrypt)
btn_save.pack(pady=(4, 4))
btn_dec = tk.Button(container, text="Decrypt", width=20, command=decrypt_from_text)
btn_dec.pack(pady=(0, 6))

root.mainloop()