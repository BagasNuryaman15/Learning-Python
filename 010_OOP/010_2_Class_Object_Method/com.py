print("\n")
print(" Class, Object, dan Method ".center(150, "="), "\n")
'''
                                                                            Class, Object, And Methode

Sebelum mengenal secara teknis class, object, dan method. Mari kita berandai-andai sejenak untuk memahami konsep object-oriented programming (OOP). 

Bayangkan Anda adalah seorang penggiat mobil, suatu waktu teman Anda yang berasal dari antah-berantah datang menghampiri. Kalian pun mulai berbincang dan dimulai dengan dia yang bertanya satu hal, "Apa itu mobil?".

Anda bisa menjawab, "Mobil adalah jenis kendaraan dengan empat roda yang memiliki kemampuan untuk bergerak maju, mundur, berbelok, dan berhenti. Mobil dapat melaju dengan kecepatan dari 0 hingga 160 km/jam. Mobil juga memiliki variasi warna yang beragam, termasuk merah, hitam, dan warna lainnya."

Berdasarkan ilustrasi tersebut, mobil dapat dikatakan sebagai sebuah kelas (class) dan perilaku (method) mobil tersebut dapat melaju, mundur, berbelok, dan berhenti. Mobil memiliki atribut warna dan warna tersebut bisa beragam, seperti merah, hitam, dan sebagainya serta memiliki kecepatan berkisar antara 0 hingga 160 km/jam.

Class dapat diibaratkan sebagai blueprint atau cetakan. Dalam contoh percakapan di atas, mobil dapat digambarkan sebagai contoh class atau blueprint. Ketika class telah dibuat, Anda dapat membuat sebuah objek baru berdasarkan class tersebut. Objek baru ini memiliki karakteristik, atribut, dan perilaku sama dengan class yang menjadi cetakannya. Anda pun dapat mengubah nilai atribut dari objek tersebut. Perhatikan gambar di bawah ini.

Class adalah cetakan atau blueprint yang digunakan untuk membuat objek. Objek adalah instance dari class. Objek memiliki atribut dan perilaku yang sama dengan class yang menjadi cetakannya.

        Kelas (Mobil)
    
    Perilaku (Method)          Atribut
    - Melaju                   - Warna
    - Mundur                   - Kecepatan
    - Berbelok
    - Berhenti

        Mobil Bagas Ferarri (objek)
    Perilaku (method)          atribut
    - Melaju                   - Warna (Merah)
    - Mundur                   - Kecepatan (356 km/jam)
    - Berbelok
    - Berhenti

Pada gambar di atas, kita memiliki sebuah kelas bernama Mobil. Kelas ini memiliki method, yaitu bergerak maju, mundur, berbelok, dan berhenti. Dari kelas ini, kita bisa membuat objek baru, misalkan membuat mobil Bagas Ferarri.

Objek baru tersebut memiliki unsur method dan atribut sama dengan kelas yang menjadi cetakannya. Bahkan, kita bisa mengubahnya sesuai keinginan. Misalnya pada objek Mobil Dicoding, kita mengubah warnanya menjadi biru. Jika kita tarik ke perandaian lain, ini mirip seperti manusia di seluruh dunia. Kita memiliki teman bernama Budi, Herman, dan Asep yang walaupun nama mereka berbeda, tetapi mereka tetaplah sama-sama manusia seperti kita.

Tidak hanya objek, Anda juga dapat membuat kelas baru untuk mewarisi kelas yang sudah ada.

Dalam contoh di atas, kita membuat kelas Mobil. Kita bisa membuat kelas baru bernama Mobil Sport yang mewarisi kelas Mobil. Kelas Mobil Sport memiliki method dan atribut yang sama dengan kelas Mobil 

Secara umum, konsep OOP dalam pemrograman sangat mirip seperti ilustrasi-ilustrasi di atas. Object-oriented programming adalah paradigma pemrograman berorientasi pada pengorganisasian kode menjadi objek-objek yang memiliki atribut dan perilaku (method). Objek merupakan perwujudan dari class dengan anggapan bahwa kelas adalah cetakan yang memungkinkan kita dapat membuat banyak objek berdasarkan cetakan tersebut.

Method adalah perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Sebagaimana halnya maju, mundur, berbelok, dan berhenti pada contoh sebelumnya. Atribut adalah variabel yang menjadi identitas dari objek atau kelas, seperti warna dan kecepatan pada contoh sebelumnya.

Mari sederhanakan dengan tabel berikut.

    Nama                Dekripsi                                                                                                            Contoh
    class(Kelas)        Cetakan (blueprint) untuk membuat objek-objek yang memiliki karakteristik dan perilaku serupa.                      Mobil dan Manusia
    Object(Objek)       Perwujudan dari kelas.                                                                                              Mobil Dicoding; Budi, Herman, Asep.
    Perilaku (Method)   Perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas.                                                  Maju, mundur, berbelok, berhenti.
    Atribut             Variabel yang menjadi identitas dari objek atau kelas.                                                              Warna, kecepatan, merek.
'''
# ============================================================================= Class ==================================================================
'''
                                                                                Class

Pembuatan class dalam Python mirip seperti fungsi, yakni perlu menggunakan keyword untuk bisa membuatnya. Keyword atau kata kunci untuk membuat kelas dalam Python adalah "class". Mari kita buat sebuah kelas bernama mobil.

    class Mobil:
        pass

    Pada contoh di atas, kita membuat kelas bernama Mobil. Namun, kelas ini atribut dan method-nya belum didefinisikan sehingga kita masukkan pernyataan "pass" supaya tidak menghasilkan error. Ingat bahwa class merupakan blok kode sehingga Anda perlu memperhatikan indentasi untuk membuatnya.

    Selanjutnya, mari isi kelas tersebut dengan sebuah atribut. Ingat bahwa atribut adalah variabel yang menjadi identitas dari objek atau kelas.
    class Mobil:
        # Atribute
        warna = "Merah"

    Pada contoh di atas, kita memberikan variabel warna untuk menjadi atribut atau identitas bawaan dari kelas Mobil. Jika Anda jalankan kode tersebut, tidak akan ada output yang keluar. Hal ini karena kita belum memanggil kelas tersebut dan mendefinisikan kembalian nilai (return).
'''

