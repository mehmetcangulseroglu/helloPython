import tkinter
from tkinter import messagebox


#işlemleri daima bir fonksiyon içinde yapın çünkü mesela button yapısında parametre olarak fonksiyon ismi verilir ve o fonksiyon çağrılır çünkü
#bunu kesinlikle unutmayın kod yazarken düz yazmayın fonksiyon içinde yazın işlemleri fonksiyon içinde yapın

def bmi_hesapla():
    try:
        kilo = kilo_entry.get()
        boy = boy_entry.get()

        if not kilo or not boy:
            messagebox.showwarning("Uyarı", "Kilo ve boy alanlarını boş bırakmayınız!")
            return

        #tür dönüşümü yapıyoruz çünkü entry den gelen değer string olarak gelir hatırla pythonda inputtan gelen değerlerde string geliyordu
        kilo = float(kilo)
        boy = float(boy)

        if kilo <= 0 or boy and kilo and boy <= 0 :
            messagebox.showwarning("Uyarı", "Kilo ve boy pozitif sayı olmalıdır!")
            return

        bmi = kilo / (boy ** 2)#python java gibi değil illa değişkenler en üstte olmak zorunda değil kullanacağın yerde de tanımlayabilirsin
        if bmi < 18.5:
            durum = "Zayıf"
        elif 18.5 <= bmi < 25:
            durum = "Normal"
        elif 25 <= bmi < 30:
            durum = "Fazla Kilolu"
        else:
            durum = "Obez"

        sonuc_label.config(text=f"BMI: {bmi:.2f} - {durum}")#virgül ile değişkeni yazdırma sadece print ile olur mecbur format kullandık

    except ValueError:
        messagebox.showerror("Hata", "Lütfen kilo ve boy için geçerli bir sayı giriniz!")

pencere = tkinter.Tk()
pencere.title("BMI Hesaplayıcı")
pencere.minsize(300, 200)

kilo_label = tkinter.Label(pencere, text="Kilo (kg):")
kilo_label.pack()
kilo_entry = tkinter.Entry(pencere)
kilo_entry.pack()

boy_label = tkinter.Label(pencere, text="Boy (metre):")
boy_label.pack()
boy_entry = tkinter.Entry(pencere)
boy_entry.pack()

hesapla_button = tkinter.Button(pencere, text="Hesapla", command=bmi_hesapla)#fonksiyonu referans olarak verdik paranteze gerek yok bu daima böyledir unutma
hesapla_button.pack(pady=10)

sonuc_label = tkinter.Label(pencere, text="")
sonuc_label.pack()

pencere.mainloop()