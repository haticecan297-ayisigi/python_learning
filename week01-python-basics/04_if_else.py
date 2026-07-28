#Karşılaştırma operatörleri
print(7 == 7)
print(7 != 13)
print(13 > 7)
print(7 < 13)
print(7 <= 13)
print(13 >= 7)
# if statements
yas = 20
if yas >= 18:
    print("Ehliyet alabilir.")
else:
    print("Ehliyet alamaz.")
#elif statements
puan = 94
if puan >= 90:
    print("AA")
elif 80 <= puan < 90:
    print("BA")
elif 70 <= puan < 80:
    print("BB")
elif 60 <= puan < 70:
    print("CB")
elif 50 <= puan < 60:
    print("CC")
else:
    print("FF")
#and / or
ortalama = 3.68
devamsizlik = 3
if ortalama >= 3.0 and devamsizlik <= 5:
    print("Burs alabilirsiniz.")
else:
    print("Burs alamazsiniz.")
#not
aktif = False
if not aktif:
    print("Aktif degilsiniz")
else:
    print("Hosgeldiniz.")
#iç içe if
yas = int(input("Yasiniz: "))
ehliyet = input("Ehliyet var mi(evet/hayir): ")
if yas >= 18:
    if ehliyet == "evet":
        print("araba kullanabilirsiniz.")
    else:
        print("Araba kullanamzsiniz ehliyetiniz yok.")
else:
    print("Yasiniz 18'den kucuk araba kullanamazsiniz.")
#soru-1
sayi = int(input("Sayi girin: "))
if sayi > 0:
    print("Sayi pozitif.\n")
elif sayi < 0:
    print("Sayi negatif.\n")
else:
    print("Sayi sifirdir.\n")
#soru-2
if sayi % 2 == 0:
    print("Sayi cifttir.\n")
else:
    print("Sayi tektir.\n")
#soru-3
sayi1 = int(input("Birinci sayiyi girin: "))
sayi2 = int(input("Ikinci sayiyi girin: "))
sayi3 = int(input("Ucuncu sayiyi girin: "))
if sayi1 >= sayi2 and sayi1 >= sayi3:
    print("En buyuk sayi: ", sayi1)
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    print("En buyuk sayi: ", sayi2)
else:
    print("En buyuk sayi: ", sayi3)
#soru-4
sifre = "python123"
deneme = input("Sifreyi girin: ")
if sifre == deneme:
    print("Giris basarili.")
else:
    print("Sifre hatali.")
#soru-5
yil = int(input("Bir yil girin: "))
if yil % 400 == 0:
    print(yil, "artik yil.")
elif yil % 100 != 0 and yil % 4 == 0:
    print(yil ,"artil yil.")
else:
    print(yil, "artik yil degil.")
#Günlük mini proje
print("""-------MENU-------
1- Bakiye Goruntule
2- Para Yatir
3- Para Cek
4- Cikis
-----------------""")
secim = int(input("Hangi islemi yapmak istiyorsunuz: "))
bakiye = 5000
if secim == 1:
    print("Guncel Bakiye: ", bakiye)
elif secim == 2:
    bakiye += int(input("Eklemek istediginiz miktari girin: "))
    print("Guncel Bakiye: ", bakiye)
    print("Basariyla para yatirma gerceklesmistir.")
elif secim == 3:
    takeMoney = int(input("Cekmek istediginiz miktari girin: "))
    if bakiye >= takeMoney:
        bakiye -= takeMoney
        print("Guncel Bakiye: ", bakiye)
        print("Basariyla para cekme gerceklesmistir.")
    else:
        print("Yeterli bakiye bulunmamaktadir.")
elif secim == 4:
    print("Cikis yapiliyor...")
else:
    print("Menudeki sayilar girilmeli yanlis islem!")