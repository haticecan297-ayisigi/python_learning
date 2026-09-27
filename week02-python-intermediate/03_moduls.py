'''# math modülünü kullanarak bir sayının karekökünü hesapla.
from math import sqrt
print(sqrt(16))

# Bir sayının faktöriyelini hesapla.
from math import factorial
print(factorial(5))

# random kullanarak 1–100 arasında rastgele sayı üret.
import random
for i in range(10):
    print(random.randint(1, 100)) # 10 tane sayıyı kendim üretmek istedim.

# Bir listedeki elemanlardan rastgele birini seç.
liste = [2,4,7,67,41,55,34]
print(random.choice(liste))

# shuffle(): Bir listenin elemanlarını karıştırır ve doğrudan mevcut listeyi değiştirir.
random.shuffle(liste)
print(liste)

# Bugünün tarihini ve saatini yazdır.
import datetime
print(datetime.datetime.now())

# Bir tarih nesnesinden yıl, ay ve gün bilgilerini ayrı ayrı al.
tarih = datetime.datetime(2006,6,14)
print(tarih.year)
print(tarih.month)
print(tarih.day)

# Kendi math_operations.py dosyanı oluştur ve içine toplama, çıkarma, çarpma fonksiyonları yaz.
# Bu fonksiyonları moduls.py içinden çağır.
import math_operations as m
m.add(3,2)
m.subtract(7,1)
m.power(2,-3)
m.multipy(5,6)
m.divide(90,3)'''

## MİNİ PROJE: RASTGELE ŞİFRE ÜRETİCİSİ
import random
havuz = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','H','I','J','K','L','M','N','.',',','!','?','*']
sifre = []
uzunluk = int(input("Sifre uzunlugunu girin: "))
if uzunluk < 4 and uzunluk > 16:
    raise ValueError("Sifre uzunlugu 4-16 arasinda olmalidir!")
for i in range(uzunluk):
    sifre.append(random.choice(havuz))
print(sifre)