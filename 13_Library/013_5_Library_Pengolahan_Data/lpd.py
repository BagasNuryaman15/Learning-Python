print("\n")
print(" Library Pengolahan Dara ".center(150, "="), "\n")
'''
                                                                            Library Pengolahan Data

Library pengolahan data bertujuan untuk membantu dalam manipulasi, analisis, dan pemrosesan data. Library ini menyediakan berbagai fungsi dan metode yang memudahkan pengguna untuk melakukan operasi pengolahan data dengan lebih efisien dan cepat.

Tujuan dari library ini untuk menyederhanakan tugas-tugas kompleks yang berkaitan dengan pengolahan data sehingga Anda tidak perlu mengimplementasikan semuanya dari awal. Berikut adalah beberapa library populer yang digunakan untuk pengolahan data.

    1.  Pandas
        Pandas adalah library populer yang digunakan untuk pengelolaan dan analisis data. Library ini menyediakan struktur data dan alat untuk membantu pengguna dalam melakukan manipulasi, pembersihan, transformasi, dan analisis data dengan mudah dan efisien.

        Meskipun pandas sudah terinstal secara otomatis pada beberapa IDE dan versi Python, perlu diingat bahwa pandas bukan merupakan library bawaan Python. Oleh karena itu, Anda harus menginstal library ini terlebih dahulu sebelum dapat menggunakannya. Silakan buka command prompt dan jalankan kode berikut.

            pip install pandas

        Atau jika Anda ingin menggunakan conda, silakan jalankan kode berikut untuk menginstalnya.

            conda install pandas

        Setelah berhasil diinstal, Anda dapat mengimpor library pandas dengan menggunakan kode berikut.
'''

# Contoh Penerapan Library Pandas
print("~ 1. Pandas ~".center(50, "-"), "\n")
print("> Contoh Penerapan Library Pandas \n")

import pandas as pd

# Membuat DataFrame dari Dictionary
data ={
    'Nama': ['Andi', 'Budi', 'Caca', 'Deni'],
    'Umur': [21, 22, 23, 24],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya', 'Semarang'],
    'Hobi': ['Membaca', 'Menulis', 'Menggambar', 'Menari']
}

df = pd.DataFrame(data)
print(df, "\n")

'''
    Output dari kode di atas adalah sebagai berikut.

            Nama  Umur      Kota       Hobi
        0  Andi    21   Jakarta    Membaca
        1  Budi    22   Bandung    Menulis
        2  Caca    23  Surabaya  Menggambar
        3  Deni    24  Semarang     Menari
    
    Pada contoh di atas, kita membuat DataFrame dari dictionary dan menampilkannya ke layar. DataFrame merupakan struktur data utama dalam pandas yang mirip seperti tabel atau spreadsheet. DataFrame merupakan struktur dua dimensi yang menyimpan data dalam bentuk baris dan kolom.
'''

'''
    2.  NumPy
        Library NumPy adalah package fundamental yang sering digunakan untuk scientific computing pada Python. Library ini menyediakan objek array multidimensi, berbagai jenis objek lainnya, seperti masked array dan matrix, dan sebagainya.

        NumPy termasuk library eksternal, meskipun NumPy juga sudah terinstal secara otomatis pada beberapa IDE dan versi Python, perlu diingat bahwa NumPy bukan termasuk library bawaan Python. Oleh karena itu, Anda harus menginstal library ini terlebih dahulu sebelum dapat menggunakannya.

        Silakan buka command prompt dan jalankan kode berikut.

            pip install numpy
        
        Atau jika Anda ingin menggunakan conda, silakan jalankan kode berikut untuk menginstalnya.
        
            conda install numpy

        Setelah berhasil diinstal, Anda dapat mengimpor library NumPy dengan menggunakan kode berikut.
'''

# Contoh Penerapan Library NumPy
print("~ 2. NumPy ~".center(50, "-"), "\n")
print("> Contoh Penerapan Library NumPy \n")

import numpy as np

# Membuat Array NumPy
arr = np.array([1, 2, 3, 4, 5])

print(arr, "\n")

# Membuat Array NumPy dengan Matriks
matriks = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f"Ini adalah contoh penggunaan Library Numpy dengan penggunaan untuk membuat matriks:\n{matriks} \n")

'''
Pada kode di atas kita membuat array NumPy dengan menggunakan np.array() dan menampilkannya ke layar. Array NumPy merupakan struktur data utama dalam NumPy yang mirip seperti list pada Python. Array NumPy merupakan struktur data satu dimensi yang menyimpan data dalam bentuk elemen-elemen yang sama. Selain itu, kita juga membuat matriks dengan menggunakan np.array() dan menampilkannya ke layar. Matriks merupakan struktur data dua dimensi yang menyimpan data dalam bentuk baris dan kolom.
'''

'''
    3.  Matplotlib
        Selanjutnya adalah matplotlibyang merupakan library untuk melakukan visualisasi data. Matplotlib termasuk jenis library eksternal sehingga Anda perlu melakukan instalasi matplotlib terlebih dahulu. Silakan jalankan kode berikut.
            python -m pip install -U matplotlib
        Anda bisa juga jalankan kode berikut jika ingin menggunakan conda.

            conda install matplotlib
        Berikut adalah contoh penerapan matplotlib.
'''

# Contoh Penerapan Library Matplotlib
print("~ 3. Matplotlib ~".center(50, "-"), "\n")
print("> Contoh Penerapan Library Matplotlib \n")

import matplotlib.pyplot as plt
 
# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
 
# Membuat plot garis
plt.plot(x, y)
 
# Menambahkan judul dan label sumbu
plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
 
# Menampilkan plot
plt.show()

'''
Pada kode di atas, kita akan membuat visualisasi berdasarkan data dari variabel x dan y. Hal pertama yang dilakukan adalah mengimpor library dengan menggunakan sintaks “import matplotlib.pyplot as plt".

Selanjutnya, ini adalah contoh sehingga kita perlu membuat variabel sebagai data yang akan digunakan. Di sini kita membuat variabel x dan y sebagai data yang akan divisualisasi.

Untuk membuat visualisasinya, kita menggunakan sintaks “plt.plot(x, y)” dengan argumennya adalah variabel x dan y. Lalu, kita menambahkan informasi tambahan seperti title, xlabel, dan ylabel. Terakhir, kita menampilkan visualisasi tersebut dengan sintaks “plt.show()”.
'''

