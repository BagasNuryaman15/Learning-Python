print("\n")
print(" Method ".center(150, "="), "\n")
'''
                                                                                    Method

Setelah atribut, saatnya membahas method sebagai perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Pada pembuatan metode , sebenarnya kita membuat fungsi di dalam kelas itu sendiri. Dengan kata lain, kita menggunakan kata kunci "def" atau membuat fungsi sebagai suatu metode. Python membagi method menjadi tiga jenis.

    1.  Metode dari object (object method).
    2.  Metode secara statis (static method).
    3.  Metode dari class (class method).

  Dua metode terakhir sangat erat kaitannya dengan konsep dekorator. Kita tidak akan membahasnya lebih detail mengenai dekorator, tetapi secara umum saja.  Dekorator adalah fungsi dalam Python yang mengembalikan fungsi lain, biasanya diawali dengan sintaks "@" di awal. Contoh sederhana dekorator sebagai berikut.
'''

# Contoh sintaks sederhana dekorator sebagai berikut.
print("> Contoh sederhana Dekorator\n")

def my_decorator(func):
    def wrapper():
        print("Sebelum Fungsi Di Eksekusi!.")
        func()
        print("Tara Setelah Fungsi Di Eksekusi!.\n")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator # Kita memakai @ untuk memanggil decorator
def say_hello():
    print("Hello Selamat Datang di Pembelajaran Python With Dicoding Well!!!")

# Memanggil Fungsi yang sudah di dekorasi
say_hello()

'''
    Ouput :

    Sebelum Fungsi Di Eksekusi!.
    Hello Selamat Datang di Pembelajaran Python With Dicoding Well!!!
    Tara Setelah Fungsi Di Eksekusi!.

    Penjelasan dari contoh di atas adalah berikut.

    1. Pertama, kita mendefinisikan sebuah fungsi bernama my_decorator. Dekorator ini menerima sebuah fungsi func sebagai parameternya.
    2. Dalam fungsi my_decorator, kita mendefinisikan fungsi wrapper(). Fungsi wrapper() bertindak sebagai "pembungkus" yang menambahkan perilaku sebelum dan setelah eksekusi dari fungsi func.
    3. Setelah itu, fungsi  my_decorator mengembalikan (return) fungsi wrapper sebagai hasilnya. Return ini juga menyebabkan fungsi wrapper dijalankan.
    4. Kemudian, kita mendefinisikan fungsi say_hello(). Fungsi ini akan menjadi target dekorasi.
    5. Untuk mendekorasi say_hello(), kita menggunakan simbol "@" diikuti dengan nama dekorator, yaitu @my_decorator sebelum mendefinisikan fungsi say_hello.
    6. Jadi, secara alur, ketika fungsi say_hello() dipanggil, sebenarnya yang dieksekusi adalah fungsi wrapper() yang menjadi hasil dari dekorasi. Oleh karena itu, pesan "Sebelum fungsi dieksekusi." dicetak terlebih dahulu, kemudian fungsi say_hello() dieksekusi dan mencetak "Hello Selamat Datang di Pembelajaran Python With Dicoding Well!!!", lalu akhirnya, pesan "Setelah fungsi dieksekusi." dicetak.

    Dekorator sangat berguna untuk menambahkan fungsionalitas tambahan pada suatu fungsi atau metode tanpa harus mengubah kode asli dari fungsi tersebut. Anda bisa membaca lebih dalam mengenai dekorator pada laman ini.
'''


# ==================================================================== 1. Metode dari Objek (Object Method) ============================================
'''
Jenis pertama adalah method yang melekat terhadap objek. Ciri dari jenis metode ini adalah adanya parameter self yang merujuk pada objek saat ini. Perhatikan contoh di bawah ini, asumsikan bahwa kita membuat kelas mobil yang sama seperti sebelumnya. Namun, kita menambahkan metode bernama "tambah_kecepatan" dan setiap metode ini dipanggil maka kecepatan mobil akan bertambah 10.
'''