# Contoh penerapan class dalam python
print("~ 1. Class\n> Contoh Penerapan Class\n")
print("""Saya akan menggunakan fungsi print() untuk menampilkan contohnya karena class ini tidak di panggil
> Contoh kode program class

Def Mobil:
    # Atribute
    warna = "Merah"
""")


# ============================================================================= Object(Objek) ==================================================================
'''
                                                                                Object (Objek)

Untuk memanggil kelas yang telah dibuat, kita membuat sebuah objek. Berdasarkan KBBI dari kemendikbud, objek merupakan benda, hal, dan sebagainya yang dijadikan sasaran untuk diteliti, diperhatikan, dan sebagainya. Keterkaitan antara objek dan class sangat erat. Contohnya, jika Anda membuat kelas bernama manusia, objeknya adalah manusia dengan nama yang berbeda.

Anda bisa umpamakan kelas adalah bentuk abstrak dari objek, layaknya cetakan atau blueprint. Saat kelas diwujudkan menjadi bentuk yang lebih nyata, proses ini disebut sebagai instansiasi. Itulah sebabnya objek disebut juga sebagai instance atau instance of the class.

Pada contoh sebelumnya, kita telah membuat class. Untuk memanggilnya, kita harus mengubahnya menjadi bentuk yang lebih nyata atau bisa dikatakan objek dari kelas tersebut perlu dibuat. 

    class Mobil:
        # Atribute
        warna = "Merah

    mobil_satu = Mobil

    Pada contoh di atas, kita memanggil sebuah class dengan menyebutkan namanya diikuti oleh tanda kurung buka dan tutup "()", mirip seperti memanggil fungsi. Selanjutnya pada baris kode "mobil_satu = Mobil()", kita membuat sebuah objek dari kelas Mobil dan menyimpannya dalam variabel mobil_satu.

    Tidak seperti fungsi, variabel dalam contoh di atas adalah objek yang merupakan perwujudan dari kelas yang telah kita buat. Ini berarti variabel tersebut sekarang memiliki atribut yang identik dengan kelas tersebut.
'''

