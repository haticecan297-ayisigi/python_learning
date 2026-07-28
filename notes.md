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