# Penerapan Metode dari Objek (Object Method)
print("~ 1. Object Methode\nContoh Sintaks dan Penerapannya\n")

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "Ferarri", 365)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

print("Setelah ditambahkan: ")
print(mobil_1.kecepatan)

'''

    Output :

    Sebelum ditambahkan: 
    365
    Setelah ditambahkan: 
    375

    Pada contoh di atas, kita membuat kelas Mobil dan mengimplementasikannya pada objek bernama "mobil_1". Dalam kelas tersebut, kita memiliki constructor ('__init__') yang digunakan untuk menginisialisasi atribut 'warna', 'merek' dan 'kecepatan' pada objek yang dibuat (mobil_1).

    Ketika objek 'mobil_1' dibuat dari kelas Mobil, kita memberikan beberapa argumen yang menjadikannya atribut dari objek tersebut, yakni 'Merah' sebagai warna mobil, 'DicodingCar' sebagai merek, dan 'kecepatan' sebagai kecepatan awal mobil tersebut.

    Dalam kelas Mobil yang dibuat, kita menambahkan method berupa fungsi "tambah_kecepatan" dan digunakan untuk meningkatkan kecepatan mobil. Setiap metode ini dipanggil, kecepatan mobil akan bertambah sebesar 10.

    Pada bagian kode berikut lebih tepatnya, kita memanggil metode yang telah dibuat tersebut.

        print("\nSebelum ditambahkan: ")
        print(mobil_1.kecepatan)

        mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

        print("\nSetelah ditambahkan: ")
        print(mobil_1.kecepatan)

    Hasilnya bisa kita lihat pada output dalam program tersebut, bahwa sebelum ditambahkan, kecepatannya adalah 365. Namun setelah itu, kecepatannya bertambah menjadi 375.

    Jika menyadarinya, perbedaan ketika Anda memanggil method dan atribut terletak pada penempatan tanda kurung “()”. Ketika memanggil atribut, Anda cukup menyebutkan nama atribut tersebut tanpa ada tanda kurung “()”, contohnya “mobil_1.kecepatan”. Namun untuk memanggil method, Anda harus menempatkan tanda kurung “()” setelahnya, contohnya “mobil_1.tambah_kecepatan()”.

    Selain itu, saat kode di bawah ini dieksekusi,

        mobil_1.tambah_kecepatan()

    ia setara dengan kita melakukan kode berikut.

        Mobil.tambah_kecepatan(mobil_1)

    Hal inilah yang dimaksud dengan self pada object method karena ketika kita memanggil object method, argumen pertamanya adalah objek dia sendiri (self).

    Namun, object method adalah metode yang melekat terhadap suatu objek dan menggunakan parameter self. Jadi, kita tidak bisa memanggil metode ini langsung melalui kelasnya.

        class Mobil:
            def __init__(self, warna, merek, kecepatan):
                self.warna = warna
                self.merek = merek
                self.kecepatan = kecepatan
    
            def tambah_kecepatan(self):
                self.kecepatan += 10
        
        Mobil.tambah_kecepatan()

        Output:
        Traceback (most recent call last):
            File "/home/glot/main.py", line 10, in <module>
              Mobil.tambah_kecepatan()
        TypeError: tambah_kecepatan() missing 1 required positional argument: 'self'

    Pada contoh di atas, kita perlu membuat kelas yang sama seperti sebelumnya. Namun kali ini, kita memanggil object method melalui kelasnya secara langsung. Hal ini menyebabkan error karena kita mendefinisikan fungsi tambah_kecepatan sebagai object method. Artinya, metode ini memerlukan parameter self dan merujuk pada objek yang dibuat, sedangkan kita memanggilnya melalui kelas tanpa membuat objek.

    Jika ingin membuat metode yang tidak melekat pada objek, kita bisa menggunakan class method atau static method.  
'''


