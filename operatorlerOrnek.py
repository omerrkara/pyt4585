#Örnek 1) Dışardan alınan iki sayının toplamıyla farkının bölümünden kalan kaçtır?

#Örnek 2) Dışardan girilen bir sayının 10 eksiğinin 20 fazlasının ikiye bölümnden kalan kaçtır?

#Örnek 3) 
# ---------------------
#cevap 1 

# sayi1 = int(input("Lütfen bir sayı giriniz : "))
# Sayi2 = int(input("Lütfen ikinci bir sayı giriniz : "))

# toplam = sayi1 + Sayi2
# fark = sayi1 - Sayi2
# mod = toplam % fark
# print("İşlem sonucu : ", mod)



# toplam = sayi1 + Sayi2
# fark = sayi1 - Sayi2
# Kalan = (sayi1 + sayi2) % (sayi1-Sayi2)

# print(Kalan)
# ----------------

# cevap 2
# sayi = sayi - 10
# sayi = sayi + 20
# sayi = sayi % 2
# print("işlem sonucu : ", sayi)

# # sayi1 = int(input("Lütfen bir sayı giriniz : "))          # bu olmaz çünkü paremetre değişebilir. 
# # x = (int(sayi1) + 10) / 2
# # print(x)

# # veya 
# sayi = ((sayi - 10) + 20) % 2
# print("işlem sonucu : ", sayi)

#cevap 3
# sayi1 = int(input("Lütfen bir sayı giriniz : "))
# Sayi2 = int(input("Lütfen ikinci bir sayı giriniz : "))

# kare1 = sayi1**2
# kare2 = sayi2**2

# toplam = kare1 + kare2
# fark = kare1 - kare2
# print(("işlem sonucu : ", (toplam + fark))

 
 #cevap 4

# vizenotu = float(input("Lütfen bir vize notu giriniz : "))
# finalnotu = float(input("lütfen final notunuzu giriniz : "))
#  _not = (vizenotu * 0.30) + (finalnotu * 0.70)
#  print("Not ortalamanız : ", _not)

 # cevap 5  

isim = input("lütfen adınızı giriniz : ")
soyisim = input("lütfen soyadınızı giriniz : ")
mail = "{}.{}@hotmail.com".format(isim,soyisim)
print(mail)


