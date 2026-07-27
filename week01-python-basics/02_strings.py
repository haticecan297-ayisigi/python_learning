#görev-1
isim = "Hatice"
print(isim.upper())
print(isim.lower())
print(len(isim))
print(isim[0])
print(isim[-1])
print(isim[:3])
#görev-2
isim = input("Isminiz: ")
print("Merhaba ",isim)
uzunluk = f"Isminiz {len(isim)} karakterden olusmaktadir"
print(uzunluk)
#görev-3
sentence = "Learnin python is so fun"
sentence = sentence.upper()
print(sentence)
sentence = sentence.lower()
print(sentence)
sentence = sentence.replace("fun","boring")
print(sentence)
print(sentence.split(sep=" ", maxsplit=-1))
print(sentence.split(sep= " ", maxsplit = 2))
print(sentence.count("p"))
print(sentence.count("i"))