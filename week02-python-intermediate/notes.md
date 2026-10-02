## File Handling
- Bir dosya oluşturduktan sonra onun yerini değiştirmediğimde tekrar o isimde "w" modunda bir dosya oluşturduğumda eski dosya geri dönmemek üzere siliniyor ama oluşturulduğu klasör veya masaüstünden yerini değiiştirdiğimde o dosya korundu. Her zaman işe yarar mı bilmiyorum şu an ama gözlemim bu şekilde olduğu için aktarıyorum.
- "a" modu ile dosyaya bir şey eklemek istedim ama yerini değiiştirdiğim dosyaya eklenmedi, tekrar o konumda dosya oluştu ve eklediğim yazı da dosyada vardı.
- readlines() fonksiyonu bir dosyadaki tüm satırları okuyup bir liste halinde döndürür. Her bir satır listenin birer elemanıdır.Satırları tek tek işlemek için uygundur.
- "r+" modunda dosyaya bir şey ekleyince başa ekliyor(sanırım[imleç neredeyse ekliyor da olabilir])

## Exception Handing

- syntax Errors: Python'da 'parsing error' ifadesi kullanılır. Dil bilgisel hataları ifade eder. Programın çalışma mantığına henüz bakılmamıştır.

- Exception: Yazılan kod hatasız bir sytax ile çalıştırıldıktan sonra problem çıkıyor bunlara exception diyoruz. Program normal biçimde çalışırken ortaya çıkan ve normal kontrol akışını bozan olağan dışı durum olarak da tanımlayabiliriz. Çok karşılaşılan exception türleri:
    1. ZeroDivisionError: Bir sayıyı sıfıra bölmeye çalıştığımızda ortaya çıkar.
    2. ValueError: Doğru türde bir işlem istiyorsun ama verdiğin değer uygun değilse yanı data türü ile gereken tür farklıysa ortaya çıkar. sayi = int("Hello")
    3. TypeError: İşlem açısından türler uyuşmadığında ortaya çıkar. Örneğin: "10" + 5  burada "10" bir str olduğu için error verir.
    4. NameError: Bir değişken ismi ile işlem yatıysan ama henüz değişkeni tanımlamadıysan oluşan hatadır.
    5. IndexError: Bir liste veya bir benzerinde içinde bulunmayan bir index ile işlem yapmaya kalkarsan oluşacak hata mesajıdır.

Bütün bunları düşününce yazdığımız bir programın çökmemesi için exception handling yaparız. Temel yapı:
    try:
        # hata oluşturabilecek kod
 
    except SomeException:
        # hata oluşursa yapılacak işlem
Bu yapı hatayı yok etmez, hatayı yönetir.
- Bu yapıya else ekleyebiliriz:
    try:
        number = int(input("Sayı: "))
 
    except ValueError:
        print("Geçersiz sayı.")
 
    else:
        print("Her şey başarılı.")
Else bloğu try bloğu exception üretmeden tamamlanırsa çalışır.
- Finally yapısı: Bu yapı ister exception olsun ister olmasın yine de çalıştırılır.Python dokümantasyonu finally yapısını temizleme işlemleri gibi mutlaka yürütülmesi gereken davranışlar için açıklar.
- Raise yapısı: Yukarıda bahsettiklerimin hepsi pythonun oluşturduğu exceptionlardı, kendimiz exception oluşturmak istediğimizde ise bu yapıyı kullanırız.Örneğin yaş isteyen bir program olsun:
    age = -5  # Runtime olarak aslında doğru ama yaş negatif olamayacağı için yanlış
 
    if age < 0:
        raise ValueError("Yaş negatif olamaz.")
- Try-Except ile raise yapısının mantığını birbirnin tersi gibi düşünebiliriz aslında matematiksel olarak ters değillerdir. Raise: exception oluşturur ve dışarı göderir. Except: exception yakalar ve karşılar. Görsellştirmek gerekirse:
    Fonksiyon
        │
        │ raise ValueError
        │
        ▼
        Exception
        │
        ▼
        except ValueError
        │
        ▼
        handle

- Syntax error ≠ Runtime error ≠ Exception:
    1. Syntax Error: "Yazdığın şeyi Python dili açısından anlayamıyorum."
    2. Runtime Error: "Kodunu anlayabildim, fakat çalıştırırken bir problem meydana geldi."
    3. Exception: "Çalışma sırasında ortaya çıkan olağan dışı durumu bir nesne/tür sistemi üzerinden temsil ediyorum ve bu durum yakalanıp yönetilebilir."