# ==================================================================== 2. Metode secara Statis (Static Method) ============================================
'''
Static method adalah fungsi atau method pada sebuah kelas yang bersifat statis. Artinya, metode atau fungsi ini bersifat independen dan tidak terikat pada instance kelas. Metode ini dapat dianggap seperti kita membuat fungsi seperti biasa, tetapi didefinisikan dalam kelas sehingga ini menjadi perilaku untuk kelas tersebut. Untuk membuat static method, Anda bisa menambahkan dekorator @staticmethod tepat sebelum mendefinisikan fungsi atau metode.
'''

# Penerapan Metode secara Statis (Static Method) 
print("~ 1. Static Method\nContoh Sintaks dan Penerapannya\n")

# Contoh
class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

"""
Output:
Ini adalah metode dari kelas Mobil
Ini adalah metode dari kelas Mobil

Pada contoh di atas, kita membuat sebuah fungsi bernama intro_mobil() yang menjadi metode atau perilaku dari kelas Mobil dengan diawali oleh dekorator @staticmethod. Fungsi atau metode yang kita buat bernama intro_mobil dan mencetak pesan "ini adalah metode dari kelas Mobil".
"""

# ==================================================================== 2. Metode dari Kelas (Class Method) ============================================
'''
Metode terakhir adalah class method yang termasuk jenis metode cukup spesial dalam Python. Jika object method identik dengan parameter self yang merujuk pada objek, class method juga memerlukan sebuah parameter yang merujuk pada kelas. Mari buat contoh yang sama dengan sebelumnya, tetapi kali ini menggunakan class method.
'''

# Penerapan Metode dari kelas (Class Methho)
print("~ 1. Class Method\nContoh Sintaks dan Penerapannya\n")

# Contoh
class Sapa():
    def __init__(self, sapaan):
        self.sapaan = "Selamat Datang di Python"

    @classmethod
    def intro_sapaan(cls):
        print("Sap gengs! Welcome To Course Learnig Language Python")

Sapa.intro_sapaan()
sapaanUser = Sapa(sapaan= "Bagas")
sapaanUser.intro_sapaan()

'''
    Output  :
    Sap gengs! Welcome To Course Learnig Language Python
    Sap gengs! Welcome To Course Learnig Language Python

    Pada contoh di atas, kita membuat program yang sama, tetapi ada sedikit perbedaan, yakni dekorator @classmethod digunakan. Perhatikan baik-baik pada bagian kode berikut.

        def intro_sapaan(cls):
            print("Sap gengs! Welcome To Course Learnig Language Python")    

    Pada bagian fungsi intro_sapaan, kita menambahkan parameter cls. Ini adalah parameter wajib dalam menggunakan dekorator @classmethod.

        Catatan:
                Penamaan cls merupakan kesepakatan bersama dari programmer Python untuk memudahkan pembacaan kode. Anda dapat mengganti namanya, tidak harus cls.

    Mengapa demikian? Sebab, ketika menggunakan class method, kita akan menambahkan argumen tambahan pada posisi pertama berupa kelas itu sendiri. Perhatikan kode berikut.
'''

print("> Contoh jika Class Methode(cls) cls nya diganti dengan argumen lain\n")
class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(*args):
        print(args)
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

"""
    Output:
    (<class '__main__.Mobil'>,)
    (<class '__main__.Mobil'>,)

    Pada contoh kode di atas, fungsi intro_mobil() menggunakan variadic positional parameter, yakni *args untuk melihat argumen yang diterima oleh fungsi tersebut. Perhatikan lebih baik output-nya, kode di atas menerima sebuah parameter, yakni kelas Mobil walaupun ketika pemanggilan fungsi intro_mobil() kita tidak memberikan argumen apa pun.

        Mobil.intro_mobil()
        mobil_1 = Mobil("DicodingCar")
        mobil_1.intro_mobil()

    Ini membuktikan bahwa ketika Anda menggunakan class method, Python akan secara otomatis menambahkan kelas tersebut sebagai argumen pertama.
"""







