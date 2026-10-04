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

### JSON VE VERİ SAKLAMA
"JavaScript Object Notation" ifadesinin kısaltması olan JSON, farklı yazılım uygulamaları arasında (örneğin mikroservisler arası) veri alışverişinde ve verilerin kalıcı olarak saklanmasında endüstri standardı olarak sık kullanılan bir veri formatıdır. Bugün temel mühendislik amacımız; çalışma zamanındaki Python nesnelerini JSON formatına dönüştürmeyi (serialization/serileştirme) ve dış kaynaklı JSON verilerini Python belleğine geri aktarmayı (deserialization/ters serileştirme) öğrenmektir.
Veri transferi yaparken dil bağımsız bir standart kullanmak esastır. Bu bağlamda JSON'un temel veri türlerinin (data types) Python dilindeki veri yapılarıyla eşleşmesini (mapping) öğrenmeniz gerekmektedir:
- JSON'daki Object veri yapısı, Python dilinde anahtar-değer çiftlerinden oluşan dict yapısına denk gelir.
- JSON'daki sıralı dizi olan Array, Python'da list olarak temsil edilir.
- JSON'daki String türü, Python'da str veri tipiyle eşleşir.
- JSON'daki Number türü, Python'da sayısal değerler olan int veya float olarak haritalanır.
- Mantıksal durumu belirten Boolean yapısı, Python'da bool olarak değerlendirilir.
- Herhangi bir değer barındırmayan Null veri tipi ise Python'da None objesine karşılık gelir.
# JSON Modülü
Python standart kütüphanesinde yer alan bu modül, dönüşüm ve ayrıştırma operasyonlarını yönetir. Öğrenmeniz gereken temel fonksiyonlar ve görevleri şunlardır:
* json.dump() fonksiyonu: Bellekteki Python verisini doğrudan bir JSON dosyasına yazar (I/O akışı sağlar).
* json.dumps() fonksiyonu: Python verisini ağ (network) üzerinden aktarmak üzere bir JSON metnine (string karakter dizisine) dönüştürür.
* json.load() fonksiyonu: Diskteki bir JSON dosyasını okuyarak veriyi doğrudan Python verisine dönüştürür.
* json.loads() fonksiyonu: Bir API'den dönen JSON metnini (string'i) bellekte Python verisine ayrıştırır (parse eder).
# JSON Dosyası Oluşturma ve Okuma
Kalıcı veri depolama operasyonlarında dosya işlemlerini standartlara uygun yönetmek kritik öneme sahiptir. Bu kapsamda dikkat edilecek hususlar şunlardır:
- Kaynak sızıntılarını önlemek için dosya açma işlemi bağlam yöneticisi olan with open() ile yapılmalıdır.
- Karakter kodlaması uyuşmazlıklarını engellemek adına uluslararası bir standart olan encoding="utf-8" kullanılmalıdır.
- Veri bütünlüğü açısından, Türkçe karakterlerin diskte okunabilir biçimde saklanması için serileştirme esnasında ensure_ascii=False argümanı verilmelidir.
- Oluşturulan JSON dosyasının bir insan tarafından kolayca incelenebilmesi için indent=4 parametresi kullanılarak dosyanın düzenli biçimde yazılması sağlanmalıdır.
# Hata Yönetimi
Dağıtık ve I/O bağımlı sistemlerde kodun çökmesini (crash) engellemek için defansif programlama yapılmalıdır. Bu amaçla JSON dosyası okunurken karşılaşılabilecek hata durumlarını öğrenmelisiniz:
* İşletim sisteminde dosyanın bulunamaması durumuyla karşılaşılabilir.
* Dosya içindeki JSON biçiminin yapısal olarak bozuk (syntax hatası) olması durumu ortaya çıkabilir.
* Okunmaya çalışılan dosyanın tamamen boş olması sorunu yaşanabilir.
* Ayrıştırma (parsing) işlemi sırasında sisteminizin algoritmasına uymayan, beklenmeyen bir veri yapısıyla karşılaşılması mümkündür.
* Uygulama istikrarını korumak için, veri I/O operasyonlarında sıklıkla fırlatılan FileNotFoundError (dosya yoksa) ve json.JSONDecodeError (biçim bozuksa) hatalarını (exceptions), önceki günlerde öğrendiğiniz try-except hata yakalama mimarisi ile birleştirerek yönetmelisiniz.
## Örneklerle pekiştirme
# Makine Öğrenmesi Model Konfigürasyonlarının Yönetimi
Yapay zeka projelerinde, bir modelin eğitim sürecindeki hiperparametreleri (hyperparameters) ve mimari ayarları kalıcı hale getirmek, deneylerin tekrarlanabilirliği (reproducibility) açısından zorunludur. Model ağırlıkları genellikle .h5 veya .pt gibi binary (ikili) formatlarda devasa dosyalar olarak saklanırken, insan tarafından okunması ve düzenlenmesi gereken konfigürasyonlar JSON formatında tutulur.
    import json

    # Model eğitim parametrelerini temsil eden Python sözlüğü
    model_config = {
        "model_name": "transformer_steganalysis_v1",
        "hyperparameters": {
            "learning_rate": 0.001,
            "batch_size": 64,
            "epochs": 150,
            "optimizer": "Adam"
        },
        "dataset_path": "/data/train_set",
        "is_training_complete": True
    }
    # Konfigürasyonu diske yazma (Serileştirme)
    # Hata yönetimi için 'with' bloğu kullanılır, dosya otomatik kapatılır.
    with open("model_config.json", "w", encoding="utf-8") as file:
        json.dump(model_config, file, indent=4, ensure_ascii=False)
    
