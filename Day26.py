# tkinter nedir ?
# tkinter python ile GUI uygulamaları geliştirmek için kullanılan standart bir kütüphanedir
# tkinter ile butonlar, etiketler, metin kutuları, menüler ve daha fazlasını içeren grafiksel kullanıcı arayüzleri oluşturabilirsiniz
# tkinter, Python'un standart kütüphanesine dahil edilmiştir, bu nedenle ek bir kurulum gerektirmez
# turtle daha çok grafik ve çizim işlemleri için kullanılırken, tkinter daha geniş bir yelpazede GUI uygulamaları geliştirmek için kullanılır.


#from tkinter import * # yukarıdaki gibi de import edilebilir ama bu şekilde yaparsak tkinter içindeki her şeyi import etmiş oluruz ve bu da isim çakışmalarına neden olabilir
#ayrıca pencere = Tk() yaparsın önceki gibi tkinter.Tk() demene gerek kalmaz ama bu şekilde kullanmak pek önerilmez
#işte text = Text() yaparsın mesela direk text yazarsın tkinter.Text demene gerek kalmaz bildiğin nesne oluşturma şekli javadan farkı başları sil



# pencere oluşturma
import tkinter
from tkinter import IntVar

#ekran = tkinter.Tk()# tkinter modülünden Tk sınıfını kullanarak bir pencere oluşturuyoruz
#değişken adı = tkinter.Tk() diye yazılır
#ekran.title("Python GUI Uygulaması")# Pencerenin başlığını ayarlıyoruz
#ekran.minsize(400, 400)



#label = kullanıcı arayüzünde metin veya görüntü göstermek için kullanılan bir widget'tır
#değişken adı = tkinter.Label(opsiyonel)# Label widget'ını oluşturuyoruz

#myLabel=tkinter.Label(ekran,text="bu bir labeldır", font=("Arial", 20))#label de aklında bulunsun text ve font
#içine ekran ekledik çünkü hangi pencereye ekleyeceğimizi belirtmemiz lazım diğerlerinde yapmıyorum anla ama
#myLabel.config(bg="red",fg="white")# config ile labelın özelliklerini değiştirebiliriz her sefer baştan yazmak yerine
#myLabel.pack()# pack metodu, widget'ı pencereye ekler ve görünür hale getirir bunu yapmazsak label gözükmez grid ve place metotları da var bunu yapan

#button nasıl yapılır onu görelim
#buttonda yine text aklında bulunsun ve command da aklında bulunsun command butona tıklandığında çalışacak fonksiyonu belirtir
#def butonaTiklandi():
    #giris=myEntry.get()
    #print(giris)# butona tıklandığında entry'deki metni alıp bastırıyoruz

#button = tkinter.Button(text="Bana Tıkla",command=butonaTiklandi)
#button.pack()# butonu pencereye ekliyoruz bunu eklemezsek buton gözükmez


#entry nedir onu görelim = entry, kullanıcıdan metin girişi almak için kullanılan bir widget'tır
#myEntry=tkinter.Entry(width=40)
#myEntry.pack()# entry'i pencereye ekliyoruz

#button = tkinter.Button(text="Tıkla",command=butonaTiklandi)
#button.pack(side="bottom")

#############################################pack-place-grid#####################################################
#pack de içine parametre alabiliyor mesela sağa yerleştir sola yerleştir vs gibi işlemlerde
#side parametresi var mesela side="left" dersek sola yerleştirir side="right" dersek sağa yerleştirir side="top" dersek yukarıya yerleştirir side="bottom" dersek aşağıya yerleştirir

#pack dışında birde place var bunun da x ve y parametreleri var mesela place(x=100,y=200) dersek x ekseninde 100 y ekseninde 200 noktasına yerleştirir daha esnek bir yerleştirme yaparız
#button.place(x=100,y=100)

#pack ve place dışında birde grid var grid ile satır ve sütun bazlı yerleştirme yapabiliriz mesela grid(row=0,column=0) dersek 0. satır ve 0. sütuna yerleştiririz
#grid zaten ızgara demek o mantıkla çalışıyor
#grid mantığında x ve  y leri söylemek yerine row ve columnları söylüyoruz farkı bu place ve pack'ten

#myButton2=tkinter.Button(text="yardımcı buton")
#myButton2.grid(row=1,column=1)


#myLabel.config(text=myEntry.get()) mesela my label önce idi ama geldim config ile değiştirdim

#############################################text yapısını görelim#####################################################
#text widget'ı, kullanıcıdan çok satırlı metin girişi almak veya çok satırlı metin görüntülemek için kullanılan bir widget'tır
#text widget'ı entry widget'ından farklı olarak, birden fazla satır metin içerebilir ve metin biçimlendirme seçenekleri sunar