* except ValueError: ile except Exception: arasındaki fark nedir?
    İlkinde spesifik bir sorunu ele alırız, ikincisinde ise genel olarak oluşacak tüm sorunları ele alırız. Mantıken ikinciyi kullanmak dah iyi gibi gözükse de pratikte pek kullanışlı olmaz çünkü genel olduğu için hatalı diyeceğiz ama hatayadan bahsedemeyeceğiz. Bu sebeple kullanırken tek tek spesifik hataların exceptionlarını verdikten sonra genelolarak başka hata varsa diye 'except exception:' yapılmalı. Önce spesifik olanların sonra genel exception kullanmak önemli çünkü eğer başta kullanırsak o yazdığımız spesifik hatalar da içine girer.

# Moduls and Imports
## 1. Module Nedir? 
Python'da bir **module**, içerisinde Python kodları bulunan `.py` dosyasıdır.
Bir modül içerisinde şunlar bulunabilir:
- Değişkenler
- Fonksiyonlar
- Class'lar
- Sabitler
- Başka modüllerden yapılan importlar
Amaç, büyük programları daha küçük ve yönetilebilir dosyalara bölmek ve aynı kodu tekrar tekrar yazmamaktır.
## 2. import
Başka bir Python modülündeki kodları kullanabilmek için import kullanılır.
Temel kullanım:
    import math

    print(math.sqrt(25))
    print(math.pi)

Burada modülün içindeki öğelere ulaşırken:
    module_name.item
    şeklinde kullanılır.
Bu kullanım özellikle kod büyüdüğünde sqrt, pi gibi isimlerin nereden geldiğini açıkça gösterdiği için okunaklıdır.

## 3. from ... import ...
Bir modülün tamamını değil, sadece ihtiyacımız olan belirli öğeleri almak için kullanılır.Örneğin:
    from math import sqrt
    print(sqrt(25))
Artık:
    math.sqrt(25)
yazmak yerine doğrudan:
    sqrt(25)
yazabiliriz.
Birden fazla öğe de alınabilir:
    from math import sqrt, pi
     
    print(sqrt(16))
    print(pi)

## 4. import ... as ...
Bir modüle farklı veya daha kısa bir isim vermek için as kullanılır.
    import math as m
     
    print(m.sqrt(25))
    print(m.pi)
Genel yapı:
    import module_name as alias
Başka örnekler:
    import numpy as np
    import pandas as pd
as, modülün gerçek adını değiştirmez. Sadece bulunduğumuz dosya içerisinde kullanacağımız bir takma ad oluşturur.

## 5. from ... import ... as ...
Modülün içerisindeki belirli bir öğeye de takma isim verebiliriz.
    from math import sqrt as square_root
 
    print(square_root(25))
Genel yapı:
    from module_name import item as alias

## 6. import *
Bir modül içerisindeki birçok ismi doğrudan mevcut dosyaya aktarır.
    from math import *
 
    print(sqrt(25))
    print(pi)
Ancak genellikle kullanılması önerilmez.Çünkü hangi fonksiyonun veya değişkenin hangi modülden geldiğini anlamayı zorlaştırabilir ve isim çakışmalarına neden olabilir.
Bunun yerine:
    import math
veya:
    from math import sqrt, pi
daha açıktır.

## 7. Kendi Modülümüzü Oluşturmak
Her .py dosyası başka bir Python dosyası tarafından modül olarak kullanılabilir.
Dosya yapısı:
    project/
    │
    ├── main.py
    └── calculator.py

- calculator.py
    def add(a, b):
    return a + b
     
    def subtract(a, b):
    return a - b
     
    def multiply(a, b):
    return a * b
     
    def divide(a, b):
    return a / b

- main.py
    import calculator
     
    print(calculator.add(10, 5))
    print(calculator.multiply(4, 3))

## 8. Modülden Belirli Fonksiyonları Import Etmek
Modülün tamamını almak zorunda değiliz.
    from calculator import add, subtract
     
    print(add(10, 5))
    print(subtract(10, 5))
Bu durumda multiply() ve divide() import edilmemiştir.

