## List Comprehension(Liste Üreticileri)
Bir listenin elemanlarını dönüştürmek veya belirli bir koşula göre yeni bir liste inşa etmek için kullanılan yapısal bir araçtır. Bellek ve işlemci optimizasyonu açısından geleneksel döngülere kıyasla C seviyesinde daha optimize çalışır.
# Temel List Comprehension
Sadece bir döngü ve çalıştırılacak ifadeden oluşur.Örneğin:
    # 0'dan 9'a kadar olan sayıların karelerini hesaplama
    kareler = [x**2 for x in range(10)]
# Koşullu List Comprehension
Veri setini filtrelemek amacıyla döngünün sonunda bir if bloğu entegre edilir. Örneğin:
    # Sadece çift sayıların karelerini alma (Filtreleme işlemi)
    cift_kareler = [x**2 for x in range(10) if x % 2 == 0]
# if-else İçeren List Comprehesion
Dönüşüm mantığı bir koşula bağlıysa(örneğin duruma göre A veya B yap), if-else ifadesi döngüden önce, çıktı üretme aşamasında yazılır. Örneğin:
    # Çiftleri olduğu gibi bırak, tek sayıların yerine -1 yaz (Mapping/Dönüştürmme işlemi)
    degistirilmis = [x if x % 2 == 0 else -1 for x in range(10)]
# İç İçe Döngülerle List Comprehesion
Birden fazla for yapısı barındırır. Kartezyen çarpım veya veri bilimi süreçlerinde karşılaşılan matris düzleştirme(flatting) operasyonlarında sıklıkla kullanılır.Örneğin:
    matris = [[1, 2], [3, 4]]
    # 2D matrisi 1D listeye indirgeme (O(n^2) karmaşıklıkta)
    duz_liste = [eleman for satir in matris for eleman in satir]

## Dictionary Comprehension(Sözlük Üreticileri)
Anahtar-değer (key-value) çiftleri oluştururken döngü ve koşulları tek bir syntax içinde birleştirerek yapılandırmayı sağlar. Genellikle algoritmik arama tabloları (lookup tables) veya ters indeksleme işlemleri için idealdir.
# Yeni Sözlük Oluşturma:
    # Sayılar (anahtar) ve onların küpleri (değer)
    kupler_sozlugu = {x: x**3 for x in range(1, 6)}
# Mevcut Sözlükten Yeni Sözlük Üretme
Veri manipülasyonunda var olan bir mapping yapısını dönüştürmek için kullanılır. Örneğin:
    dolar_fiyatlar = {'sunucu_A': 100, 'sunucu_B': 250, 'sunucu_C': 400}
    # Kur dönüşümü (Örn: 1 USD = 34 TRY)
    tl_fiyatlar = {sunucu: fiyat * 34 for sunucu, fiyat in dolar_fiyatlar.items()} 
# Koşullu Sözlük Oluşturma
    # Maliyeti 200 dolardan yüksek olan sunucuları filtreleme
    pahali_sunucular = {sunucu: fiyat for sunucu, fiyat in dolar_fiyatlar.items() if fiyat > 200}

## Set Comprehension(Küme Üreticileri)
Matematiksel küme operasyonlarına (kesişim, birleşim) uygun, tekrarsız (unique) elemanlardan oluşan bir veri yapısı oluşturmayı sağlar. Syntax'ı liste üreticilerine benzer ancak köşeli parantez yerine süslü parantez {} gerektirir. Örneğin:
ham_veri = [1, 2, 2, 3, 4, 4, 4, 5]
    # Listedeki tekrarları eleyip, sadece tek sayıları tutan bir küme oluşturma
    tekil_sayilar = {x for x in ham_veri if x % 2 != 0} # Çıktı: {1, 3, 5}

## Normal Döngü ve Comprehesion Karşılaştırması
Yazılım mühendisliği süreçlerinde aynı işlemin hem for döngüsü hem de comprehension ile yazılması, okunabilirlik ve performans bağlamında önemli bir karar noktasıdır.
- Geleneksel for Dongüsü Paradigması:
    sonuclar = []
    for i in range(10):
        if i % 2 == 0:
            sonuclar.append(i * 2)
- Comprehension Paradigması:
    sonuclar = [i * 2 for i in range(10) if i % 2 == 0]
Karşılaştırma yapıldığında, comprehension yapısı append() metodunun arka plandaki çağrılma maliyetini (function call overhead) ortadan kaldırdığı için genellikle daha hızlı çalışır ve daha bildirimseldir (declarative). Okunabilirlik açısından da tek satırda niyetin açıkça belli olması bir avantajdır. Ancak iç içe üçten fazla döngü veya karmaşık algoritmik durumlar söz konusu olduğunda, kodun bakım edilebilirliğini (maintainability) sağlamak adına geleneksel döngülere dönülmesi tavsiye edilir.


### LAMBDA, MAP(), FİLTER() VE SIRALAMA
Bu fonksiyonel yapılar; özellikle listeler, sözlükler ve nesne listeleri üzerinde karmaşık veri operasyonları (data manipulation) yaparken işinize yarayacaktır.

