# Bir öğrenci sözlüğünü JSON dosyasına yaz.
import json
ogrenci = {
    "id": 1,
    "ad": "Ahmet",
    "yas": 20,
    "not": 85
}

with open("ogrenci.json", "w", encoding="utf-8") as file:
    json.dump(ogrenci,file,ensure_ascii=False, indent=4)
print("1) Öğrenci sözlüğü JSON dosyasına yazıldı.\n")

# JSON dosyasını tekrar okuyarak sözlüğe dönüştür.
with open("ogrenci.json", "r", encoding="utf-8") as file:
    okunan_ogrenci = json.load(file)
print("2) JSON'dan okunan sözlük:")
print(okunan_ogrenci, "\n")

# Bir öğrenci listesini JSON dosyasında sakla
ogrenciler = [
    {"id": 1, "ad": "Ahmet", "not": 85},
    {"id": 2, "ad": "Ayşe", "not": 90},
    {"id": 3, "ad": "Mehmet", "not": 78}
]

with open("ogrenciler.json", "w", encoding="utf-8") as file:
    json.dump(ogrenciler,file,ensure_ascii=False, indent=4)

print("3) Öğrenci listesi JSON dosyasına kaydedildi.\n")

# Bir JSON metnini loads() ile Python nesnesine dönüştür.
json_metin = '{"ad":"Zeynep","yas":22,"not":95}'
python_nesnesi = json.loads(json_metin)
print("4)  bir JSON metini loads() ile python nesnesine çevrildi.\n")
print(python_nesnesi)

# Bir Python sözlüğünü dumps() ile JSON metnine dönüştür.
sozluk = {
    "ad": "Ali",
    "yas": 21,
    "not": 88
}
json_metin2 = json.dumps(sozluk,ensure_ascii=False, indent=4)
print("5) dumps() sonucu:")
print(json_metin2, "\n")

# Bir JSON dosyasına yeni bir öğrenci ekle.
with open("ogrenciler.json", "r", encoding="utf-8") as file:
    ogrenciler = json.load(file)

yeni_ogrenci = {
    "id": 4,
    "ad": "Elif",
    "not": 92
}

ogrenciler.append(yeni_ogrenci)

with open("ogrenciler.json", "w", encoding="utf-8") as dosya:
    json.dump(ogrenciler, dosya, ensure_ascii=False, indent=4)

print("6) Yeni öğrenci eklendi.\n")

# JSON dosyasındaki belirli bir öğrenciyi ara.
aranan_isim = "Ayşe"

with open("ogrenciler.json", "r", encoding="utf-8") as dosya:
    ogrenciler = json.load(dosya)

bulundu = False

for ogrenci in ogrenciler:
    if ogrenci["ad"] == aranan_isim:
        print("7) Öğrenci bulundu:")
        print(ogrenci)
        bulundu = True
        break

if not bulundu:
    print("7) Öğrenci bulunamadı.")

# JSON dosyasındaki bir öğrencinin notunu güncelle.
guncellenecek_id = 3
yeni_not = 95

for ogrenci in ogrenciler:
    if ogrenci["id"] == guncellenecek_id:
        ogrenci["not"] = yeni_not

with open("ogrenciler.json", "w", encoding="utf-8") as file:
    json.dump(ogrenciler, file, ensure_ascii=False, indent=4)
print("8) Öğrencinin notu güncellendi. \n")

# Dosya yoksa uygun davranışı belirle.
try:
    with open("olmayan_dosya.json", "r",encoding="utf-8") as file:
        veri = json.load(file)
except FileNotFoundError:
    print("9) Dosya Bulunamadı! \n")

# Bozuk JSON dosyası durumunu try-except ile yönet.
try:
    with open("bozuk.json", "w", encoding="utf-8") as file:
        file.write('{"ad": "Ahmet","yas": 20,}')   ## Hatalı JSON

    with open("bozuk.json", "r", encoding="utf-8") as file:
        veri = json.load(file)
except json.JSONDecodeError as hata:
    print("10) JSON okuma hatası: ")
    print(hata)

## MİNİ PROJE: KALICI ÖĞRENCİ SİSTEMİ
'''Önceki öğrenci yönetim sistemini JSON ile veri saklayacak hale getir.
Gereksinimler:
Öğrenciler students.json dosyasında saklanmalı.
Program açıldığında kayıtlı öğrencileri dosyadan okumalı.
Yeni öğrenci eklenebilmeli.
Öğrenci aranabilmeli.
Öğrencinin notları güncellenebilmeli.
Öğrenci silinebilmeli.
Program kapatıldığında veriler kaybolmamalı.
Program tekrar açıldığında kayıtlar yüklenmeli.
Öğrencileri not ortalamasına göre sırala.
Başarılı ve başarısız öğrencileri ayrı listele.
JSON dosyası bozuksa kullanıcıya açıklayıcı hata mesajı göster
Verileri bir sınıf yapısıyla yönetmeyi dene.'''
import json
import os

