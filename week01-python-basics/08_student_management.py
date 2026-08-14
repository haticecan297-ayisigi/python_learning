# Öğrenci Bilgilendirme Sistemi

def menu_goster():
    print("================================")
    print(" OGRENCİ BİLGİLENDİRME SİSTEMİ")
    print("================================")
    print("""1- Ogrenci Ekle
2- Ogrencileri Listele
3- Ogrenci Ara
4- Ortalama Goster
5-Gecenleri Goster
6- Kalanlari Goster
7- Ogrenci Sil
8- Cikis""")

def ogrenci_ekle():

    durum = "Faild"
    grade = "FF"

    isim = input("Adini giriniz: ")
    soyisim = input("Soyadini giriniz: ")
    vize = int(input("Vize notunu giriniz: "))
    final = int(input("Final notunu giriniz: "))

    ortalama = vize * 0.4 + final * 0.6

    if ortalama >= 50:
        durum = "Passed"
    if ortalama >= 90:
        grade = "AA"
    elif ortalama < 90 and ortalama >= 80:
        grade = "BA"
    elif ortalama < 80 and ortalama >= 70:
        grade = "BB"
    elif ortalama < 70 and ortalama >= 60:
        grade = "BC"
    elif ortalama < 60 and ortalama >= 50:
        grade = "CC"

    ogrenci = {}

    ogrenci.update({'isim': isim, 
                    'soyisim': soyisim, 
                    'vize': vize,
                    'final': final,
                    'ortalama': ortalama,
                    'grade': grade,
                    'durum': durum})

    ogrenciler.append(ogrenci)

def ogrencileri_listele():

    print("============= OGRENCİLER =============\n")

    for i, ogrenci in enumerate(ogrenciler, start = 1):
        print(f"{i}. {ogrenci['isim']} {ogrenci['soyisim']} {ogrenci['ortalama']} {ogrenci['grade']} {ogrenci['durum']}")

def ogrenci_ara():

    ara = input("Aradiginiz ogrencinin adini giriniz: ")

    bulundu = False

    for ogrenci in ogrenciler:
        if ogrenci['isim'].lower() == ara:
            print("İsim: ", ogrenci['isim'])
            print("Soyisim: ", ogrenci['soyisim'])
            print("Vize: ", ogrenci['vize'])
            print("Final: ", ogrenci['final'])
            print("Ortalama: ", ogrenci['ortalama'])
            print("Grade: ", ogrenci['grade'])
            print("durum: ", ogrenci['durum'])
            bulundu = True

    if not bulundu:
        print("Ogrenci bulunamadi!")

def ortalama_goster():

    toplam = 0

    for ogrenci in ogrenciler:
        toplam += ogrenci['ortalama']

    print("Genel Ortalama: ", toplam / len(ogrenciler))

def gecenleri_goster():

    gecenler = []
    
    for ogrenci in ogrenciler:
        durum = "Passed"
        if durum == ogrenci['durum']:
            gecenler.append(ogrenci)

    print("============= PASSED =============")

    for gecen in gecenler:
        print(f"{gecen['isim']} {gecen['grade']}", sep = '-')

def kalanlari_goster():

    kalanlar = []
        
    for ogrenci in ogrenciler:
        durum = "Faild"
        if durum == ogrenci['durum']:
            kalanlar.append(ogrenci)

    print("============= FAILD =============")

    for kalan in kalanlar:
        print(f"{kalan['isim']} {kalan['grade']}", sep = '-')
    
def ogrenci_sil():

    sil = input("Silmek istediginiz ogrencinin adini giriniz: ")

    for ogrenci in ogrenciler:
            if ogrenci['isim'].lower() == sil:
                ogrenciler.remove(ogrenci)

menu_goster()

ogrenciler = []

islem = 0

while islem != 8:
    islem = int(input("Isleminizi seciniz: "))
    if islem == 1:
       ogrenci_ekle()
    elif islem == 2:
        ogrencileri_listele()
    elif islem == 3:
        ogrenci_ara()
    elif islem == 4:
        ortalama_goster()
    elif islem == 5:
        gecenleri_goster()
    elif islem == 6:
        kalanlari_goster()
    elif islem == 7:
        ogrenci_sil()
    elif islem == 8:
        print("Cikis yapiliyor...")
    else:
        print("Menudeki islemleri seciniz!")