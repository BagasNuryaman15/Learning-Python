from re import I
from sre_compile import JUMP


print("\n")
print(" Function (Fungsi) ".center(150, "="), "\n")
'''
                                                            Konsep Function

    1.  Konsep Function Dalam Matematika
        Fungsi dalam pemrograman sebenarnya didasari oleh konsep pemetaan (asosiasi) dan fungsi dalam matematika. Fungsi pada matematika merupakan pemetaan antara dua himpunan nilai, yaitu domain dan range. Kita bisa bayangkan fungsi sebagai sebuah mesin yang memiliki input (domain) dan output (range). Output tersebut pasti terkait dengan input bagaimana pun kondisinya.

        Notasi atau bentuk rumus fungsi dalam matematika beragam. Salah satu yang umum dijumpai adalah notasi berikut.

        f(x) = 2x

        1. f adalah nama fungsi
        2. (x) adalah Input                         Kami menyebutnya f dari x sama dengan 2 kali x
        3. 2x adalah apa yang harus dikeluarkan (Output)

        Mari kita lihat salah satu soal fungsi sederhana dalam matematika. Asumsikan bahwa kita memiliki sebuah fungsi untuk mengalikan bilangan bulat dengan nilai 2. Jadi, berikut perhitungannya.

        Input(Domain)                                   f(x) = 2x                                           Output(Range)
        0                                               2x0                                                 0
        4                                               2x4                                                 8
        16                                              2x16                                                32

        Perhatikan pada gambar tersebut. Sebab fungsi kita bertujuan untuk mengalikan bilangan bulat dengan nilai 2, setiap elemen yang berada pada himpunan domain akan dikalikan dua dan hasilnya ditampung pada himpunan range. 

        Notasi f(x)=2x menunjukkan bahwa fungsi "f" mengambil "x" dan mengalikannya dengan 2.
            f(x) = 2x 
            f(4) = 2.4 = 8
            f(10) = 2.10 = 20
        
        Sampai sini, kita sudah memahami secara mendasar mengenai fungsi dalam matematika. Ingat bahwa fungsi "f(x)=2x" yang kita deklarasikan akan mengalikan bilangan bulat dengan 2, berapa pun bilangannya. Mari kita lanjutkan mengenai fungsi dalam pemrograman.
    

    2.  Function dalam Pemrograman
        Fungsi dalam pemrograman didasari oleh fungsi dalam matematika. Jadi, baik fungsi pemrograman maupun fungsi matematika memiliki tujuan yang sama, yaitu mengubah suatu bentuk menjadi bentuk lain dengan aturan yang sama. 

        Mari analogikan kembali dengan konsep lain, kita bisa umpamakan fungsi dalam pemrograman seperti merakit isi black box.

            Keadaan Awal ----> Fungsi ----> Keadaan Akhir

        Analogikan Fungsi adalah kotak hitam ya. Selayaknya black box, kita tidak perlu tahu tentang hal yang terjadi dalam kotak (fungsi) tersebut. Kita hanya perlu fokus pada keadaan awal yang merupakan himpunan nilai yang terdefinisi sebagai input (domain) dan keadaan akhir yang merupakan himpunan nilai yang terdefinisi sebagai output (range).

        Mari ambil contoh salah satu fungsi yang sedari materi awal sudah kita kenal, yakni fungsi "print()". Fungsi ini bertujuan untuk menampilkan teks ke layar tanpa kita perlu ketahui hal yang terjadi di dalamnya. Hal yang perlu kita lakukan adalah memasukkan teks yang diinginkan ke fungsi "print()".

            print("Hello World")

            Output : 
            Hello World

        Contohnya pada gambar di atas, kita hanya perlu memasukkan teks "Hello World" tanpa tahu proses fungsi di dalamnya. Fungsi tersebut akan menghasilkan output dengan memunculkan teks "Hello World" ke layar. 

        Jadi, kalau kita definisikan, fungsi dalam pemrograman adalah blok kode yang dapat digunakan kembali untuk mengeksekusi fungsionalitas tertentu saat dipanggil. Dalam Python, fungsi terbagi menjadi dua jenis.

            1.  Built-in Functions
                Built-in functions atau dalam bahasa Indonesia berarti fungsi bawaan adalah kumpulan fungsi yang sudah terintegrasi dengan bahasa pemrograman Python sehingga tidak perlu mengimpor modul atau library tambahan. Fungsi bawaan ini menyediakan fungsi-fungsi inti dan dasar dari bahasa Python. Contoh dari fungsi bawaan adalah print(), len(), type(), range(), dan sebagainya.

            2.  User-defined Functions
                User-defined functions atau dalam bahasa Indonesia berarti fungsi yang didefinisikan pengguna adalah jenis fungsi yang kita definisikan sendiri untuk melakukan tugas spesifik tertentu. Contoh dari user-defined functions adalah fungsi yang telah kita buat di awal materi ini tentang mencari luas persegi panjang. Tetapi mari bahas function baru.
'''

