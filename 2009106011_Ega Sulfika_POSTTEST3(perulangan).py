import os
import time

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("***************************************************")
        print("\t\tMATERI PERULANGAN ")
        print("***************************************************")
        #2009106011 + 10 = 21 
        bilangan = int(input("Masukkan NIM dengan 2 digit terakhir + 10 : "))
        x = 1
        y = 1
        while (x <= bilangan):
            print (y)
            y += 1
            if (y == 10):
                y -= 9
            x += 1
        break
    #apabila sebuah string yang dimasukkan
    except ValueError:
        print("***************************************************")
        print("Silahkan Coba lagi, karena itu angka no valid...")
        print("***************************************************")
        time.sleep(2)
