# ======================================================== Operasi pada List, Set, dan String =============================================
print(" Operasi pada List, Set, dan String ".center(150, '='))

# Operasi pada List, Set, dan, String merupakan operasi yang sama seperti operasi kepada tipe data pada umumnya, tetapi sebenarnya sih saya sudah menuliskan pada Tipe Data, tetapi karena Saya sedang melakukan pembelajaraan pada DiCoding maka saya akan sekalian menyalin pemhaman nya kesini.

# ------------------------------------------------------- 1. len() --------------------------------------------------
print(" Operasi Pada len() ".center(100, '-'))
# Fungsi len() bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string. Khusus pada string, program akan menghitung jumlah karakternya.

# Contoh Dalam List
print("> Contoh dalam Tipe Data list")

contoh_list = [1, 2, 15, 1, 3, 3, 3, 10, 11, 6]
print(contoh_list)
print(len(contoh_list))

'''
    Output :
    [1, 2, 15, 1, 3, 3, 3, 10, 11, 6]
    10

    Dari List diatas kita dapat melihat bahwa angka 10 adalah panjang dari kelompok list
'''

# Contoh Dalam Set
print("> Contoh dalam Tipe Data Set")

contoh_set = set([10 , 100, 110, 10, 5, 5, 3 , 230, 50, 100, 7])
print(contoh_set)
print(len(contoh_set))

'''
    Output :
    {3, 100, 5, 230, 7, 10, 110, 50}
    8

    Kalian sudah tau kan kenapa dituliskan 8 dan bukan 11, Ya karena ini adalah Tipe Data Set Bosku karena Tipe Data set dapat menhilangkan duplikat ya bosku
     
'''

# Contoh Dalam String (str)
print("> Contoh dalam Tipe Data String")

contoh_str = "Saya ingin mennjadi AI Speacialist dan Blockchain Developer"
print(contoh_str)
print(len(contoh_str))

'''
    Output :
    Saya ingin mennjadi AI Speacialist dan Blockchain Developer
    59

    Kita sudah mengetahui bahwa spasi atau karakter space (whitespace) akan di hitung juga oleh len
'''

# ----------------------------------------------------- 2. Min() Dan (Mix) --------------------------------------------------
print(" Min() dan Mix() ".center(100, '-'))
'''
Selain menghitung panjang atau banyaknya elemen, Anda juga dapat mengetahui berapa nilai minimum dan maksimum dari suatu list menggunakan fungsi min() dan max().
'''

# Contoh Penerapan Min() dan Mix()
print("> Contoh Penerapan Min() dan Mix()")

# Min() : Mengambil angka yang paling terendah dari suatu value atau Data.
print("Contoh Min() :")
contoh_min = [100, 1000, 2000, 75, 1085, 124, 125, 65]
print(min(contoh_min))

# Outputnya : 65, karena dia merupakan nilai angka terkecil.

# Max() : Kebalikan Dari Min()
print("Contoh Max() :")
contoh_max = [100, 1000, 2000, 75, 1085, 124, 125, 65]
print(max(contoh_max))

# Output : 2000

# --------------------------------------------------------- 3. Count  --------------------------------------------------
print(" Count ".center(100, '-'))
# Fungsi count() digunakan untuk mengetahui berapa kali suatu objek muncul dalam list.

# Contohnya 
print("Contoh Penerapan Count :")
angka = [1, 4, 4, 4, 3, 4, 4, 4, 10, 5]
print(angka)
print(angka.count(4))

'''
    Output :
    [1, 4, 4, 4, 3, 4, 4, 4, 10, 5]
    6

    Pada kode di atas, program akan menghitung banyaknya angka 4 dalam list. Namun, pada kode di bawah, program akan menghitung banyaknya substring/huruf "a" dalam string.
'''
# Contoh Penerapan Pada String
print("> Contoh Penerapan Count pada String :")
count_str = (f"Saya adalah Satria Dirgantara Nuryaman, Ingin menjadi 'AI Speacialist' dan Blockchian Developer")
print(count_str)
print(count_str.count("a"))

'''
    Output :
    Saya adalah Satria Dirgantara Nuryaman, Ingin menjadi 'AI Speacialist' dan Blockchian Developer
    17

'''


# ----------------------------------------------------------- 4. In and Not In  --------------------------------------------------
print(" In and Not In".center(100, ('-')))

'''
In dan not in merupakan operator yang diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list. Anda bisa menggunakan operator ini untuk memastikan suatu nilai ada dalam list bahkan dalam string. Operator in dan not in akan mengembalikan nilai boolean True atau False. 
'''
# Contoh Penerapan In and Not In
print("> Contoh Penerapan In and Not In :")
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

"""
Output:
True
False
False
True

Ada empat baris kode di atas. Pada baris pertama, Anda mencari kata atau substring "Dicoding" dalam variabel kalimat. Hasilnya, kata tersebut ada dalam variabel kalimat sehingga mengembalikan nilai True. 

Hal ini berlaku sebaliknya pada baris kode ketiga, Anda justru memastikan bahwa substring "Dicoding" tidak ada dalam variabel kalimat. Hasilnya tentu False karena kita sudah tahu pada baris kode pertama bahwa substring "Dicoding" ada dalam variabel kalimat. 

Hal ini juga yang dilakukan pada baris kode kedua dan keempat. Pada kode tersebut yang dicari adalah substring "tidak". Apakah jawabannya? Silakan Anda telaah lebih dalam.


"""

print(dict([['name','Dicoding'],['age',17]]))