# Contoh User-defined Functions
print("> Contoh Penerapan User-defined Functions", "\n")

def faktorial(n):
  """Fungsi menghitung faktorial dari bilangan n"""
  faktorial = 1
  for i in range(1, n+1):
    faktorial *= i
  return faktorial

output = faktorial(6)
print(f"Hasil dari Faktorial 6 adalah =", output, "\n")  


'''
    Output: 
    720

    Kita akan bahas lebih detail tentang fungsi ini nanti. Saat ini Anda cukup mengetahui bahwa kode di atas berperan layaknya black box. Kita perlu memasukkan angka yang merupakan faktorial yang ingin di ketahui untuk dimasukkan ke fungsi dan akhirnya menerima output nilai faktorial.

    Jika ingin menggunakan fungsi lain di luar dari built-in functions, Anda bisa mengimpor sebuah library. Library adalah koleksi dari banyaknya modul yang saling terkait dan dapat digunakan berulang kali. Modul adalah file berisi kode Python berupa fungsi, kelas, dan sebagainya. 

    Library dalam Python terdiri dari dua jenis.

    1.  Python Standard Library
        Python Standard Library adalah jenis library yang telah terpasang secara otomatis ketika Anda melakukan instalasi Python. Python Standard Library berisi kumpulan modul dan paket yang disertakan secara default oleh Python. Paket (package) merupakan sebuah direktori berisi satu atau lebih modul yang terkait dan saling berhubungan.

        Anda tidak perlu melakukan instalasi untuk menggunakan Python Standard Library. Contoh Python Standard Library adalah "os", "datetime", "re", dan sebagainya. Anda bisa melihat banyaknya jenis library ini pada laman website berikut.

    2.  External Library
        Jika sebelumnya impor library tidak perlu dilakukan untuk Python Standard, berbeda halnya dengan external library yang mengharuskan Anda mengimpor library untuk bisa menggunakannya. External Library adalah jenis library yang dikembangkan oleh individu atau organisasi di luar tim inti pengembang Python.

        Sederhananya, di luar sana banyak developer yang turut membuat kode untuk diri mereka sendiri dan pada akhirnya disebarluaskan untuk digunakan oleh developer lainnya. Contoh dari external library adalah TensorFlow yang merupakan library populer untuk menyelesaikan permasalahan pemelajaran mesin (machine learning). 
'''    

