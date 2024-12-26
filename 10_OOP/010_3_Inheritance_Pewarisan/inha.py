print("\n")
print(" Inheritance (Pewarisan)".center(150, "="), "\n")
'''
                                                                                Inheritance (Pewarisan)

Sebagaimana ilustrasi awal, kita dapat membuat sebuah kelas baru dengan menggunakan kelas induk yang sudah ada. Konsep ini disebut dengan 'inheritance' atau dalam bahasa Indonesia artinya pewarisan.

    1.  Mekanisme Pewarisan

        Kelas A ------> Fitur Inharitance -------> Kelas B Mewarisi Kelas A

        Untuk melakukan pewarisan, anggap kita memiliki "kelas A" sebagai induk atau kelas dasar. Dari kelas A tersebut kita membuat kelas baru bernama "kelas B" sebagai kelas turunan dari kelas yang didapatkan (kelas A). Ketika kelas B mewarisi kelas A, secara otomatis kelas ini memiliki fitur-fitur yang dimiliki oleh kelas A tersebut, dalam hal ini atribut-atribut dan metode-metode. 

        Sebagaimana halnya pada ilustrasi di sampingnya, Anda mempunyai kelas Mobil sebagai kelas dasar atau induk. Lalu, kita membuat kelas Sport sebagai turunan dari kelas mobil yang sudah ada. Selanjutnya, kita bisa memiliki perilaku dan atribut yang sama dengan kelas sebelumnya. Bahkan kita bisa menambahkan hal baru, seperti perilaku turbo pada kelas mobil sport.

        Hal yang perlu diperhatikan, jika kelas B memiliki nama metode yang sama dengan kelas A, metode tersebut akan menimpa metode yang diwariskan oleh kelas A. 

        Mari lihat contoh pewarisan di bawah ini, asumsikan bahwa kita perlu membuat kelas Mobil sebagai kelas dasar. Dari kelas Mobil ini, kita akan membuat kelas Mobil baru bernama Mobil Sport dengan fitur yang sama seperti kelas dasarnya. Namun, ada tambahan fitur baru pada kelas tersebut, yakni turbo untuk meningkatkan kecepatan mobil hingga 50 km/jam.

    Mari mulai dengan kelas dasar Mobil.
'''

# Contoh penerapan makanisme inharitance atau Pewarisan
print("~ 1. Mekanisme Inharitance(Pewarisan)\n> Contoh penerapannya\n")

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

"""
Output:
160

Pada contoh di atas, kita membuat sebuah kelas bernama Mobil dengan atributnya adalah warna, merek, dan kecepatan. Kelas ini juga memiliki metode, yaitu tambah_kecepatan untuk meningkatkan kecepatan mobil sebesar 10. Anggap bahwa kode ini tidak boleh diubah sama sekali.

Kita akan membuat sebuah kelas baru bernama "MobilSport" yang mewarisi atribut dan metode kelas Mobil dasar. Lalu, kita menambahkan metode baru, yaitu turbo untuk meningkatkan kecepatan sebesar 50.
"""

# Contoh setelah kita gunakan metode inheritance
print("\n> Mari kita gunakan Mekanisme Inheritance(Pewarisan)\n")

# Kita masukan programnya disini
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

"""
Output:
160
160
210

Pada contoh di atas, kita membuat kelas baru bernama MobilSport yang mewarisi kelas sebelumnya, yaitu kelas Mobil. Mari fokus terlebih dahulu pada bagian kode berikut.

    class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

Pada bagian kode tersebut, kita mendefinisikan kelas MobilSport dengan menambahkan parameter tambahan, yaitu kelas Mobil. Dengan demikian, kelas MobilSport akan mewarisi seluruh fitur dari kelas Mobil, seperti atribut warna, merek, kecepatan, dan sebagainya. 

Dalam kelas MobilSport, kita membuat object method baru, yaitu turbo untuk meningkatkan kecepatan mobil. Perhatikan bahwa dalam kelas tersebut, kita tidak perlu mendefinisikan kembali atribut sehingga parameter self akan merujuk pada atribut bawaan, yakni kelas Mobil.

Selanjutnya, pada bagian kode berikut.

    # Kelas Mobil Sport
    mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
    print(mobil_sport_1.kecepatan)
    mobil_sport_1.turbo()
    print(mobil_sport_1.kecepatan)

Pada contoh di atas, kita memanggil kelas baru dan membuat objek bernama "mobil_sport_1". Perhatikan bahwa kita juga perlu menambahkan argumen sesuai atribut yang didefinisikan. 

Perintah "print()" pertama akan mencetak kecepatan mobil_sport_1 saat ini, yaitu 160, dan itu adalah nilai bawaan dari kelas mobil dasar. Lalu, kita memanggil metode baru yang telah dibuat, yaitu "mobil_sport_1.turbo()". Hal ini menyebabkan kita memanggil atribut kecepatan yang bertambah dari 160 menjadi 210 (bertambah 50).

Dengan melakukan pewarisan, Anda dengan mudah bisa menambahkan (extend) kemampuan dari suatu kelas dengan fitur yang dibuat sendiri. 
"""

