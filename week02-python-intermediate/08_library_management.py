## OOP UYGULAMASI: KÜTÜPHANE YÖNETİM SİSTEMİ
#Sınıflar
    #Book Sınıfı: Kitabın bilgilerini tutar.
        # Kitap adı, yazar,ISBN veya kitap numarası, ödünç durumu. 
        # Metotlar: Kitap bilgilerini göster, kitabın ödünç verilebilir olup olmadığını kontrol et.
    #Library Sınıfı: Kitapları yönetir.
        #Kitapları bir listede tut
        #Kitap ekleme metodu
        #Kitapları listeleme metodu
        #Kitap arama metodu
        #Kitap ödünç verme metodu
        #Kitap iade alma metodu
#Menü
    #Programcının kullanıcıya sunacağı menü:        
'''===== LIBRARY MANAGEMENT SYSTEM =====

    1. Add Book
    2. List Books
    3. Search Book
    4. Borrow Book
    5. Return Book
    6. Show Available Books
    7. Exit'''
    #Menüyü while döngüsü ile sürekli çalıştır.
#Proje gereksinimleri:
    #Kitaplar Book nesneleri olarak tutulmalı.
    #Kütüphane işlemleri Library sınıfında yönetilmeli.
    #Kitap eklenirken o kitabın library sınıfında olup olmadığına 
        #bakılıp öyle eklenmeli.
    #Kitap araması kitap adı veya ISBN ile yapılabilmeli.
    #Ödünç alınmış bir kitap tekrar ödünç verilememeli.
    #İade edilen kitap yeniden ödünç verilebilmeli.
    #Geçersiz menü seçimleri kontrol edilmeli.
    #Kod mümkün olduğunca sınıflara ve metotlara ayrılmalı.
    #Kitap silme özelliği ekle.
    #Aynı ISBN ile ikinci kitap eklenmesini engelle.
    #Kütüphanedeki toplam ve ödünçteki kitap sayısını göster.
    #Birden fazla kitabı aynı anda ödünç alma özelliği ekle.

## OOP UYGULAMASI: KÜTÜPHANE YÖNETİM SİSTEMİ

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.durum = False
    
    def show_info(self):
        status = "Ödünç Verildi" if self.durum else "Müsait"
        print("-" * 40)
        print(f"Kitap Adı : {self.title}")
        print(f"Yazar     : {self.author}")
        print(f"ISBN      : {self.isbn}")
        print(f"Durum     : {status}")

    def odunc_verilir_mi(self):
        return not self.durum  

    def odunc_verildi_mi(self):
        return self.durum

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        # Aynı ISBN ile ikinci kitap eklenmesini engelle
        for book in self.books:
            if book.isbn == isbn:
                print(f"HATA: {isbn} ISBN numarasına sahip kitap zaten mevcut!")
                return
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"'{title}' başarıyla eklendi.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print("Kitap başarıyla silindi.")
                return
        print("HATA: Silinmek istenen kitap bulunamadı.")

    def list_books(self):
        if not self.books:
            print("Kütüphanede henüz kitap bulunmuyor.")
            return
        for book in self.books:
            book.show_info()

    def search_book(self, keyword):
        found = False
        for book in self.books:
            if (keyword.lower() in book.title.lower() or keyword == book.isbn):
                book.show_info()
                found = True
        if not found:
            print("Aranan kriterlere uygun kitap bulunamadı.")

    def borrow_books(self, isbns):
        # Birden fazla kitabı aynı anda ödünç alma işlemini destekler
        for isbn in isbns:
            found = False
            for book in self.books:
                if book.isbn == isbn:
                    found = True
                    if book.odunc_verilir_mi():
                        book.durum = True
                        print(f"'{book.title}' (ISBN: {isbn}) başarıyla ödünç verildi.")
                    else:
                        print(f"UYARI: '{book.title}' (ISBN: {isbn}) zaten ödünç alınmış durumda.")
                    break
            
            if not found:
                print(f"HATA: {isbn} ISBN numaralı kitap kütüphanede bulunamadı.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.odunc_verildi_mi():
                    book.durum = False
                    print(f"'{book.title}' başarıyla iade edildi.")
                else:
                    print("UYARI: Bu kitap zaten kütüphanede gözüküyor.")
                return
        print("HATA: İade edilmek istenen kitap sistemde bulunamadı.")

    def show_available_books(self):
        available_books = [book for book in self.books if not book.durum]
        if not available_books:
            print("Şu anda müsait kitap bulunmuyor.")
            return
        for book in available_books:
            book.show_info()

    def show_statistics(self):
        total = len(self.books)
        borrowed = len([book for book in self.books if book.durum])
        available = total - borrowed
        print("\n===== KÜTÜPHANE İSTATİSTİKLERİ =====")
        print(f"Toplam Kitap  : {total}")
        print(f"Ödünçte Kitap : {borrowed}")
        print(f"Müsait Kitap  : {available}")

def show_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book (Kitap Ekle)")
    print("2. List Books (Kitapları Listele)")
    print("3. Search Book (Kitap Ara)")
    print("4. Borrow Book (Kitap Ödünç Al)")
    print("5. Return Book (Kitap İade Et)")
    print("6. Show Available Books (Uygun Kitapları Göster)")
    print("7. Kitap Sil")
    print("8. İstatistikleri Göster")
    print("9. Çıkış")

def main():
    # Library sınıfından nesne oluşturulması
    my_library = Library()
    
    while True:
        show_menu()
        try:
            secim = int(input("\nSeçiminiz (1-9): "))

            if secim == 1:
                title = input("Kitap Adı: ")
                author = input("Yazar: ")
                isbn = input("ISBN: ")
                my_library.add_book(title, author, isbn)
                
            elif secim == 2:
                my_library.list_books()
                
            elif secim == 3:
                keyword = input("Aranacak Kitap adı veya ISBN: ")
                my_library.search_book(keyword)
                
            elif secim == 4:
                # Çoklu ödünç alma desteği için girdiyi virgül ile bölüyoruz
                girdi = input("Ödünç alınacak ISBN numaralarını girin (Birden fazla ise virgülle ayırın): ")
                isbn_listesi = [isbn.strip() for isbn in girdi.split(",")]
                my_library.borrow_books(isbn_listesi)
                
            elif secim == 5:
                isbn = input("İade edilecek ISBN: ")
                my_library.return_book(isbn)
                
            elif secim == 6:
                my_library.show_available_books()
                
            elif secim == 7:
                isbn = input("Silinecek kitabın ISBN'i: ")
                my_library.remove_book(isbn)
                
            elif secim == 8:
                my_library.show_statistics()
                
            elif secim == 9:
                print("Program sonlandırıldı.")
                break
            else:
                print("Lütfen 1-9 arasında geçerli bir seçim yapınız!")
                
        except ValueError:
            # Hata mesajındaki limit 1-9 olarak düzeltildi
            print("Harf girişi yapmayınız! Lütfen 1 ile 9 arasında bir sayı seçiniz.")

# Ana programı çalıştır
if __name__ == "__main__":
    main()
