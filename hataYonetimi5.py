# try:
#     sayi = int(input("Lütfen sayı giriniz : "))
#     print("Tebrikler")
# except:
#     print("vazgeçtim")

    # -----------------------

try:
    # db connection open
    sayi = int(input("Lütfen sayı giriniz : "))
    #connection error
    print("Tebrikler")
    # - db connection close - (- buraya ifadeyi yazmamamız gerektiği anlamına geliyormuş)
except:
    print("vazgeçtim")
    # - db connection close -
finally:                                                
    print("her durumda bir defa tetiklenir")
    # db connection close 
    # her iki durumda da yapılması gerekn işlemleriniz varsa bunu finally içerisine yazmanız kod tekrarını engelleyecktir.