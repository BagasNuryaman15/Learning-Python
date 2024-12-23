print("\n")
print(" Operasi Matriks pada Python ".center(150, "="), "\n")
'''
                                                        Operasai Matriks pada Python

Dalam matematika ataupun pemrograman, operasi matriks dapat melibatkan dua matriks sekaligus atau pun satu matriks saja. Beberapa operasi tersebut di antaranya sebagai berikut.

    a.  Operasi 1 matriks.
        1.  Menghitung total semua elemen matriks.
        2.  Mengalikan elemen matriks dengan konstanta.
        3.  Transpose matriks.
        4.  Inverse matriks.
        5.  Menentukan determinan, dan sebagainya.

    b.  Operasi 2 matriks:
        1.  Menambahkan dua matriks.
        2.  Mengalikan dua matriks.
        3.  Pembagian dua matriks, dan sebagainya.

Dari berbagai operasi matriks yang tersedia, mari kita pelajari salah satu di antaranya, yakni mengalikan elemen matriks dengan konstanta.

Dalam matematika, mengalikan elemen matriks dengan konstanta dapat diilustrasikan seperti gambar berikut. Asumsikan ukuran matriksnya adalah 2x2 atau 2 baris dan 2 kolom.

        --    --    --     -- 
    2 X | 5  0 | =  | 10  0 |           
        | 1 -2 |    | 2  -4 |
        --    --    --     --  

    Berikut kalkulasinya :
    2 x 5 = 10              2 x 0 = 0
    2 x 1 = 2               2 x-2 = -4

Pada ilustrasi tersebut, kita mengalikan matriks "[5, 0], [1, -2]" dengan konstanta "2". Nilai konstanta tersebut kemudian dikalikan dengan setiap elemen matriks. Kalkulasinya dapat kita urai seperti berikut. 

    1.  Pertama, konstanta "2" akan dikalikan dengan elemen 5 yang menghasilkan nilai 10 (2 X 5 = 10).
    2.  Kedua, konstanta "2" akan dikalikan dengan elemen 0 yang menghasilkan nilai 0 (2 X 0 = 0).
    3.  Ketiga, konstanta "2" akan dikalikan dengan elemen 1 yang menghasilkan nilai 2 (2 X 1 = 2).
    4.  Terakhir, konstanta "2" akan dikalikan dengan elemen -2 yang menghasilkan nilai -4 (2x-2 = -4).

Jika kita ubah ke dalam pemrograman, hasilnya sebagai berikut.
'''

# Contoh penerapan Operasi pada Matriks
print("> Contoh penerapan Operasi pada Matriks", "\n")

# Membuat matriks 2x2
var_mat = [[5, 0],
          [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
    def_mat[i][j] = var_mat[i][j]*2

print(def_mat)

"""
Output:
[[10, 0], [2, -4]]

Perhatikan penjelasan berikut untuk memahami contoh di atas.

    1.  Pertama, kita mendeklarasikan variabel "var_mat" dan menginisialisasikannya dengan matriks yang diinginkan. Di sini, matriks yang digunakan berukuran 2x2 atau 2 baris dan 2 kolom.
    2.  Kedua, kita perlu mendeklarasikan variabel "def_mat" sebagai matriks default baru dengan nilai (0). Matriks dengan nilai default ini harus berukuran sama dengan matriks yang asli.
    3.  Ketiga, kita akan melakukan perulangan berdasarkan dua kondisi. Kondisi pertama adalah perulangan berdasarkan banyaknya list di dalam matriks ([5, 0], [1, -2]) yang merepresentasikan baris. Kondisi kedua adalah perulangan berdasarkan banyaknya elemen pada setiap list (5,0 dan 1,-2).

    Perulangan pertama (i) akan mengulang sebanyak dua kali karena variabel "var_mat" memiliki dua list di dalamnya. Perulangan kedua (j) akan mengulang sebanyak dua kali karena setiap elemen list yang diambil memiliki dua nilai. Jadi, elemen list pertama adalah "5 dan 0" serta elemen list kedua adalah "1 dan -2".

    Pada setiap perulangannya, nilai i = 0, 1; j =0, 1. Ingat, ini disebabkan kita mengambil panjang dari variabel "var_mat" yang memang memiliki dua list dan panjang elemen dari setiap list-nya. Fungsi "range()" selalu memulai bilangan dari nol.

    4.  Selanjutnya, kita akan meng-update matriks default dengan nilai yang dihasilkan berdasarkan perulangan dan mengalikannya dengan konstanta 2.

    Jadi, elemen def_mat[0][0] yang bernilai 0 akan diubah dengan elemen var_mat[0][0] yang bernilai 5 lalu dikalikan dengan 2 dan hasilnya adalah 10. Elemen def_mat[0][0] yang awalnya bernilai 0 berubah menjadi 10.

    5. Perulangan ini terus terjadi hingga semua kondisi terpenuhi dan menyebabkan semua elemen variabel "def_mat" berubah sesuai perkalian dengan konstanta 2.

    Phew, materi kali ini sangat erat dengan perhitungan matematika. Cara yang kita pelajari di atas terbilang cukup rumit. Nah, sebenarnya ada cara yang lebih efektif, yaitu dengan menggunakan library NumPy. Perhatikan kode di bawah ini.
"""

# Contoh penerapan dengan libary Numpy
print("> Contoh penggunaan dengan libary numpy", "\n")

import numpy as np 

exNumpy = np.array([[20, 5],
                    [10, 2]])

hasil = exNumpy * 2

print(f'''Hasilnya akan menjadi =
{hasil}''')

'''
    Output:
    [[40 10]
     [20  4]]

Pada contoh di atas, kita melakukan operasi perkalian matriks dengan konstanta yang sama seperti sebelumnya. Bedanya, kali ini kita menggunakan library NumPy untuk mempermudah pengkodean. Bisa Anda lihat bahwa dengan menggunakan NumPy kita tidak perlu lagi menggunakan nested for dan cukup mengalikan matriks dengan konstanta yang diinginkan. Dalam hal ini ditunjukkan pada kode berikut.

    hasil = exNumpy * 2

Anda masih bisa bereksplorasi dengan operasi matriks lainnya seperti transpose matriks, inverse matriks, dan sebagainya. Silakan bereksplorasi.
'''



