print(" Jenis Jenis Ekpresi ".center(150, "+")+ "\n")
''' 
                                                    Ekspresi Menurut Arity dari Operator

1. Ekspresi unary: operasi yang hanya memiliki satu operand
    Contohnya adalah :
    (x += 1), (x-=1), (not x).
2. Ekspresi binary: operasi yang memiliki dua operand 
    Contohnya adalah : 	
    (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).

3. Ekspresi ternary: operasi yang memiliki tiga operand
    Contohnya adalah :
    (x if y else z).

Ekspresi biner merupakan jenis yang memiliki dua operan. Operatornya meliputi penjumlahan (+), pengurangan (-), perkalian (*), pembagian (/), perpangkatan (**), lebih kecil dari (<), lebih kecil dari sama dengan (<=), lebih besar dari (>), lebih besar dari sama dengan (>=), modulus (%), sama dengan (==), dan tidak sama dengan (!=).

Namun, ekspresi uner adalah jenis ekspresi yang memiliki bentuk dasar operasi dengan satu operan. Contohnya adalah increment (x+=1), decrement (x-=1), dan negasi (not x).

Ekspresi terner adalah jenis ekspresi yang memiliki bentuk dasar operasi dengan tiga operan. Contohnya adalah (x if y else z). 
'''

# Anda sudah melihat penerapan ekspresi biner pada submodul sebelumnya dan berikut adalah penerapan ekspresi uner.

# Contoh ekspresi uner
print(" Contoh ekspresi uner: ".center(20, "="))

a = True
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)

'''
Output:
False
5
7
-10

Mari kita bedah satu persatu kode di atas.

    1. Variabel a bernilai True, jika kita memberikan ekspresi "not a" yang artinya "not True", hasil yang didapat adalah False. 
    2. Baik increment maupun decrement, keduanya adalah pola yang sama untuk menambahkan dan mengurangi suatu variabel dengan jumlah tetap.
        A. a += 1 memiliki tujuan yang sama dengan struktur a = a + 1. Jika diasumsikan variabel a bernilai 1, seolah-olah kita melakukan operasi penjumlahan "1+1". Inilah alasan ia disebut dengan increment yang artinya kenaikan.

        B. Decrement dapat dijelaskan sebagai a -=1, memiliki tujuan yang sama dengan struktur a = a - 1. Jika diasumsikan variabel a bernilai 1, seolah-olah kita melakukan operasi pengurangan "1-1".

    Penjelasan lebih detail mengenai operator akan kita bahas pada materi selanjutnya. Saat ini mari kita lanjut membahas ekspresi menurut tipe data yang dihasilkan.
'''

''' 
                                                    Ekspresi Menurut Tipe Data yang Dihasilkan
    1. Ekspresi aritmetika: <numerik> <operator> <numerik> = <numerik>
        contohnya adalah = 2 + 2 = 4, 2 - 2 = 0

    2. Ekspresi relasional: <numerik> <operator> <numerik> = <boolean>
        contohnya adalah = 2 > 1 = True, 2 < 1 = False

    3. Ekspresi logika: <boolean> <operator> <boolean> = <boolean>
        contohnya adalah = True and True = True, True or False = True True not False = True


    Sebagaimana judulnya, jenis-jenis ini adalah ekspresi yang dikelompokkan berdasarkan tipe data yang dihasilkan. Mari kita bedah satu per satu.

    1. Ekspresi aritmetika: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan numerik.
    2. Ekspresi relasional: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan nilai boolean/logika.
    3. Ekspresi logika: jenis ekspresi yang memiliki operan bertipe boolean/logika dan menghasilkan nilai boolean/logika.
'''

# Contoh ekspresi aritmetika
print("Contoh ekspresi aritmetika:".center(20, "="))

a = 10
b = 2
c = a + b
print(c)

'''
Output:
12

Mari kita bedah satu persatu kode di atas.

    1. Variabel a bernilai 10, variabel b bernilai 2, dan variabel c bernilai 12.
    2. Variabel c bernilai 12 karena hasil dari operasi penjumlahan "10+2".

Dan bisa kita lihat bahwa ada operan dan operator yang digunakan dalam ekspresi aritmetika. Operan adalah variabel yang digunakan untuk menyimpan nilai, sedangkan operator adalah simbol yang digunakan untuk melakukan operasi.
'''

# Contoh ekspresi relasional
print("Contoh ekspresi relasional:".center(20, "="))

a = 10
b = 2
c = a > b
print(c)

'''
Output:
True

Mari kita bedah satu persatu kode di atas.

    1. Variabel a bernilai 10, variabel b bernilai 2, dan variabel c bernilai True.
    2. Variabel c bernilai True karena hasil dari operasi relasional "10>2".

Dan bisa kita lihat bahwa ada operan dan operator yang digunakan dalam ekspresi relasional. Operan ke 1 adalah variabel a dan operan ke 2 adalah variabel b. Operator yang digunakan adalah ">" yang artinya "lebih besar dari".
'''

# Contoh ekspresi logika
print("Contoh ekspresi logika:".center(20, "="))

a = True
b = False
c = a and b
print(c)

'''
Output:
False

Mari kita bedah satu persatu kode di atas.

    1. Variabel a bernilai True, variabel b bernilai False, dan variabel c bernilai False.
    2. Variabel c bernilai False karena hasil dari operasi logika "True and False".

Dan bisa kita lihat bahwa ada operan dan operator yang digunakan dalam ekspresi logika. Operan ke 1 adalah variabel a dan operan ke 2 adalah variabel b. Operator yang digunakan adalah "and" yang artinya "dan".
'''

# Contoh Ekpresi Terner
print("Contoh ekspresi terner:".center(20, "="))

a = 10
b = 2
c = 3
d = a if a > b else c
print(d)

'''
Output:
10

Mari kita bedah satu persatu kode di atas.

    1. Variabel a bernilai 10, variabel b bernilai 2, variabel c bernilai 3, dan variabel d bernilai 10.
    2. Variabel d bernilai 10 karena hasil dari operasi terner "10 if 10 > 2 else 3".

Dan bisa kita lihat bahwa ada operan dan operator yang digunakan dalam ekspresi terner. Operan ke 1 adalah variabel a, operan ke 2 adalah variabel b, dan operan ke 3 adalah variabel c. Operator yang digunakan adalah "if" yang artinya "jika".
'''

# Contoh Ekpresi Campuran
print("Contoh ekspresi campuran:".center(20, "="))

a = 10
b = 2
c = 3
hasilArtimatika = a + b
hasilRelasional = a > b
hasilLogika = a and b
hasilTerner = a if a > b else c
hasilCampuran = hasilArtimatika + hasilRelasional + hasilLogika + hasilTerner
print(hasilCampuran)
'''
Output:
25

Mari kita bedah satu persatu kode di atas.

    1. Variabel a bernilai 10, variabel b bernilai 2, variabel c bernilai 3, dan variabel d bernilai 10.
    2. Variabel d bernilai 10 karena hasil dari operasi terner "10 if 10 > 2 else 3".
    3. Variabel e bernilai 3 karena hasil dari operasi terner "10 if 10 > 2 else 3 if 3 > 10 else 2".

Dan pada kode di atas kita melibatkan beberapa ekspresi yang berbeda. Operan dan operator yang digunakan dalam ekspresi campuran adalah operan dan operator yang digunakan dalam ekspresi aritmetika, ekspresi relasional, ekspresi logika, dan ekspresi terner.

'''


