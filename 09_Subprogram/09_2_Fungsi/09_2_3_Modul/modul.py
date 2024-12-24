import sys
sys.path.append('/path/to/LEARNING-PYTHON/09_Subprogram/09_2_ungsi/09_2_3_Modul')
print(" Menulis Modul pada Python ".center(150, ("=")))
'''
                                                                                Modul

Pembahasan terakhir terkait fungsi adalah kita akan mempelajari cara memanggil sebuah fungsi dari berkas lain. Masih ingat dengan modul? Ia adalah sebuah file berisi kode Python dan di dalamnya terdapat fungsi, kelas, dan sebagainya.

Sebab setiap file berekstensi .py dapat direferensikan sebagai modul, Anda bisa melakukan impor file dari satu file ke yang lainnya. Layaknya ketika Anda menggunakan library, modul, dan sebagainya.

Untuk mengikuti materi kali ini, kami rekomendasikan untuk menggunakan IDE, seperti Visual Studio Code atau PyCharm untuk memaksimalkan pembelajaran. Selain itu, kita akan membuat dua buah file. Pastikan kedua file tersebut berada dalam folder atau direktori yang sama. Mari kita mulai.

    1.  Pertama , buat sebuah file bernama hello.py berisi fungsi yang ingin kita impor. Berikut kodenya

        def welcome_message(title):
            bintang = "*" * (len(title) + 10)
            print(bintang)
            print(f"**** {title} ****")
            print(bintang)
    
        Kode di atas merupakan fungsi untuk menampilkan sapaan awal pada sebuah program yang sering kita temui misalkan "Hallow Bagas Ganteng Selamat Datang". Kita akan memanggil fungsi ini pada file Python lain.
    2.  Kedua, buat sebuah file bernama main.py. Pastikan ia berada dalam satu folder atau direktori dengan file sebelumnya.
        Pada file main.py, masukkan kode pemanggil fungsi berikut.

            from hello import welcome_message
            welcome_message("Selamat Datang Tuan Raja KING! Satria Dirgantara Nuryaman")
    3.  Terakhir, jalankan file main.py. Jika berhasil, maka output yang akan muncul adalah sebagai berikut.
    
'''
# Import modul sapaan
from sapaan import welcome_message

# Memanggil fungsi welcome_message
print('\n')
welcome_message("Selamat Datang Tuan Raja KING! Satria Dirgantara Nuryaman")
'''
        Pada kode di atas, kita mengimpor modul sapaan yang berisi fungsi welcome_message. Kemudian, kita memanggil fungsi tersebut dengan parameter "Selamat Datang Tuan Raja KING! Satria Dirgantara Nuryaman". Jika Anda menjalankan file main.py, maka output yang akan muncul adalah sebagai berikut.

        *******************************************************************
        **** Selamat Datang Tuan Raja KING! Satria Dirgantara Nuryaman ****
        *******************************************************************
        Dengan begitu, kita telah berhasil memanggil fungsi dari modul yang berbeda. Selamat mencoba!
'''

