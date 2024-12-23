print("\n")
print(" Implementasi Matriks pada Python ".center(150, "="), "\n")
'''
                                                    Implementasi Matriks pada Python

Sebelumnya kita telah belajar cara mengimplementasikan matriks yang merupakan array dua dimensi menggunakan nested list. Ingat bahwa setiap elemen matriks dideklarasikan memiliki tipe homogen, yang artinya elemen tersebut harus memiliki tipe data yang sama. Jika Anda mendeklarasikan suatu elemen bertipe data float, elemen lainnya pun adalah float.

Sekarang, kita pelajari cara mengimplementasikan matriks pada Python lebih dalam. Kita akan mulai dengan cara mendeklarasikan matriks hingga mengakses setiap elemen matriks dengan metode indexing.
'''


# ====================================================== 1. Deklarasi Matriks ===================================================
print(" 1. : Deklarasi Matriks ".center(70, "-"), "\n")
'''
                                                            Deklarasi Matriks

Ada dua cara untuk mendeklarasikan matriks menggunakan Python sebagai berikut.

    1.  Deklarasi sekaligus inisialisasi nilai matriks.
        Cara pertama adalah mendeklarasikan matriks sekaligus menginisialisasikan nilainya dengan ukuran N baris dan M Kolom (NxM). Cara ini dilakukan jika kita telah mengetahui nilai yang perlu diberikan.

Berikut adalah struktur untuk mendeklarasikan matriks dengan menginisialisasikan nilainya sekaligus.

    <nama-var> = [[nilai1, nilai2, ..., nilaiM], 
                  [nilai1, nilai2, ..., nilaiM],
                  [val-n1, val-n2, ..., val-nM]]

    Gambar di atas merupakan struktur jika kita ingin mendeklarasikan matriks dengan ukuran nxm. Ingat bahwa tipe elemen tersebut akan bergantung pada nilai yang diberikan. Jika nilai yang diberikan adalah bilangan bulat, tipe elemen adalah integer. Jika nilai yang diberikan adalah bilangan real, tipe elemen adalah float.

Mari lihat implementasi kodenya di bawah ini.
'''

# Contoh penerapan deklarasi matriks sekaligus inisialisasi nilai matriks.
print("> Contoh Penerapan Deklarasi Matriks", "\n")

matriks_1 = [[1, 0, 0, 0, 1 ],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [1, 0, 0, 0, 1]]

# Cetak matriks_1
print(matriks_1, "\n")

'''
    Output:
   [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]

    Pada kode di atas, kita mendeklarasikan variabel matriks dan menginisialisasikannya dengan matriks satuan dan memiliki ukuran baris = 5 dan ukuran kolom = 5. Matriks satuan adalah jenis matriks dengan elemen bernilai hanya 0 dan 1.
'''


# ====================================================== 2. Deklarasi dengan nilai default ===================================================
print(" 2. : Deklarasi dengan nilai default ".center(70, "-"), "\n")
'''
                                                            Deklarasi dengan nilai default

Cara kedua adalah mendeklarasikan matriks dengan nilai default. Sebagaimana materi array, nilai default ditentukan oleh kesepakatan bersama sesuai kebutuhan dengan nilainya di luar rentang yang ditentukan. Misalnya, tim Anda menentukan nilai dalam list harus berkisar dari 1 hingga 10. Kita bisa menyepakati nilai "0" sebagai nilai default karena di luar jangkauan yang disepakati (1-10). Cara kedua ini melibatkan list comprehension yang sama seperti pada materi array.

Struktur dari deklarasi dengan nilai default sebagai berikut.

    <nama-var> = [[<default-val for j in range(<m>)] for i in range(<n>)]

Terlihat pada struktur tersebut, cara kedua ini menggunakan dua metode sekaligus, yakni nested list dan nested for. Kita menggunakan nested for atau for bersarang untuk membuat baris dan kolom. Perhatikan baik-baik, perulangan dalam atau perulangan kedua diapit oleh tanda siku "[]" yang artinya hasil dari perulangan kedua adalah baris pada matriks, sedangkan perulangan pertama atau perulangan luar menghasilkan kolom pada matriks.

Nilai dari <default-val> ditentukan kesepakatan bersama, misalnya jika range yang disepakati adalah 1 hingga 10, kita bisa memilih 0 untuk nilai default-nya. Ada pula <n> sebagai jumlah baris matriks yang ingin dibuat dan <m> sebagai jumlah kolom matriks yang diinginkan.

Selanjutnya, mari lihat penerapan kodenya di bawah ini.
'''

