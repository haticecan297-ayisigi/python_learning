# while
x = 1
while x <= 10:
    print(x)
    x += 1
x = 10
while x > 0:
    print(x)
    x -= 1
while x <= 10:
    print(x)
    x += 2
x = 10
while x > 0:
    print(x)
    x -= 5

# for

for i in range(1,11):
    print(i)
for i in range(1,21):
    print(i)
for i in range(10,0,-1):
    print(i)
for i in range(0,101,5):
    print(i)

# range()

print(list(range(5)))
print(list(range(1,6)))
print(list(range(1,20,2)))
print(list(range(10,0,-1)))   # bunları for ile yazdğımda ise sayı olarak yine aynısını verecekti

# Break

for i in range(1,20):
    if i == 13:
        break
    print(i)

# continue

for i in range(1,21):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1,21):
    if i % 2 != 0:
        continue
    print(i)
# pass

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)

# enumerate()

meyveler = ['elma', 'armut', 'muz', 'kiraz']
for index, fruit in enumerate(meyveler,start = 1):
    print(f"{index}. {fruit}\n")

# soru 1: 1-100 arasındaki sayıların toplamını hesapla

sum = 0
for i in range(1,101):
    sum += i
print("Toplam: ", sum)

# soru 2: faktöriyel

faktoriyel = 1
for i in range(1,101):
    faktoriyel *= i
print("Faktoriyel: ", faktoriyel)

# soru 3: Kullanıcıdan kaç sayı gireceğini alıp ortalamasını hesapla

tane = int(input("Kac tane sayi gireceksiniz: "))
sum = 0
for i in range(tane):
    sayi = int(input(f"{i + 1}. sayiyi giriniz: "))
    sum += sayi
print("Ortalama: ", sum / tane)

# soru 4: Bir sayının çarpım tablosunu oluştur

for i in range(1,11):
    print(f"7 x {i} = {i * 7}")

# soru 5: Bir sayının asal olup olmadığını kontrol et

sayi = int(input("Kontrol etmek istediginiz sayiyi girin: "))

if sayi > 1:
    asal_mi = True
    
    for i in range(2, sayi):
        if sayi % i == 0:
            asal_mi = False
            break
            
    if asal_mi:
        print(f"{sayi} bir asal sayidir.")
    else:
        print(f"{sayi} bir asal sayi değildir.")

else:
    print(f"{sayi} bir asal sayi değildir.")

# soru 6: Fibonacci dizisinin ilk N terimini yazdır

n = int(input("Kaç terim yazdirmak istiyorsunuz? "))

a, b = 1, 1

if n <= 0:
    print("Lütfen pozitif bir tam sayi girin.")
else:
    print(f"\nFibonacci dizisinin ilk {n} terimi:")
    
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
        
print()

# soru 7: 0-100 arasindaki çift sayı adeti ve tek sayi adetini hesapla

tek = 0
cift = 0
for i in range(0,101):
    if i % 2 == 0:
        cift += 1
    else:
        tek += 1
print(f"{tek} adet tek sayi vardir.\n{cift} adet cift sayi vardir.")

# MİNİ PROJE: GELİSTİRİLMİS ATM
bakiye = 10000
print("""======= ATM =======
1- Bakiye
2- Para Yatir
3- Para Çek
4- Cikis""")

islem = 1
while islem != 4:
    islem = int(input("Yapmak istediginiz islemi giriniz: "))
    if islem == 1:
        print(f"Bakiyeniz: {bakiye}")
    elif islem == 2:
        yatir = int(input("Kac para yatiracaginizi giriniz: "))
        if yatir > 0:
            bakiye += yatir
            print(f"Guncel Bakiyeniz: {bakiye}")
        else:
            print("Negatif deger yatirilamaz!")
    elif islem == 3:
        cek = int(input("Kac para cekeceginizi giriniz: "))
        if cek < bakiye:
            bakiye -= cek
            print(f"Guncel Bakiyeniz: {bakiye}")
        else:
            print("Bakiyenizden fazla para cekemezsiniz!")
    elif islem == 4:
        print("Cikis Yapiliyor...")
        break
    else:
        print("Menudeki numaralari giriniz!")