# Contoh Object(Objek) 
print("~ 2. Object\n> Contoh Penerapan Object\n")
class sapaan():
    # Atribute
    sapa = "What`s Up gengs apakah kamu sudah makan hari ini"
sapaanSatu = sapaan()
print(sapaanSatu.sapa, "\n")

'''
    Output :

    What`s Up gengs apakah kamu sudah makan hari ini

    Pada contoh di atas, kita memanggil atribut objek yang berasal dari kelas Sapa, yaitu "What`s Up gengs apakah kamu sudah makan hari ini". Untuk memanggil atribut, kita dapat menyebutkan objek atau instance diikuti dengan nama atributnya. 

        print(sapaanSatu.sapa)
        
        sapaanSatu = Nama Object
        sapa       = Nama Atribute

    Dengan membuat objek yang merupakan instance dari kelas, kita pun dapat mengubah atribut tersebut sesuai kebutuhan. Contohnya berikut.
''' 
# Mengenal sifat intace pada Object(Objek)
print("> Mengenal sifat Instace pada Object karena object bisa mengganti atribute dari class\n")
class sapaan():
    # Atribute
    sapa = "What`s Up gengs apakah kamu sudah makan hari ini"

sapaanSatu = sapaan()
sapaanSatu.sapa = "Hello Selamat Datang ganteng ganteng nya akuhhhh"
print(sapaanSatu.sapa, "\n")

'''
    Output :
    Hello Selamat Datang ganteng ganteng nya akuhhh

    Pada contoh di atas, kita mengubah atribut kelas yang awalnya bernilai merah menjadi biru dengan mendeklarasikan ulang nilainya. Perhatikan kode "sapaanSatu= 'Hello Selamat Datang ganteng ganteng nya akuhhh'", itu merupakan kode yang digunakan untuk mengubah nilai atribut kelas.
'''

# ============================================================================= Atribute ==================================================================
'''
                                                                                Atribute 

Dalam Python, ada dua jenis atribut kelas yang dapat dibagi, yaitu atribut kelas dan atribut objek atau instance. Atribut kelas adalah jenis atribut yang secara otomatis terdefinisi dan menjadi bawaan kelas ketika instance dibuat berdasarkan kelas tersebut. Anda dapat menganggapnya sebagai nilai default atau bawaan dari kelas. Jika Anda membuat beberapa objek berdasarkan kelas yang memiliki jenis atribut ini, setiap objek akan memiliki atribut yang sama dengan nilai yang sama. 

Namun, perlu diperhatikan bahwa jenis atribut kelas memiliki kelemahan, yaitu ketika nilai atribut kelas diubah, perubahan tersebut akan memengaruhi semua objek yang dibuat berdasarkan kelas tersebut.

Perhatikan contoh berikut. Asumsikan bahwa kita membuat sebuah kelas bernama "Mobil" dengan atribut "warna". Lalu, dari kelas tersebut kita akan membuat dua objek atau instance.
'''


# Contoh untuk kelemahan di Atribute
print("~ 3. Atribute\n> Contoh Kelemahan Dari Atribute\n")

# Contoh nya 
class Mobil:
    # Atribut kelas
    warna = "Merah"

mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

# Mengubah atribut kelas
Mobil.warna = "Hitam"

print(mobil1.warna)
print(mobil2.warna, "\n")

