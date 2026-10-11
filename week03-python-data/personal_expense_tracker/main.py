#CLI Arayüzü ve Hata Yönetimi:Bu modül, menü döngüsünü (while) çalıştırır ve kullanıcı girdilerindeki hataları (try-except ile) filtreler.
import sys
from datetime import datetime
from tracker import ExpenseTracker
from models import Transaction

def get_valid_amount(prompt):
    """Kullanıcı tutar yerine metin girdiğinde veya negatif/sıfır girdiğinde hata yönetimi."""
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Hata: Tutar sıfır veya negatif olamaz!")
                continue
            return val
        except ValueError:
            print("Hata: Geçersiz format. Lütfen tutar yerine metin girmeyiniz!")

def get_valid_date(prompt):
    """Kullanıcı geçersiz tarih girdiğinde kontrol et."""
    while True:
        date_str = input(prompt + " (YYYY-AA-GG) [Enter: Bugün]: ").strip()
        if not date_str:
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Hata: Geçersiz tarih formatı! Lütfen YYYY-AA-GG formatında girin.")

def main():
    tracker = ExpenseTracker()
    
    # Menüyü while döngüsüyle çalıştır
    while True:
        print("\n" + "="*5 + " PERSONAL EXPENSE TRACKER " + "="*5)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. List Transactions")
        print("4. Search Transactions")
        print("5. Filter by Category")
        print("6. Filter by Date")
        print("7. Show Financial Summary")
        print("8. Show Category Report")
        print("9. Update Transaction")
        print("10. Delete Transaction")
        print("11. Advanced / Extra Features") # Ek görevler menüsü
        print("12. Exit")
        print("="*36)
        
        choice = input("Seçiminiz: ")

        if choice == '1': # Gelir ekleme
            desc = input("Açıklama: ")
            amount = get_valid_amount("Tutar: ")
            cat = input("Kategori (Maaş, Prim vb.): ")
            date = get_valid_date("Tarih")
            tracker.add_transaction(Transaction(desc, amount, cat, date, "gelir"))
            print("Gelir eklendi.")

        elif choice == '2': # Gider ekleme
            desc = input("Açıklama: ")
            amount = get_valid_amount("Tutar: ")
            cat = input("Kategori (Market, Fatura vb.): ")
            date = get_valid_date("Tarih")
            tracker.add_transaction(Transaction(desc, amount, cat, date, "gider"))
            print("Gider eklendi.")

        elif choice == '3': # Tüm işlemleri listeleme
            for t in tracker.get_transactions(): print(t.show_info())

        elif choice == '4': # İşlem ara
            q = input("Aranacak kelime: ").lower()
            res = [t for t in tracker.transactions if q in t.description.lower() or q in t.category.lower()]
            for t in res: print(t.show_info())

        elif choice == '5': # Kategoriye göre harcamaları filtreleme
            cat = input("Kategori adı: ")
            for t in tracker.get_transactions(category=cat): print(t.show_info())

        elif choice == '6': # Tarihe göre işlemleri filtreleme
            dt = get_valid_date("Tarih")
            for t in tracker.get_transactions(date=dt): print(t.show_info())

        elif choice == '7': # Financial Summary (Finansal Özet)
            print("\n--- FİNANSAL ÖZET ---")
            print(f"Toplam Gelir: {tracker.calc_total_income():.2f} TL")
            print(f"Toplam Gider: {tracker.calc_total_expense():.2f} TL")
            print(f"Güncel Bakiye: {tracker.calc_balance():.2f} TL")
            _, max_cat = tracker.generate_category_report()
            print(f"En Çok Harcama Yapılan Kategori: {max_cat}")

        elif choice == '8': # Kategori Raporu
            report, _ = tracker.generate_category_report()
            print("\n--- KATEGORİ BAZINDA HARCAMALAR ---")
            for cat, data in report.items():
                print(f"{cat.ljust(15)} : {data['total']:.2f} TL (%{data['percent']:.1f})") # Yüzde hesabı 

        elif choice == '9': # İşlem Güncelleme
            t_id = input("Güncellenecek İşlem ID: ")
            print("Değiştirmek istemediğiniz alanları boş (Enter) geçin.")
            desc = input("Yeni Açıklama: ")
            amt_str = input("Yeni Tutar: ")
            cat = input("Yeni Kategori: ")
            
            kwargs = {}
            if desc: kwargs['description'] = desc
            if amt_str: 
                try: kwargs['amount'] = float(amt_str)
                except: print("Geçersiz tutar atlandı.")
            if cat: kwargs['category'] = cat
            
            if tracker.update_transaction(t_id, **kwargs):
                print("İşlem güncellendi.")
            else:
                print("Hata: Olmayan bir işlem numarası girildi.")

        elif choice == '10': # İşlem Silme
            t_id = input("Silinecek İşlem ID: ")
            if tracker.delete_transaction(t_id):
                print("İşlem silindi.")
            else:
                print("Hata: Olmayan bir işlem numarası girildi.")

        elif choice == '11': # EK GÖREVLER MENÜSÜ
            print("\n--- EK GÖREVLER ---")
            print("A. Bütçe Belirle")
            print("B. Son 7 Günün Harcamaları")
            print("C. En Yüksek Tutarlı Harcama")
            print("D. Belirli Bir Ayın Raporu (İsteğe Bağlı Görev)")
            print("E. CSV Olarak Dışa Aktar")
            sub_choice = input("Seçiminiz: ").upper()
            
            if sub_choice == 'A':
                budget = get_valid_amount("Aylık Bütçe Hedefi (TL): ")
                tracker.save_budget(budget)
                print("Bütçe kaydedildi.")
            elif sub_choice == 'B':
                print("\n--- SON 7 GÜN ---")
                for t in tracker.get_last_7_days_expenses(): print(t.show_info())
            elif sub_choice == 'C':
                max_t = tracker.get_highest_expense()
                if max_t: print(f"En Yüksek Harcama: {max_t.show_info()}")
            elif sub_choice == 'D':
                ym = input("Yıl-Ay (Örn: 2026-10): ")
                inc, exp = tracker.generate_monthly_report(ym)
                print(f"{ym} Raporu -> Gelir: {inc} TL | Gider: {exp} TL")
            elif sub_choice == 'E':
                f = tracker.export_to_csv()
                print(f"Veriler başarıyla aktarıldı: {f}")

        elif choice == '12': # Çıkış
            sys.exit("Uygulamadan çıkılıyor. Verileriniz güvende.")
        else:
            print("Geçersiz işlem türü seçildi!")

if __name__ == "__main__":
    main()