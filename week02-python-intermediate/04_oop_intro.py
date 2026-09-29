'''# Car sınıfını oluştur. Marka, model ve yıl özellikleri olsun
class car:
    def __init__(self, marka, model, year):
        self.marka = marka
        self.model = model
        self.year = year

    def full_info(self):
        print(f"{self.marka} - {self.model}, {self.year}")

car1 = car('bmw', 'f30', 2025)
car2 = car('mercedes', 'g-6023', 2026)
car3 = car('hudai', 'i20', 2027)

print(car1.model)
print(car2.year)
car3.full_info()

# Book sınıfı oluştur. Kitap adı, yazar ve sayfa sayısı özelliklerini ekle.

class book:
    def __init__(self, name, yazar, pages):
        self.name = name
        self.yazar = yazar
        self.pages = pages

# Student sınıfı oluştur. Ad, soyad ve not bilgilerini tut. Öğrenci bilgilerini ekrana yazdıran bir fonksiyon yaz.

class student:
    def __init__(self, isim, soyisim, nots = []):
        self.isim = isim
        self.soyisim = soyisim
        self.nots = nots
    def info(self):
        print(f"{self.isim} {self.soyisim} - {self.nots}")

stdnt1 = student("hatice", "can", [90,95,98])
stdnt2 = student("Beyza", "Isik", [100,90,97])

stdnt1.info()
stdnt2.info()'''

## MİNİ PROJE: KİTAP BİLGİ SİSTEMİ

class book:
    def __init__(self, name, yazar, pages):
        self.name = name
        self.yazar = yazar
        self.pages = pages
    def bilgileri_yazdir(self):
        print(f"Kitap Ismi : {self.name}")
        print(f"Yazar : {self.yazar}")
        print(f"Sayfa Sayisi: {self.pages}")
        print("-" * 30)

kitap1 = book("Sefiller", "Victor Hugo", 1488)
kitap2 = book("Kürk Mantolu Madonna", "Sabahattin Ali", 177)
kitap3 = book("1984", "George Orwell", 328)
kitap4 = book("Simyaci", "Paulo Coelho", 184)

kitaplar = [kitap1, kitap2, kitap3, kitap4]

kitaplar.sort(key=lambda kitap: kitap.name)
print("=== ALFABETİK SIRALANMIŞ KİTAPLAR ===\n")

for kitap in kitaplar:
    kitap.bilgileri_yazdir()