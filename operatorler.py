# aritmetik operatorler

# +, -, /, *, %, **

# sayi1 = 120
# sayi2 = 50

# toplam = sayi1 + sayi2
# print("işlem sonucu" + " "*50 + str(toplam)) # 50 tane boşluk at dedik. ve sonucu stringe çevir.


# Ödevler:
# dışarıdan girilen 2 sayının toplaması, çarpımı, çıkarımını, bölümünü yap.

sayi1 = 30
sayi2 = 20

toplam = sayi1 + sayi2
print(toplam)

çarpım = sayi1 * sayi2
print(çarpım)

çıkarma = sayi1 - sayi2
print(çıkarma)

böl = sayi1 / sayi2
print(böl)

üstel = sayi1 ** sayi2
print(üstel)

yüzde = sayi1 % sayi2
print(yüzde)

sayi1 = float(input("lütfen 1. sayıyı giriniz : "))
sayi2 = float(input("lütfen 2. sayıyı giriniz : "))

toplam = sayi1 + sayi2
carpim = sayi1 * sayi2
çıkarma = sayi1 - sayi2
böl = sayi1 / sayi2
üstel = sayi1 ** sayi2
yüzde = sayi1 % sayi2

result = "toplama işlemi sonucu : " + \
    str(toplam) + "\nbölme işlemi sonucu : " + str(böl) + \
    "\nMod işlemi sonucu : " + \
    str(yüzde)+"\nKuvvet alma işlemi sonucu : " + \
    str(üstel)+"\nÇarpma işlemi sonucu : " + str(carpim)

print(result)

