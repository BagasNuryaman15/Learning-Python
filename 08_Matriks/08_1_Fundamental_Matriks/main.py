print("\n")
print(" Fundamental Matriks ".center(150, "="), "\n")
'''
                                                        Fundamental Matriks

Pada materi sebelumnya, kita telah mempelajari cara menyimpan data yang sama menggunakan array dalam Python dengan list. Untuk pengingat, array merupakan salah satu jenis struktur data linear dan terdiri dari kumpulan elemen bertipe data sama dengan indeks yang berurutan atau linear. 

Sebenarnya, array adalah jenis struktur data 1 dimensi yang menyimpan semua datanya secara linear. Pada materi ini, kita akan mempelajari jenis array 2 dimensi, yakni matriks.

            Array 1 dimensi : ----> |1| |2| |3| |4| |5|
                                     |   |   |   |   |
                                    Terdiri Dari 5 Kolom   

            Array 2 dimensi : ----> |1| |2| |3| -----> Baris 1
                                    |4| |5| |6| -----> Baris 2

Matriks pada matematika merupakan himpunan yang terdiri dari bilangan atau elemen berdasarkan baris dan kolom. Dalam matematika, struktur matriks sebagai berikut.            

            Matriks 2 dimensi :---> [1, 2, 3, 0, 0] ----> Baris 1
                                    [4, 5, 6, 0, 0] ----> Baris 2
                                    [7, 8, 9, 0, 0] ----> Baris 3
                                    [0, 0, 0, 0, 0] ----> Baris 4
                                    [0, 0, 0, 0, 0] ----> Baris 5

Dalam matematika, penamaan baris dan kolom dibuat secara berurutan, baris ke-1 dimulai dari atas hingga ke bawah dan kolom ke-1 dimulai dari kiri ke kanan.

Contoh matriks dalam matematika beragam jenisnya, beberapa di antaranya sebagai berikut.

    1.  Matriks Pengukuran

        Matriks pengukuran adalah jenis matriks dengan indeks (i, j) yang merepresentasikan suatu titik koordinat. Setiap elemen dari matriks ini merepresentasikan hasil pengukuran pada suatu titik koordinat tertentu dan termasuk bilangan real atau tipe data float.


            |-------|-------|-------|
            |  1.1  |  2.2  |  3.3  |
            |-------|-------|-------|
            |  4.4  |  5.5  |  6.6  |
            |-------|-------|-------|
            |  7.7  |  8.8  |  9.9  |
            |-------|-------|-------|

        Gambar di atas merupakan matriks pengukuran yang merepresentasikan suatu titik koordinat tertentu. Perhatikan bahwa setiap elemennya merupakan bilangan real atau bertipe data float dalam pemrograman.

    2.  Matriks Kesatuan

        Matriks kesatuan adalah jenis matriks dengan indeks (i, j) yang merepresentasikan suatu titik koordinat. Setiap elemen dari matriks ini merepresentasikan hasil pengukuran pada suatu titik koordinat tertentu dan termasuk bilang an atau tipe data integer.

            |-------|-------|-------|
            |   1   |   2   |  3    |
            |-------|-------|-------|
            |   4   |   5   |   6   |
            |-------|-------|-------|
            |   7   |   8   |   9   |
            |-------|-------|-------|

        Gambar di atas merupakan matriks satuan dengan indeks baris adalah 1 sampai dengan 3 dan indeks kolom 1 sampai dengan 3. Perhatikan bahwa setiap elemennya merupakan bilangan integer atau bertipe data integer dalam pemrograman.

        Masih banyak penggunaan matriks dalam matematika yang dapat kita pelajari, seperti matriks nama hari yang merepresentasikan nama hari ke-1 hingga hari ke-7 dan elemen matriksnya bertipe string, matriks value, serta masih banyak lagi.

        Anda pun dapat melakukan berbagai operasi pada matriks, seperti penjumlahan, perkalian, menentukan determinan, transpose, dan sebagainya. Bahkan matriks juga dapat dipakai untuk persoalan algoritmik, yakni untuk menyimpan informasi yang cirinya ditentukan oleh dua dimensi atau baris dan kolom, seperti cell pada spreadsheet.

        Sementara itu dalam pemrograman, matriks adalah kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi berdasarkan baris dan kolom. Matriks dalam pemrograman diimplementasikan menggunakan array dua dimensi. Bahkan dalam Python, matriks dapat diimplementasikan menggunakan nested list atau list di dalam list.

            matriks = [[1, 2, 3], ----> Baris 1
                       [4, 5, 6], ----> Baris 2
                       [7, 8, 9]] ----> Baris 3
                       |   |  |
                       --------
                 Kolom 1 Kolom 2 Kolom 3

        Dalam gambar di atas, kita mendeklarasikan variabel "matriks" dan menginisialisasikannya dengan nested list atau list di dalam list. Perhatikan lebih baik,  pada gambar tersebut terdapat dua kurung siku "[]" dan kurung siku pertama adalah list yang membungkus tiga list di dalamnya, yakni "[1, 2, 3], [4, 5, 6], [7, 8, 9]". Sementara kurung siku kedua adalah list yang membungkus tiga elemen dalam list di dalamnya, yakni "1, 2, 3", "4, 5, 6", dan "7, 8, 9".

        Matriks dalam pemrograman dapat kita simpulkan sebagai berikut.

        1.  Matriks adalah kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi berdasarkan baris dan kolom.
        2.  Setiap elemen matriks dapat diakses melalui metode indexing jika kedua indeks telah diketahui.
        3.  Elemen matriks dideklarasikan memiliki tipe homogen yang artinya elemen tersebut harus mempunyai tipe data yang sama. Jika elemen tersebut adalah bilangan real, seluruh elemen lainnya pun adalah bilangan real. Walaupun dalam list Python Anda dapat membuat matriks dengan tipe data berbeda, alangkah lebih baik jika tetap mengikuti aturan ini.

Selanjutnya mari ubah gambar di atas menjadi kode Python yang dapat dieksekusi.
'''

