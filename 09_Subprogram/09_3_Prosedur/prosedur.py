# ============================================================================ Prosedur ====================================================================
'''
Setelah mengetahui berbagai hal tentang fungsi pada bagian materi sebelumnya, mari kita simak penjelasan prosedur berikut.
'''
print('\n')
print(" Fundamental Prosedur ".center(150, "="), "\n")
'''
                                                                            Fundamental Prosedur

Dalam KBBI, kata prosedur memiliki makna sebagai tahap kegiatan untuk menyelesaikan suatu aktivitas. Hal ini sama seperti prosedur sebagai subprogram yang merupakan pengelompokan instruksi-instruksi yang sering dipakai dalam program. 

Berbeda dengan fungsi, prosedur tidak mengharuskan adanya parameter input atau output dan dapat dipandang sebagai fungsi yang tidak menghasilkan nilai. Dalam Python, prosedur didefinisikan dengan return tanpa ekspresi atau nilai yang dihasilkan di akhir fungsi.

    def nama_prosedur(parameter1, parameter2, ...):
        # Blok kode prosedur
        # Tindakan atau perintah yang ingin dilakukan
        # ...
    
    # Pemanggilan prosedur
    nama_prosedur(nilai1, nilai2, ...)

    Secara konsep, gambar di atas merupakan kerangka dasar prosedur pada Python. Sekilas memang sangat mirip dengan fungsi, hanya saja kita tidak mendefinisikan return dan bahkan return value. 

    Berikut adalah contoh prosedur dalam Python.
'''

# Contoh Penerapaan Prosedur
def sapa(name, pesan):
    print(f"Halo {name}, {pesan}!")

'''
Pada contoh di atas, kita membuat fungsi bernama "sapa()" untuk menyapa nama siapa pun yang dikirimkan. Perhatikan bahwa kita tidak mendefinisikan return dan membuat return value. Konsep ini disebut sebagai prosedur, yakni fungsi Python yang kita buat tidak mengeluarkan nilai dari fungsi tersebut.

Kita sebenarnya bisa menambahkan pernyataan return, tetapi kita tidak menyertakan return value setelahnya.
'''

# Contoh Prosedur dengan Return
def sapa(name, pesan):
    print(f"Halo {name}, {pesan}!")

# Pada kode di atas, kita membuat prosedur dengan kode yang sama seperti sebelumnya, hanya saja kita mendefinisikan return dan tidak memberikan return value setelahnya.


# ========================================================= Mendefinisikan dan Memanggil Prosedur ======================================================
'''
                                                            Mendefinisikan dan Memanggil Prosedur

Untuk memanggil prosedur, caranya serupa seperti Anda memanggil fungsi. Cukup mendefinisikan satu baris instruksi, seperti "sapa()". Untuk pemberian argumen dan parameter pada prosedur, kita dapat memakai cara yang sama seperti pada fungsi yang telah dijelaskan sebelumnya. 
'''
# Mendefinisikan dan Memanggil Prosedur
print(" Mendefinisikan dan Memanggil Prosedur ".center(70, "-"), "\n")

# Contoh Pemanggilan Prosedur
print("> Contoh Pemanggilan Prosedur\n")
def sapa(name, pesan):
    print(f"Halo {name}, {pesan}!")

sapa("Jajang", "Apa kabar?")

'''
    Output:
    Halo Jajang, Apa kabar?

    Pada contoh di atas, kita mendefinisikan prosedur tanpa adanya return statement. Perhatikan bahwa program tetap menampilkan hasil fungsi karena kita langsung menggunakan fungsi "print()" dalam prosedur yang telah dibuat. Jadi, walaupun tidak ada return atau return value, kita tetap mendapatkan output-nya.

    Kita juga bisa membuat prosedur yang tidak memiliki parameter input. Ketika kita memanggil prosedur tersebut, program akan langsung menjalankannya.

    Mari kita ubah kode di atas jika tidak memiliki parameter.
'''

# Contoh Prosedur Tanpa Parameter
print("\n> Contoh Prosedur Tanpa Parameter\n")
def welcome_massage():
    print("Selamat datang di Python!\n")

welcome_massage()

'''
    Output:
    Selamat datang di Python!

    Pada contoh di atas, prosedur "welcime_massage" tidak menggunakan parameter sama sekali. Namun, sebab body prosedur tersebut memiliki perintah “print()” untuk menampilkan pesan “Selamat datang di Python!” ke layar, prosedur tersebut akan menampilkan teks ketika kita memanggilnya dengan perintah “welcome_massage()”. 
'''