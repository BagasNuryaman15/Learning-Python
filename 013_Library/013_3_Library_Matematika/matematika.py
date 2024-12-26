print("\n")
print(" Library Matematika ".center(150, "="), "\n")
'''
                                                                    Library Matematika

Selanjutnya adalah library math yang termasuk salah satu modul bawaan Python dan menyediakan berbagai fungsi dan konstanta matematika. Anda hanya perlu melakukan impor untuk modul math. Berikut contoh penerapannya. 
'''
# Contoh penerapan library math
print("> Contoh Penerapan Library Math \n")

import math # Langkah yang paling awal ketika kita ingin memakai library atau modul adalah dengan mengimportnya

# Kita Akan gunakan math untuk Normalisasi Data Dan Transformasi Data
print("1. Penggunaan Math Untuk Normalisasi Data Dan Transformasi Data:\n")
data = [10, 100, 1000, 10000]
log_transformed = [math.log(x) for x in data]
print(f"Log Transformed Data: {log_transformed}\n")

# Kita Akan gunakan math untuk Menghitung Jarak Euclidean
print("2. Penggunaan Math Untuk Menghitung Jarak Euclidean:\n")
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]
euclidean_distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print(f"3. Euclidean Distance: {euclidean_distance}\n")

# Kita Akan gunakan math untuk Menghitung Faktorial
print("4. Penggunaan Math Untuk Menghitung Faktorial:\n")
n = 10
factorial = math.factorial(n)
print(f"Faktorial dari {n} adalah {factorial}\n")


'''
Ini hanya beberapa saja kalian bisa mengeksplorasi lebih banyak lagi dengan membaca dokumentasi resmi dari Python.
'''


