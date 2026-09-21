"""f = open("example.txt", "w", encoding="UTF-8")
f.write("Hello python!\n")
f.close()

'''v = open("example.txt", "w", encoding="UTF-8")
v.write("Hello!\n")
v.close()

b = open("example.txt", "w", encoding="UTF-8")
b.write("Python!\n")
b.close()'''

f = open("example.txt", "a", encoding="UTF-8")
f.write("This is my learning journey\n")
f.close()"""

#f = open("example.txt", "a", encoding="UTF-8")
#f.write("Today I'm learning file handing\n")
#f.close()

#f = open("example.txt", "r", encoding="UTF-8")
#print(f.read(3))
#print(f.read(4))
#print(f.read(13))
#f.seek(0)  # dosyanın başına geri dönmesi için 
#print(f.readline())
#print(f.readline())
#print(f.readlines())
#print(f.readlines())
#for line in f:
  #  print(line)
#f.close()

#with open("example.txt","r",encoding="utf-8") as f:
 #   veri = f.read()
 #  print(veri)

#with open("example.txt", "a", encoding="utf-8") as f:
    #f.write("I love writing code")

## Problem-1 : Günlük

'''notAl = input("Notunuzu Girin: ")
gun_sayisi = 1
with open("journal.txt", "r", encoding="utf-8") as f:
  satirlar = f.readlines()
  gun_sayisi = len(satirlar) + 1
with open("journal.txt", "a",encoding="utf-8") as f:
  f.write(f"{gun_sayisi}. gun:{notAl}\n")'''

## Problem-2 : Dosyadaki Satır Sayısı

'''with open("journal.txt", "r", encoding="utf-8") as f:
  satirlar = f.readlines()

satir_sayisi = len(satirlar)
print(satir_sayisi, "Lines\n")'''

## Problem-3 : Kelime Sayısı

'''with open("journal.txt", "r", encoding="utf-8") as f:
    veri = f.read()
    kelime = veri.split()
    print(len(kelime))'''

##Problem-4 : Arama

'''with open("journal.txt", "r", encoding="utf-8") as f:
    arama = input("Search: ")
    veri = f.read()
    durum = 0
    for sonuc in veri.split():
        if sonuc == arama:
            durum = 1
            break
        else:
            durum = 0

    if durum == 0:
        print("Not Found!")
    else:
        print("Found!")'''

## MİNİ PROJE: PERSONAL JOURNAL
def show_menu():
    print("=====================")
    print("     MY JOURNAL      ")
    print("=====================")
    print("1. Add Entry")
    print("2. Show Entries")
    print("3. Search")
    print("4. Exit\n")

def add_entry():
      notAl = input("Notunuzu Girin: ")
      gun_sayisi = 1
      with open("journal.txt", "r", encoding="utf-8") as f:
        satirlar = f.readlines()
        gun_sayisi = len(satirlar) + 1
      with open("journal.txt", "a",encoding="utf-8") as f:
        f.write(f"{gun_sayisi}. gun:{notAl}\n") 

def show_entries():
    with open("journal.txt", "r", encoding="utf-8") as f:
        veri = f.read()
        print(veri)

def search_entries():
    with open("journal.txt", "r", encoding="utf-8") as f:
        arama = input("Search: ")
        veri = f.read()
        durum = 0
        for sonuc in veri.split():
            if sonuc == arama:
                durum = 1
                break
            else:
                durum = 0

        if durum == 0:
            print("Not Found!")
        else:
            print("Found!")

show_menu()
secim = 0
while secim != 4:
    secim = int(input("Choose: "))
    if secim == 1:
        add_entry()
    elif secim == 2:
        show_entries()
    elif secim == 3:
        search_entries()
    elif secim == 4:
        print("Exit")
    else:
        print("choose number between 1-4!")