#text içindeki metni almak için get metodu kullanılır ve iki parametre alır başlangıç ve bitiş indeksleri çünü birden fazla metin var
#ama entry de tek satır metin var o yüzden get metodu parametre almıyordu aklında bulunsun
"""
def butonaTiklandi():
    
    giris=myText.get("1.0",tkinter.END)# text widget'ındaki metni alıyoruz 1.0 demek 1.satır 0.karakter demek yani en baştan başla demek
    print(giris)# text widget'ındaki metni bastırıyoruz
"""

#myWindow = tkinter.Tk()
#myWindow.title("Text Widget Örneği")
#myWindow.minsize(400, 400)

#my_button=tkinter.Button(text="Metni Al", command=butonaTiklandi) # Buton oluşturuyoruz
#my_button.pack(side="bottom")

#myText = tkinter.Text(height=10, width=30) # Text widget'ını oluşturuyoruz
#myText.insert(tkinter.END, "Merhaba, bu bir Text widget örneğidir.\n") # Text widget'ına başlangıç metni ekliyoruz
#myText.pack()

#############################################scale yapısını görelim#####################################################
#aşağı yukarı kaydırılabilir bir kaydırıcı oluşturur yine command ile fonksiyon bağlanabilir vs vs widt height mevzuları da hepsinde var genişlik vs ayarlamak için unutma
#from alt çizgi ile kullanılır
"""
myScale=tkinter.Scale(from_=0,to=100)# from ve to parametreleri kaydırıcının minimum ve maksimum değerlerini belirler orient parametresi kaydırıcının yatay mı dikey mi olacağını belirler
myScale.pack()

myScale.mainloop()# Pencerenin açık kalmasını sağlar ve kullanıcı etkileşimlerini bekler
"""
#############################################spinbox yapısını görelim#####################################################
#scale ile benzer ama bu sefer kullanıcıya belirli bir aralıkta sayısal değerler sunar ve kullanıcı bu değerler arasında seçim yapabilir
"""
mySpin=tkinter.Spinbox(from_=0,to=100)
mySpin.pack()

mySpin.mainloop()
"""

#############################################checkbutton yapısını görelim#####################################################
#checkbutton, kullanıcıya bir veya daha fazla seçenek sunan ve bu seçeneklerin seçilip seçilmediğini belirten bir widget'tır
#checkbutton seçildi mi seçilmedi mi bunu boolean olarak tutar ve variable ile bağlanırız
#checkbutton seçildiğinde bir fonksiyon çalıştırmak için command parametresi kullanılır

pencere = tkinter.Tk()
pencere.title("Checkbutton Örneği")
pencere.minsize(300, 200)

#kontrol değişkeni oluşturduk onu variable parametresine atadık ve checkbutton'ın durumunu tutacak buton içinde de kontrol değişkenini kullanacağız
"""
def checkbuttonTiklandi():
    print(kontrol.get())# checkbutton'ın durumunu alıyoruz ve bastırıyoruz

kontrol=IntVar()
mycheckbutton=tkinter.Checkbutton(text="Beni Seç",variable=kontrol,command=checkbuttonTiklandi)
mycheckbutton.pack()

pencere.mainloop()# Pencerenin açık kalmasını sağlar ve kullanıcı etkileşimlerini bekler
"""
#############################################radiobutton yapısını görelim#####################################################
#radiobutton, kullanıcıya bir grup seçenek sunan ve bu seçeneklerden yalnızca birinin seçilmesine izin veren bir widget'tır
#radiobutton'lar genellikle birbirleriyle ilişkili seçenekler için kullanılır
#burda da yine variable parametresi ile bir değişkene bağlanırız ve seçilen radiobutton'ın değerini bu değişkende tutarız ayrıca text command vs vs yine var
"""
def tiklama():
    print(kontroll.get())

kontroll=IntVar()
my_radio=tkinter.Radiobutton(text="Seçenek 1",value=10,variable=kontroll,command=tiklama)
my_radio.pack()
my_radio.mainloop()
#value tıklandığında değişkene atanacak değeri belirtir

"""

#############################################listbox yapısını görelim#####################################################
#listbox, kullanıcıya bir liste halinde seçenekler sunan ve bu seçeneklerden bir veya daha fazlasının seçilmesine izin veren bir widget'tır

def listboxTiklandi(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox=tkinter.Listbox()
name_list=["mehmet","ahmet","ayşe","fatma","ali","veli"]

for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])# listbox'a eleman eklemek için insert metodunu kullanıyoruz

my_listbox.bind("<<ListboxSelect>>",listboxTiklandi)
my_listbox.pack()

my_listbox.mainloop()
