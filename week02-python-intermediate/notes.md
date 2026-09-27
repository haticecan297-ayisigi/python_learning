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
