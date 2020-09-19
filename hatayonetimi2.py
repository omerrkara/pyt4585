try:
    sayi_bir = int(input("Lütfen bir sayı giriniz : "))
    sayi_iki = int(input("Lütfen ikinci sayıyı giriniz : "))

    toplam = sayi_bir + sayi_iki
    fark = sayi_bir - sayi_iki
    carpim = sayi_bir * sayi_iki
    bolum = sayi_bir / sayi_iki
    mod = sayi_bir % sayi_iki

    print(f"sayıların toplamı : {toplam}\nSayıların Farkı : {fark}\nSayıların  Bölümü : {bolum}\nSayıların Bölüm Farkı : {mod}\nSayıların Çarpımı : {carpim}")

except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print(ZeroDivisionError)
except FileExistsError:
    print("FileExistsError")
except:
    print("Tüm hataları kabul ediyorum, özür dilerim.")