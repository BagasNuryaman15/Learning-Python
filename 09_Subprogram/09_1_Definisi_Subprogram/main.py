print("\n")
print(" Definsi Subprogram ".center(150, "="), "\n")
'''
                                                          Definisi Subprogram

Sejauh ini, Anda telah membuat program yang beragam. Setiap program yang Anda bangun, pada akhirnya akan semakin besar seiring dengan kompleksitas masalah yang perlu diselesaikan. Semakin besar sebuah program, bagian kode yang berulang akan bertambah sehingga tidak efisien jika Anda perlu mengetik ulang atau bahkan melakukan copy-paste. Salah satu kode yang sering berulang adalah rumus atau formula, perhatikan kode di bawah ini.

'''

# Salah satu contoh rumurs atau formula
print("> Salah satu contoh rumus atau formula", "\n")
# Luas pertama
panjang = 15
lebar = 6

luas_persegi_panjang = panjang * lebar
print(f"Dan inilah hasil dari luas persegi panjang = {luas_persegi_panjang}", "\n")

'''
    Output:
    Dan inilah hasil dari luas persegi panjang = 90

Kode di atas merupakan program untuk mencari luas persegi panjang. Perhatikan bahwa kita perlu menuliskan dua rumus kode yang sama untuk mencari luas persegi panjang dengan nilai panjang dan lebar berbeda.

Lalu, apakah ada cara untuk menghindari kode yang perlu diketik berulang, dan sebaliknya, dapat digunakan berkali-kali? Jawabannya adalah ada, inilah yang disebut sebagai subprogram dan salah satu jenisnya adalah fungsi.

Bandingkan kode sebelumnya dengan kode berikut.
'''

# Contoh penggunaan subprogram def yang memudahkan kita untuk cleaning code.
print("> Contoh penggunaan subprogram (def)", "\n")

def mencaei_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

# Persegi panjang pertama
persegi_panjang_pertama = mencaei_luas_persegi_panjang(20, 17)
print(f"Hasil dari persegi panjang pertama tanpa kita menuliskan cape cape lagi. Hasilnya = {persegi_panjang_pertama}", "\n")

# Persegi panjang kedua
persegi_panjang_kedua = mencaei_luas_persegi_panjang(5, 3)
print(f"Hasil dari persegi panjang kedua adalah = {persegi_panjang_kedua}")


'''
    Output :
    340
    15

Kode di atas merupakan program yang sama dengan sebelumnya dan bertujuan untuk mencari luas persegi panjang. Namun, kali ini kita menggunakan sebuah konsep yang disebut fungsi. Blok fungsi pada kode di atas dimulai dari "def" hingga "return".

Ini adalah tujuan akhir dari materi kali ini, Anda diharapkan memahami subprogram yang di antaranya adalah fungsi dan prosedur.

Subprogram adalah serangkaian instruksi dirancang untuk melakukan operasi yang sering digunakan dalam suatu program. Subprogram yang sering digunakan terdiri dari dua jenis, yakni berikut.

    1.  Fungsi
        Fungsi adalah blok kode yang dapat menerima input, melakukan pemrosesan, dan mengembalikan output. Hasil atau output tersebut dinyatakan dalam sebuah tipe data yang eksplisit. Artinya, fungsi yang dibuat dapat ditentukan untuk mengembalikan tipe data integer, string, atau lainnya.
    2.  Prosedur
        Prosedur adalah deretan instruksi yang jelas keadaan awal (initial state) dan keadaan akhirnya (final state). Prosedur mirip dengan program secara umum, tetapi memiliki cakupan yang kecil dan terbatas.

    Sekarang, mari kita pelajari satu per satu mengenai fungsi dan prosedur.
'''
