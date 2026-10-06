import csv

# Bir CSV dosyası oluştur ve öğrenci bilgilerini yaz.
students = [
    ["Ahmet", 20, 85],
    ["Ayşe", 21, 92],
    ["Mehmet", 19, 75],
    ["Zeynep", 22, 88]
]

with open("ogrenciler.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Ad", "Yas", "Not"])
    writer.writerows(students)

print("ogrenciler.csv oluşturuldu.\n")

# CSV dosyasını reader() ile oku.
print("===  reader() ile okuma  ===")
with open("ogrenciler.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# DictReader() kullanarak verileri sözlük biçiminde oku.
print("===  DicReader() ile okuma   ===")

with open("ogrenciler.csv", "r", newline="", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(row)

# DictWriter() ile öğrenci verilerini CSV dosyasına yaz.
print("===  DictWriter() ile yazma  ===")

students_dict = [
    {"Ad": "Ali", "Yas": 20, "Not": 90},
    {"Ad": "Veli", "Yas": 21, "Not": 80},
    {"Ad": "Fatma", "Yas": 22, "Not": 95}
]

with open("ogrenciler_dict.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Ad", "Yas", "Not"]
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students_dict)

print("ogrenciler_dict.csv oluşturuldu!\n")

# Yeni bir öğrenci kaydı ekle.
new_student = ["Can", 23, 87]

with open("ogrenciler.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(new_student)

print("Yeni öğrenci eklendi!\n")

# Belirli bir öğrenciyi CSV dosyasında ara.
search_name = "Ayşe"
print(f"\n=== {search_name} aranıyor ===")

found = False

with open("ogrenciler.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == search_name:
            print("Bulundu:", row)
            found = True

if not found:
    print("Öğrenci bulunamadı.")

# Öğrencilerin not ortalamasını hesapla.
total = 0
count = 0

with open("ogrenciler.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += int(row["Not"])
        count += 1

average = total / count

print(f"Not Ortalaması:{average:.2f}")

# Başarılı öğrencileri ayrı bir CSV dosyasına yaz.
successful_students = []

with open("ogrenciler.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["Not"]) >= 85:
            successful_students.append(row)

with open("basarili_ogrenciler.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Ad", "Yas", "Not"]
    writer = csv.DictWriter(file, fieldnames =fieldnames)
    writer.writeheader()
    writer.writerows(successful_students)

print("Başarılı Öğrenciler Kaydedildi.")

# Ürün adı, fiyat ve stok bilgilerini içeren bir CSV dosyası oluştur.
products = [
    ["Laptop", 30000, 10],
    ["Telefon", 20000, 15],
    ["Tablet", 12000, 20],
    ["Kulaklık", 1500, 50]
]

with open("urunler.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Urun", "Fiyat", "Stok"])
    writer.writerows(products)

print("Ürünler urun.csv dosyasına başarıyla kaydedildi.\n")

# CSV dosyasındaki ürünleri fiyatlarına göre sırala.
urunler = []
with open("urunler.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Fiyat"] = float(row["Fiyat"])
        urunler.append(row)

urunler.sort(key=lambda x: x["Fiyat"])

print("Fiyata Göre Sıralı Ürünler:")
for urun in urunler:
    print(
    f"{urun['Urun']} - "
    f"{urun['Fiyat']} TL - "
    f"Stok: {urun['Stok']}"
    )

## MİNİ PROJE: öĞRENCİ NOT RAPORU
import os

# Önce bir CSV dosyası oluşturmalıyım.
def ornek_veri_olustur(dosya_adi="ogrenci_notlari.csv"):
    veri = [
        "OgrenciNo,Isim,Vize,Final",
        "101,Hatice Can,85,95",
        "102,Beyza Işık,40,45",      # Başarısız
        "103,Pınar Adalı,90,100",
        "104,Azra Turhan,invalid,70",   # Hatalı veri
        "105,Berivan Doğan,60,",        # Eksik veri
        "106,İrem ERen,75,80"
    ]
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write("\n".join(veri))

def harf_notu_hesapla(ortalama):
    """Öğrencilerin harf notlarını hesaplama."""
    if ortalama >= 90: return 'AA'
    elif ortalama >= 85: return 'BA'
    elif ortalama >= 80: return 'BB'
    elif ortalama >= 75: return 'CB'
    elif ortalama >= 65: return 'CC'
    elif ortalama >= 60: return 'DC'
    elif ortalama >= 50: return 'DD'
    else: return 'FF'


def rapor_olustur(girdi_dosyasi="ogrenci_notlari.csv", cikti_dosyasi="basarililar.csv", baraj=60):
    gecerli_ogrenciler = []
    hatali_kayitlar = []

    # Öğrenci bilgilerini CSV dosyasından oku
    with open(girdi_dosyasi, "r", encoding="utf-8", newline="") as f:
        okuyucu = csv.DictReader(f)
        
        for satir in okuyucu:
            try:
                # Hatalı veya eksik verileri kontrol et
                if not satir["Vize"] or not satir["Final"]:
                    raise ValueError("Eksik not verisi")
                
                vize = float(satir["Vize"])
                final = float(satir["Final"])
                
                # Her öğrencinin not ortalamasını hesapla
                # Vize %40, Final %60 yani genelde
                ortalama = round((vize * 0.4) + (final * 0.6), 2)
                
                # Veri Zenginleştirme(yeni verileri csv dosyasına ekliyouz.)
                satir["Ortalama"] = ortalama
                satir["HarfNotu"] = harf_notu_hesapla(ortalama)
                
                gecerli_ogrenciler.append(satir)
                
            except ValueError as e:
                satir["Hata"] = str(e)
                hatali_kayitlar.append(satir)

    if not gecerli_ogrenciler:
        print("Sistemde işlenecek geçerli veri bulunamadı.")
        return

    # Öğrencileri not ortalamasına göre sırala
    gecerli_ogrenciler = sorted(gecerli_ogrenciler, key=lambda x: x["Ortalama"], reverse=True)

    # Sınıf ortalamasını hesaplama
    sinif_ortalamasi = sum(ogr["Ortalama"] for ogr in gecerli_ogrenciler) / len(gecerli_ogrenciler)

    # En yüksek notu alan öğrenciyi bul & En yüksek ve en düşük notları göster
    en_yuksek = max(gecerli_ogrenciler, key=lambda x: x["Ortalama"])
    en_dusuk = min(gecerli_ogrenciler, key=lambda x: x["Ortalama"])

    # Başarılı ve başarısız öğrencileri belirle
    basarililar = list(filter(lambda x: x["Ortalama"] >= baraj, gecerli_ogrenciler))
    basarisizlar = list(filter(lambda x: x["Ortalama"] < baraj, gecerli_ogrenciler))

    # Sonuçları ekrana yazdır
    print(f"\n{'='*40}")
    print(f"{'ÖĞRENCİ NOT RAPORU (ANALİZ SONUÇLARI)':^40}")
    print(f"{'='*40}")
    print(f"Sınıf Genel Ortalaması : {sinif_ortalamasi:.2f}")
    print(f"En Yüksek Başarı       : {en_yuksek['Isim']} ({en_yuksek['Ortalama']} - {en_yuksek['HarfNotu']})")
    print(f"En Düşük Başarı        : {en_dusuk['Isim']} ({en_dusuk['Ortalama']} - {en_dusuk['HarfNotu']})")
    
    print("\n[+] BAŞARILI ÖĞRENCİLER:")
    for ogr in basarililar:
        print(f"    - {ogr['Isim']}: {ogr['Ortalama']} [{ogr['HarfNotu']}]")

    print("\n[-] BAŞARISIZ ÖĞRENCİLER:")
    for ogr in basarisizlar:
        print(f"    - {ogr['Isim']}: {ogr['Ortalama']} [{ogr['HarfNotu']}]")

    print("\n[!] HATALI / EKSİK KAYITLAR (Sistem Dışı Bırakıldı):")
    for hata in hatali_kayitlar:
        print(f"    - No:{hata.get('OgrenciNo','?')} / {hata.get('Isim','?')} -> Sebep: {hata.get('Hata')}")
    print(f"{'='*40}")

    # Başarılı öğrencileri ayrı bir CSV dosyasına kaydediyoruz
    if basarililar:
        with open(cikti_dosyasi, "w", encoding="utf-8", newline="") as f:
            # extrasaction='ignore' parametresi, yapılandırılan 'alanlar' haricinde sözlükte 
            # fazladan veri (örneğin ham vize/final notları) varsa hata vermesini engeller.
            alanlar = ["OgrenciNo", "Isim", "Ortalama", "HarfNotu"]
            yazici = csv.DictWriter(f, fieldnames=alanlar, extrasaction='ignore')
            
            yazici.writeheader()
            yazici.writerows(basarililar)
            print(f"\n>>> SİSTEM BİLGİSİ: Başarılı öğrenciler başarıyla '{cikti_dosyasi}' dosyasına aktarıldı.")

if __name__ == "__main__":
    ornek_veri_olustur() # Test verisini diskte yarat
    rapor_olustur()      # Analiz motorunu başlat