"""
    Output:
    Merah
    Merah
    Hitam
    Hitam

    Pada contoh di atas, kita membuat kelas bernama "Mobil" dengan atribut "warna" diisi dengan nilai "Merah". Selanjutnya, pada kode di bawah ini kita buat dua instance baru yang diambil dari kelas mobil tersebut. Instance pertama adalah "mobil1" dan instance kedua adalah "mobil2".

        mobil1 = Mobil()
        print(mobil1.warna)

        mobil2 = Mobil()
        print(mobil2.warna)

    Tahap selanjutnya, pada kode di bawah ini kita ubah atribut kelas Mobil. Dengan kode tersebut, kini nilai atribut warna pada kelas mobil telah berubah. 

        Mobil.warna = "Hitam"

    Apa yang terjadi dengan objeknya? Kita cetak atribut mobil1 dan mobil2 dengan menggunakan print(). Hasilnya seperti yang Anda lihat sebelumnya bahwa kini kedua atribut pada masing-masing objek ikut mengalami perubahan yang awalnya "Merah" menjadi "Hitam".

    Kelemahan ini akan menjadi masalah jika kita ingin setiap objek memiliki atribut masing-masing yang menjadi ciri khasnya. Sama seperti manusia yang bisa beragam dan mempunyai ciri khas walau dalam satu "blueprint" yang sama.

    Jenis atribut yang kedua adalah atribut objek atau atribut instance. Jenis atribut ini memungkinkan setiap instance dari kelas memiliki atribut yang berbeda-beda sesuai dengan keinginan. 

    Namun, untuk membuat atribut instance kita perlu menggunakan class constructor.
"""

# ============================================================================= Class Constructor ==================================================================
'''
Pembangun kelas atau class constructor adalah sebuah fungsi khusus dalam Python yang digunakan untuk menentukan nilai awal atau kondisi awal dari suatu kelas. Dengan fungsi ini, saat kita melakukan proses instansiasi atau pembuatan objek baru, hal pertama yang dilakukan adalah memanggilnya terlebih dahulu.

    class Mobil:
        def __init__(self):
            self.warna = "Merah"
        
    Pada contoh di atas, kita membuat fungsi bernama "__init__" sebagai fungsi khusus untuk menjadi constructor. Selanjutnya, kita menggunakan parameter self, yakni sebuah kata kunci untuk merujuk pada objek yang sedang diproses saat ini.

    Ini artinya ketika Anda membuat instance baru bernama "mobil_1", constructor akan dipanggil pertama kali dan self akan merujuk pada instance atau objek "mobil_1" tersebut. Begitu pun kalau kita membuat instance baru lainnya bernama "mobil_2", constructor akan dipanggil pertama kali dan self akan merujuk pada instance "mobil_2". 

    Hal ini memungkinkan setiap objek baru tersebut memiliki atribut masing-masing, tidak lagi atribut kelas. Jadi, kita dapat mengubah atribut suatu objek tanpa memengaruhi objek lainnya. 

    Dengan begitu, self.warna yang didefinisikan dalam constructor adalah jenis dari atribut instance atau atribut objek, yakni atribut yang terkait dengan instance atau objek itu sendiri, bukan kelas. 

    Mari kita kembali pada contoh kelas mobil dengan atribut warna. Kali ini kita akan mengubah nilai atribut kembali, tetapi perbedaannya adalah atribut tersebut bukan jenis atribut kelas melainkan atribut instance.
'''

# Contoh Penerapan SuperPower Class Constructor
print("~ 4. Class Constructor\n> Penerapannya Sebagi Di Bawah:\n")

class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'
        
mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna, "\n")

