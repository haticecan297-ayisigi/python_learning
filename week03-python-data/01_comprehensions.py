# 1–100 arasındaki sayıların karelerinden oluşan bir liste oluştur.
'''kareler = [x ** 2 for x in range(1,100)]
print(kareler)'''

# Bir listedeki çift sayıları seç.
'''liste = [1,3,4,7,13,24,14,6,8,56]
cift_sayilar = [x for x in liste if x % 2 == 0]
print(cift_sayilar)'''

# Bir listedeki sayıların iki katını içeren yeni bir liste oluştur.
'''liste = [1,3,4,7,13,24,14,6,8,56]
double = [x * 2 for x in liste]
print(double)'''

# Bir cümledeki kelimelerin uzunluklarını içeren bir liste oluştur.
'''cumle = "Python dilini öğreniyorum"
liste = [len(kelime) for kelime in cumle.split()]
print(liste)'''

# Bir listedeki negatif sayıları filtrele.
'''liste = [0,-4,23,-5,7,8,-88,-6]
negatif = [x for x in liste if x < 0]
print(negatif)'''

# Bir öğrenci notları sözlüğünden başarılı öğrencileri seç.
'''dic = {'ogrenci1': 45, 'ogrenci2':78, 'ogrenci3': 98 }
basarili = {x: basari for x, basari in  dic.items() if basari >= 50}
print(basarili)'''

# Bir listedeki kelimelerin uzunluklarını sözlükte tut.
'''liste = ["ben", "bir", "yazılım", "mühendisliği", "öğrencisiyim"]
dic = {x : len(x) for x in liste}
print(dic)'''

# Bir listedeki tekrarsız sayıların kümesini comprehension ile oluştu(Set Com.).
'''sayilar = [1, 2, 2, 3, 4, 4, 5]
kume = {sayi for sayi in sayilar}
print(kume)'''

# İç içe listelerden tek bir liste üret.
'''listeler = [[1, 2], [3, 4], [5, 6]]
sonuc = [eleman for alt_liste in listeler for eleman in alt_liste]
print(sonuc)'''

# En az üç görevi önce normal döngüyle, sonra comprehension ile çöz.
# 1. Listedeki sayıların karesini al
'''sayilar = [1, 2, 3, 4, 5]
kareler = []
for sayi in sayilar:
    kareler.append(sayi ** 2)
print(kareler)

kareler = [sayi ** 2 for sayi in sayilar]
print(kareler)
# 2. Çift sayıların karesini al
sayilar = [1, 2, 3, 4, 5, 6]
sonuc = []
for sayi in sayilar:
    if sayi % 2 == 0:
        sonuc.append(sayi ** 2)
print(sonuc)

sonuc = [sayi ** 2 for sayi in sayilar if sayi % 2 == 0]
print(sonuc)
# 3. Bir listedeki tekrarsız sayıların kümesini oluştur
sayilar = [1, 2, 2, 3, 4, 4, 5]
kume = set()
for sayi in sayilar:
    kume.add(sayi)
print(kume)

kume = {sayi for sayi in sayilar}
print(kume)'''

## MİNİ PROJE: ÖĞRENCİ NOT ANALİZ SİSTEMİ
'''Bir öğrenci notları sözlüğü oluştur.
- Öğrenci adı → Not
Program:
Başarılı öğrencileri seçmeli.
Başarısız öğrencileri seçmeli.
Her öğrencinin notunu 100 üzerinden 5 puan artırarak yeni bir sözlük oluşturmalı.
Notu 80 ve üzerinde olan öğrencileri listelemeli.
Öğrencilerin isimlerini ve notlarını kullanarak yeni listeler oluşturmalı.
Öğrencileri notlarına göre sıralanmış bir listeye dönüştür.'''
ogrenci_notlari = {
    'Hatice': 80,
    'Beyza': 100,
    'Murat': 98,
    'Pinar': 78,
    'Azra':46
    }
basarili = {x: basari for x, basari in  ogrenci_notlari.items() if basari >= 50}
print("Başarılı Öğrenciler:")
print(basarili)

failed = {x: fail for x, fail in  ogrenci_notlari.items() if fail < 50}
print("\nBaşarısız Öğrenciler:")
print(failed)

yeni_notlar = {ogrenci: min(newNot + 5,100) for ogrenci, newNot in ogrenci_notlari.items()}
print("\n+5 Puan Eklenmiş Notlar:")
print(yeni_notlar)

uzeri80 = [isim for isim, notu in ogrenci_notlari.items() if notu >= 80]
print("\n80 ve Üzeri Alanlar:")
print(uzeri80)


isimler = [isim for isim in ogrenci_notlari.keys()]
print("\nİsimler:")
print(isimler)
notlar =[notlar for notlar in ogrenci_notlari.items()]
print("\nNotlar:")
print(notlar)

sirali_ogrenciler = sorted(
        ogrenci_notlari.items(),
        key=lambda x: x[1],
        reverse=True
    )
print("\nNotlara Göre Sıralı Liste:")
for isim, notu in sirali_ogrenciler:
    print(f"{isim}: {notu}")