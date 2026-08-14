# Problem 1 - Kullanıcıdan 5 sayı al ve en büyüğü bul
'''def en_buyuk(sayilar):
    buyuk = sayilar[0]
    for sayi in sayilar:
        if buyuk < sayi:
            buyuk = sayi
    return buyuk

count = 1
sayilar = []
while count <= 5:
    sayilar.append(int(input(f"{count}. sayiyi girin: ")))
    count += 1


print("En buyuk sayi: ", en_buyuk(sayilar))'''

# Problem 2 - sayı analizi

'''count = 1
nums = []
while count <= 10:
    nums.append(int(input(f"{count}. sayiyi giriniz: ")))
    count += 1

pozitif = 0
negatif = 0
sifir = 0
cift = 0
tek = 0
for num in nums:
    if num < 0:
        negatif += 1
    elif num > 0:
        pozitif += 1
    else:
        sifir += 1
    if num % 2 == 0:
        cift += 1
    else:
        tek += 1

analiz={'pozitif': pozitif, 
        'negatif': negatif, 
        'sifir': sifir, 
        'cift': cift, 
        'tek': tek}

print("Pozitif Sayi Adeti: ", pozitif)
print("Negatif Sayi Adeti: ", negatif)
print("Sifir Sayi Adeti: ", sifir)
print("Cift Sayi Adeti: ", cift)
print("Tek Sayi Adeti: ", tek)'''

# Problem 3 - Kelime Analizi

cumle = input("Bir cumle giriniz: ")
cumle_lower = cumle.lower()

karakter = len(cumle)

kelime_sayisi = len(cumle.split())

a_sayisi = cumle_lower.count("a")

ters_cumle = cumle[:: -1]

print("Karakter Sayisi: ", karakter)
print("Kelime Sayisi: ", kelime_sayisi)
print("'a' harfi sayisi: ", a_sayisi)
print("Cumlenin Tersi: ", ters_cumle)

# Problem 4- Liste Analizi
#Kendi kodlarımla

liste = [12,5,8,21,3,17,10,4]

en_buyuk = liste[0]
en_kucuk = liste[0]
toplam = 0
cift = []
tek = []

for i in liste:
    if i > en_buyuk:
        en_buyuk = i
    toplam += i

for k in liste:
    if k < en_kucuk:
        en_kucuk = k

ortalama = toplam / len(liste)

for c in liste:
    if c % 2 == 0:
        cift.append(c)
    else:
        tek.append(c)

print("En buyk sayi: ", en_buyuk)
print("En kucuk sayi: ", en_kucuk)
print("Toplami: ", toplam)
print("Ortalamalari: ", ortalama)
print("Cift sayilarin listesi: ", cift)
print("Tek sayilarin listesi: ", tek)

#Hazır fonksiyonlarla
print("En buyk sayi: ", max(liste))
print("En kucuk sayi: ", min(liste))
print("Toplami: ", sum(liste))
print("Ortalamalari: ", sum(liste) / len(liste))

cift = [x for x in liste if x % 2 == 0]
tek = [x for x in liste if x % 2 != 0]

print("Cift sayilarin listesi: ", cift)
print("Tek sayilarin listesi: ", tek)

# Problem 5 - Öğrenci Analizi

ogrenci = {
    "Hatice": 90,
    "Beyza": 98,
    "Pinar": 50,
    "Murat": 49,
    "Melih": 88
}

def ortalama(ogrenci):
    toplam = 0
    for i in ogrenci.values():
        toplam += i
    average = toplam / len(ogrenci)
    return average

def yuksek_not(ogrenci):
    yuksek = 0
    for i in ogrenci.values():
        if i > yuksek:
            yuksek = i
    return yuksek

def dusuk_not(ogrenci):
    dusuk = 100
    for i in ogrenci.values():
        if i < dusuk:
            dusuk = i
    return dusuk

def gecen(ogrenci):
    gecti = []
    for isim, notu in ogrenci.items():
        if notu >= 50:
            gecti.append(isim)
    return gecti

def kalan(ogrenci):
    kaldi = []
    for isim, notu in ogrenci.items():
        if notu < 50:
            kaldi.append(isim)
    return kaldi

print("Sinif Ortalamasi: ", ortalama(ogrenci))
print("En Yuksek Not: ", yuksek_not(ogrenci))
print("En Dusuk Not: ", dusuk_not(ogrenci))
print("Gecen Ogrenciler: ", gecen(ogrenci))
print("Kalan Ogrenciler: ", kalan(ogrenci))

# Problem 6 - ATM'yi fonksiyonla yaz

def menu():
    print("======= ATM MENU =======\n")
    print("""1- Bakiye Sorgula
    2- Para Çek
    3- Para Yatir
    4- Cikis""")
    print("========================\n")

def bakiye_goster(bakiye):
    print("Bakiyeniz: ", bakiye)

def para_cek(cekilen, bakiye):
    if cekilen > bakiye:
        print("Yeterli bakiye bulunmamaktadir!")
    else:
        bakiye = bakiye - cekilen
        print("Para cekme islemi gerceklesmistir!")
    return bakiye

def para_yatir(yatirilan, bakiye):
    if yatirilan <= 0:
        print("Yatirilan para sifir veya negatif olamaz!")
    else:
        bakiye += yatirilan
    return bakiye

bakiye = 10000

menu()

islem = 0
while islem != 4:
    islem = int(input("Yapmak istediginiz islem: "))

    if islem == 1:
        bakiye_goster(bakiye)
    elif islem == 2:
        cekilen = int(input("Cekmek istediginiz miktari girin: "))
        bakiye = para_cek(cekilen, bakiye)
    elif islem == 3:
        yatirilan = int(input("Yatirmak istedginiz miktari girin: "))
        bakiye = para_yatir(yatirilan, bakiye)
    elif islem == 4:
        print("Cikis Yapiliyor...")
    else:
        print("Menudeki islemleri seciniz!")