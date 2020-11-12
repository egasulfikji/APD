import os
import datetime
import time

#list
mahasiswa = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def date_time():
    x = datetime.datetime.now()
    print("\nTanggal saat ini :",x.day,"/",x.month,"/",x.year)
    print("Waktu saat ini   :" ,x.hour,":",x.minute,":",x.second)
    if x.hour >= 1 and x.hour < 12:
        print("\nSelamat Pagi")
    elif x.hour >=12 and x.hour < 15:
        print("\nSelamat Siang")
    elif x.hour >=15 and x.hour < 18:
        print("\nSelamat Sore")
    else:
        print("\nSelamat Malam")
    print("*************************************************************************") 

def welcome():
    clear_screen()
    print("*************************************************************************") 
    print("SELAMAT DATANG DI PROGRAM BIODATA & PERHITUNGAN RATA-RATA NILAI MAHASISWA")
    print("*************************************************************************") 
    date_time()
    time.sleep(10)
    daftar()

def daftar():
    clear_screen()
    print("**************************************************************")
    print("Silahkan Pilih Daftar Menu Di Bawah!!!")
    print("[1] Biodata Mahasiswa")
    print("[2] Perhitungan Rata-Rata Nilai Mahasiswa")
    print("[3] Keluar")
    print("**************************************************************")  
    Menu = str(input("Masukkan Pilihan Anda: "))
    if (Menu == "1"):
        clear_screen()
        biodata()
    elif (Menu == "2"):
        clear_screen()
        nilai()
    elif (Menu == "3"):
        print("**************************************************************")  
        print("Terima Kasih Sudah Menggunakan Program Kami")
        print("**************************************************************")
        exit()  
    else: 
        print("**************************************************************")
        print("Anda Memilih Menu yang Salah!!!")
        print("**************************************************************")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter Untuk Kembali...")
    daftar()

#menginput nama, Nim dan nilai
def biodata():
    print("\n*************************************************************************") 
    print("************************* Masukkan Biodata Anda *************************")
    print("*************************************************************************") 
    nama = str(input("Masukkan Nama Lengkap               : "))
    mahasiswa.insert(0,nama)
    ttl = str(input("Masukkan Tempat, Tanggal Lahir      : ")) 
    mahasiswa.insert(1,ttl)
    suku = str(input("Masukkan Suku                       : "))
    mahasiswa.insert(2,suku)
    alamat_rumah = str(input("Masukkan Alamat Rumah               : "))
    mahasiswa.insert(3,alamat_rumah)
    jumlah_saudara = int(input("Masukkan Jumlah  Saudara            : "))
    mahasiswa.insert(4,jumlah_saudara)
    slta = str(input("Masukkan Asal SLTA                  : "))
    mahasiswa.insert(5,slta)
    organisasi = str(input("Masukkan Penggalaman Organisasi     : "))
    mahasiswa.insert(6,organisasi)
    prodi = str(input("Masukkan Prodi                      : "))
    mahasiswa.insert(7,prodi)
    nim = int(input("Masukkan NIM                        : "))
    mahasiswa.insert(8,nim)

    clear_screen()
    print("*******************************************************")
    print("Rincian Biodata Anda")
    print("*******************************************************")
    print("Perkenalkan nama saya {}.".format(mahasiswa[0]), "Saya lahir di {} dan tepat pada tanggal itu di tahun 2021 saya genap berusia 18 tahun.".format(mahasiswa[1]), "Saya keturunan dari suku {}.".format(mahasiswa[2]), "Saya berdomisili di Tanah Grogot tepatnya di {}.".format(mahasiswa[3]), "Dikelurga, saya anak ke-2 dari {} bersaudara.".format(mahasiswa[4]), "Saat SLTA saya menempuh pendidikan di {} dengan jurusan Teknik Komputer & jaringan.".format(mahasiswa[5]), "Selama menempuh pendidikan SLTA saya mengikuti organisasi {} dengan masa jabatan anggota kurang dari 3 tahun.".format(mahasiswa[6]), "Sekarang saya menjadi mahasiswi di Universitas Mulawarman, Fakultas Teknik, Prodi {}".format(mahasiswa[7]), "dengan NIM {}.".format(mahasiswa[8]))   
    print("\n")
    print("*******************************************************")
    back_to_menu()

def nilai():
    print("*******************************************************") 
    print("***************** Masukkan Nilai Anda *****************")
    print("*******************************************************") 
    quiz = int(input("Masukkan Nilai Quiz Anda                      :"))
    mahasiswa.insert(9,quiz)
    uts = int(input("Masukkan Nilai UTS Anda                       :"))
    mahasiswa.insert(10,uts)
    uas = int(input("Masukkan Nilai UAS Anda                       :"))
    mahasiswa.insert(11,uas)
    absensi = int(input("Masukkan Berapa Persentase Kehadiran Anda (%) :"))
    mahasiswa.insert(12,absensi)

    #formula mencari masing-masing nilai
    Quiz = quiz*20/100
    Uts = uts*30/100
    Uas = uas*40/100
    Absensi = absensi*10/100

    #formula mencari nilai akhir
    nilai_akhir = float((Uts+Uas+Quiz+Absensi)/100*4)
    mahasiswa.insert(13,nilai_akhir)

    #menampilkan output nama, nim dan nilai yang telah diinputkan
    clear_screen()
    print("*************************************************")
    print("Nama             : {}".format(mahasiswa[0]))
    print("NIM              : {}".format(mahasiswa[8]))
    print("Prodi            : {}".format(mahasiswa[7]))   
    print("*************************************************")
    print("Nilai Quiz       : {}".format(mahasiswa[9]))
    print("Nilai UTS        : {}".format(mahasiswa[10]))
    print("Nilai UAS        : {}".format(mahasiswa[11]))
    print("Nilai Absensi    : {}".format(mahasiswa[12]))
    print("*************************************************")
    print("Nilai Akhir      : {}".format(mahasiswa[13]))
    print("*************************************************") 
    
    #kondisi if untuk menentukan keterangan LULUS atau TIDAK LULUS
    if nilai_akhir >= 2.50: 
        print("Keterangan: LULUS ")
        print("*************************************************") 
    else:
        print("Keterangan: TIDAK LULUS")
        print("*************************************************") 
    back_to_menu()

if __name__ == "__main__": 
    while True:
        welcome()