'''
    Output:

    Merah
    Merah
    Hitam
    Merah

    Pada contoh di atas, kita membuat kelas bernama Mobil dengan atribut instance adalah warna dan nilainya merah. Selanjutnya, kita membuat dua instance baru bernama "mobil_1" dan "mobil_2". Jika kita cetak atribut kedua objek tersebut ke layar, hasilnya adalah "Merah" untuk kedua atribut tersebut.

    Selanjutnya kita ubah atribut instance pada instance "mobil_1" dengan sintaks mobil_1.warna = "Hitam". Sintaks ini mengganti atribut objek tersebut dari awalnya merah menjadi hitam.

    Untuk mengetahui perbedaannya, kita cetak kembali kedua instance tersebut menggunakan fungsi "print()". Hasilnya atribut instance mobil_1 berubah menjadi hitam, sedangkan instance mobil_2 tetap merah. 

    Jika terlintas dalam benak Anda, mengapa sintaksnya mobil_1.warna = "Hitam" bukan Mobil.warna = "Hitam"? Jawabannya dapat dilihat jika Anda mengubah kode di atas dengan kode tersebut. Silakan untuk melakukan copy-paste terhadap sintaks yang dimaksud. 

    Output yang dihasilkan adalah program menampilkan "Merah" semuanya. Artinya atribut pada setiap objeknya tidak terjadi perubahan. Hal ini karena pada kelas yang kita buat tidak memiliki atribut kelas, sedangkan sintaks Mobil.warna = "Hitam" bertujuan untuk mengubah jenis atribut kelas. 

    Jika sebelumnya kita hanya menggunakan parameter self saja dalam class constructor, parameter lain pun dapat ditambahkan sesuai kebutuhan.
'''
# Contoh parameter self dan parameter lain bisa kita tambahkan
print("> Contoh Parameter self bisa kita tambahkan parameter yang lain nya juga\n")

# Contoh Penerapan
class Sapa():
    def __init__(self, nama, umur, mimpi):
        self.nama = "Holla! " + nama
        self.umur = umur + " Tahun"
        self.mimpi = mimpi

# Pemanggilan Kelas Sapa()
sapaSatu = Sapa("Satria Dirgantara Nuryaman", "22", "Menjadi Machine Learning Engginer Dan Blockchain Developer!")

# Ouput
print(sapaSatu.nama)
print(sapaSatu.umur)
print(sapaSatu.mimpi)

'''
    Output:

    Holla! Satria Dirgantara Nuryaman
    22 Tahun
    Menjadi Machine Learning Engginer Dan Blockchain Developer!

    Pada contoh di atas, kita membuat kelas yang berbeda dengan class Sapa(), tetapi ada perbedaan dengan yang sebelumnya. Perbedaannya adalah pada kode di atas, kita membuat parameter tambahan, yaitu "nama, umur, mimpi". Parameter tambahan ini membuat kita perlu menggunakan argumen ketika memanggil kelas mobil "sapaSatu('Satria Dirgantara Nuryaman', '22', Menjadi Machine Learning Engginer dan Blockchain Developer!)". Jika Anda memanggil kelas tanpa argumen yang disebutkan, program akan menyebabkan error.

    Hal penting yang perlu diketahui adalah perbedaan antara kode di atas dengan kode sebelumnya. Sebelumnya, kode hanya menggunakan parameter "self". Lalu, jika kita menggunakan kode seperti berikut.

        class Mobil():
            def __init__(self):
                self.warna = 'Merah'
        
        Kode di atas berarti kita langsung menentukan nilai default terhadap suatu objek. Itulah sebabnya ketika proses instansiasi, program tidak memunculkan error walaupun kita tidak memberikan argumen apa pun.

    Lain halnya pada kode di bawah ini.

        class Mobil();
            def __init__(self, warna, merek, kecepatan):
                self.warna = warna
                self.merek = merek
                self. kecepatan = kecepatan
            
        Semua atribut yang telah ditetapkan tidak memiliki nilai default. Ketika membuat sebuah objek dari kelas tersebut, kita perlu menambahkan argumen tambahan seperti yang disebutkan, yaitu warna, merek, kecepatan. Inilah sebabnya ketika proses instansiasi atau pembuatan objek, program akan memunculkan error jika tidak memberikan argumen apa pun.


                            METHODE NYA KITA PISAHKAN DI FILE YANG LAIN YA AGAR TIDAK TERLALU BANYAK
'''