## 9. Modüle Alias Vermek
Kendi oluşturduğumuz modüllerde de as kullanılabilir.
    import calculator as calc
     
    print(calc.add(10, 5))
    print(calc.divide(20, 4))

## 10. name
Python her module için otomatik olarak özel bir __name__ değişkeni oluşturur. Bir Python dosyasını doğrudan çalıştırdığımızda: __name__ == "__main__" olur.
Örnek:
    print(__name__)
Dosyayı direkt çalıştırırsak: __main__ çıktı olarak görürüz.

## 11. if name == "main"
Bir .py dosyasının hem doğrudan çalıştırılabilmesini başka bir dosyada module olarak kullanılabilmesini istediğimizde çok önemlidir.
- calculator.py
    def add(a, b):
        return a + b
     
    def subtract(a, b):
        return a - b
     
    if __name__ == "__main__":
    print(add(10, 5))
    print(subtract(10, 5))

Şimdi: calculator.py ile dosyayı doğrudan çalıştırırsak if içerisindeki kod çalışır. Ancak başka bir dosyada: import calculator yaparsak if __name__ == "__main__": içerisindeki kod çalışmaz.
Bu sayede modül içerisindeki test veya çalıştırma kodlarının import sırasında otomatik olarak çalışmasını engelleyebiliriz.

## 12. Module İçindeki Kodlar Import Sırasında Çalışabilir
Örneğin:
    test.py
    print("test.py çalıştı")
 
    def hello():
        print("Hello")
    main.py
    import test
main.py çalıştırıldığında: test.py çalıştı çıktısını görürüz. Çünkü Python modülü import ederken modül içerisindeki kodu yükler ve üst seviyedeki ifadeleri çalıştırır.
Bu yüzden çalıştırmaya özel kodları genellikle: if __name__ == "__main__":  içerisinde tutarız.

## 13. Built-in Modules
Python kurulduğunda beraberinde birçok hazır modül gelir. Bunlara Standard Library içerisindeki modüller denir.
* math: Matematiksel işlemler:
    import math
     
    print(math.sqrt(64))
    print(math.pi)
    print(math.ceil(4.2))
    print(math.floor(4.8))
* random: Rastgele değer üretme:
    import random
     
    print(random.randint(1, 10))
* datetime: Tarih ve zaman işlemleri:
    from datetime import datetime
     
    now = datetime.now()
    print(now)
* os: İşletim sistemi ve dosya/dizin işlemleriyle ilgili araçlar:
    import os
     
    print(os.getcwd())
## 14. Third-Party Modules
Bazı modüller Python ile birlikte gelmez. Bunların ayrıca kurulması gerekir. Örneğin:
- numpy
- pandas
- requests
Genellikle pip kullanılarak kurulur: pip install numpy 
Sonrasında normal şekilde import edilir: import numpy as np

## 15. ModuleNotFoundError
Python import etmek istediğimiz modülü bulamazsa: import something şuna benzer bir hata alınabilir: ModuleNotFoundError: No module named 'something' 
Olası nedenler:
- Modül kurulu değildir.
- Yanlış Python environment kullanılıyordur.
- Modül adı yanlış yazılmıştır.
- Kendi oluşturduğumuz .py dosyası Python tarafından bulunabilecek konumda değildir.
Örneğin üçüncü parti bir paket eksikse:
    pip install package_name
gerekebilir.

## 16. Package Nedir?
Bir module genellikle tek bir .py dosyasıdır. Bir package ise ilgili modülleri bir arada düzenlemek için kullanılan bir klasör yapısıdır. Örneğin:
    project/
    │
    ├── main.py
    │
    └── calculator/
        ├── __init__.py
        ├── basic.py
        └── advanced.py
Burada:
    basic.py
    advanced.py
modüllerdir.
calculator ise bunları organize eden package'dır.
Örneğin:
    from calculator.basic import add

## 17. Import Yöntemlerinin Özeti
* Tüm modülü yükle
    import math
     
    math.sqrt(25)
* Belirli bir öğeyi al
    from math import sqrt
     
    sqrt(25)
* Birden fazla öğeyi al
    from math import sqrt, pi
     
    sqrt(25)
    print(pi)
* Modüle alias ver
    import math as m
 
    m.sqrt(25)
* Öğeye alias ver
    from math import sqrt as square_root
 
    square_root(25)
* Kendi modülünden import et
    from calculator import add
 
    add(5, 3)

