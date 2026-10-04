# Lambda kullanarak iki sayının çarpımını hesapla.
'''carpim = lambda x, y: x * y
print(carpim(5,4))

# map() kullanarak bir listedeki sayıların karelerini hesapla.
kare = list(map(lambda x: x ** 2, [1,2,3,4]))
print(kare)

# filter() ile çift sayıları seç.
cift = list(filter(lambda x: x % 2 == 0, [1,2,3,4]))
print(cift)

# Bir öğrenci listesini notlarına göre sırala.
ogrenciler= [
        ("Ali", 75),
        ("Ayşe",100),
        ("Mehmet", 60),
        ("Zeynep", 85)
    ]
sirali = sorted(ogrenciler, key=lambda x: x[1])
print(sirali)

# Bir ürün listesini fiyatlarına göre sırala.
urunler = [
        ("Telefon", 25000),
        ("Kulaklık", 1500),
        ("Tablet", 10000),
        ("Saat", 5000)
    ]
sirali = sorted(urunler, key=lambda x: x[1])
print(sirali)

# Bir kelime listesini uzunluklarına göre sırala.
kelimeler = ['Elma', 'muz', 'üzüm', 'nektari']
sirali = sorted(kelimeler, key = len)
print(sirali)

# zip() ile isim ve not listelerini eşleştir.
isimler = ["Ali", "Ayşe", "Mehmet"]
notlar = [80, 95, 70]
eslestirilmis = list(zip(isimler, notlar))
print(eslestirilmis)

# zip() ile bir sözlük oluştur.
isimler = ["Ali", "Ayşe", "Mehmet"]
notlar = [80, 95, 70]
sozluk = dict(zip(isimler, notlar))
print(sozluk)

# Bir listedeki en büyük üç sayıyı bul.
sayilar = [12, 45, 78, 3, 99, 21, 91, 50, 67]
en_buyuk_uc = sorted(sayilar, reverse=True)[:3]
print(en_buyuk_uc)'''

## MİNİ PROJE: ÜRÜN SIRALAMA VE FİLTRELEME SİSTEMİ
'''Bir ürün listesi oluştur. Her ürünün adı, fiyatı ve stok miktarı olsun.
Program:
Ürünleri fiyata göre küçükten büyüğe sıralamalı.
Ürünleri fiyata göre büyükten küçüğe sıralamalı.
Belirli bir fiyatın altındaki ürünleri filtrelemeli.
Stok miktarı sıfırdan fazla olan ürünleri göstermeli.
En pahalı üç ürünü listelemeli.
Ürünleri isimlerine göre alfabetik sıralamalı.'''
urunler = [
    ("Kalem", 27, 5),
    ("Silgi", 35, 9),
    ("Defter", 70, 0),
    ("Boya kalemi", 48, 11),
    ("Cetvel", 62, 23)
]

sirali = sorted(urunler, key=lambda x: x[1])
print(sirali)

print(list(reversed(sirali)))

filtreli = list(filter(lambda x: x[1] > 20, urunler))
print(filtreli)

stok = list(filter(lambda x: x[2] > 0, urunler))
print(stok)

print(list(reversed(sirali))[:3])

alfabetik = sorted(urunler, key=lambda x: x[0])
print(alfabetik)