print(" Argumen Dan Parameter ".center(150, "="), "\n")
'''
                                                        Argumen dan Parameter

Ingat bahwa argumen dan parameter adalah hal yang berbeda, sering kali programmer tertukar akan kedua istilah tersebut. Sederhananya, Anda bisa bayangkan parameter seperti black box yang akan menampung nilai dan nilai tersebut adalah argumen.

Contohnya, saat Anda membuat fungsi berikut.

    def kalikali(a, b, c):
        # Function Body

    Ketika Anda membuat fungsi di atas, a, b, c merupakan parameter. Namun pada saat Anda memanggilnya, nilai 1, b=50,  c='Dicoding' menjadi argumen.

    kalikali(1, b=50, c='Dicoding')
'''

# ========================================================= 1. Argumen =================================================
print(" 1. Argumen ".center(150, "-"), "\n")
'''
                                                              Argumen
Argumen adalah nilai yang akan diberikan kepada fungsi. Setidaknya ada dua jenis argumen yang dikenal dalam Python.

    1.  Keyword Argument
        Keyword Argument adalah jenis argumen yang disertai dengan nama parameter (identifier) dan secara eksplisit disebutkan. Ketika nama parameter dalam sebuah argumen secara langsung disebutkan, artinya kita menggunakan keyword argument.

        Kita bisa lihat contoh penerapan nya ada di bawah ini.
'''

# 1. Keyword Argument
print(" 1. Keyword Argument ".center(50, "-"), "\n")
print("> Contoh Penerapan Keyword Argument", "\n")

# Contoh Penerapan nya
def nama(nama_depan, nama_belakang):
    namaSaya = nama_depan + " " + nama_belakang
    return namaSaya

namaSaya1 = nama(nama_depan="Bagas", nama_belakang="Ganteng")
print(f"Maka Ouput yang akan di hasilkan adalah seperti ini: \n{namaSaya1} \n")

'''
    Ouput :
    Bagas Ganteng

Ketika kita memanggil fungsi "nama" dengan menuliskan nama parameter diikuti tanda sama dengan (=) dan nilai yang ingin diberikan, itu disebut keyword argument.

Pada contoh di atas, keyword argument "nama_depan="Bagas"" dan "nama_belakang="Ganteng"" diberikan saat pemanggilan fungsi.

Kelebihan dari jenis argumen ini adalah walaupun kita harus menuliskan lebih banyak kata, urutan parameter fungsi tidak perlu dipikirkan.
'''

# Kelebihan Keyword Argument
print("Kelebihan Keyword Argument\n> Contoh Pembuktian Kelebihan Keyword Argument\n")

def biodata(nama, umur, asal):
    Btambahan = nama + " " + umur + " " + asal
    return Btambahan

biodata1 = biodata(umur="22", nama="Satria", asal="Bandung")
print(f"Maka Ouput yang akan di hasilkan adalah seperti ini: \n{biodata1} \n")

'''
    Ouput :
    Satria 22 Bandung

Pada contoh di atas, kita bisa melihat bahwa parameter "nama", "umur", dan "asal" diberi nama dan nilai yang sesuai. Kita bisa melihat bahwa urutan parameter tidak perlu dipikirkan jika kita menggunakan Keyword.
'''
