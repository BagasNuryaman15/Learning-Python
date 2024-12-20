print(" Pengertian Ekspresi ".center(150, "=") + "\n" + "\n")
''' 
Pengertian Ekspresi
Phew, setelah melewati pembahasan tipe data yang sangat komprehensif, Anda memiliki bekal cukup untuk membuat program dan belajar pada modul-modul berikutnya. 

Salah satunya adalah materi ekspresi kali ini. Data yang Anda simpan pada suatu variabel umumnya akan dioperasikan untuk menghasilkan suatu nilai sesuai keinginan. Masih ingat ekspresi pada matematika? Ekspresi pada matematika adalah kombinasi dari simbol-simbol matematika, seperti angka, variabel, operasi matematika, dan sebagainya. Contohnya seperti pada gambar berikut.

Pada gambar di atas, "4x-7" merupakan ekspresi, sedangkan "4x", "7", dan "5" merupakan suku bilangan. Apabila kita mengingat kembali, operasi pada matematika ataupun pemrograman merupakan suatu proses yang dilakukan untuk mendapatkan hasil nilai tertentu.

Lalu, apa itu ekspresi dalam pemrograman? Ekspresi pada pemrograman merupakan kombinasi dari satu atau lebih variabel, konstanta, operator, dan fungsi yang bermakna untuk menghasilkan suatu nilai dalam suatu tipe tertentu.

Struktur umum ekspresi yang sering dijumpai adalah <operan1> <operator> <operan2>. Namun, perlu Anda ketahui bahwa struktur umum tersebut merupakan struktur ekspresi biner (jenis ekspresi menggunakan dua operan). Mari bedah struktur tersebut lebih dalam.

Operan dapat berupa nilai, variabel, konstanta, atau ekspresi lain.
Operator merupakan suatu fungsi standar yang disediakan dalam bahasa pemrograman untuk melakukan beberapa hal dasar, seperti perhitungan aritmetika, logika, dan relasional. Contohnya adalah penjumlahan (+), pengurangan (-), perkalian (*), modulus (%), dan sebagainya.
'''

# Di bawah ini, penerapan ekspresi pada Python.
print(" Penerapan Ekpresi Pada Python ".center(70, "-") + "\n")

# Contohnya
print(" Contoh ".center(20, "="))
x = 10
y = 2
result = x - y

print(result)
print("")

"""
Output:
8

Lantas, mengapa kita harus paham terlebih dahulu mengenai ekspresi? Sebab, ini merupakan dasar dalam pemrograman untuk melakukan semua perhitungan dan manipulasi data. 

Karena itu, Anda harus mengetahui dasar-dasar ekspresi dalam pemrograman.
"""

# Salah satunya adalah melakukan penggabungan dan replikasi pada list.
print(" Penggabungan dan Replikasi Pada List ".center(70, "-") + "\n")

# Contohnya
print(" Contoh ".center(20, "="))
angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf

print(gabung)

"""
Output:
[2, 4, 6, 8, 'P', 'Y', 'T', 'H', 'O', 'N']

"""

# Contohnya
print(" Contoh dengan perkalian ".center(20, "="))
angka = [2, 4, 6, 8]
replikasi = angka * 3

print(replikasi)

"""
Output:
[2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]

Pada kode di atas, Anda menggabungkan dua list dengan menggunakan operator penjumlahan (+). Namun, pada kode di bawah ini, Anda mereplikasi list dengan menggunakan operator perkalian (*).
"""
