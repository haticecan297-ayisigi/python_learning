'''try:
    number = int(input("Bir sayi gir: "))
    print(number)
except ValueError:
    print("Gecerli bir sayi girin!")'''

'''try:
    number = int(input("Kaca bolmek istedginizi girin: "))
    print(20 / number)
except ZeroDivisionError:
    print("Sifira bolunmez!")'''

'''try:
    number = input("Bir sayi girin: ")
    print(number + 5)
except TypeError:
    print("Veri turleri ayni degil!")'''

'''try:
    liste = []
    for i in range(0,3):
        liste.append(int(input(f"{i+1}. elemani girin: ")))
    print(liste[5])
except IndexError:
    print("Index hatasi!")'''

'''try:
    dic = {'name': "Hatice", 'surname': "Can", 'age': 20, 'garde': 2}
    print(dic['depertmant'])
except KeyError:
    print("Bu bilgi maalesef yok!")'''

'''try:
    number = int(input("Bir sayi girin:"))
    print(20 / number)
    print("5" + number)
except ZeroDivisionError:
    print("Sifira bolunmez!")
except TypeError:
    print("Gecerli bir sayi girin!")'''

'''try:
    number = int(input("Bir sayi girin:"))
    print(20 / number)
except ZeroDivisionError:
    print("Sifira bolunmez!")
else:
    print("Islem basarili!")'''

'''try:
    number = int(input("Bir sayi girin:"))
    print(5 + number)
except Exception:
    print("Bir hata oluştu!")
finally:
    print("Finally hata olsa da olmasa da calisir!")'''

'''age = int(input("Yasinizi girin: "))
if age < 0:
    raise ValueError("Yas negatif olamaz!")'''

## Problem-1: Güvenli Sayı Alma

'''def get_number():
    try:
        number = int(input("Bir sayi girin:"))
        return number
    except ValueError:
        print("Gecerli bir sayi girin!")
print(get_number())'''

## Problem-2: Güvenli Bölme

'''def divide(a,b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Bolme icin 2. sayi sifir olamaz!")

a = int(input("Birinci sayiyi girin: "))
b = int(input("Ikinci sayiyi girin: "))
divide(a,b)'''

## Problem-3: Liste Elemanı

'''liste = [1,2,3,4]
try:
    index = int(input("Istediginiz index numarasini girin: "))
    print(liste[index])
except ValueError:
    print("Index numarasi icin sayi girmelisiniz!")
except IndexError:
    print("Boyle bir index numarasi yoktur!")'''

## Problem-4: Dictionary

'''dic = {'name': "Hatice", 'surname': "Can", 'age': 20, 'garde': 2}
try:
    arama = input("Aradiginiz anahtar sozcugu girin: ")
    print(dic[arama])
except KeyError:
    print("Bu bilgi maalesef yok!")'''

## MİNİ PROJE: SAFE CALCULATOR

def show_menu():
    print("=========================")
    print("     SAFE CALCULATOR     ")
    print("=========================\n")
    print('''1. Addition
2. Subtraction
3. Power
4. Multiplication
5. Division
6. Exit
''')

def get_number():
    while True:
        try:
            ilk = int(input("Birinci sayiyi girin: "))
            ikinci = int(input("Ikinci sayiyi girin: "))
            return ilk, ikinci
        except ValueError:
            print("Bir sayi giriniz!")

def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def power(a, b):
    pow = 1
    if b > 0:
        for i in range(b):
            pow *= a
        print(pow)
    elif b == 0:
        print(pow)
    else:
        for i in range(-b):
            pow *= a
        print(1 / pow)

def multipy(a, b):
    print(a * b)

def divide(a, b):
    try:
        div = a / b
        print(div)
    except ZeroDivisionError:
        print("Sifira bolunmez!")

show_menu()
secim = 0
while secim != 6:
    secim = int(input("Choose: "))
    if secim < 6 and secim > 0:
        a , b = get_number()
        if secim == 1:
            add(a, b)
        elif secim == 2:
            subtract(a, b)
        elif secim == 3:
            power(a, b)
        elif secim == 4:
            multipy(a, b)
        else:
            divide(a, b)

    elif secim == 6:
        print("Cikis yapiliyor...")
        break
    else:
        print("choose number between 1-6!")