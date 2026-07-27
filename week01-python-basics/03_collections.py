#görev-4
meyveler = ['muz', 'kiraz', 'erik', 'elma', 'kivi']
meyveler.append('mandalina')
print(meyveler)
meyveler.remove('elma')
print(meyveler)
meyveler[2] = 'armut'
print(meyveler)
meyveler.pop(-1)
print(meyveler)
meyveler.sort()
print(meyveler)
meyveler.reverse()
print(meyveler)
#görev-5
tuple_1 = ('matematik', 'fizik', 'Resim', 'edebiyat')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
#tuple_1[0] = 'muzik'
#print(tuple_1) 
# tuples are immutuble so TypeError: 'tuple' object does not support item assignment

#görev-6
sets = {'kalem', 'kagit', 'silgi', 'uc', 'kalem'}
print(sets)  #Sets duplicate elemanları kaldırır çünkü matematiksel küme gibi çalışır, yalnızca benzersiz elemanları barındırır.

#görev-7
student = {'isim': 'Hatice', 'soyisim': 'can', 'yas': 20, 'bolum': 'Yazilim Muh.', 'ortalama': 3.68}
student.update({'numara': 240229050})
print(student)
student.update({'yas': 19})
print(student)
del student['yas']
print(student)
for key in student:
    print(key)
for item in student.items():
    print(item)
for deger in student.values():
    print(deger)

#mini günlük görev
isim = input("Isminiz: ")
soyisim = input("Soyisiminiz: ")
yas = input("Yasiniz: ")
uni = input("Universite: ")
bolum = input("Bolumunuz: ")
student = {'isim': isim, 
           'soyisim': soyisim, 
           'yas': yas, 
           'universite': uni, 
           'bolum': bolum
        }
print("=======Ogrenci Bilgileri=======\n")
for key, deger in student.items():
    print(f"{key:<12} : {deger}")
print("\n==============================")