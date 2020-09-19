# telefonNumarasi = int(input("Lütfen telefon numaranızı giriniz : "))
# print("Tebrikler, hayatta birkez de olsa bir şey başardınız!")

try:
    telefonNo = int(input("Lütfen telefon numaranızı giriniz : "))  # print("işlem yapılacak kod blokları")
    print("tebrikler") 

except ValueError:
    print("valueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("işlem hatası")



    