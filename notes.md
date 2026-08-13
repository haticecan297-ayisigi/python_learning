Bugün öğrendiklerim(24.07.26)

- Python'da değişken tanımlarken veri tipi belirtilmez.
- input() her zaman string döndürür.
- type() veri tipini gösterir.
- int() ile dönüşüm yapılabilir. Girilen sayı input ile girldiyse stringtir ve o sayı ile matematiksel işlem yapacaksak int() ile integar değere dödürmeliyiz.
- Python'da print()ile birden fazla satır yazdıracaksak 3 tane çift tırnak kullanmalıyız.
- Aritmatik İşlem İşaretleri:
    toplama: +
    çıkarma:-
    çarpma: *
    bölme: /
    mod alma: %
    üst alma: **
    tam bölme: //
- lists mutiable'dır yani değiştirilebilirler ve köşeli paranetzle kullanılırlar.
- tuples is immutable'dır yani değiştirilemezler  ve normal parantez kullanılır.
- sets ise matematikteki küme mantığına dayanır tanımlarken süslü parantez kullanılır. Her eleman eşsizdir bu yüzden iki kere yazan bile sadece birini alır yani duplicate elemanlar kaldırılır. Ayrıca sırayı önemsemezler bu sebeple filtreleme etiket(tag) sistemlerinde kullanılırlar.
- Dictionary ise anahtar değer uyumu ile çalışır. İçinde değer olarak farklı veri yapılarını içerebilir.
- Koşullu durumlarda if kullanılır yani bir şey olması için önce başka bir durumun gerçekleşmesi gerekiyorsa bunlar koşullu durumlardır.
- elif kullanımı için en az 3 farklı durum olması gerekir. bu koşul değilse bu koşulu sağlyıyor mu diye bakarken elif kullanılır.
- and, or ve not operatörleri koşul ifadelerinde kullanılır. and ve or birden fazla koşulu tek bir if yapısında kontrol ediyorsak kullanılır. 
    * and: Her iki ifade de doğruysa True değerini döndürür. Koşullardan en az biri bile yanlışsa sonuç yanlış olur.
    * or: En az bir ifade doğruysa True değeri döndürür. Tüm ifadeler yanlışsa sonuç yanlış olur.
not operatörü: if yapısı içindeki koşulun sonucu True ise False, False ise True yapar.
- İlk if yapısı doğru ise bloğun içine girer ve içerideki if yapısına bakar doğruysa içine şeklinde devam eder. Bu durum kodun okunabilirliğini azaltır ve hata ayıklamayı zorlaştırır. 
- pass bir değişken değil bir ifadedir. kullanım amaçları:
    * Yer tutucu: Gövdesi boş bırakılmış fonksiyon veya sınıflardan, gelecekte eklenecek kod için yer tutucu olarak kullanılır.
    * Döngü kontrolü: Döngü içinde, mevcut yinelemeyi atlamak ve bir sonraki yinelemeye devam etmek için kullanılır.
 pass ifadesi, bir ifadenin beklendiği her yerde kullanılabilir. Ancak, bir hata oluşmadığı sürece, yorumlayıcı pass ifadesiyle karşılaştığında bunu yok sayar ve hata vermeden devam eder.
* for: Belirli bir aralık veya koleksiyon üzerinde yineleme yapmak için kullanılır.
* while: Koşul doğru olduğu sürece çalışır; koşula bağlı tekrarlar için tercih edilir.
* break: Döngüyü tamamen sonlandırır.
* continue: Döngünün o adımını atlayıp sonraki adıma geçer.
* pass: Hiçbir şey yapmaz; boş bloklar için yer tutucu olarak kullanılır.
* range(): Belirtilen aralıkta sayılar üretir, genellikle for döngüsüyle birlikte kullanılır.
* enumerate(): Bir koleksiyon üzerinde hem elemanları hem de indekslerini birlikte döndürür.
- Fonksiyon tanımlarken def anahtarını kullanırız.
- parameter fonksiyon tanımında kullandığımız değişkendir, argument ise fonksiyonu çağırırken parameter yerlerine koyduğumuz gerçek değerlerdir.
- Default parameter: Bir kaç parameter'a sahip fonksiyonda tüm parameter yerine birkaç argument girmediğimizde fonksiyonun çalışması için o parametrenin sahip olacağı en olası veriyi default olarak tanımlamaktır. Yani o değer yerine başka bir değer girilmediğinde o değer varsayılan olarak çalışır. 
- Docstring: Python'da fonksiyonların ne işe yaradığını fonksiyonun tanımını yaparken en  üstünde kısaca açıklayan yazılardır.
- Local Variables: Bir fonksiyon içinde tanımlanan ve sadece fonksiyon içinde kullanılabilen bir değişkendir.
- Global Variables: Fonksiyonların dışında tanımlanan ve istenilen yerde kullanılabilen değişkenlerdir eğer fonksiyon içinde bu değişkenleri kullanmak istersek 'global' key kullanılır.
- *args: Kaç tane değer geleceğini bilmediğimiz durumlarda fonksiyona sınırsız sayıda argüman göndermemizi sağlar. Verileri tuple olarak tutar.
- **kwargs: Hangi isimli parametre geleceğini bilmediğimizde fonksiyona sınırsız sayıda keyword argümanı göndermek için kullanılır. Bir dictionary olarak saklanır.