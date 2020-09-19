# try:
#     sayi = int(input("Lütfen sadece sayısal değer giriniz : "))
#     print("gelen sayı : ", sayi)
#     sayi = sayi/0
#     print("işlem sonucu")
# except ValueError as ex:        # value error un yerine artık burdaki ex geçerlidir.
#     print("Lütfen tekrar deneyiniz")
#     print("Sistem mesajı :", ex)
# except Exception as ex:
#     print("İşlem hatası")
#     print("işlem hatası :", ex)                                      # int in bir üst limiti var her sayıyı veremezsin, 24 verdiğinde 
                                                                       # de hata vermesinin sebebi sayi/0 dan dolayı.

