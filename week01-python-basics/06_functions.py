# Konu 1: basit fonksiyon
def greet():
    ...

greet()

def selam_ver():
    print("Selam!")

def bolum():
    print("Yazilim Muhendisligi ogrencisiyim.")

def basladim():
    print("Python ogrenmeye basladim.")

selam_ver()
bolum()
basladim()

#konu 2: Parametereler

def square(number):
    return number * number

def cube(number):
    return number * number * number

def sum_numbers(a,b):
    return a + b

print(square(3))
print(cube(5))
print(sum_numbers(10,4))

# Konu 3: return vs print()

def add(a,b):
    print(a + b)

def add(a,b):
    return a + b

result = add(5,3)
print(result)   # REturn değeri kullanmamız için döndürmüş olur biz onu bir variable a atayabilir ya da farklı işlemlerde kullanabiliriz ama print dersek sadece ekrana yazar ve fonksiyon dışında o değeri kullanamayız.

# Konu 4: Birden Fazla Parametre
def calculate_average(a,b,c):
    sum = a + b + c
    return sum / 3

def calculate_area(width, height):
    return width * height

def calculate_age(birth_year, current_year):
    return current_year - birth_year

print(calculate_age(2006,2026))
print(calculate_area(34,10))
print(calculate_average(12,12,23))

#konu 5: Default Parameters

def greet(name, message = "Hello"):
    print(name, message)

greet("Hatice")
greet("Hatice", "Welcome")

# Konu 6: Keyword Arguments

def student_info(name, age, department):
    print(f"Isim: {name}")
    print(f"Yas: {age}")
    print(f"Bolum: {department}")

student_info("Beyza", 20, "dis")
student_info(department = "Yazilim", age = 20, name = "Hatice")

#konu 7: Scope

def fonksiyon():
    x = 10  # local variable
    print(x)

fonksiyon()
#print(x)  # Hata: x tanımlı değil

y = 5  # global variable

def fonksiyon():
    global y
    y = 20
    print("Fonksiyon ici:", y)

fonksiyon()
print("Fonksiyon disi:", y)

# ALIŞTIRMALAR
#1- pozitif/negatif/ sıfır
def check_number(number):
    if number < 0:
        print("Sayi negatiftir.")
    elif number > 0:
        print("Sayi pozitiftir.")
    else:
        print("Sayi sifirdir.")

check_number(8)

# 2- Cift / Tek
def is_even(number):
    if number % 2 == 0:
       print("Sayi cifttir.")
    else:
       print("Sayi tektir.")

# 3- En büyük Sayı

def find_max(a, b, c):
    max = a
    if max < b:
        max = b
    elif max < c:
        max = c
    return max

print(find_max(12,23,21))

# 4- faktöriyel

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(6))

# 5- Asal Sayı Kontrolü

def is_prime(sayi):
    if sayi > 1:
        asal_mi = True
    
        for i in range(2, sayi):
            if sayi % i == 0:
                asal_mi = False
                break

    return asal_mi

print(is_prime(7))

# 6- Not Hesaplama

def calculate_grade(score):
    if score >= 90:
        print("AA")
    elif 80 <= score < 90:
        print("BA")
    elif 70 <= score < 80:
        print("BB")
    elif 60 <= score < 70:
        print("CB")
    elif 50 <= score < 60:
        print("CC")
    else:
        print("FF")

calculate_grade(97)

# MİNİ PROJE: ÖĞRENCİ NOT SİSTEMİ

#calculate_average()
def calculate_average(midterm,final):
    return (midterm + final) / 2 

# calculate_grade()
def calculate_grade(score):
    if score >= 90:
        return "AA"
    elif 80 <= score < 90:
        return "BA"
    elif 70 <= score < 80:
      return "BB"
    elif 60 <= score < 70:
        return "CB"
    elif 50 <= score < 60:
        return "CC"
    else:
        return "FF"
# is_passed()
def is_passed(score):
    if score > 50:
        return True
    else:
        return False

# print_student_info
def print_student_info(name, midterm, final):
    score = calculate_average(midterm, final)
    print("======= STUDENT INFO =======\n")
    print("Name      : ",name)
    print("Midterm   : ",midterm)
    print("Final     : ", final)
    print("Average   : ", score)
    print("Grade     : ", calculate_grade(score))
    print("Status    : ", is_passed(score))
    print("\n============================\n")

isim = input("İsminiz: ")
midterm = int(input("Donem ici notunuzu girin: "))
final = int(input("Final notunuzu girin: "))

print_student_info(isim, midterm, final)