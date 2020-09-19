try:
    sayi1 = int(input("Lütfen sayı giriniz : "))
    sayi2 = int(input("Lütfen sayı giriniz : "))
    sonuc = sayi1 / sayi2

except ValueError as ex:
    print("işlem hatası")
else:
    try:
        print(sayi1 / sayi2)
        print("işlem sonucu")  
    except ZeroDivisionError as ex:
        print(ex)

