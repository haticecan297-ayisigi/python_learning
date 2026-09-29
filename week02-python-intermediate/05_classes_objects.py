# Person sınıfı oluştur. Ad, soyad ve yaş bilgilerini __init__() ile al. Kişinin bilgilerini gösteren introduce() metodunu yaz.
class person:
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
    def introduce(self):
        print(f"{self.ad} {self.soyad} - {self.yas}")

# BankAccount sınıfı oluştur. Hesap sahibi ve bakiye özellikleri olsun. Para yatırma metodu yaz. Para çekme metodu yaz. Bakiye yetersizse işlem yapılmasın.
'''class bankAccount:
    def __init__(self, sahip, bakiye):
        self.sahip = sahip
        self.bakiye = bakiye

    def para_yatir(self, ekle):
        self.ekle = ekle
        self.bakiye += ekle
        print(self.bakiye)
    def para_cek(self, cek):
        self.cek = cek
        if cek <= self.bakiye:
            self.bakiye -= cek
            print(self.bakiye)
        else:
            print("Yetersiz bakiye!")

hesap1 = bankAccount("hatice", 100000)
hesap2 = bankAccount("beyza", 200)
hesap1.para_yatir(50000)
hesap2.para_cek(300)
hesap1.para_cek(70000)'''

# Rectangle sınıfı oluştur. Uzunluk ve genişlik özelliklerini tanımla. Dikdörtgenin alanını ve çevresini hesaplayan metotlar yaz.
class rectangle:
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik
    def alan(self):
        return self.genislik * self.uzunluk
    def cevre(self):
        return 2 * (self.uzunluk + self.genislik)
dortgen1 = rectangle(4,5)
dortgen2 = rectangle(6,3)
print(dortgen1.alan())
print(dortgen2.cevre())

# Student sınıfında öğrencinin not ortalamasını hesaplayan bir metot oluştur.
class Student:
    def __init__(self, ad, soyad, notlar=[]):
        self.ad = ad
        self.soyad = soyad
        self.notlar = notlar
    def ortalama(self):
        toplam = 0
        count = 0
        for not_in in self.notlar:
            toplam += not_in
            count += 1
        return toplam / count

stdnt1 = Student("Hatice", "can", [90,98,96])
sonuc = stdnt1.ortalama()
print(sonuc)

## MİNİ PROJE: BANKA HESABI SİMÜLASYONU
class bankAccount:
    def __init__(self, sahip, bakiye):
        self.sahip = sahip
        self.bakiye = bakiye

    def para_yatir(self):
        miktar = int(input("Yatirmak istediginiz miktar: "))
        if miktar <= 0:
            raise ValueError("yatirilan para sifirdan buyuk olmalidir!")
        self.bakiye += miktar
    def para_cek(self):
        cek = int(input("Cekmek istediginiz miktar: "))
        if cek <= 0:
            raise ValueError("Cekilecek para sifirdan buyuk olmalidir!")
        if cek <= self.bakiye:
            self.bakiye -= cek
        else:
            print("Yetersiz bakiye!")
    def hesap(self):
        print(f"{self.sahip} - Bakiye: {self.bakiye}")
hesap1 = bankAccount("hatice", 1000000)
hesap2 = bankAccount("hatice", 300)
hesap1.para_yatir()
hesap1.hesap()
hesap2.para_cek()
hesap2.para_cek()
hesap2.hesap()