# Donanım ve Gömülü Sistem Durum (State) Yönetimi
Sensör donanımları veya bir 4K Ultra HD Wi-Fi aksiyon kamerası gibi IoT tabanlı uç cihazlar (edge devices), kullanıcının cihaz üzerindeki son yapılandırmalarını dahili hafızasında bir settings.json dosyası içinde tutar. Cihazın güç döngüsü (reboot) her gerçekleştiğinde, yazılım bu dosyayı okuyarak (deserialization) donanımı kullanıcının bıraktığı konuma getirir.
    import json
    import os

    def kamerayi_baslat():
        dosya_yolu = "camera_settings.json"
        
        # Bellekte tutulan varsayılan fabrika ayarları
        ayarlar = {
            "resolution": "1080p",
            "fps": 30,
            "wifi_enabled": False,
            "water_resistance_mode": "off"
        }

        # Eğer kullanıcının kaydettiği geçerli bir ayar dosyası varsa, onu belleğe yükle
        if os.path.exists(dosya_yolu):
            try:
                with open(dosya_yolu, "r", encoding="utf-8") as file:
                    ayarlar = json.load(file)
            except json.JSONDecodeError:
                print("Kritik: Ayar dosyası JSON formatı bozuk, fabrika ayarlarına dönülüyor.")
            except PermissionError:
                print("Kritik: Dosya okuma izni yok.")
                
        # Kamerayı donanımsal olarak ayarlar ile yapılandır (Simülasyon)
        print(f"Kamera başlatılıyor... Çözünürlük: {ayarlar['resolution']}, Wi-Fi: {ayarlar['wifi_enabled']}")
        return ayarlar

    aktif_ayarlar = kamerayi_baslat()

# Siber Güvenlik Loglarının İzlenmesi ve İletimi
Sistemdeki anormal aktiviteleri veya yetkisiz erişim denemelerini kayıt altına almak için (audit logging), güvenlik olayları yapısal olmayan (unstructured) metinler yerine bir JSON dizisi (array of objects) formatında dış bir SIEM (Security Information and Event Management) sistemine iletilir. Bu, verinin makineler tarafından anında ayrıştırılmasını ve indekslenebilmesini sağlar.
    import json
    import datetime

    # Güvenlik ihlali olaylarını simüle eden veriler (Python Listesi içinde Sözlükler)
    security_events = [
        {
            "timestamp": datetime.datetime.now().isoformat(),
            "event_type": "failed_login",
            "source_ip": "192.168.1.105",
            "target_user": "root",
            "severity_level": "high"
        },
        {
            "timestamp": datetime.datetime.now().isoformat(),
            "event_type": "unauthorized_file_access",
            "file_path": "/etc/shadow",
            "source_ip": "10.0.0.12",
            "severity_level": "critical"
        }
    ]

    # Logları bir ağ soketi üzerinden merkezi sunucuya göndermek üzere metne dönüştürme
    # json.dumps(), veriyi diske yazmadan doğrudan ağ paketine (payload) koymak için kullanılır.
    network_payload = json.dumps(security_events)

    print("İletilecek Byte/String Payload (API'ye gönderilen raw format):")
    print(network_payload)