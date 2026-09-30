# 1. Product sınıfı oluştur. Ürün adı ve fiyatı olsun.
# 2. Fiyatın negatif olmasını engelle.
# 3. Fiyat özelliğini @property ile yönet.
'''class Product:
    def __init__(self, isim , fiyat):
        self.isim = isim
        self.fiyat = fiyat

    @property
    def fiyat(self):
        return self.__fiyat

    @fiyat.setter
    def fiyat(self, value):
        if value < 0:
            raise ValueError("Fiyat negatif olamaz!")
        self.__fiyat = value

product1 = Product("Laptop", 50000)
print(product1.isim)
print(product1.fiyat)
product1.fiyat = 55000

# 1. Employee sınıfında ortak şirket adını class attribute olarak tut.
# 2. Her çalışanın adını ve maaşını ayrı instance attribute olarak tut.
# 3. @classmethod ile sınıf için alternatif bir nesne oluşturma yöntemi yaz.
# 4. @staticmethod ile bir sayının pozitif olup olmadığını kontrol eden yardımcı metot oluştur.
# 5. Class attribute ile instance attribute farkını deneyerek gözlemle.
class Employee:
    company_name = "Microsoft"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        return cls(name, int(salary))

    @staticmethod
    def is_positive(number):
        return number > 0

emp1 = Employee("Hatice", 70000)
emp2 = Employee("Ali", 60000)
print(emp1.name)
print(emp1.salary)
print(emp2.name)
print(emp2.salary)
print(Employee.company_name)
# CLASSMETHOD TESTİ
emp3 = Employee.from_string("Ayşe-80000")
print(emp3.name)
print(emp3.salary)
# STATICMETHOD TESTİ
print(Employee.is_positive(10))
print(Employee.is_positive(-5))
# CLASS vs INSTANCE
# ATTRIBUTE FARKI
print(emp1.company_name)
print(emp2.company_name)
Employee.company_name = "Google"
print(emp1.company_name)
print(emp2.company_name)
emp1.name = "Zeynep"
print(emp1.name)
print(emp2.name)'''

## MİNİ GÖREV: ÜRÜN VE STOK YÖNETİMİ
'''Gereksinimler:
1. Ürün adı, fiyatı ve stok miktarı tutulmalı.
2. Ürün fiyatı negatif olamamalı.
3. Stok miktarı negatif olamamalı.
4. Stok artırma ve azaltma metotları bulunmalı.
5. Yeterli stok yoksa satış yapılamamalı.
6. Ürün bilgileri ekrana yazdırılmalı.
İsteğe bağlı: Birden fazla ürünü listede tut ve toplam stok değerini hesapla.'''
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Fiyat negatif olamaz!")
        self.__price = value

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stok negatif olamaz!")
        self.__stock = value

    def increase_stock(self, amount):
        if amount > 0:
            self.__stock += amount

    def decrease_stock(self, amount):
        if amount <= 0:
            return

        if amount > self.__stock:
            print(f"{self.name}: Yetersiz stok!")
        else:
            self.__stock -= amount
            print(f"{amount} adet satis yapildi.")

    def show_info(self):
        print(
            f"Urun: {self.name} | "
            f"Fiyat: {self.price} TL | "
            f"Stok: {self.stock}"
        )

products = [
    Product("Laptop", 50000, 10),
    Product("Telefon", 30000, 15),
    Product("Tablet", 20000, 8)
]

print("ÜRÜNLER")
for product in products:
    product.show_info()

products[0].decrease_stock(3)
products[2].decrease_stock(50)
products[1].increase_stock(5)

total_value = 0

for product in products:
    total_value += product.price * product.stock

print("Toplam Stok Değeri:", total_value, "TL")