# Mari kita sederhanakan semua penjelasan dengan tabel berikut.
'''
Nama        Fungsi                                                                                                          Contoh
Fungsi      Blok kode yang dapat digunakan kembali untuk mengeksekusi fungsionalitas tertentu saat dipanggil.               print(), len(), faktorial()

Built-in    Kumpulan fungsi yang sudah terintegrasi dengan bahasa pemrograman Python sehingga tidak perlu mengimpor modul   print(), len(), range()
Functions   atau Library Tambahan.

Userdefined Jenis fungsi yang kita definisikan sendiri untuk melakukan tugas spesifik tertentu.                             faktorial() persegi_panjang()
function

Modul       File berisi kode Python berupa fungsi, kelas, dan sebagainya.                                                   Math, dan semua file yang kita 
                                                                                                                            buat sendiri dengan ekstensi ".py" (main.py, var.py, dan lain sebagainya)

Package     Sebuah direktori berisi satu atau lebih modul yang terkait dan saling berhubungan.                              NumPy, Pandas

Library     Koleksi dari banyaknya modul dan paket yang saling terkait dan dapat digunakan berulang kali.                   Matplotlib, TensorFlow, Beautiful 
                                                                                                                            Soup
Kerap kali kita salah mengartikan library, package, dan modul. Ketiga hal tersebut sebenarnya saling berkaitan. Misalnya, terkadang ketika menyebut NumPy sebagai library, sebenarnya itu sah-sah saja karena library berisi package dan juga modul.
'''

# ========================================================= Keguanaan Functions ============================================
print(" Keguanan Functions ".center(70, "-"), "\n")
'''
                                                            Kegunaan Fungsi

Mengapa kita harus menggunakan fungsi dalam pemrograman? Sebenarnya terdapat banyak sekali kegunaan fungsi yang dapat menyelesaikan masalah pada pemrograman. Beberapa kegunaannya sebagai berikut.

    1.  Program dapat dipecah menjadi bagian yang lebih kecil (sub).

            Main Program            
            ......                              fungsi1()
            fungsi1() --------------------------->   ....
            ......
            fungsi2() ----------------------------------------> fungsi2()
                                                                .... 

    Ketika membuat kode program yang kompleks, Anda bisa membagi setiap programnya menjadi bagian-bagian kecil dengan mendefinisikan fungsi, dan di dalamnya setiap fungsi dapat dipanggil sebagai satu baris atau ekspresi dalam program utama.

    2.  Penggunaan ulang kode alih-alih menulis ulang kode.

            Main Program
            ......
            fungsi1()                                fungsi1()
            fungsi1()       -----------------------> .......
            fungsi1()                                .......
            ......

        Ketika Anda merasa perlu membuat kode yang berulang-ulang, pemrograman akan menjadi lebih efisien jika kode tersebut diorganisasikan sebagai sebuah fungsi. Contohnya fungsi untuk mencari luas persegi panjang akan sangat berguna dalam berbagai jenis persoalan dengan nilai panjang dan lebar yang berbeda.

    3.  Setiap fungsi bersifat independen dan dapat diuji secara terpisah.

        def penjumlahan(a, b):
            result = a + b
            return  result

        penjumlahan(2, 3)
        5
        penjumlahan(10, 20)
        30

    Setiap fungsi bersifat independen, artinya Anda dapat menguji setiap fungsi tersebut dalam interpreter (mode interaktif Python) tanpa perlu membuat program utuh terlebih dahulu. Ketika bekerja dalam program yang lebih kompleks dan melibatkan banyak programmer, hal ini juga mempermudah pembagian tugas masing-masing.
'''

# ========================================================= Mendefinisasikan Functions ============================================
'''
                                                        Mendefinisikan Fungsi dalam Python
Baiklah, Anda sudah memahami secara mendasar tentang fungsi dan kegunaannya. Mari kita mulai membuat fungsi sendiri (user-defined functions). 

Secara umum, fungsi terdiri dari header, body, dan return, seperti gambar berikut.

    def perkalian(a, b):
        result = a * b
        return result

    Dengan catatan sebagai berikut.

    1.  Function header (def perkalian(a, b):) memberi tahu Python bahwa kita mulai mendefinisikan suatu fungsi.

    2.  Function body (result = a * b) adalah blok kode yang diindentasi setelah header fungsi menentukan hal yang dilakukan fungsi tersebut. Kita menentukan semua kode yang akan dibuat dalam function body. Ingat bahwa bagian ini adalah blok kode sehingga Anda harus memperhatikan indentasi untuk menghindari kesalahan.

    3.  Function (return) adalah pernyataan yang digunakan dalam fungsi untuk mengembalikan nilai atau hasil eksekusi dari fungsi tersebut. Ketika sebuah fungsi dieksekusi, biasanya ada situasi bahwa kita ingin mendapatkan nilai atau hasil dari proses yang dilakukan oleh fungsi tersebut. Untuk itu, kita menggunakan pernyataan 'return' dalam fungsi untuk mengembalikan nilai kepada pemanggil fungsi.

Membuat Fungsi
Mari kita gunakan kembali fungsi yang sempat disebut di awal.
'''

