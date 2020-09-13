# yorum satırı
print("hello dünya")


# degisken tanimlama kurallari
# 1) degisken, ismi sayi ile baslayamaz
# 2) degisken, 2 veya fazla kelimeden olusamaz, olusacak ise, ornk
# benim kullaniciAdim = "kahramanmaraslimustafa" yanlış
# benim_kullaniciAdim = "kahramanmaraslimustafa" doğru
# 3) degisken tanimlamasi yapilirken, kesinlikle tanimli kelimeler kullanilamaz
# print = 12 yanlış
# 4) degisken adinda lutfen, turkce karakter kullanmayiniz.

benim_adim = "murat vuranok"
mail_adresim = "murat.vuranok@bilgeadam.com"
adim = "murat"
soyadim = 'vuranok'

# int, strin, float
sayi = 5  # int tam sayi veri tipi
print(sayi)
print(type(sayi))

print(adim)
print(soyadim)

print(adim + " " + soyadim)
print(adim, soyadim)

fullname = adim + " "+ soyadim
print(fullname)

x = True
y = False

print(x)
print(y)
print(type(x))

# \n bir alt satıra geç => new line
print((fullname + "\n")*5)

print(type(fullname))

print("""
bilge
adam
yazılım
kursu
""")
#üç tırnak konulmasının amacı çıktıyı istedigimiz gibi göstermek, yukardaki gibi altalta örneğin.

print("bilge adam \"beşiktaş\" yazılım dersleri istanbul\n\
    python kursu\
    test satırı")
    