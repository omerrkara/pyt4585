# convert : elinizdeki bir veri tipini farklı bir veri tipine çevirme işlemi yapar. 

# int() : tam sayı veri tipiine çevirir
# str() : string(metinsel) değere çevirme işlemi yapar
# float() : ondalıklı değere çevirme işlemi
# chr() : verdiğiniz sayısal değerin, karakter karşılığını teslim eder
# ord() : verdiğiniz karekterin, ascii (sayısal) karşılıgını teslim eder.

# sayi1 = input("lütfen 1.sayıyı giriniz : ")
# sayi2 = input("lütfen 2.sayıyı giriniz : ")

# print(sayi1)
# print(type(sayi1))

# print(sayi1 + sayi2)

# ctrl + k + c => yorum satırına alır
# ctrl + k + u => yorum satırından alır
# alt + shift + f => kodları düzenle

# toplam = float(sayi1) + float(sayi2)
# print(toplam)

# result = int(sayi1) + int(sayi2)
# print(result)

print(chr(65), ord('A'))
print(chr(90), ord('Z'))
print(chr(97), ord('a'))
print(chr(122), ord('z'))

sayi = 100

print("Sayının değeri " + str(sayi))
