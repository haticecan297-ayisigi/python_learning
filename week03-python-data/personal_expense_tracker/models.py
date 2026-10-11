# Bu modül, sistemdeki her bir finansal işlemi (gelir/gider) nesne yönelimli (OOP) olarak temsil eden Transaction sınıfını içerir.
'''Projenin temel özellikleri
Program şu işlemleri yapabilmeli:
-Gelir ekleme
-Gider ekleme
-Tüm işlemleri listeleme
-Kategoriye göre harcamaları filtreleme
-Tarihe göre işlemleri filtreleme
-Toplam gelir hesaplama
-Toplam gider hesaplama
-Mevcut bakiyeyi hesaplama
-En çok harcama yapılan kategoriyi bulma
-İşlem silme
-İşlem güncelleme
-Verileri dosyaya kaydetme ve dosyadan yükleme
1. Transaction sınıfı
Her gelir veya gider işlemini temsil eder.
Özellikler:
*İşlem numarası
*Açıklama
*Tutar
*Kategori
*Tarih
*İşlem türü: gelir veya gider
Metotlar:
-İşlem bilgilerini göster.
-İşlemin gelir mi gider mi olduğunu belirt.
-İşlem verilerini sözlük biçimine dönüştür.
2. ExpenseTracker sınıfı
İşlemleri yöneten ana sınıftır.
Metotlar:
*İşlem ekle.
*İşlemleri listele.
*İşlem ara.
*İşlem sil.
*İşlem güncelle.
*Toplam gelir hesapla.
*Toplam gider hesapla.
*Bakiye hesapla.
*Kategori raporu oluştur.
*Verileri kaydet.
*Verileri yükle.
C. Menü tasarımı
===== PERSONAL EXPENSE TRACKER =====

1. Add Income
2. Add Expense
3. List Transactions
4. Search Transactions
5. Filter by Category
6. Filter by Date
7. Show Financial Summary
8. Show Category Report
9. Update Transaction
10. Delete Transaction
11. Exit
Menüyü while döngüsüyle çalıştır.
D. Veri saklama
Bu projede verileri JSON dosyasında saklamanı öneriyorum.
Örnek dosya:
data/
└── transactions.json
Program açıldığında kayıtlı işlemleri yüklemeli, yeni işlem eklendiğinde veya güncellendiğinde verileri dosyaya kaydetmeli.
E. Hata yönetimi
Aşağıdaki durumları kontrol et:
-Kullanıcı tutar yerine metin girdiğinde.
-Negatif veya sıfır tutar girildiğinde.
-Geçersiz işlem türü seçildiğinde.
-Olmayan bir işlem numarası girildiğinde.
-JSON dosyası bulunamadığında.
-JSON dosyasının içeriği bozuk olduğunda.
-Kullanıcı geçersiz tarih girdiğinde.
F. Raporlama
Programın finansal özet bölümünde şunları göstermesini sağla:
*Toplam gelir
*Toplam gider
*Güncel bakiye
*En çok harcama yapılan kategori
*Kategori bazında toplam harcama
*Belirli bir ayın gelir ve gider raporunu oluştur.
3. Projeyi aşamalara böl
Proje kontrol listesi
-Transaction sınıfını oluştur.
-ExpenseTracker sınıfını oluştur.
-Gelir ve gider ekleme işlemlerini yaz.
-İşlemleri listeleme ve arama işlemlerini ekle.
-JSON dosyasına kaydetme ve dosyadan yükleme işlemlerini yaz.
-Toplam gelir, gider ve bakiye hesaplamalarını ekle.
-Kategori ve tarih filtrelerini ekle.
-İşlem güncelleme ve silme özelliklerini ekle.
-Hata yönetimini tamamla.
-Menüyü oluştur ve tüm özellikleri test et.

4. Proje için ek görevler
Temel özellikleri bitirdikten sonra aşağıdaki görevlerden birkaçını seçebilirsin:
-Kullanıcının aylık bütçe belirlemesini sağla.
-Bütçe aşıldığında uyarı ver.
-Son 7 günün harcamalarını listele.
-En yüksek tutarlı harcamayı göster.
-Kategoriye göre harcama yüzdesi hesapla.
-Gelir ve giderleri CSV dosyasına aktar.
-Uygulamayı farklı Python dosyalarına böl.
'''

import uuid
from datetime import datetime

class Transaction:
    """Her gelir veya gider işlemini temsil eden veri sınıfı."""
    
    def __init__(self, description, amount, category, date, t_type, t_id=None):
        # İşlem numarası yoksa otomatik benzersiz ID (UUID) üretilir
        self.t_id = t_id if t_id else str(uuid.uuid4())[:8] 
        self.description = description # Açıklama
        self.amount = float(amount)    # Tutar
        self.category = category       # Kategori
        self.date = date               # Tarih
        self.t_type = t_type           # İşlem türü: 'gelir' veya 'gider'

    def is_income(self):
        """İşlemin gelir olup olmadığını belirtir."""
        return self.t_type.lower() == 'gelir'

    def is_expense(self):
        """İşlemin gider olup olmadığını belirtir."""
        return self.t_type.lower() == 'gider'

    def show_info(self):
        """İşlem bilgilerini biçimlendirilmiş metin olarak gösterir."""
        sembol = "+" if self.is_income() else "-"
        # ANSI Kaçış Kodları: \033[92m metni parlak yeşil (gelir), \033[91m parlak kırmızı (gider) yapar.
        renk = "\033[92m" if self.is_income() else "\033[91m" 
        # \033[0m: Renk formatlamasını sıfırlar, böylece terminalin geri kalanı yeşil/kırmızı kalmaz (renk sızıntısını önler).
        reset = "\033[0m"
        return f"[{self.t_id}] {self.date} | {self.category.ljust(15)} | {self.description.ljust(20)} | {renk}{sembol}{self.amount:.2f} TL{reset}"

    def to_dict(self):
        """İşlem verilerini JSON serileştirmesi için sözlük biçimine dönüştürür."""
        return {
            "t_id": self.t_id,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "t_type": self.t_type
        }