## 18. Module vs Package vs Library
Kavramları karıştırmamak önemli:
- Module
    ↓
    Tek bir Python dosyası
    calculator.py
 
- Package
    ↓
    Birden fazla modülü organize eden yapı
    calculator/
 
- Library
    ↓
    Belirli amaçlar için hazırlanmış daha geniş kod koleksiyonu

Özet olarak:
.py file → module
modules → package
packages/modules → library
Bu ayrım kavramsaldır; gerçek projelerde library ve package ifadelerinin kullanımı bağlama göre değişebilir.

## 19. İyi Kullanım
Modülün nereden geldiğinin açık olması için:
    import math
     
    result = math.sqrt(25)
oldukça okunaklıdır.
Sık kullanılan birkaç fonksiyon varsa:
    from math import sqrt, ceil
     
    result = sqrt(25)
kullanılabilir.
Kaçınılması gereken kullanım:
    from math import *
Çünkü hangi isimlerin mevcut namespace'e eklendiğini takip etmek zorlaşır.
Kısa Özet
import module
→ Tüm modülü import eder.
from module import item
→ Modülden belirli bir şeyi import eder.
import module as alias
→ Modüle takma isim verir.
from module import item as alias
→ Import edilen öğeye takma isim verir.
if __name__ == "__main__":
→ Dosya doğrudan çalıştırıldığında çalışacak kodları ayırmak için kullanılır.
.py file → Module
Module collection → Package
Broader reusable code collection → Library
Modüllerin temel amacı kodu:
    bölmek,
    düzenlemek,
    tekrar kullanılabilir hale getirmek,
    büyük projelerin yönetimini kolaylaştırmaktır.

# OOP BASİCS
## OOP Nedir?
Nesne yönelikli programlama, programı nesneler ve bu nesnelerin özellikleri ile davranışları etrafında düzenlyen bir programlama yaklaşımıdır. Örneğin bir öğrenci nesnesi:
    - Attributes(Özellikler): Ad, soyad, numara, notlar
    - Methods(Davranışlar): Not hesaplama, bilgileri gösterme

## Temel Kavramlar
* class: Nesnelerin yapısını tanımlayan şablon
* Object: Sınıftan oluşturulan somut örnek
* Attribute: Nesnenin sahip olduğu veri
* Method: Sınıf içinde tanımlanan fonksiyon
* Instance: Bir sınıfın oluşturulmuş örneği

!!! Procedural ve OOP yaklaşımı:
     Aynı problemi dictinory ve class ile yazılmasını ifade ediyor. Fonksiyon ve dic ile yazmak mı yoksa oop yaklaşımıyla class oluşturmak mı daha faydalı olacağı uzerinde kafa yorma yaklaşımıdır. Amaç, OOP'nin her zaman daha iyi olduğunu düşünmek değil; hangi yaklaşımın hangi durumda faydalı olduğunu anlamaktır.
## __init__ metodu
Bir nesne oluşturulduğunda başlangıç değerlerini belirlemek için kullanılan özel metottur.
- Ne zaman çalışır? Bir sınıftan bir nesne oluşturulduğunda otomatik çalışır.
- Parametreleri nasıl tanımlanır? self parametresinden sonra istediğiniz parametreyi ekleyebiliriz. def __init__(self, parametre1, parametre2)
- Nesnenin başlangıç özellikleri naıl belirlenir?  Parametrelerden gelen değerleri self kullanarak nesnenin özelliklerine atarız. def __init__(self, parametre):  self.değişken = parametre

## self kavramı
self kavramı sınıfın mevcut nesnesini temsil eder. Bir nesnenin kendi verilerine ve metotlarına erişmesini sağlar. Bu mevcut nesne class olunca otomatik oluşturulan default nesnedir.
- Neden ilk parametre olduğuna gelirsek, Python bir nesnenin metodunu çağırdığında, o nesneyi otomatik olarak ilk parametre olarak gönderir. Örneğin: 
    class person:
        def selam_ver(self):
            print("Merhaba")
    kisi1 = person()
    kisi1.selam_ver()
Python bunu arka planda şöyle yorumlar: person.selam_ver(kisi1) yani person class'ındaki selam_ver() metodunun ilk parametresi olur. Yani kisi1 nesnesi otomatik olarak ilk parametreye gönderilir. Bu yüzden ilk parametrenin adı genellikle self olur.
- İki farklı nesnenin özellikleri nasıl birbirinden bağımsız tutulur? Bu soruyu soruyorum çünkü bunu self yapar. Her nesne bellekte ayrı bir alanı vardır ve self sayesinde her nesne kendi verisini saklar.

