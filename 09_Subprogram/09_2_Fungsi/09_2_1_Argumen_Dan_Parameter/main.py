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

    2. Positional Argument

        Kebalikan dari keyword adalah positional, artinya Anda tidak menyebutkan nama parameter (identifier) secara eksplisit. Ketika memanggil fungsi, Anda hanya harus memasukkan nilai yang ingin diberikan. Namun, Anda harus mengikuti urutan dari parameter fungsi tersebut.

        Di Contohkan sama seperti yang Keyword Argument
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


# 2. Positional Argument
print(" 2. Positional Argument ".center(50, "-"), "\n")
print("> Contoh Penerapan Positional Argument", "\n")

# Contoh Penerapannya 
def rumusSegitiga(alas, tinggi):
    rumus = (alas * tinggi) / 0.5
    return rumus

segitiga1 = rumusSegitiga(5, 3)
print(f"Lihatlah akan menjadi seperti ini:\n= {segitiga1} \n")

'''
    Output:
    30.0

    Pada kode diatas kita mnerapkan functions untuk mencari rumus segitiga, dan lihatlah pemanggilan argumen nya harus tepat dan seurutan jika tidak maka akan terjadi sebuah eror. Coba saja kalian coba sayamah engga berani ah.
'''

# ========================================================= 2. Parameter =================================================
print(" 2. Parameter ".center(50, "-"), "\n")
print("Ada 5 jenis Parameter yang akan dibahas pada materi kali ini\n")
# Parameter 
# Menurut dokumentasi resmi Python, ada 5 jenis parameter yang bisa kita atur.

# 1. Positional-or-Keyword
'''
Jenis ini merupakan parameter default dalam Python. Dengan jenis ini, kita dapat menggunakan positional maupun keyword argument ketika memanggil fungsi.
'''
# Contoh penerapan Positional or Keyword
print("~ 1. Positional-or-Keyword \n> Contoh Penerapan nya!\n")

# Functions Programs
def sapa(nama, sapaan):
    hasil = "Hola King!, "+ nama + "! " + sapaan
    return hasil

print(sapa("Satria", "Kamu kok ganteng sekali ya sampai saya terheran heran!"))
print(sapa(sapaan="Kamu ganteng nan rupawan!", nama="Jajang"), "\n")

'''
    Output:
    Hola King!, Satria! Kamu kok ganteng sekali ya sampai saya terheran heran!
    Hola King!, Jajang! Kamu ganteng nan rupawan!

    Pada contoh di atas, kita membuat fungsi untuk menyapa dengan parameternya adalah “nama” dan “sapaan”. Ketika memanggil fungsi tersebut, kita bisa menggunakan dua jenis argumen, yakni positional dan keyword.
'''


# 2. Positional-Only
'''
Parameter ini hanya dapat dimanfaatkan dengan menggunakan jenis argumen posisi saat pemanggilan fungsi. Parameter ini ditentukan menggunakan sintaks "/".
'''
# Contoh penerapan Positional-only
print("~ 2. Positional-only \n> Contoh Penerapan nya!\n")

# Functions Programs
def perkalian(a, b, /):
    result = a * b
    return result

perkalian1 = perkalian(5, 5)
print(f"Pada Contoh Positions-Only saya membuat Fungsi untuk perkalian 5 * 5:\n= {perkalian1}", "\n")

'''
    Output:
    25

    Pada contoh di atas, kita memanggil fungsi yang telah didefinisikan menggunakan positional argument. Perhatikan juga bahwa kita mendefinisikan parameter fungsi dengan sintaks "/".

    Silahkan kalian buat seperti penerapan pada Keyword a = 5, b = 5 maka akan menyebabkan eror.
'''


# 3. Keyword-Only
'''
Jenis ketiga adalah kebalikan dari yang sebelumnya. Kita harus menggunakan keyword argument untuk memanggil fungsi dengan jenis parameter ini. Ia ditentukan dengan sintaks "*" (asterisk).
'''

# Contoh penerapan keyword-only
print("~ 3. Keyword-Only \n> Contoh Penerapan nya!\n")

# Functions Program
def rumus_persegi_panjang(*, panjang, lebar):
    rumusPP = panjang * lebar
    return rumusPP

contoh1 = rumus_persegi_panjang(lebar=20, panjang=45)
print(f"Pada contoh Keywords-Only saya membuat Fungsi untuk menghitung persegi panjang :\n= {contoh1}", "\n")

'''
    Output :
    900

    Pada contoh di atas, kita menggunakan keyword argument untuk memanggil fungsi yang telah dibuat. Perhatikan bahwa kita menggunakan sintaks "*" untuk mendefinisikan bahwa parameter fungsi ini hanya bisa dipanggil menggunakan keyword argument.

    Coba kalian ubah menjadi position maka akan menjadikan eror program. 
'''

# 4. Var-Positional (Variadic Positional Parameter)
'''
Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan menggunakan sintaks *args. *args memungkinkan sebuah fungsi menerima banyak argumen posisional dalam bentuk tuple. Kamu bisa menggunakannya ketika jumlah argumen yang akan diberikan tidak diketahui sebelumnya.
'''

# Contoh penerapan Var-Positional
print("~ 4. Var-Positional (Variadic Positional Parameter)\n> Contoh Penerapan nya!\n")

# Functions Program
def penambahan(*args):
    print(type(args), "\n")
    total = sum(args)
    return total

contoh_satu = penambahan(1, 2, 3, 4, 5, 6, 10, 20, 50, 200)
print(f"Pada contoh Var-Positional saya membuat sum() untuk lebih efisein karena *args memungkinkan sebuah fungsi menerima banyak argumen posisional dan hasilnya adalah\n={contoh_satu}\n")

'''
    Output :
    <class 'tuple'>
    301

    Pada contoh di atas, parameter *args mengumpulkan semua argumen posisi yang diberikan saat pemanggilan fungsi dan membungkusnya menjadi tuple "args". Dalam situasi ini, Anda bisa memasukkan angka sebanyak apa pun dalam argumen fungsi.

    Silakan tambahkan integer lainnya sebanyak yang Anda mau pada kode pemanggil fungsi di atas untuk mengetahui perbedaannya. 
'''


# 5. Var-Keyword (Variadic Keyword Parameter)
'''
Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya). Argumen pada pemanggil fungsi akan berperan sebagai value dan parameter (identifier) berperan sebagai key.
'''

# Contoh penerapan Var-Keywords
print("~ 5. Var-Keyword (Variadic Keyword Parameter)\n> Contoh Penerapan nya\n")

# Sesekali kita menggunakan for ya mhehehe untuk functions nya
def perkenalan(**kwargs):
    for key, value in kwargs.items():
        print(f"Key nya adalah = {key} ----> valuenya = {value}")

# Pemanggilan 
pemanggilan = perkenalan(nama="Satria Dirgantara Nuryaman", umur=22, mimpi="Machine Learning Engginer")

'''
    Output:

    Key nya adalah = nama ----> valuenya = Satria Dirgantara Nuryaman
    Key nya adalah = umur ----> valuenya = 22
    Key nya adalah = mimpi ----> valuenya = Machine Learning Engginer

    Pada contoh di atas, parameter **kwargs akan mengumpulkan semua pasangan key-value yang diberikan sebagai keyword argument. Dalam situasi ini, Anda bisa menambahkan parameter dan argumen sejumlah yang diinginkan.
'''