# Contoh penggunaan matriks dalam Python
print("> Contoh penggunaan matriks dalam Python", "\n")

matriks = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

print(f'''
Lihat Outputnya akan menjadi seperti ini:
{matriks}
''', "\n")

'''
Output :

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Pada kode di atas, kita mendeklarasikan variabel "matriks" dan menginisialisasikan dengan nested list. Output yang dihasilkan adalah matriks "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]".

Namun, perlu diingat bahwa mendeklarasikan matriks menggunakan list sangat memakan banyak memori. Masih ingatkah Anda dengan materi array yang menyatakan bahwa setiap nilai atau elemen dalam list akan disimpan pada masing-masing tempat memori? Hal ini berlaku juga pada matriks. 

Jika kita membuat matriks dengan 100 kolom dan 100 baris akan menghasilkan 10.000 elemen integer dalam matriks tersebut dan menggunakan 10.000 penyimpanan untuk menampung semua elemen integer.

Oleh karena itu, menggunakan nested list sebagai matriks dianggap cara yang cukup praktis, tetapi tidak efektif dalam mengelola penyimpanan memori. Jika Anda ingin membuat matriks dengan jumlah elemen yang besar, programmer Python biasanya menggunakan library tambahan seperti NumPy untuk melakukan tugasnya. Library merupakan sekumpulan kode yang telah dibuat oleh developer atau programmer dan disediakan kepada pengguna lain agar dapat digunakan ulang dalam pengembangan program atau perangkat lunak. 

Library NumPy sering dipakai oleh programmer Python untuk melakukan tugas-tugas dalam ranah science dan engineering karena dianggap memiliki penggunaan penyimpanan memori yang efisien. 

Silakan periksa bahwa library NumPy tersedia di komputer Anda dengan menjalankan kode berikut di terminal Anda.

    ======================
        pip show numpy
    ======================
    Jika dalam komputer Anda belum memiliki NumPy, silakan buka kembali terminal Anda dan jalankan perintah berikut.
    ======================
      pip install numpy
    ======================
    Mari lanjutkan dengan implementasi matriks menggunakan NumPy.    
'''

# Implementasi matriks menggunakan NumPy
print("> Implementasi matriks menggunakan NumPy", "\n")

# Pertama-tama import library NumPy
import numpy as np

# Buat matriks dengan NumPy
matriks = np.array([[10, 20, 30], [60, 50, 40], [70, 80, 90]])

print(f'''
Ini adalah contoh penerapan array menggunakan NumPy:
{matriks}
''', "\n")

'''
Output:

[[10 20 30]
 [60 50 40]
 [70 80 90]]

Pada kode di atas, kita mengimpor library "numpy" terlebih dahulu untuk mengambil fungsi-fungsi atau kode yang berada pada library tersebut. Selanjutnya, kita mendeklarasikan variabel "matriks" dan menginisialisasikannya dengan numpy array.

Ingat bahwa matriks adalah array dua dimensi sehingga pada library NumPy kita menggunakan fungsi ".array()" untuk membuat matriks atau array dua dimensi. Pada kode di atas, kita menggunakan fungsi ".array()" dengan nilai di dalamnya adalah nested list.

Jika Anda bertanya, apakah library NumPy bisa dipakai juga untuk array? Jawabannya adalah iya, Anda bisa menggunakan library ini untuk membuat array juga. Programmer sering kali menggunakan library NumPy jika perlu membuat array atau matriks dalam Python.

Sekarang, mari bandingkan ukuran memori yang digunakan jika kita menggunakan matriks Python dan matriks NumPy.
'''

# Bandingkan ukuran memori yang digunakan jika kita menggunakan matriks Python dan matriks NumPy
print("> Bandingkan ukuran memori yang digunakan jika kita menggunakan matriks Python dan matriks NumPy", "\n")

import numpy 
import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)


"""
Output:
Ukuran keseluruhan elemen list dalam bytes =  240
Ukuran keseluruhan elemen NumPy dalam bytes =  72

Tenang, jika kode di atas cukup sulit dipahami tidak apa-apa. Anda cukup memperhatikan output dari kode di atas. Pada kode program di atas, kita membandingkan ukuran memori yang dihasilkan dari matriks menggunakan numpy array dan list Python.

Dengan menggunakan matriks yang sama, yakni "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]" menghasilkan jumlah memori yang berbeda terhadap masing-masing metode. Jika kita menggunakan NumPy, memori yang digunakan untuk keseluruhan elemen adalah 72. Namun, jika kita menggunakan list, memori yang digunakan untuk keseluruhan elemen adalah 240.

Inilah alasan banyak programmer Python cenderung memilih NumPy untuk memproses matriks bahkan hingga ke tahap machine learning. 

    Catatan: Seluruh materi pada modul ini akan menggunakan list Python untuk mengimplementasikan matriks.


"""