## Istance Attributes ve Istance Methods
Bu konu, bir nesnenin neleri bildiğini ve neler yapabildiğini anlamamızı sağlar.
- Instance Attribute (Örnek Özniteliği): Nesneye ait veri veya özellik.
- Instance Method (Örnek Metodu): Nesne üzerinde işlem yapan fonksiyon.
Bir insanı düşünün: Adı, yaşı, boyu özellikleridir yani Attributes; yürümek, koşmak, yemek yemek ise davranışlarıdır yani Methods.

# Encapsulation( Kapsülleme )
Encapsulation, bir nesnenin: verilerini(attributes), bu verilere erişen metotları(methods) tek bir yapı içinde toplama ve veriye erişimi kontrollü hale getirme prensibidir. Basitçe: Nesnenin iç detaylarını sakla, dış dünyaya yalnızca gerekli olan kısmı göster. Encapsulation gerekli olma sebebi yania amacı:
- Veri Güvenliği: Hatalı değişikleri önlemek
- Kontrol: Veri üzerinde kurallar koymak
- Bakım Kolaylığı: Kodun iç yapısını değiştirebilmek
- Hata Azaltma: Geçersiz değerlerin atanmasını engellemek

Encapsulation erişim kontrolü sağlıyor ve bunu isimlendirmedeki bazı kurallar yardımıyla yapıyor. Bu kurallar erişim belirleyicilerdir.
# Erişim Belirleyiciler
Python'da C++ ve Java gibi public/protected/privite yapıları yoktur bunu erişim belirleyiciler yardımıyla yapıyoruz.
* Public Attribute(name): Tek alt çizgisiz isimdir.Örneğin:
    class Person:                Kullanımı:
        def __init__(self):                 p = Person()
        self.name = "Hatice"                print(p.name)
                                            p.name = "Ali"
* Protected Attribute(_name): İsimlendirmeden önce tek çizgi kullanırsın. Bu bir kuraldır ve Python "Buna erişebilirsin ama erişmemelisin." demeye çalışır. Yani gerçek protected değil lütfen dokunma uyarısıdır.
* Private Attribute(__name): İsimlendirirken çift alt çizgi kullanırsın.Örneğin:
    class person:
        def __init__(self):
            self.__name = 'Hatice'
    p = person()
    print(p.__name)   ##AttributeError der
Python burada 'name mangling' uygular.
# Name Mangling
Name mangling ile tamamen gizleyemeyiz sadece yanlışlıkla erişilmesiini zorlaştırabilriz. Name mangling'e takılmadan private attribute'lara ulaşmak için:
    class Person:
        def __init__(self):
        self.__name = "Hatice" 
    p = Person()
    print(p._Person__name)    # Çıktı: Hatice
# Getter ve Setter Mantığı
Diğer dillerde çok yaygındır(C++ ile aynı mantık). Kullanımlarına tam örnek verirsek:
class BankAccount:                  Kullanımı:
    def __init__(self):                  acc = BankAccount()
        self.__balance = 0               acc.set_balance(1000)
    def get_balance(self):               print(acc.get_balance())
        return self.__balance            # Çıktı: 1000
    def set_balance(self, amount):
        if amount >= 0:
        self.__balance = amount
# @property
Modern Python'da getter/setter yazmanın daha güzel yolu vardır. @property bir özelliğe kontrollü erişim sağlamak için kullanılır.Örnekte göstermek istersek:
class BankAccount:                         Kullanımı:
    def __init__(self):                       acc = BankAccount()
        self.__balance = 0                    acc.balance = 100
                                              print(acc.balance)
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Negatif değer!")
        self.__balance = value
DİKKAT: Getter/setter çalışıyor ama kullanım normal attribute gibi görünüyor.

# class attributes ve instance attributes
Bir benzetmeyle anlatırsak eğer class'ı bir apartman olarak düşünelim: class student: ... 
Bu apartmandaki daireler ise nesneler(objects): s1 = student(), s2 = student()
Bu benzetmeyi düşünerek:
* Instance Attributes: Her nesneye özel olarak tutulan özelliklerdir. Genellikle __init__iinde oluşturulur.
    class student:
        def__init__(self, name):
            self.name = name      # self.name bir instance attributes