'''
    2.  Override

        Selanjutnya, seperti yang dijelaskan di awal, ketika kita membuat metode baru di kelas turunan (kelas baru) dengan nama yang sama seperti metode di kelas induk, itu akan menyebabkan metode baru menimpa (override) metode dari kelas induk.
'''

# Contoh Penerapan Override 
print("~ 2. Override\n> Contoh Penerapannya\n")

# Kode Programnya
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 20

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

"""
Output:
160
180

Pada contoh di atas, kita menambahkan metode baru bernama tambah_kecepatan. Metode ini juga ada di kelas mobil dasar. Namun, kita melakukan perbedaan pada metode baru ini berupa penambahan kecepatan yang awalnya sebesar 10 di kelas induk, menjadi sebesar 20 di kelas baru. Hasilnya, dapat kita lihat bahwa kecepatan kini bertambah 20 setiap kita memanggil metode tambah_kecepatan().

Namun, perlu dipahami bahwa menimpa bukan berarti mengubah metode dari kelas induk. Hal ini karena metode dari kelas baru tersebut merupakan hasil dari pewarisan sehingga tidak akan mengubah metode dari kelas induk. Silakan tambahkan kode berikut ke program di atas pada bagian akhir kode (sebelum komentar output).

    # Kelas Mobil Dasar
    mobil_1 = Mobil("Merah", "DicodingCar", 160)
    print(mobil_1.kecepatan)
    mobil_1.tambah_kecepatan()
    print(mobil_1.kecepatan)

Anda akan melihat bahwa ketika kita membuat objek dari kelas dasar, lalu memanggil metode dari kelas dasar tersebut, program tetap menambah kecepatan sebesar 10 walaupun kita sudah melakukan overriding (menimpa) di kelas baru.

Saat Anda menjalankan program, Python akan mencari nama metode dengan nama yang sesuai di kelas baru terlebih dahulu. Jika tidak ada, nama akan dicari di kelas induk.
"""

'''
    3.  Super

        Lantas, bagaimana cara untuk kita ingin menggunakan metode atau atribut dari kelas induk, tetapi tidak ingin menuliskan ulang semua kode? Ini adalah tujuan dari adanya super dalam konsep OOP. Nama super sebenarnya merujuk pada kelas induk yang disebut juga sebagai super class. Kita bisa memanfaatkan konsep ini untuk menghindari kode berulang dan memanfaatkan fungsi yang sudah ada pada kelas induk (super class).

        Mari kita lihat contohnya, kita akan menggunakan program yang sama seperti pada materi overriding. Namun, alih-alih menambah kecepatan, mari kita tambahkan teks baru berupa "Kecepatan Anda meningkat! Hati-Hati!".
'''


# Contoh Penerapan Super
print("~ 2. Super\n> Contoh Penerapannya\n")

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

"""
Output:
Kecepatan Anda meningkat! Hati-hati!
170

Pada contoh di atas, kita membuat kelas MobilSport sebagai kelas turunan dengan metode tambahan, yaitu tambah_kecepatan().

    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

Pada metode ini, kita menggunakan "super()" untuk mengambil metode tambah_kecepatan yang berasal dari super class atau induknya, yaitu kelas Mobil. Dengan begitu, program akan menjalankan metode tersebut dan di bawahnya kita menambahkan teks baru sesuai kebutuhan pada kelas turunan berupa "Kecepatan Anda meningkat! Hati-hati!".
"""