# Contoh penerapan deklarasi dengan nilai default.
print("> Contoh Penerapan Deklarasi dengan Nilai Default", "\n")

# Contoh
matriks_default = [[0 for j in range(5)] for i in range (3)]
print(f'''
Output dari penggunaan Nilai Default akan seperti di bawah ini:
{matriks_default}''', "\n")


'''
    Output :
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] 

Pada kode di atas, kita mendeklarasikan variabel matriks dan menginisialisasikannya dengan nested list dan nested for serta nilai default-nya adalah 0. Matriks yang dibuat pada program di atas adalah matriks value dengan setiap elemennya bertipe integer serta memiliki ukuran baris = 3 dan ukuran kolom = 5.
'''



# ====================================================== 3. Akses Elemen Matriks ===================================================
print(" 3. : Akses Elemen Martiks ".center(70, "-"), "\n")
'''
                                                                Akses ELemen Matriks

Sekarang, mari pelajari cara mengakses elemen pada matriks. Ingat bahwa matriks merupakan tabel data yang terdiri dari baris dan kolom. Jadi, jika Anda ingin mengakses elemen dari matriks, perlu mengetahui indeks dari baris dan kolom.

Kita akan mengakses elemen matriks menggunakan metode indexing. Ini artinya Anda perlu mengetahui indeks dari baris dan kolom yang ingin diakses. Berikut adalah struktur untuk mengakses elemen matriks dengan metode indexing.

    <nama-var> = [<n-baris>][<n-kolom>]

Berdasarkan struktur di atas, <namamatriks> merupakan variabel yang berisi nilai matriks, <nbrs> merupakan nomor indeks baris yang ingin diakses, dan <nkol> nomor indeks kolom yang ingin diakses.

Perhatikan gambar di bawah ini untuk memahami maksud dari indeks baris dan kolom.


Asumsikan Anda memiliki matriks dengan ukuran 5 baris dan 5 kolom yang setiap elemennya berisi angka dari 1 hingga 25 seperti gambar di atas. Indeks baris ke-0 dimulai dari 1 hingga 5, indeks baris ke-1 dimulai dari 6 hingga 10, dan seterusnya. Indeks kolom ke-0 dimulai dari "1, 6, 11, 16, 21", begitu pun indeks kolom ke-1 dimulai dari "2, 7, 12, 17, 22", dan seterusnya.

Jika kita ingin mengakses nilai 12 pada matriks di atas, nilai tersebut berada pada indeks baris ke-2 dan indeks kolom ke-1. Dalam pemrograman, nilai tersebut bisa diasumsikan dengan "[2][1]" dengan nilai 2 adalah indeks atau nomor baris dan nilai 1 adalah indeks atau nomor kolom.

Mari lihat penerapannya di bawah ini.
'''

# Contoh penerapan untuk mengakses elemen dalam matriks
import numpy as np

matriks = np.array = ([[1, 2 ,3 ,4 ,5],
                       [5, 6, 7, 8, 9],
                       [10, 11, 12, 13, 14],
                       [15, 16, 17, 18, 19],
                       [20, 21, 22, 23, 24]])

print(matriks[2][3])

"""
    Output:
    13
    
    Pada contoh di atas, kita mendeklarasikan variabel "matriks" dan menginisialisasikan dengan matriks yang sama seperti gambar sebelumnya. Selanjutnya, kita mengakses elemen matriks yang berada pada indeks baris ke-2 dan indeks kolom ke-1 ([2][1]) serta menampilkannya ke layar. Output dari program tersebut adalah "12" dan nilai tersebut adalah elemen yang berada pada indeks yang kita cari.

    Silakan bereksplorasi dengan kode di atas untuk mencari nilai yang Anda inginkan. Ubah "var_mat[2][3]" dengan variabel dan indeks yang diinginkan.
"""