Eğer nesneleri oluşturursak:
    s1 = student("Hatice")
    s2 = student("Beyza")
    s3 = student("Murat")
bunların her biri bellekte kendilerine ait birer kopyaları olur çünkü bunlar dairelerin kendisine ait yani her nesne kendi verisini taşır.
* Class Attributes: Sınıfa ait olan ve tüm nesneler tarfından ortak kullanılan özelliktir. Sınıf seviyesinde tanımlanır.
class Student:

    school = "Oxford"   #class attributes

    def __init__(self, name):
        self.name = name
Oluşturulan tüm nesneler onu kullanır bu yüzden de class içinde sadece bir kere yazılır. Bellek görüntüleri: 
Student Class
 └── school = Oxford

s1
 └── name = Hatice

s2
 └── name = Ali

s3
 └── name = Ayşe

ÖNEMLİ TEHLİKE: SHADOWİNG(GÖLGELEME):
class student.
    school = "Oxford"
s1 = student()
print(s1.school)     # çıktı: Oxford    // sınıftan okuyor
s1.school = "MIT"   // class att. değişmedi python yeni bir instance att. oluşturdu.
print(s1.school)    # çıktı: MIT
print(student.school)  #çıktı: oxford
bellek görüntüsü:
Student
 └── school = Oxford

s1
 └── school = MIT
buradan da gördüğümüz üzere python bir nesne attribute ararken şu sırayı izler:
1. Nesnenin içinde ara
2. Sınıfta ara
3. Parent sınıflarda ara
# @classmethod kullanımı
@classmethod, ilk parametre olarak nesneyi(self) değil, sınıfı(cls) alan methottur. Eğer class attribute'larla çalışıyorsak nesneyi değil sınıfı bilmemiz gerekir. Class method, sınıf seviyesindeki verilere erişmek veya sınıfı kullanarak yeni nesneler üretmek için kullanılan metottur.Pratikte iki temel kullanım alanı vardır:
1. Class attribute yönetimi
2. Alternatif constructor (alternatif nesne oluşturma)
İkinci kullanım çok daha önemlidir.
* Class Attribute Yönetmek
class Student:                            Kullanımı:
    school = "Oxford"                        Student.change_school("MIT")
                                             print(Student.school)  # çıktı: MIT doğrudan sınıf değişkeni değiiştirildi. Hiç nesne olluşturulmadı.
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
* @classmethod ile Alternatif Constructor
class Person:
                                         Kullanımı:
    def __init__(self, name, age):             p1 = person("Hatice", 25)
        self.name = name                       p2= person.from_string("Ali-30")
        self.age = age

    @classmethod
    def from_string(cls, data):

        name, age = data.split("-")

        return cls(name, int(age))
Bellekte şöyle tutulur:
Person.from_string("Ali-30")
          ↓
name = Ali
age = 30
          ↓
Person("Ali",30)
          ↓
Yeni nesne
- örnekte olduğu gibi iki farklı bilgi girmesi gerekirken tek bir text giriyor biz de onu olması gereken formata çeviriyoruz.

# @staticmethod kullanımı
@staticmethod, sınıfın içinde bulunan ancak ne nesneye(self) ne de sınıfa(cls) ihtiyaç duyan metottur.Örneğin:
class Math:
                           Kullanımı:
    @staticmethod              print(Math.add(3,5))   #Çıktı: 8
    def add(a, b):
        return a + b
Bu methotu yazmaktansa fonksiyon yazabilirdik ama yaptığımız metot mantıksal olarak o sınıfa aittir.

## Inheritance(Kalıtım)
Kalıtım, bir sınıfın başka bir sınıfın özelliklerini(attributes) ve davranışlarını(methods) devralmasıdır. Gerçek hayatta düşünürsek: Hayvan adında bir class'ımız var ve isim, yaş ve nefes al() özelliklerine ve davranışlarına sahip sonuç olarak her hayvan buna sahiptir. Bir de köpek class'ı oluşturalım. O da bir hayvan oluğu için adı, yaşı vardır ve nefes alıyordur. Bu yüzden köpek Class'ta animal class'ından yararlanır, köpek sınıfı Animal sınıfından kalıtımsal miras alır.
* Parent Class(Üst Sınıf): Özellikleri sağlayan sınıftır. Base veya superclass da kullanılır. Kalıtımı sağlayan, özelliklerinden yararlanılan, paylaşan sınıftır.
* Child Class(Alt Sınıf): Üst sınıftan miras alan sınıftır. Derived veya subclass da denir.
Hiyerarşi:
Animal
   │
   ├── Dog
   ├── Cat
   └── Bird