# Contoh Mmebuat Fungsi

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

'''
Ingat bahwa permasalahan yang ingin diselesaikan adalah kita tidak ingin mengulang untuk menulis rumus perkalian. Jadi, kita menggunakan fungsi untuk membungkus rumus tersebut. Perhatikan gambar di bawah ini untuk lebih menjelaskan setiap elemen fungsi.

   def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

    Fungsi yang kita buat sebelumnya terdiri dari beberapa elemen, yakni berikut.

Fungsi yang kita buat sebelumnya terdiri dari beberapa elemen, yakni berikut.

    1. def digunakan sebagai pernyataan bahwa kita membuat fungsi.
    2. "mencari_luas_persegi_panjang" merupakan nama fungsi yang kita tentukan. 
    3. Setiap fungsi memiliki parameter bertujuan untuk menyimpan nilai yang akan digunakan oleh fungsi dalam proses eksekusinya. Dalam contoh mencari luas persegi panjang, parameter "panjang, lebar" akan menyimpan setiap input yang masuk, seperti jika Anda memasukkan panjang 5cm dan lebar 10cm.

    4. Setiap definisi fungsi harus diakhiri dengan colon atau titik dua ":" untuk menandakan awal blok kode fungsi.
    5. Setelah function header selesai, selanjutnya kita definisikan function body yang berisi kode untuk dieksekusi. Dalam contoh mencari luas persegi panjang, kita memasukkan rumus luas persegi di bagian ini. Hasil dari rumus tersebut disimpan dalam variabel "luas_persegi_panjang". 

    6. Terakhir, kita menggunakan return keyword yang merupakan bagian dari return statement. Return statement bertujuan untuk mengembalikan nilai atau hasil eksekusi fungsi tersebut. Dalam contoh di atas, kita mengembalikan variabel "luas_persegi_panjang" sebagai hasil dari proses eksekusi fungsi.
'''

# ========================================================= Memanggil Functions ============================================
'''
                                                            Memanggil Fungsi    

Sekarang, bagaimana cara memanggil fungsi tersebut? Pada dasarnya, kita bisa memanggil fungsi dengan cara menuliskan nama fungsi seperti kita menggunakan "print()", "len()", dan sebagainya.

    def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

mencari_luas_persegi_panjang(10,5)  # memanggil fungsi mencari_luas_persegi_panjang dengan parameter panjang=10 dan lebar=5

Namun, layar tidak menampilkan hasil eksekusi dari fungsi karena kita tidak menampilkannya ke layar atau menggunakan "print()". Maka dari itu, umumnya programmer akan menggunakan variabel untuk menyimpan hasil dari eksekusi fungsi.
'''
# Contoh penerapan memanggil fungsi
print("Contoh Penerapan Memanggil Functions", "\n")

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(20, 3)
print(f"Ini adalah hasil dari rumus luas persegi panjang = {persegi_panjang_pertama}")

