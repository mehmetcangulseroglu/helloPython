# modül ve paketlere giriş
# modül: birden fazla python kodunu tek bir dosyada toplamak için kullanılır.
# paket: birden fazla modülü tek bir klasörde toplamak için kullanılır.

#modül dediğimiz herhangi bir yazılmış python kodunu içeren dosyadır.
#paket ise birden fazla modülü tek bir klasörde toplamak için kullanılır.

#örnek olması için kendi modülümüzü yazalım.

def ornekFonksiyon():
    print("Mehmet Can modül fonksiyon")

ornekFonksiyon()

#şimdi başka sınıftan bu modülü import edelim.

#komple modülü import etmek için:
#import day14
#--klasör ismi ile import edilebilir.
#artık day14. dediğimiz zaman day14.py dosyasındaki fonksiyonlara erişebiliriz.

#bu da komple değil modülü import etmek için:
# from day14 import
#ornekFonksiyon şeklinde de import edebiliriz.
#yani diyor ki day14.py dosyasındaki ornekFonksiyon fonksiyonunu import et. kullanabileyim


#pypi yazıp aratırsan bu paketlerin bulunduğu siteye ulaşabilirsin. ordan bakılabilir



##############################################PAKET ÇALIŞMA PRENSİPLERİ##############################################
#sağ tık-> new ->python package diyerek yeni bir paket oluşturabiliriz.
#paketler klasör şeklinde oluşturulur. içlerinde otomatik olarak  __init__.py dosyası bulunur.
#paketin içinde farklı paketler de olabilir. bu da alt paket olarak geçer.

#bir paketim olsun AnimalPackage diye içinde catpackage diye paket var
#ve info.py var
#geldim main.py dosyasına bu paketi #from AnimalPackage import info# şeklinde import edebilirim.
#böylece info.py dosyasındaki fonksiyonlara erişebilirim.


##################ALT PAKETİ İMPORT ETME##########################
#peki diyelim paketin içindeki paketi import etmek istiyorum. ordaki dosya için
#yani AnimalPackage var altında catpackage ve onun içinde meow.py var
#bunu import etmek için
#from AnimalPackage.catpackage import meow şeklinde import edebilirim.


#########################################ÖZETLE#########################################
from atilmodule import example_func#SINIF ADI İLE İÇİNDEKİ FONKSİYONLARI İMPORT ETME
from AnimalPackage import info#PAKET ADI İLE İÇİNDEKİ DOSYALARI İMPORT ETME
from AnimalPackage.CatPackage import meow#PAKET İÇİNDEKİ PAKET İÇİNDEKİ DOSYAYI İMPORT ETME

#ÖDEV-> YOUTUBE DOWNLOADER,PDF ÇEVİRİCİ,QR KOD OLUŞTURMA GİBİ PROJELER YAPILACAK