class Animal:
    def __init__(self, name):
        self.name = name
    def breathe(self):
        print("Nefes alıyor")
class Dog(Animal):
    pass
dog = Dog("Karabas")
dog.breathe()

Inheritance'ın avantajları nelerdir?
1. Kod tekrarını azaltır: Her özelliği tekrar tekrar her classta yazmaktansa üst sınıfta yazıp diğerlerinde kullanırız.
2. Bakımı kolaylaştırır: Bier değişiklik gerektiğinde yalnızca üst sınıf değiştirilir.
Alt sınıfın üst sınıfın metotlarına erişebildiğini söyledik peki ama nasıl?
# super() Fonksiyonu
Bu fonksiyon ile alt sınıf üst sınıfın metotlarına erişebilir. 
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   #Animal.__init__(name)'i çağırmış olur. Yani Dog içinden Animal'ın kurucusu çalıştırılır.
        self.breed = breed

# Method Overriding(Metot Ezme)
Üst sınıftan gelen bir metodun alt sınıfta yeniden tanımlanmasıdır.Yani:
"Bu davranışın genel hali var ama ben kendi sınıfım için özel davranış istiyorum.". Örneğin:
    class Animal:
        def make_sound(self):
            print("Bir ses çıkarıyor")

    class Dog(Animal):
        def make_sound(self):
            print("Hav hav!")
Animal'daki metod çalışmaz. Çünkü Dog onu override etmiştir. Burada override neden gerekli? Çünkü her hayvan ses çıkarır ama her biri farklı şekilde işte bu yüzden üst sınıf genel davranışı tanımlar, alt sınıflar özelliştirir.
# super() ile Overriding Birlikte
Üst sınıf davranışını koruyup genişletebiliriz.
    class Animal:                     Çıktı:
        def make_sound(self):             ses çıkartıyor.
            print("Ses çıkarıyor")        Hav hav

    class Dog(Animal):
        def make_sound(self):
            super().make_sound()
            print("Hav hav")
Önce animal sonra dog bölümü çalıştı.
# Overriding ve Overloading Farkı
Bu ikisi çok karıştırılır.
- overriding alt sınıf mevcut metodu değiştirir.
    class Dog(Animal):
    def make_sound(self):
        pass
- overloading ayni isimli metodun farklı parametrelerle kullanılmasıdır.
    add(a,b)
    add(a,b,c)
Python'da gerçek anlamda metod overloading yoktur. Varsayılan parametreler veya *args kullanılır.
# Polymorphism(Çok Biçimlilik)
Bir nesnenin farklı şekillerde davranabilmesidir. Aynı metot çağrısı farklı nesnelerde farklı sonuçlar üretebilir.
class Dog:
    def make_sound(self):           Çıktı:
        print("Hav hav")                Hav hav
                                        Miyav
class Cat:
    def make_sound(self):
        print("Miyav")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()  # Kod aynı kaldı ama her nesnede davranışı değişti işte buna polymorphism diyoruz.

## Composition(Bileşim)
Bir nesnenin başka nesneleri kendi içinde kullanmasıdır. Bunu şu şekilde düşünebiliriz: Car has an Engine / Araba motora SAHİPTİR. Ama car bir engine değildir.

Bu ilişkileri bir kurala göre belirliyoruz:
1. IS-A İlişkisi
Dog is an animal    # kalıtım
2. Has-A İlişkisi
Car has an engine   # Composition

Bir yazılım mimarı gözüyle bakarsak, iyi tasarlanmış sistemlerin büyük çoğunluğu Composition üzerine kuruludur, kalıtım ise yalnızca gerçekten güçlü bir "is-a" ilişkisi varsa kullanılır. Bu yüzden modern frameworklerde sıkça duyacağın prensip şudur:
"Kalıtım davranışı miras alır, Composition ise yetenekleri bir araya getirir."
Ve çoğu zaman yetenekleri bir araya getirmek, yani Composition, daha esnek ve daha sürdürülebilir bir tasarım sağlar.