'''
    Output:
    60

    Dari kode di atas, secara sekuensial program akan berjalan seperti berikut.

    1. Pertama, kita menggunakan fungsi bernama "mencari_luas_persegi_panjang()" yang memiliki dua parameter, yaitu panjang dan lebar. Fungsi ini menghitung luas persegi panjang dengan mengalikan nilai panjang dan lebar serta mengembalikan hasilnya.

    2. Ketika memanggil fungsi "mencari_luas_persegi_panjang(20, 3)", kita menyimpan hasilnya dalam variabel bernama "persegi_panjang_pertama". Dalam pemanggilan ini, angka 20 dianggap sebagai nilai panjang dan angka 3 dianggap sebagai nilai lebar.

    3. Kemudian, dalam fungsi, nilai panjang dan lebar digunakan untuk menjalankan kode "panjang * lebar". Hasil dari operasi ini disimpan dalam variabel "luas_persegi_panjang".

    5. Selanjutnya, kita mengembalikan nilai luas_persegi_panjang kepada pemanggil fungsi dengan menggunakan pernyataan "return".
    6. Sekarang, nilai yang dikembalikan oleh fungsi tersebut disimpan dalam variabel "persegi_panjang_pertama" sehingga kita dapat mencetaknya ke layar menggunakan fungsi "print(persegi_panjang_pertama)".

Ke depannya, kita bisa menggunakan variabel tersebut berulang-ulang. Secara struktur, pemanggil fungsi terdiri beberapa elemen, yakni berikut.

    persegi_panjang_pertama = mencari_luas_persegi_panjang(20, 3)

    1.  persegi_panjang_pertama merupakan untuk menyimpan nilai yang dikembalikan functions.
    2.  mencari_luas_persegi_panjang merupakan nama fungsi yang akan dipanggil atau inilah pemanggilan fungsi.
    3.  (20, 3) merupakan argumen yang akan dikirim ke fungsi.

    Ketika Anda memanggil sebuah fungsi, ada dua elemen sebagai berikut.

    1. Nama fungsi; tentu Anda harus menyebutkan nama fungsi yang ingin digunakan. Namun ingat, gunakan kurung tutup "()" untuk memanggilnya.
    2. Argumen bisa dikatakan sebagai nilai yang diberikan kepada fungsi. Nantinya, nilai tersebut akan disimpan dalam parameter fungsi. Pada contoh fungsi di atas, argumen 5 dan 10 merepresentasikan parameter panjang dan lebar dalam fungsi "mencari_luas_persegi_panjang()" yang kita buat sebelumnya.
'''


# ========================================================= Docstring ============================================
'''
                                                            Docstring

Terakhir, untuk membuat fungsi lebih mudah dipahami oleh programmer lain, kita bisa membuat dokumentasi berupa docstring. Docstring adalah akronim dari documentation string, bertujuan untuk membuat dokumentasi terhadap fungsi yang dibuat. Umumnya, dokumentasi yang dijelaskan berupa argumen, return, deskripsi fungsi, dan sebagainya.

Mari lihat contoh penerapannya di bawah ini.
'''

# Contoh penerapan docstring
print("Contoh Penerapan Docstring", "\n")
def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

'''
Output:
50
Pada kode di atas, kita mendefinisikan docstring dengan memberikan blok komentar dengan tiga double quote (""") tepat di bawah "def" keyword. Hal ini untuk menegaskan sebelum kode dibaca, kita harus memahami dokumentasi di bawahnya terlebih dahulu.

Dokumentasi di atas memiliki tiga elemen, yakni berikut.

    1. Deskripsi: Teks yang menjelaskan tujuan dari fungsi yang dibuat. Pada contoh di atas, kita mendefinisikan teks "Fungsi ini digunakan untuk menghitung luas persegi panjang" yang artinya fungsi ini ditujukan untuk menghitung luas persegi panjang. 

    2. Argumen: bagian yang menjelaskan argumen yang diterima oleh fungsi. Dalam contoh di atas, argumen yang diterima adalah panjang dan lebar dengan keduanya termasuk bilangan bulat atau bertipe data integer. 

    3. Return: Bagian ini menjelaskan nilai yang akan dikembalikan oleh fungsi. Dalam contoh di atas, fungsi akan mengembalikan nilai luas persegi panjang hasil perhitungan yang termasuk bilangan bulat atau bertipe data integer.
'''








    
