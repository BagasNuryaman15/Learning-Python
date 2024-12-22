print(" Python Interpreter ".center(150, ("=")))
'''
Python termasuk bahasa pemrograman yang mudah dimengerti oleh manusia karena sintaksnya yang mudah dipahami. Tahukah Anda bahwa proses komputer menjalankan kode yang Anda bangun tidak sesederhana Anda memahaminya? 

Kode dari program Python yang Anda bangun akan ditransformasi menjadi kode yang mudah dimengerti oleh mesin menggunakan program compiler atau interpreter. Compiler merupakan program yang akan menerjemahkan bahasa pemrograman menjadi bahasa mesin sebelum dijalankan dan menghasilkan output. Ini artinya program yang Anda bangun secara keseluruhan akan diubah terlebih dahulu semuanya menjadi bahasa mesin. 

    ==============================================================

    How Compiler Works :

    Sourcee Code  --> Compiler    --> Machine Code    --> Output.

    How Interpreter Works :

    Source Code   --> Interpreter --> Output

    ==============================================================

Hal berbeda terjadi pada interpreter, yang akan menerjemahkan bahasa Python satu per satu dan menghasilkan output secara langsung. Hal ini memungkinkan Anda untuk melihat hasil program segera setelah satu baris kode dieksekusi hingga selesai. Implementasi interpreter ada pada mode interaktif Python. Anda dapat menjalankan satu atau dua lebih baris kode secara langsung dan melihat hasilnya.

Python memiliki aturan yang membantu Anda untuk menulis kode dengan baik dan benar. Guido van Rossum selaku pembuat bahasa Python merasa bahwa kode lebih sering dibaca dibandingkan ditulis. Dengan membuat kode yang baik dan benar akan memudahkan Anda untuk memahami kode bahkan membantu interpreter atau compiler berjalan dengan baik. 
'''

print(" Block Of Code ".center(150, ("=")) + "\n")
'''
                                                        Block Code
Sebuah program Python dapat berupa pernyataan atau statement, bisa juga terdiri atas blok kode. Sebuah blok merujuk pada potongan kode program Python yang dijalankan sebagai satu unit. Kode blok dapat berupa modul, fungsi, kelas, control flow, dan sebagainya. Tenang! Anda akan mempelajari istilah-istilah tadi lebih dalam pada materi-materi selanjutnya.

Kode di bawah merupakan contoh implementasi dari blok kode. Kode ini merupakan penerapan materi perulangan. Anda akan mempelajari lebih detail pada materi "Control Flow".
'''

# Contoh Block Kode
print("> Contoh Block Kode"+ "\n")
for i in range(10):
    print(i)

"""
Output:
0
1
2
3
4
5
6
7
8
9

Kode di atas merupakan satu unit kode blok perulangan yang akan mencetak angka 0 hingga 9. Perhatikan bahwa kode perulangan di atas juga melakukan aksi sekuensial, yakni setiap kode akan dijalankan lalu diulangi hingga kondisi akhir terpenuhi. Mengapa memahami kode blok penting? Alasannya adalah Anda harus membuat kode yang mudah dimengerti oleh Anda dan orang lain sebagai seorang programmer. Selain itu, kode blok yang baik dan benar akan memudahkan interpreter atau compiler untuk berjalan dengan baik dan tidak menghasilkan error. 
"""

# Perhatikan dan jalankan kode di bawah ini.
print("\n" + " Indentation Error ".center(50, ("=")) + "\n")
print("> Contoh Indentation Error")
print('''
for i in range(10):
print(i)

Kode ini akan menghasilkan error karena kode "print(i)" tidak memiliki indentasi. Indentasi adalah sebuah kode yang digunakan untuk menentukan letak awal dan akhir sebuah blok kode. Dalam Python, indentasi digunakan untuk menentukan letak awal dan
''')

"""
Output:
IndentationError: expected an indented block

Kode blok di atas merupakan program yang sama dengan sebelumnya. Perbedaannya terletak pada indentasi kode blok tersebut. Program akan menghasilkan error karena interpreter akan menganggap bahwa kode "print(i)" merupakan bagian dari kode blok "for i in range(10)". Error dihasilkan karena harusnya terdapat indentasi (biasanya berupa empat spasi) sebelum kode "print(i)".

Python sangat memperhatikan indentasi karena hal tersebut tidak hanya membantu merapikan kode yang Anda bangun, tetapi juga menjelaskan satu kode blok secara utuh. Dengan indentasi, program akan mengetahui letak awal dan akhir sebuah blok kode. Ke depannya, Anda akan melihat sebuah fungsi, modul, dan kelas yang ada dalam Python juga dengan memperhatikan indentasi untuk menyatakan kode blok secara utuh.
"""


print(" Case-Sensitive ".center(50, ("=")), '\n')
''' 
                                                            Case-Sensitive

Python termasuk bahasa pemrograman case-sensitive. Ini artinya Python memperlakukan huruf besar dan kecil sebagai karakter yang berbeda dalam penamaan variabel, nama fungsi, atau penulisan kode secara umum.
'''

# Perhatikan kode di bawah ini untuk memahami maksud dari case-sensitive.
print("> Contoh Case-Sensitive", "\n")

teks = "Dicoding"
Teks = "Indonesia"

print(teks)
print(Teks)

"""
Output:
Dicoding
Indonesia

Pada program di atas, Anda membuat dua variabel dengan nama "teks" dan "Teks". Python akan menganggap bahwa variabel tersebut berbeda, walaupun bagi kita sebagai manusia, mereka memiliki arti yang sama.

Bahkan jika Anda menambahkan sintaks "print()" untuk menampilkan variabel "TEks" seperti di bawah ini. Hasilnya akan menampilkan pesan Error.
"""

print('''
teks = "Dicoding"
Teks = "Indonesia"

print(teks)
print(Teks)
print(TEks)

Output:
Dicoding
Indonesia
NameError: name 'TEks' is not defined
''')

# Hal ini disebabkan variabel "teks", "Teks", dan "TEks" dianggap sebagai variabel yang berbeda oleh Python.
