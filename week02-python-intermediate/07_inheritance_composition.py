# 1. Animal üst sınıfını oluştur. 
# 2. Dog ve Cat alt sınıflarını oluştur. 
# 3. Her alt sınıfta make_sound() metodunu yeniden tanımla. 
# 4. super() kullanarak üst sınıfın __init__() metodunu çağır.
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Bir ses cikariyor!")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print("Hav hav")
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print("Miyav")

dog1 = Dog("Macar")
dog1.make_sound()
cat1 = Cat("Tomris")
cat1.make_sound()
# 1. Vehicle sınıfı oluştur. Car ve Motorcycle sınıfları bundan türesin. 
# 2. Engine sınıfı oluştur ve Car sınıfı içinde kullan.
class Vehicle:
    def __init__(self):
        pass
    def drive(self):
        print("Arac gidiyor!")
class Engine:
    def start(self):
        print("Motor calisti!")
class Car(Vehicle):
    def __init__(self):
        super().__init__() 
        self.engine = Engine()
    def drive(self):
        print("Araba gidiyor!")
class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__()
    def drive(self):
            print("Motor gidiyor!")

car = Car()
print(car.drive)
motor = Motorcycle()
print(motor.drive())

# 1- Library sınıfının birden fazla Book nesnesini tuttuğu bir yapı oluştur.
# 2- Aynı metodu farklı sınıfların nesneleri üzerinde çağırarak polymorphism kavramını gözlemle.
class Library:
    def __init__(self, name, yazar, pages):
        self.name = name
        self.yazar = yazar
        self.pages =pages
    def show_info(self):
        print("{}-{}-{}".format(self.name, self.yazar, self.pages))
book1 = Library("Atomik Aliskanliklar", "James Clear", 333)
book2 = Library("Kardesimin Hikayesi", "Livaneli", 150)
book3 = Library("Sinirsiz Zihin", "Jo Boelar", 450)
book1.show_info()
book2.show_info()
book3.show_info()

## MİNİ PROJE: ÇALIŞAN YÖNETİM SİSTEMİ
# 1. Employee adlı bir üst sınıf oluştur.
# 2. Çalışanın adı, soyadı ve maaşı olsun.
# 3. Manager ve Developer sınıfları Employee sınıfından türesin.
# 4. Her alt sınıfın kendine özgü bir metodu olsun.
# 5. Çalışan bilgilerini gösteren ortak bir metot bulunsun.
# 6. Alt sınıflar ortak metodu gerektiğinde yeniden tanımlasın.
# 7. Bir Department sınıfı oluştur ve içinde çalışan nesnelerini tut. 
# Bu görevde composition kullan.
class Employee:

    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas

    def show_info(self):
        print("{} {} - {}".format(self.ad, self.soyad, self.maas))
        
class Manager(Employee):

    def __init__(self, ad, soyad, maas):
        super().__init__(ad, soyad, maas)

    def show_info(self):
        print("=== Yönetici Bilgileri ===")
        super().show_info()

    def make_meeting(self):
        print(f"{self.ad} toplanti duzenliyor.")

class Developer(Employee):

    def __init__(self, ad, soyad, maas):
        super().__init__(ad, soyad, maas)

    def show_info(self):
        print("=== Yazilimci Bilgileri ===")
        super().show_info()
   
    def write_code(self):
        print(f"{self.ad} kod yaziyor.")

# COMPOSITION
class Department:

    def __init__(self, departman_adi):
        self.departman_adi = departman_adi
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        print(f"\n{self.departman_adi} Departmanı")
        print("-" * 30)

        for emp in self.employees:
            emp.show_info()
        print()
# Nesneler
manager = Manager("Ahmet", "Yilmaz", 50000)
developer = Developer("Ayse", "Demir", 40000)
# Özel metotlar
manager.make_meeting()
developer.write_code()
print()
# Composition kullanımı
it_department = Department("Bilgi Teknolojileri")
it_department.add_employee(manager)
it_department.add_employee(developer)
it_department.list_employees()