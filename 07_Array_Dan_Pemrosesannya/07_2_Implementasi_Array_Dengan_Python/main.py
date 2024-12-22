print("\n")
print(" IMPLEMENTASI ARRAY DENGAN PYTHON ".center(150,('=')),"\n")
'''
                                                    Implementasi Array dengan Python

Dalam materi ini, Anda akan mempelajari bentuk-bentuk penerapan Array dengan Python. Pertama, kita akan membahas deklarasi array. Kedua, kita akan membahas cara mengakses elemen array.
'''

# ===================================================== 1. Mendeklarasikan Array ======================================================
'''
                                                            Mendeklarasi Array

Pada materi sebelumnya, sudah disebutkan bahwa dalam Python kita dapat mendeklarasikan array menggunakan dua cara. Pertama dengan memanfaatkan list dan kedua menggunakan library Python.

Perlu Anda ingat, setiap elemen yang ada pada list sebetulnya disimpan pada satu memori. Jika list adalah "[1, 2, 3]", sebetulnya Anda memerintahkan memori komputer untuk menyimpan integer "1" ke dalam satu tempat memori, begitu pun integer "2" akan disimpan dalam satu tempat memori, dan seterusnya.

Perhatikan kode di bawah ini.
'''
print(" Contoh 1. : Mendeklarasikan Array(List) ".center(150, "-"), "\n")
print("> Contoh list akan menyimpan elemennya pada memory yang berbeda beda", "\n")
var_list = [1,2,3]
for elemen in var_list:
    show = id(elemen)
    print(f"Lihat memory nya = {show}")

'''
Ketika Anda menjalankan kode di atas, ia akan menghasilkan lokasi memori setiap elemen yang berada pada list. Lokasi tersebut bisa berubah jika Anda menjalankan ulang program, tetapi perhatikan bahwa semua elemen tersebut memiliki ID lokasi penyimpanan yang berbeda.

Sekarang mari lebih detailkan cara deklarasi array dalam Python menggunakan list. Ada dua cara untuk melakukan deklarasi array menggunakan list, yakni berikut.
'''


# ======================================================== 1. Mendefinisasikan Isi Array(List) =============================================
'''
                                                                Mendefinisikan Isi Array(List)

Cara pertama adalah dengan mendeklarasikan variabel array sekaligus mendefinisikan isi array. Cara ini dilakukan jika kita sudah tahu nilai yang perlu diberikan. 

Berikut adalah struktur mendeklarasikan variabel array dengan mendefinisikan isi array secara langsung.

    <nama_var> = [elemen1, elemen2, elemen3, ..., elemenn]
                    0         1        2            n-1

<nama-var> merupakan nama variabel array yang dideklarasikan sebanyak n dengan elemen-elemennya adalah <val0>, <val1>, <val2>, … , <valn-1>. Perlu diingat bahwa elemen tersebut terurut berdasarkan indeks dari 0 hingga n-1. 

Contohnya sebagai berikut.
'''                       
print("\n")
print(" Contoh 1. :  Mendefinisasikan Isi Array(List) ".center(70, "-"), "\n")
print("> Contoh Indeks dalam list", "\n")

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr, "\n")

"""
Output:
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

Pada variabel "var_arr" kita menyimpan elemen bertipe integer dengan panjangnya adalah 10 elemen dan alamat setiap elemen array (indeks) adalah indeks ke-0 hingga 9.
"""



# ======================================================== 2. Mendefinisasikan Nilai Default =============================================
'''
                                                                Mendefinisikan Nilai Default

Jika tidak mengetahui nilai yang diberikan, kita dapat memberikan nilai default terlebih dahulu sebagai upaya untuk memberikan nilai awal. Umumnya, nilai default ini ditentukan karena kita tidak tahu nilai seharusnya. 

Dalam prosesnya, kita bisa secara perlahan mengganti masing-masing nilai tersebut sesuai kebutuhan. Misal kita memiliki array "[0,0,0,0]", yang kemudian hari kita bisa memperbaruinya menjadi "[1,2,0,4]", dengan begitu kita bisa mengetahui bahwa indeks ke-2 pada array tersebut belum kita perbarui. 

Nilai default ditentukan oleh kesepakatan bersama sesuai kebutuhan yang nilainya di luar dari rentang yang disepakati. Misalnya, tim Anda menentukan nilai dalam list harus berkisar dari 1 hingga 10. Kita bisa menyepakati "0" sebagai nilai default karena di luar jangkauan yang disepakati (1-10).

Berikut adalah struktur mendeklarasikan variabel array dengan mendefinisikan nilai default.   

    <nama_var> = [<nilai_default> for in range(<n>)]

Jika Anda merasa familier dengan struktur tersebut, Anda benar. Struktur tersebut merupakan struktur yang sama dengan list comprehension. Anda dapat menginisialisasi variabel array dengan menggunakan list comprehension dan mendefinisikan nilai default. Pada materi List Comprehension, kita menggunakan ekspresi Namun, pada array kita menggunakan default value atau <default-val>.

Berikut adalah penjelasan lebih detail terkait struktur tersebut.

    1. <nama-var> merupakan variabel yang Anda deklarasikan.
    2. <default-val> merupakan nilai default yang Anda definisikan. Umumnya, programmer akan menggunakan nilai di luar range yang telah disepakati sebagai nilai default. Misalnya jika range nilai yang disepakati seharusnya 1 hingga 10, nilai default bisa kita definisikan dengan 0. 
    3. <n> merupakan ukuran panjangnya array.

Mari lihat contoh penerapannya di bawah ini. 
'''

