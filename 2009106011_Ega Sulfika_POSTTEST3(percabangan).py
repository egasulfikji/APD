import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
def awalan():
  print("********************************************************")
  print("\tSelamat Datang di Toko Kue Sule")
  print("*******************************************************")
  print("Menu kue yang ada: ")
  print("+ Kue Keju     : Rp6.000")
  print("+ Kue Cokelat  : Rp3.500")
  print("*******************************************************")
  menukue()

def menukue():
  kue_keju = 6000
  kue_cokelat = 3500
  Menukeju     = int(input("Masukkan berapa kue keju yang anda inginkan     : "))
  if int(Menukeju >=0 and Menukeju <=3):
      print("Anda tidak mendapatkan diskon")
      hasil1 = float((Menukeju*kue_keju)+0)
      print("Total yang harus anda bayarkan : Rp", hasil1)
      print("\n*******************************************************")
  elif int(Menukeju >=4 and Menukeju <=15):
      print("\nAnda mendapatkan discon 10%")
      hasil2 = float((Menukeju*kue_keju)+(10/100))
      print("Total yang harus anda bayarkan : Rp", hasil2)
      print("*******************************************************")
  elif int(Menukeju >=16 and Menukeju <=25):
      print("Anda mendapatkan diskon 15%")
      hasil3 = float((Menukeju*kue_keju)+(15/100))
      print("Total yang harus anda bayarkan : Rp", hasil3) 
      print("\n*******************************************************")
  else:
      print("Kue Keju Sold Out")
      print("Silahkan datang kembali...")
      print("\n*******************************************************")

  Menucokelat   = int(input("Masukkan berapa kue cokelat yang anda inginkan  : "))
  if int(Menucokelat >=0 and Menucokelat <=4):
      print("Anda tidak mendapatkan diskon")
      hasil5 = float((Menucokelat*kue_cokelat)+0)
      print("Total yang harus anda bayarkan : Rp", hasil5)
      print("\n*******************************************************")
  elif int(Menucokelat >=5 and Menucokelat <=20):
      print("Anda mendapatkan diskon 7%")
      hasil6 = float((Menucokelat*kue_cokelat)+(7/100))
      print("Total yang harus anda bayarkan : Rp", hasil6)
      print("\n*******************************************************")
  elif int(Menucokelat >=21 and Menucokelat <=35):
      print("Anda mendapatkan discon 12%")
      hasil7 = float((Menucokelat*kue_cokelat)+(12/100))
      print("Total yang harus anda bayarkan : Rp", hasil7)
      print("\n*******************************************************")
  else:
      print("Kue Cokelat Sold Out")
      print("Silahkan datang kembali...")
      print("\n*******************************************************")
 
awalan()