class KaliciOgrenciSistemi:
    def __init__(self, dosya_yolu="students.json"):
        self.dosya_yolu = dosya_yolu
        # Program açıldığında kayıtlı öğrencileri dosyadan okuma işlemi
        self.ogrenciler = self._verileri_yukle()

    def _verileri_yukle(self):
        """Diskteki JSON verisini belleğe (RAM) yükler."""
        if not os.path.exists(self.dosya_yolu):
            return {}
        
        try:
            with open(self.dosya_yolu, "r", encoding="utf-8") as dosya:
                return json.load(dosya)
        except json.JSONDecodeError:
            # JSON dosyası bozuksa hata mesajı gösterilir
            print("Kritik Hata: 'students.json' dosyası bozuk!")
            return {}
        except Exception as e:
            print(f"Beklenmeyen bir I/O hatası oluştu: {e}")
            return {}

    def _verileri_kaydet(self):
        """Program kapatıldığında verilerin kaybolmaması için değişiklikleri diske yazar."""
        with open(self.dosya_yolu, "w", encoding="utf-8") as dosya:
            json.dump(self.ogrenciler, dosya, ensure_ascii=False, indent=4)

    def ogrenci_ekle(self, ogrenci_no, isim, dersler_listesi, notlar_listesi):
        """Yeni öğrenci ekler"""
        ders_notlari = {ders: puan for ders, puan in zip(dersler_listesi, notlar_listesi)}
        
        self.ogrenciler[ogrenci_no] = {
            "isim": isim,
            "notlar": ders_notlari
        }
        self._verileri_kaydet()
        print(f"Başarılı: {isim} sisteme kaydedildi.")

    def ogrenci_ara(self, arama_metni):
        """Öğrenci araması yapar."""
        sonuclar = {
            no: bilgi for no, bilgi in self.ogrenciler.items() 
            if arama_metni.lower() in bilgi["isim"].lower() or arama_metni == no
        }
        return sonuclar

    def not_guncelle(self, ogrenci_no, ders_ismi, yeni_not):
        """Öğrencinin notlarını günceller."""
        if ogrenci_no in self.ogrenciler:
            self.ogrenciler[ogrenci_no]["notlar"][ders_ismi] = yeni_not
            self._verileri_kaydet()
            print(f"Başarılı: {ogrenci_no} numaralı öğrencinin {ders_ismi} notu güncellendi.")
        else:
            print("Hata: Öğrenci bulunamadı.")

    def ogrenci_sil(self, ogrenci_no):
        """Öğrenciyi sistemden siler."""
        if ogrenci_no in self.ogrenciler:
            silinen = self.ogrenciler.pop(ogrenci_no)
            self._verileri_kaydet()
            print(f"Başarılı: {silinen['isim']} sistemden silindi.")
        else:
            print("Hata: Silinecek öğrenci bulunamadı.")

    def _ortalama_hesapla(self, notlar_sozlugu):
        notlar_listesi = list(notlar_sozlugu.values())
        return sum(notlar_listesi) / len(notlar_listesi) if notlar_listesi else 0

    def ogrencileri_sirala(self):
        """Öğrencileri not ortalamasına göre yüksekten düşüğe sıralar."""
        sirali_liste = sorted(
            self.ogrenciler.items(),
            key=lambda item: self._ortalama_hesapla(item[1]["notlar"]),
            reverse=True
        )
        return sirali_liste

    def basari_durumunu_listele(self, gecme_notu=60):
        basarililar = dict(filter(
            lambda item: self._ortalama_hesapla(item[1]["notlar"]) >= gecme_notu, 
            self.ogrenciler.items()
        ))
        
        basarisizlar = dict(filter(
            lambda item: self._ortalama_hesapla(item[1]["notlar"]) < gecme_notu, 
            self.ogrenciler.items()
        ))
        
        return basarililar, basarisizlar

    def rapor_al(self):
        """enumerate() kullanarak sistemdeki öğrencileri numaralandırarak yazdırır."""
        print("\n--- SİSTEM RAPORU ---")
        # enumerate(), 1'den başlayarak indeks numarası üretir
        for indeks, (no, bilgi) in enumerate(self.ogrenciler.items(), start=1):
            ort = self._ortalama_hesapla(bilgi["notlar"])
            print(f"{indeks}. [No: {no}] {bilgi['isim']} - Ortalama: {ort:.2f}")

if __name__ == "__main__":
    sistem = KaliciOgrenciSistemi()
    
    sistem.ogrenci_ekle("101", "Hatice Can", ["Algoritma", "Matematik"], [95, 100])
    sistem.ogrenci_ekle("102", "Beyza Işık", ["Algoritma", "Matematik"], [90, 85])
    sistem.ogrenci_ekle("103", "Pınar Adalı", ["Algoritma", "Matematik"], [50, 45])
    
    print("\nArama Sonucu ('Işık'):", sistem.ogrenci_ara("Işık"))

    sistem.not_guncelle("103", "Algoritma", 60)

    print("\nOrtalamaya Göre Sıralı:")
    for ogr in sistem.ogrencileri_sirala():
        print(f"{ogr[1]['isim']} - {sistem._ortalama_hesapla(ogr[1]['notlar'])}")

    basarili, basarisiz = sistem.basari_durumunu_listele()
    print(f"\nBaşarılı Öğrenci Sayısı: {len(basarili)}")
    print(f"Başarısız Öğrenci Sayısı: {len(basarisiz)}")

    sistem.rapor_al()