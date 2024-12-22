print(" One-Linear ".center(150, ("=")), "\n")
''' 
                                                                One-liner

Selain membangun kode berdasarkan bloknya, Anda juga dapat membuat sebuah kode hanya dalam satu baris saja atau berupa single statement. Konsep ini dikenal sebagai one-liner. 

One-liner merupakan gaya penulisan pada Python yang memungkinkan Anda untuk membuat sebuah kode hanya dalam satu baris. One-liner adalah salah satu keunggulan dalam Python yang susah untuk diimplementasikan bagi beberapa bahasa pemrograman lainnya.

Tujuan dari one-liner ini adalah membuat satu baris kode yang singkat dan jelas. Perlu diingat bahwa tidak semua kode blok dapat dijadikan one-liner, seperti deklarasi fungsi, modul, dan kelas. 
'''

# Perhatikan kode di bawah ini yang merupakan program untuk menukar dua variabel menggunakan cara yang umum dilakukan.

print("> Contoh One-liner Umum", "\n")
x = 1
y = 2

temp = x
x = y
y = temp

print("Setelah pertukaran: ", "\n")
print("x = ", x)
print("y =",  y)
print("=" * 20, "\n")

"""
Output:
Setelah pertukaran: 
x = 2
y = 1

Mari bedah kode tersebut.

    1. Anda menginisialisasi variabel x dengan nilai 1 dan variabel y dengan nilai 2. 
    2. Anda menginisialisasi variabel temp dengan nilainya adalah variabel x. Hal ini menyebabkan variabel temp memiliki nilai 1.
    3. Anda menginisialisasi variabel x dengan nilai baru, yakni variabel y. Hal ini menyebabkan nilai dari variabel x menjadi 2.
    4. Anda menginisialisasi variabel y dengan nilai baru, yakni variabel temp. Hal ini menyebabkan nilai dari variabel y menjadi 1.
    5. Proses penukaran variabel telah selesai. Selanjutnya, Anda menampilkan nilai pada variabel tersebut dengan sintaks "print()".

Mungkin Anda bertanya, mengapa variabel x dan y bisa berubah? Ingat konsep aksi sekuensial, program akan menjalankan kode tersebut baris per baris. Jadi, nilai dari variabel x dan y setelah inisialisasi pertama akan berubah karena pada sintaks berikutnya Anda menetapkan nilai baru pada variabel x dan y. Anda menggunakan variabel bantuan, yakni variabel "temp" untuk menyimpan nilai awal dari variabel x. 
"""

# Kode one-liner yang dapat memudahkan Anda untuk melakukan operasi menukar dua variabel ini? Berikut adalah kodenya.

print("> Contoh One-liner", "\n")
x = 1
y = 2

x, y = y, x    # One-liner
print(" x, y = y, x", '\n')

print('Setelah pertukaran: ')
print('x =', x)
print('y =', y)



"""
Output:
Setelah pertukaran: 
x = 2
y = 1

Kode di atas memiliki tujuan yang sama dengan kode sebelumnya, yakni menukar dua variabel. Namun, pada kode program di atas, Anda menggunakan teknik one-liner untuk melakukan operasi tersebut. 

    x, y = y, x
    x ---> y
    y ------> x

Pada kode di atas, Anda seolah-olah menginisialisasikan ulang variabel x dengan nilai variabel y di sebelah kanan. Anda juga menginisialisasikan ulang variabel y dengan nilai variabel x yang ada di sebelah kanan. Sederhana, bukan? Dengan menginisialisasikan ulang variabel masing-masing, nilai tersebut pada akhirnya bisa saling bertukar.
"""