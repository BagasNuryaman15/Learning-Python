# ------------------------------------------Variable Python----------------------------------
""" 

Secara umum variable adalah suatu nama yang bisa kita gunakan untuk menyimpan sebuah nilai atau data yang nantinya kita bisa gunakan atau ubah disaat program berjalan. Bisa saya contohkan dengan di bawah ini. Nah jika di Python angka dan nama yang kita simpan dinamakan dengan Tipe Data dan ada juga namanya assigment.

"""

# ------------------------------- Rule Dalam Variable Python ----------------------
""" 
1. Nama dari sebuah variabel harus dimulai dengan huruf (a-z, A-Z) atau karakter garis bawah/underscore (_) dan tidak dapat dimulai dengan angka (0-9).

2. Variabel hanya boleh mengandung karakter alfabet dan bilangan dan underscore (a-z, A-Z, 0-9, _).

3. Variabel bersifat case-sensitive yang mengartikan bahwa variabel TINGGI, tinggi, dan Tinggi merujuk pada tiga variabel berbeda.

"""

nama = "Jajang" # Nah (nama) tersbut bisa kita sebut variable karena menyimpan sebuah nilai atau data yang bernama jajang
umur = 21  # Sama saja umur merupakan sebuah variable karena ada tipe data yang berbentuk int atau float dengan angka 10

print ("Hallow teman teman nama saya adalah", nama)
print ("Umur saya baru saja beranjak di usia", umur, "Tahun")

a = 10 # Assigment (=) menugaskan 10 untuk masuk kedalam variable a
x = 20
kmha = 100

print ("Nilai kmha adalah", kmha)
print ("Nilai a =", a)
print ("Nilai x nya eta" , x)

# Perlu kalian ketahui bahwa di Python tidak ada yang namanya deklarasi seperti pada bahasa pemrogramaan lainnya tanda (=) bisa disebut juga dengan assigemnt atau "Operator Penugasan" yang fungsinya adalah untuk memberikan nilai ke sebuah variable bisa kita liat pada contoh variable a saya akan memberikan komentar penjelasan operator penugasan di sisinya.

# --------------------------Aturan Penamaan-------------------
"""

Nah dalam penamaan kita tidak boleh memberikan spasi dan jika kamu tetap ingin memberikan sebuah nama yang panjang atau dua kalimat kamu bisa menggunakan underscore (_) tidak boleh string (-) karena itulah arutannya dan jika kamu menambahkan sebuah angka di variablenya maka angka tidak boleh berada paling depan harus paling belakang.

"""

# Contohnya 
Tanggal_Lahir =  15_09_02 # UnderScore
print ( "Tanggal lahir saya adalah ",Tanggal_Lahir)

Bagasgantengn01 = "Ganteng nian" # Menggunakan Angka
print ("Apakah bagas seganteng itu", Bagasgantengn01) 

# Pengunalangan atau pergantian variable 
"""Kita bisa mengganti nilai variable dengan memanggilnya lagi dan menuliskan nilai apa yang ingin digantikan seperti di bawah ini"""
a = "Ngaran we ayeunamah nya" # Mengganti nilai dari variable a
print ("Secara otomatis variable a akan tergantikan yang awalnya adalah 10 kini berubah menjadi nilai yang berbeda dengan tipe data bernama", a)

# Kita juga bisa menggunakan variable untuk menjadi sebuah nilai variable, ini diberinama assigment indirect
c = a # saya memerintahkan variable c mempunyai nilai yang sama dengan variable a 
print ("Sama kan noh", c)

# -------------------------------- Commentars (#) -----------------------------

"""

Comments adalah sekumpulan teks yang dituliskan dalam sebuah program dan tidak akan mempengaruhi hasil dari sebuah program. Berikut adalah contoh penulisan sinle lines dan multiple-line sudah kita gunakan dari tadi misalnya single lines yang bertanda (#), dan muliple-line yang bertanda (tanda kutip ganda sebanyak 3 kali di awal + 3 kali di akhir).

"""