# Contoh penerpan nilai default
print(" Contoh 2. : Mendefinisikan Nilai Default ".center(70, "-"), "\n")
print("> Contoh Penerapan nilai default", "\n")

# Contoh
var_angka = [0 for num in range (50)]
print(var_angka, "\n")

'''
Output: 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Pada contoh di atas, kita membuat list dengan nilai default-nya adalah "0" sebanyak 50 elemen. Perhatikan bahwa <default-val> yang ada pada struktur sebelumnya diubah menjadi "0" untuk mendapatkan nilai default "0".

Dari sini, Anda dapat mengubah nilai default tersebut dengan nilai yang baru berdasarkan hasil suatu operasi. Misalkan pada contoh di bawah ini.
'''
# Mengubah nilai default dengan nilai baru
print("> Mengubah nilai default menjadi nilai baru", "\n")

# Contoh
var_angka = [0 for num in range (50)]

for i in range(26):
    var_angka[i] = i

print(var_angka, "\n")

'''
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Pada contoh di atas, kita membuat program untuk mengubah nilai default pada variabel array "var_arr" dengan nilai 0 hingga 26. Output dari program tersebut adalah mengubah nilai yang awalnya adalah [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] menjadi seperti output di atas. Oh iya jika ada yang kebingungan mengapa variable num tidak bisa digunakan, itu karena scope dari variable num hanya berlaku pada looping for. Apa itu scope? Scope adalah sebuah konsep yang digunakan untuk menentukan lokasi dimana sebuah variable dapat diakses. Scope dapat berupa global atau local. Global scope adalah scope yang dapat diakses di mana saja di program, sedangkan local scope adalah scope yang hanya dapat diakses di dalam suatu blok kode. Jadi jika di analogikan dengan contoh di kehidupan sehari hari itu seperti ini. 

    Analogikan var_angka sebagai rumah dan num sebagai kamar. Karena num hanya bisa diakses di dalam looping for maka num hanya bisa diakses di dalam kamar rumah itu. Nah pada program di atas num digantikan menjadi i, ini seperti kita memiliki kamar baru di rumah yang sama dan memakai kamar baru untuk kita gunakan.
'''




# ======================================================== 3. Mengakses ELemen Array(list) ===============================================
'''
                                                              Mengakses ELemen Array(list) 

Mengakses elemen array dalam Python tidak berbeda dengan mengakses elemen pada list. Hal ini karena kita menggunakan list sebagai "bentuk lain" dari array. Anda dapat melakukan metode indexing untuk mengakses elemen array. Berikut adalah struktur untuk melakukan hal tersebut.

    <nama_var>[<index>]

Berikut adalah penjelasan lebih detail terkait struktur tersebut.

    1. <nama-var> merupakan variabel yang Anda deklarasikan.
    2. <index> merupakan indeks dari elemen yang ingin Anda akses.

<namaVariabelArray> merupakan nama variabel array yang sebelumnya telah Anda deklarasikan. <indeks> merupakan urutan indeks yang ingin Anda akses sehingga nilai atau elemen tersebut dapat diambil atau ditampilkan.

Mari lihat contoh penerapannya di bawah ini.
'''

# Contoh penerapan mengakses elemen array(list)
print(" Contoh 3. : Mengakses Elemen Array ".center(70, "-"), "\n")
print("> Contoh Penerapan mengakses elemen array", "\n")

var_angka = [0 for num in range (50)]

for i in range(26):
    var_angka[i] = i
    contohAkses = var_angka[15]

print(f"Nilai yang diambil adalah {contohAkses}")

'''
Output:
15

Pada kode di atas, kita menggunakan perulangan for untuk mengisi elemen array dengan nilai 0 hingga 26. Setelah itu, kita mengakses elemen array pada indeks ke-15 dan menampilkannya. Dan kita mengambil indeks ke-15 pada variabel "var_arr" yang bernilai 15. Jadi, output yang dihasilkan adalah 15. Mengapa tidak 14 bang? Karena indeks dimulai dari 0 dan var_angka juga dimulai dari 0.
'''

    


