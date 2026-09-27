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