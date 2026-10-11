#Bu modül, işlemleri yöneten ana sınıf olan ExpenseTracker'ı barındırır. 
#Dosya okuma/yazma, bütçe takibi, CSV dışa aktarımı ve lambda/filter gibi fonksiyonel programlama araçları buradadır.
import json
import os
import csv
from datetime import datetime, timedelta
from models import Transaction

class ExpenseTracker:
    """İşlemleri yöneten, hesaplamaları ve dosya I/O operasyonlarını yapan ana sınıftı."""
    
    def __init__(self, data_file="data/transactions.json", budget_file="data/budget.json"):
        self.data_file = data_file
        self.budget_file = budget_file
        self.transactions = []
        self.monthly_budget = 0.0
        
        # 'data' klasörü yoksa oluştur
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        
        self.load_data()   # Program açıldığında kayıtlı işlemleri yükler
        self.load_budget()

    # --- VERİ YÖNETİMİ ---
    def load_data(self):
        """JSON dosyasını okuyarak verileri belleğe yükler."""
        if not os.path.exists(self.data_file):
            return # JSON dosyası bulunamadığında boş başlar
            
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                # JSON listesini Transaction nesnelerine dönüştürme (List Comprehension)
                self.transactions = [Transaction(**item) for item in data]
        except json.JSONDecodeError:
            print("Kritik Hata: JSON dosyasının içeriği bozuk. Temiz bellek ile başlanıyor.")
            self.transactions = []

    def save_data(self):
        """Yeni işlem eklendiğinde veya güncellendiğinde verileri dosyaya kaydeder."""
        with open(self.data_file, "w", encoding="utf-8") as file:
            # Transaction nesnelerini to_dict() ile sözlüğe çevirip JSON'a yazma
            json.dump([t.to_dict() for t in self.transactions], file, indent=4, ensure_ascii=False)

    def load_budget(self):
        if os.path.exists(self.budget_file):
            try:
                with open(self.budget_file, "r") as f:
                    self.monthly_budget = json.load(f).get("budget", 0.0)
            except: pass

    def save_budget(self, amount):
        """Kullanıcının aylık bütçe belirlemesini sağlar."""
        self.monthly_budget = amount
        with open(self.budget_file, "w") as f:
            json.dump({"budget": amount}, f)

    # --- İŞLEM OPERASYONLARI ---
    def add_transaction(self, transaction):
        """İşlem ekler ve bütçe aşımını kontrol eder."""
        self.transactions.append(transaction)
        self.save_data()
        
        if transaction.is_expense() and self.monthly_budget > 0:
            total_exp = self.calc_total_expense()
            if total_exp > self.monthly_budget:
                print(f"\n DİKKAT: Bütçe aşıldı! (Bütçe: {self.monthly_budget} TL, Harcama: {total_exp} TL)")

    def delete_transaction(self, t_id):
        """İşlem silme operasyonu."""
        initial_count = len(self.transactions)
        # Sadece girilen ID ile eşleşmeyenleri tutarak silme işlemi (List Comprehension)
        self.transactions = [t for t in self.transactions if t.t_id != t_id]
        if len(self.transactions) < initial_count:
            self.save_data()
            return True
        return False # Olmayan bir işlem numarası girildiğinde False döner

    def update_transaction(self, t_id, **kwargs):
        """İşlem güncelleme."""
        for t in self.transactions:
            if t.t_id == t_id:
                for key, value in kwargs.items():
                    if hasattr(t, key) and value is not None:
                        setattr(t, key, value)
                self.save_data()
                return True
        return False

    def get_transactions(self, category=None, date=None):
        """Tüm işlemleri listeleme, Kategoriye ve Tarihe göre filtreleme."""
        sonuclar = self.transactions
        if category:
            sonuclar = list(filter(lambda x: x.category.lower() == category.lower(), sonuclar))
        if date:
            sonuclar = list(filter(lambda x: x.date == date, sonuclar))
        return sonuclar

    # --- FİNANSAL HESAPLAMALAR ---
    def calc_total_income(self):
        """Toplam gelir hesaplama (Generator Expression kullanımı)."""
        return sum(t.amount for t in self.transactions if t.is_income())

    def calc_total_expense(self):
        """Toplam gider hesaplama."""
        return sum(t.amount for t in self.transactions if t.is_expense())

    def calc_balance(self):
        """Mevcut bakiye hesaplama."""
        return self.calc_total_income() - self.calc_total_expense()

    def get_highest_expense(self):
        """En yüksek tutarlı harcamayı gösterir."""
        expenses = [t for t in self.transactions if t.is_expense()]
        if not expenses: return None
        return max(expenses, key=lambda x: x.amount)

    # --- GELİŞMİŞ RAPORLAMA ---
    def generate_category_report(self):
        """Kategori raporu oluşturur, Kategori bazında toplam harcama ve harcama yüzdesi hesaplar."""
        expenses = [t for t in self.transactions if t.is_expense()]
        total_expense = self.calc_total_expense()
        report = {}
        
        for t in expenses:
            report[t.category] = report.get(t.category, 0) + t.amount
            
        # En çok harcama yapılan kategoriyi bulma
        max_cat = max(report, key=report.get) if report else "Yok"
        
        # Kategoriye göre harcama yüzdesi ekleme
        detailed_report = {
            cat: {"total": amt, "percent": (amt / total_expense * 100) if total_expense > 0 else 0}
            for cat, amt in report.items()
        }
        return detailed_report, max_cat

    def get_last_7_days_expenses(self):
        """Son 7 günün harcamalarını listeler."""
        today = datetime.now()
        seven_days_ago = today - timedelta(days=7)
        return [
            t for t in self.transactions 
            if t.is_expense() and datetime.strptime(t.date, "%Y-%m-%d") >= seven_days_ago
        ]

    def generate_monthly_report(self, year_month):
        """Belirli bir ayın gelir ve gider raporunu oluşturur."""
        monthly_income = sum(t.amount for t in self.transactions if t.is_income() and t.date.startswith(year_month))
        monthly_expense = sum(t.amount for t in self.transactions if t.is_expense() and t.date.startswith(year_month))
        return monthly_income, monthly_expense

    def export_to_csv(self, filename="data/export.csv"):
        """Gelir ve giderleri CSV dosyasına aktarır."""
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Tarih", "Kategori", "Açıklama", "Tür", "Tutar"])
            for t in self.transactions:
                writer.writerow([t.t_id, t.date, t.category, t.description, t.t_type, t.amount])
        return filename