## Lambda Fonksiyonları
Bilgisayar bilimlerinde "anonim fonksiyonlar" (anonymous functions) olarak da bilinen lambda fonksiyonları, tek bir ifade içeren küçük, isimsiz fonksiyonlardır. Bellekte kalıcı bir referans tutmalarına gerek olmayan, anlık kullan-at (throw-away) senaryoları için tasarlanmışlardır.
- Lambda söz dizimi: 'lambda argümanlar: ifade' şeklindedir. Örneğin:
    kare_al = lambda x: x ** 2
- Lambda ile normal fonksiyon karşılaştırması: Normal fonksiyonlar 'def' anahtar kelimesi ile kod bloğu ve 'return' ifadesi gerektirirken, lambda doğrudan sonucu döndürür.
    Normal: def topla(a, b): return a + b
    Lambda: topla_lambda = lambda a, b: a + b
- Lambda fonksiyonlarının uygun kullanım alanları: Genellikle map(), filter(), sorted() gibi "higher-order" (başka bir fonksiyonu argüman olarak alan) fonksiyonların içine argüman olarak gönderildiklerinde en uygun kullanım alanlarını bulurlar.

## map() Fonksiyonu
Veri mühendisliğinde projeksiyon (projection) olarak da geçen bu işlem, bir fonksiyonu bir koleksiyonun(collection) tüm elemanlarına sırasıyla uygulamak için kullanılır.
- map() nasıl çalışır?: İki argüman alır: Bir fonksiyon ve iterasyon yapılabilir bir koleksiyon(iterable). Fonksiyonu her bir elemana uygular.Örneğin:
    map(lambda x: x * 2, [1,2,3])  # 2. argüman olan listenin her elemanını 2 katına çıkartır.
- Sonuç neden doğrudan liste olmayabilir?: Python 3 ile birlikte bellek optimizasyonu (memory efficiency) amacıyla map(), veriyi hafızaya anında yüklemek yerine "tembel değerlendirme" (lazy evaluation) yapan bir map objesi (iterator) döndürür. Bu, milyonlarca satırlık verilerde sistemin çökmesini engeller.
- Sonucu list() ile nasıl alırsın?: İteratördeki veriyi RAM'e döküp somutlaştırmak için veri tipini dönüştürmeniz gerekir. Örneğin:
    list(map(lambda x: x * 2, [1, 2, 3])) -> Çıktı: [2, 4, 6]

## filter() Fonksiyonu
Bir koleksiyon içerisinden, yalnızca belirli bir koşulu sağlayan elemanları seçmek (filtrelemek) için kullanılır.
- filter() ile eleman seçme: map() gibi çalışır ancak içine aldığı fonksiyonun True veya False (boolean) döndürmesi beklenir. Sadece True olanları geçirir. Örneğin:
    list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) -> Çıktı: [2, 4]
- filter() ve list comprehension karşılaştırması: Aynı işlem [x for x in [1,2,3,4] if x % 2 == 0] şeklinde list comprehension ile de yapılabilir. List comprehension genellikle daha "Pythonic" (okunabilir) kabul edilirken, filter() fonksiyonel programlama paradigmasına daha uygundur.

## sorted() ve key
Veri yapılarını belirli algoritmik kurallara göre verileri sıralamak için kullanılır. Kendi içinde stabil olan Timsort algoritmasını kullanır.
- Sayıları ve metinleri sıralama: Varsayılan olarak sayısal büyüklüğe veya alfabetik sıraya göre (lexicographical) küçükten büyüğe sıralar.
- reverse=True: Bu parametre ile sıralama yönü tersine (büyükten küçüğe) çevrilir. Örneğin:
    sorted([3, 1, 2], reverse=True) -> Çıktı: [3, 2, 1]
- key parametresi: Sıralamanın hangi kritere göre yapılacağını belirlemek için bir fonksiyon alır (genellikle bir lambda fonksiyonu).
- Sözlükleri değerlerine göre sıralama: Sözlüklerin .items() metoduyla elde edilen anahtar-değer çiftleri, key parametresi kullanılarak değerlerine göre sıralanabilir. Örneğin:
    sorted(notlar.items(), key=lambda x: x[1])
- Nesneleri bir özelliklerine göre sıralama: Özel sınıflardan üretilmiş nesne listeleri, nesnelerin spesifik bir attribute'una (özelliğine) göre sıralanabilir. Örneğin:
    sorted(ogrenci_listesi, key=lambda ogrenci: ogrenci.yas)

## zip() Fonksiyonu
Bellek açısından son derece efektif olan bu fonksiyon, birden fazla koleksiyonun elemanlarını indeks numaralarına göre karşılıklı olarak eşleştirmek için kullanılır.
- İki listeyi eşleştirme: Aynı indeksteki elemanları alıp tuple'lar (demetler) halinde birleştirir. Örneğin:
    isimler = ["Ada", "Alan"], idler = [101, 102]. list(zip(isimler, idler)) -> Çıktı: [("Ada", 101), ("Alan", 102)]
- Eşleştirilmiş verilerden sözlük oluşturma: Paralel yapıdaki iki bağımsız listeden hızlıca bir hash table (sözlük) inşa etmenin en profesyonel yoludur. Örneğin:
    dict(zip(isimler, idler)) -> Çıktı: {"Ada": 101, "Alan": 102}