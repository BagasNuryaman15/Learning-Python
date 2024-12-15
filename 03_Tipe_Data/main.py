# ======================================================= Data Typing =======================================
""" 

Sebelum kita mendalami apa itu Tipe Data kita harus mengenali apa itu Data Typing. Data Typing adalah pemahaman kita memahami bahwa komputer perlu mengetahui data yang diinginkan dengan cara melakukan deklarasi. Sebelum memahami berbagai tipe data yang umum digunakan dalam Python, kita harus mengenal terlebih dahulu cara menuliskan data dalam pemrograman.

"""

# ======================================================= Deklarasi dan Inisialisasi =======================================

""" 
Deklarasi merujuk pada pembuatan variabel dengan menentukan tipe data dan nama variabelnya. Umumnya, ini dilakukan oleh bahasa pemrograman lainnya, seperti C/C++. Contohnya berikut.

int x;
float y; : X dan Y disini adalah variable.

Sementara inisialisasi merujuk kepada pemberian nilai awal pada variabel yang sebelumnya telah dideklarasikan. Berikut contohnya jika menggunakan bahasa pemrograman C/C++.

int (name of variable) = value;
float (name of variable) = value; 

Jadi disini kita harus menentukan terlebih dahulu tipe data apa yang akan dipakai. Pada contoh kali ini kita menggunakan tipe data int untuk menyimpan nilai integer dan tipe data float untuk menyimpan nilai desimal. Misalkan jika kamu ingin membuat sebuah kalimat atau karakter maka kamu harus mendeklarasikan tipe data string terlebih dahulu.

str (kata_kata_hari_ini) = "Paham";

Kedua proses tersebut wajib dilakukan dalam bahasa pemrograman lain, seperti C. Beruntungnya Anda, Python tidak mengharuskan Kita untuk melakukan deklarasi tipe data variabel. Hal ini disebabkan Python merupakan bahasa pemrograman yang menerapkan loosely typed. Artinya, Kita tidak perlu mendeklarasikan tipe data variabel secara eksplisit.

Kode C sebelumnya jika diubah ke dalam Python akan menjadi seperti berikut.

kata_kata_hari_ini = "Paham"
angka = 100

Python juga merupakan bahasa pemrograman yang menerapkan dynamic typing. Artinya, Python adalah bahasa pemrograman yang hanya mengetahui tipe variabel saat program berjalan dan melakukan proses assignment. Hal ini memungkinkan kita untuk mengubah tipe data dari suatu variabel seiring berjalannya program.

"""

# Contohnya 
print ("=Ini Adalah Contoh Awal")

a = 6
print (type(a))

a = "6"
print (type(a))

# Pada kode di atas, variabel yang digunakan sama-sama bernama “a”, tetapi yang pertama “a” bertipe integer, sedangkan yang kedua bertipe string. 

# -----------------------------------------------------Tipe Data-----------------------------------------------
"""

Tipe Data adalah jenis informasi yang dapat di simpan kedalam variable.  Tipe data adalah cara Python mengklasifikasikan data yang kita gunakan dalam program. Tipe data menentukan jenis nilai yang dapat disimpan dalam variabel, serta bagaimana Python memproses data tersebut. Di Python, ada beberapa tipe data dasar yang sering digunakan dalam berbagai aplikasi, termasuk dalam pengembangan AI dan Machine Learning. Sebagaimana yang telah dijelaskan bahwa setiap nilai yang digunakan dalam variabel adalah sebuah data. Data sendiri memiliki tipe yang berbeda-beda, kita dapat menemuinya dalam kehidupan sehari-hari. Simak kisah berikut untuk memahami data dalam kehidupan sehari-hari.

    “Seorang pria berumur 30 tahun menjalani kehidupan di ibu kota Jakarta. Pria tersebut bernama Evans dan memiliki berat badan sebesar 75 kg. Suatu hari, Evans harus pergi ke kantor, tetapi hujan deras melanda kota tersebut. Evans pun memutuskan untuk menunggu selama 30 menit sebelum akhirnya berangkat kerja. Jika setelah 30 menit hujan tak kunjung reda, ia akan memakai jas hujan. Namun, jika hujan reda, ia tidak akan memakai jas hujan.”

Sekarang, mari kita bedah data yang dapat diambil dan diimplementasikan dengan pemrograman. Beberapa data tersebut antara lain berikut.

1. Umur
    Data umur dibentuk dari kumpulan angka. Dalam pemrograman, tipe data ini adalah numbers yang memiliki berbagai jenis. Perlu Anda ingat bahwa data umur tentu memiliki rentang, misalnya 1 sampai 100, bila kita asumsikan bahwa umur seseorang tidak lebih dari 100.

2. Nama
    Data nama dibentuk dari serangkaian huruf. Dalam pemrograman, tipe data ini adalah string. Perlu diketahui juga bahwa data nama memiliki rentang jumlah huruf. Rentang data nama adalah 1 sampai 50 huruf, bila kita asumsikan bahwa tidak ada nama yang melebihi 50 huruf. 

3. Berat Badan
    Data berat badan dibentuk dari kumpulan angka, sama seperti data umur.

4. Keputusan Memakai Jas Hujan
    Keputusan memakai jas hujan juga merupakan data. Dalam pemrograman, ini adalah data boolean yang merupakan tipe data dengan hanya dua kemungkinan, yakni True dan False. Dalam kisah di atas, keputusan Evans hanya ada dua, yakni jika hujan benar-benar terjadi (bernilai True), ia akan memakai jas hujan, sedangkan jika hujan tidak terjadi (bernilai False), ia tidak akan memakai jas hujan.

5. Waktu 
    Data waktu dibentuk dari kumpulan angka. Dalam pemrograman, tipe data ini adalah numbers yang memiliki berbagai jenis. Perlu Anda ingat bahwa data waktu tentu memiliki rentang, misalnya 1 sampai 100, bila kita asumsikan bahwa waktu yang dapat diambil dari Evans hanya 30 menit.

Sekarang mari kita fokus terhadap berbagai tipe data pada Python. Dalam Python, tipe data dikelompokkan menjadi dua, yakni tipe data primitif dan tipe data collection.

"""

# ============================================================ Tipe Data Primitif ===================================
print("Tipe Data Primitif".center(150))
# Tipe data primitif merupakan jenis paling dasar dalam pemrograman. Tipe data ini menyimpan single value. Berikut adalah berbagai tipe data primitif.


#  ------------------------------------------------------- 1. Numbers ---------------------------------------------------
"""

1. Numbers
    a. Integer 
    b. Float
    c. Complex

a. Integer (int)
    Tipe data integer adalah tipe data yang menyimpan bilangan bulat. Bilangan bulat adalah bilangan yang tidak memiliki pecahan atau desimal. 
    Contoh bilangan bulat adalah 1, 2, 3, 4, 5, dan seterusnya. Tipe data Integer juga bisa berupa positif atau negatif asal tidak memiliki angka desimal.
    Contoh: 1, -20, 999, dan 0.

b. Float (float)
    Tipe data float adalah Bilangan riil yang dapat mewakili bilangan bulat atau bilangan desimal. 
    Contoh: 3.14; 1; dan 4.01E+1

c. Complex (complex)
    Tipe data complex adalah bilangan kompleks yang terdiri dari dua bagian, yakni real dan imaginer.
    Contoh: 1+2j; 2+3j; 4+5j; dan 6+7j. Tetapi kita tidak akan menggunakannya terlebih dahulu.

Tipe data primitif pertama, yakni numbers adalah tipe data angka berupa bilangan bulat, riil, dan kompleks.

Tipe data integer merupakan bilangan bulat positif atau negatif dan tidak memiliki angka desimal. Selanjutnya, tipe data float merupakan bilangan riil yang mewakili bilangan bulat dan angka desimal. Terakhir, tipe data complex yang merupakan representasi dari bilangan kompleks dalam matematika. Tipe data complex terdiri dari bilangan riil dan imajiner dengan bentuk “x +yj”, yaitu “x” adalah bilangan riil dan “y” adalah bilangan imajiner. 

Ciri dari bilangan numbers adalah Anda dapat mengoperasikan bilangan tersebut dengan operasi matematika sederhana, seperti: 
Pertambahan (+) 
Pengurangan (-)
Perkalian (*) dan operasi matematika lainnya.

"""

# Implementasi data number ke dalam Python
print("=Implementasi data number ke dalam Python")
# Implementasi data integer ke dalam Python
print(">Implementasi data integer ke dalam Python")

a = 10
print(a)
print(type(a))

# Implementasi data float ke dalam Python
print(">Implementasi data float ke dalam Python")

b = 10.5
print(b)
print(type(b))

# Implementasi data complex ke dalam Python
print(">Implementasi data complex ke dalam Python")

c = 10+5j
print(c)
print(type(c))

# Perlu diperhatikan bahwa tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah. Mari lihat contoh di bawah ini.
print(">Perlu diperhatikan bahwa tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah.")

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

"""

Pada contoh di atas, kita berusaha untuk melakukan perubahan tipe data numbers dengan melakukan inisialisasi ulang variabel. Namun, ternyata hal tersebut bukan merupakan proses mengubah nilai variabel. Proses tersebut lebih bisa disebut sebagai membuat objek baru dengan nilai baru. Masih ingat dengan arti dari variabel? Variabel merujuk pada lokasi dalam komputer yang digunakan untuk menyimpan nilai dengan tipe data tertentu.

Ketika menjalankan program di atas, Anda juga dapat melihat alamat memori (memory address) dari variabel “var” yang pertama dan yang kedua menggunakan fungsi “id()”. Jalankan berulang kode di atas dan Anda dapat melihat bahwa alamat tersebut berubah-ubah dengan nilai yang berbeda.

Hal ini membuktikan secara natural bahwa integer atau numbers merupakan immutable. Alih-alih nilai integer di atas diperbarui, ternyata nilai tersebut masih bernilai sama karena kita masih bisa menampilkannya dengan nama variabel yang identik. 

Sebenarnya, semua tipe data primitif atau single-value (numbers, boolean, string) sudah dapat dipastikan adalah immutable secara natural. Banyak programmer beranggapan bahwa dengan melakukan inisialisasi ulang variabel pada Python dapat memperbarui atau mengubah nilai tersebut. Nyatanya, tindakan tersebut menyebabkan program membuat objek baru dengan nilai baru alih-alih mengubahnya. 

"""

#  ------------------------------------------------------- 2. Boolean ---------------------------------------------------
"""
2. Boolean
    True : bernilai benar
    False : bernilai salah

Tipe data primitif kedua adalah boolean, yakni tipe data yang hanya bernilai TRUE atau FALSE. Tipe data ini merepresentasikan nilai kebenaran (truth values). Sebenarnya, setiap variabel yang memiliki nilai bisa dievaluasi dan menghasilkan nilai true. Hanya ada beberapa nilai yang akan dianggap bernilai false sebagai berikut.

    1. Nilai yang sudah didefinisikan bernilai salah: None dan False.
    2. Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
    3. Urutan (sequence) dan koleksi (collection) yang kosong: “”, (), {}, set(), range(0). 

Selain itu, tipe data boolean juga memiliki fungsi yang berguna untuk memeriksa nilai kebenaran. Fungsi tersebut adalah fungsi bool(). Fungsi ini akan mengembalikan nilai True jika nilai yang diberikan bernilai benar, dan mengembalikan nilai False jika nilai yang diberikan bernilai salah. 

"""

# Implementasi data boolean ke dalam Python
print("=Implementasi data boolean ke dalam Python")
x = True
print(type(x))

x = False
print(type(x))

'''
Output:
<class 'bool'>
<class 'bool'>

Dari kode di atas dapat Anda pahami bahwa nilai True dan False merupakan data bertipe boolean. 
'''

#  ------------------------------------------------------- 3. String (str) ---------------------------------------------------
"""

3. String
    String merupakan karakter yang berurutan. Ketika Anda membuat variabel bernilai string tentu diawali dengan single quote atau double quote (“”). Jalankan kode di bawah ini untuk mengetahui contoh tipe data string.

"""

# Implementasi data string ke dalam Python
print("=Implementasi data string ke dalam Python")
x = "Dicoding"
print(type(x))

"""
Output: 
<class 'str'>

Variabel x yang menyimpan teks “Dicoding” adalah variabel dengan data bertipe string. Sederhananya, teks “Dicoding” tersebut adalah string. 
"""

# Fakta Menarik tentang string adalah

# 1. kita dapat menggunakan tiga single quote atau double quote untuk menyimpan string yang lebih dari satu baris (multi-line).

# contohnya 
print(">Multi Line String")

kata = """Helo Semuanya Saya Jajang
Saha maneh jajang eweuh nu nanya ge
Abiteh jajang kade kade we ah bisi kacentang"""

print(kata)
print(type(kata))

# Pada kode di atas, Anda menampilkan string lebih dari satu baris (multi-line) menggunakan double quote (”””).

# 2. String merupakan urutan karakter yang setiap karakternya memiliki indeks. Anda dapat mengakses setiap karakter dari string (substring) dengan menggunakan metode indexing. Perlu diingat bahwa indeks selalu dimulai dari 0. Ini sudah di jelaskan oleh saya dibawah di Tipe Data String.

# 3. String merupakan immutable. Artinya, tipe data string bersifat immutable. Hal ini berarti Anda tidak dapat mengubah nilai string. Mari kita lihat contoh di bawah ini.

# contoh
print(">String merupakan immutable")

# x = "Dicoding"
# x[0] = "F"

""" 
Output:
TypeError: 'str' object does not support item assignment

Pada kode di atas, diambil indeks ke-0 dari string “Dicoding”, yakni huruf “D” dan digantikan dengan huruf “F”. Namun, kode tersebut menghasilkan error dikarenakan string bersifat immutable yang artinya tidak dapat diubah.

"""

# 4. Dapat mengakses beberapa substring dengan menggunakan metode indexing dan slicing. Ini sama sudah saya jelaskan pada text dibawah


# 5. Ini yang paling menarik karena kita dapat menampilkan teks/string berdasarkan input dari pengguna dengan berbagai cara. Perhatikan metode di bawah ini dan jalankan kodenya menggunakan IDE atau notebook.

# A. Formatted String

# contoh
print("> Formatted String")

nama = "Jajang Juntang"
umur = 20
tinggi = 170.5

print(f"Nama saya {nama} umur saya {umur} tahun dan tinggi saya {tinggi} cm")

""" 
Pada kode di atas, Anda menampilkan string dengan menggunakan metode formatted string. Metode ini diperuntukkan untuk menampilkan variabel bertipe string dengan   menggunakan huruf “f” di depan string dan menempatkan variabel di dalam kurung kurawal.
"""

# Output: Nama saya Jajang Juntang, umur saya 20 tahun dan tinggi saya 170.5 cm

# B. %-Formatted

# contoh
print("> Formatted")

nama = "Dadang Fly"
timggal = "Saya tinggal di Kp. Durian Runtuh"
umur = 43 
tinggi = 200.5

print("Nama saya %s, %s umur saya %d tahun dan tinggi saya %.1f cm" % (nama, timggal, umur, tinggi))

# Output: Nama saya Dadang Fly, Saya tinggal di Kp. Durian Runtuh umur saya 43 tahun dan tinggi saya 200.5 cm
""" 
Pada kode di atas, Anda menampilkan variabel string dengan menggunakan metode “%-formatting”. Metode ini adalah pendekatan lama yang masih didukung oleh Python. Metode ini menggunakan operator Modulo (%) untuk memasukkan nilai variabel ke dalam string dengan menggunakan format khusus yang ditentukan oleh tipe data variabel.
"""

# C. Str.Format()

# contoh
print("> Str.Format()")

nama = "Yanto Bacok"
timggal = "Saya tinggal di Kp. Jeger"
umur = 30
tinggi = 130.5

print("Nama saya {}, saya tinggal {} umur saya {} tahun dan tinggi saya {} cm".format(nama, timggal, umur, tinggi))

# Output: Nama saya Yanto Bacok, Saya tinggal di Kp. Jeger umur saya 30 tahun dan tinggi saya 130.5 cm

""" 
Pada kode di atas, Anda menampilkan variabel string dengan menggunakan metode “str.format()”. Metode ini memungkinkan penggabungan variabel/nilai ke dalam string dengan menempatkan tanda kurung kurawal atau {} sebagai penempatan variabel. Sekilas mirip dengan formatted string, pembedanya adalah pada penggunaan “.format” setelah string.
"""

# ============================================================ Tipe Data Collection ===================================
""" 
Tipe data collection merupakan tipe data yang menyimpan satu atau lebih data primitif sebagai satu kelompok. Dalam Python, berikut yang termasuk tipe data collection.
"""

#  ------------------------------------------------------- 1. List ---------------------------------------------------
"""

1. List
    List merupakan jenis kumpulan data terurut (ordered sequence) dan salah satu tipe data yang sering digunakan pada Python. List dalam Python ini serupa, tetapi tak sama dengan array pada bahasa pemrograman lainnya. List Python tidak mengharuskan memiliki tipe data yang sama di dalamnya, sedangkan array sebaliknya. 

    Jika di Python kamu bisa mengelompokan tipe data apapun menggunakan list[].

    contoh : variable_list = [1(int), "hahai dedeuh"(string), True(bool), 1.2(float)]

    Jika di Kode Java kamu harus mengelompokan tipe data apapun menggunakan array[] tetepi tidak bisa semuanya kamu masukan contoh.

    contoh : int[] variable_array = {1, "hahai dedeuh", True, 1.2} nah kita tidak bisa melakukan hal ini karena tipe data yang kita masukan tidak sama. hal yang bisa kita lakukan adalah

    contoh : int[] variable_array = {1, 2, 3, 4, 5}


Melakukan inisialisasi list pada Python cukup mudah, yakni menggunakan kurung siku “[]” dan setiap elemennya dipisahkan dengan koma. Berikut adalah implementasi list pada Python.

"""

# contoh
print("> Contoh Implementasi List")

list_mix = [ 100, "Bagas Ganteng", False, 100.25]
print (type(list_mix))

print(f"Hasil Dari List Mix : {list_mix}," "Tetapi kita bisa tau bahwa Tipe Datanya adalah : <list>")

# Pada kode di atas, nilai yang diawali dengan kurung siku “[]” akan dianggap sebagai data bertipe list.

""" 
Setiap data atau elemen dalam list memiliki indeks yang selalu dimulai dari 0. Anda dapat mengakses setiap indeks pada list dengan metode indexing. 
    Contohnya : mix = [100 (indeks 0), “Bagas Ganteng” (indeks 1), False (indeks 2), 100.25 (indeks 3)]
"""

# contoh
print("> Contoh Akses List Untuk Mendapatkan Nilainya")
list_mix = [ 100, "Bagas Ganteng", False, 100.25]

print(list_mix[1])

# Output: Bagas Ganteng

""" 
Pada kode di atas, diambil indeks ke-1 dari list yang telah diinisialisasikan. Mungkin kita sadar bahwa cara tersebut sama persis dengan mengakses substring pada materi string. Hal ini karena string pada Python merupakan urutan karakter yang setiap karakternya memiliki indeks. Persis seperti list yang setiap datanya juga memiliki indeks. Kenapa memilih indeks 1 karena bagas ganteng.
"""

# List Python bersifat mutable yang artinya nilai di dalamnya dapat diubah.

# contoh
print("> Contoh Mengubah Nilai List")
list_mix = [ 100, "Bagas Ganteng", False, 100.25]

list_mix[0] = "Nanad Mirip Dugong"
print(list_mix)

# Pada kode di atas, Anda mengubah “100” dengan string “Nanad Mirip Dugong”. Hal ini dapat terjadi dalam Python karena list bersifat mutable.



# ------------------------------- Konsep Indexing -------------------------
# Konsep indexing merujuk kepada pengambilan data dalam Python berdasarkan indeksnya. Beberapa cara untuk melakukan indexing sebagai berikut.

# Contoh Dasar Indexing
print("> Contoh Dasar Indexing")
list_mix = [ "Aku", "apa", "mereun", "kasep", "kece", "mantap!", "bagas", "ganteng"]

print(list_mix[0])
print(list_mix[6])
print(list_mix[4])
print(list_mix[-1])
print(list_mix[-3])

# Output: 
# Aku 
# bagas 
# ganteng 
# kece 
# mantap

# Gabungin yu biar kece
print("Penggabungan Biar Menghasilkan sesuatu yang mantap")

result = " ".join([list_mix[0], list_mix[6], list_mix[4], list_mix[-1], list_mix[-3]])
print(result)

# Output: Aku bagas kece mantap!



# ---------------------------------------- Konsep SLicing ------------------------------
""" 
Adapun konsep slicing merujuk pada pengambilan data berdasarkan indeks dari rentang tertentu. Slicing pada Python mengikuti pola sebagai berikut.

    list_mix[start:stop:step]

    start : indeks dimulai dari 0.
    stop : indeks berhenti di sebelum indeks tersebut.
    step : jarak antara indeks yang dipilih.

    Start merupakan indeks pertama yang Kita ambil. Stop merupakan indeks terakhir yang ingin Kita ambil. Step merupakan jumlah elemen yang ingin Kita lewati di antara setiap elemen slice. Secara default, nilai step adalah 1.

    Hal penting yang harus Kita ingat adalah nilai start bersifat inklusif sedangkan stop bersifat eksklusif. Masih ingat dengan konsep tersebut dalam matematika? Konsep ini menggambarkan batas tertentu dalam suatu interval. Jika suatu interval dikatakan inklusif, batas terakhir yang telah ditentukan akan dianggap sebagai bagian dari interval. 

    a >= b

    Namun, jika suatu interval dikatakan eksklusif, batas terakhir yang telah ditentukan tidak akan dianggap sebagai bagian dari interval.

    a > b

    berikut adalah contoh penggunaan slicing pada list.
"""

# contoh
print("> Contoh Slicing")
list_mix = [ "Aku", "apa", "mereun", "kasep", "kece", "mantap", "bagas", "ganteng"]

print(list_mix[2:])
print(list_mix[:3])
print(list_mix[0:6:2])
print(list_mix[0:4:4])

# Outputna mah tinggal we nyalira nya



#  ------------------------------------------------------- 2. Tuple ---------------------------------------------------

"""

2. Tuple
    Tuple adalah jenis dari list yang tidak dapat diubah elemennya. Umumnya, tuple digunakan untuk data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat. Tuple didefinisikan dengan kurung “()“ dan setiap elemen di dalamnya dipisahkan dengan koma.

"""

# contoh
print("> Contoh Implementasi Tuple")

tuple_mix = ( 100, "Bagas Ganteng", False, 100.25)
print (type(tuple_mix))

print(f"Hasil Dari Tuple Mix : {tuple_mix},", "Bertipe : ",type(tuple_mix))

# Pada kode di atas, Kita dapat lihat bahwa nilai yang diapit tanda kurung “()” akan dianggap sebagai tuple oleh program. Anda juga dapat melakukan indexing dan slicing pada tuple sama seperti list. 

# Tetapi bedanya tuple dengan list adalah tuple bersifat immutable. Artinya, nilai di dalamnya tidak dapat diubah. Tetapi list berubah atau mutable.

# contoh
print("> Contoh Mengubah Nilai Tuple Pasti Akan Terjadi Error")
tuple_mix = ( 100, "Bagas Ganteng", False, 100.25)

# tuple_mix[2] = "Bagas Jelek"
# print(tuple_mix)

# Outputny : TypeError: 'tuple' object does not support item assignment 

""" 
Mengapa itu bisa  terjadi?
Karena  Bagas Memang Ganteng Tidak Jelek hahaha. Bercanda geng! Ya karena tuple itu pada dasarnya bersifat imutabel, yang tidak akan bisa di rubah sampai 200 tahun pun. Tetapi gak tau yah gimana Guido Van Rossum Mengizinkan Bagas Jelek.
"""


#  ------------------------------------------------------- 3. Set ---------------------------------------------------

"""

3. Set
    Set adalah jenis data yang tidak memiliki urutan dan tidak memiliki elemen yang sama.Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection), dan dapat diinisialisasikan dengan kurawal “{}” di mana setiap elemennya dipisahkan dengan koma. Tidak sama seperti list, dalam set kita tidak bisa melakukan indeksing karena set tidak memiliki indeks. Hal ini merujuk pada definisi nya yang menyatakan bahwa set merupakan kumpulan item tanpa urutan. Perhatikan kode di bawah ini.

"""

# contoh
# print("> Contoh Jika Kita Ingin Mengubah Set Pasti Akan Error")

# set_mix = { 100, "Bagas Ganteng", False, 100.25}
# print(set_mix[2])

# Outputnya : TypeError: 'set' object is not subscriptable

# Pada kode di atas, program mengembalikan output 'set' object is not subscriptable karena setiap nilai dalam set tidak memiliki indeks sehingga tidak bisa dilakukan indexing.

""" 
Selain tanpa urutan (unordered collection). Set juga bersifat unik, artinya, data yang Anda simpan pada set tidak akan ada duplikat. Anda dapat memanfaatkan hal ini untuk menghilangkan duplikat pada suatu data.

    contoh : set_int = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    maka jika kalian perintahkan fungsi print(set_int) maka akan menghasilkan {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, karena set dapat menghilangkan duplikat.

"""

# contoh
print("> Contoh Pembuktian Bahwa Set Dapat Menghilangkan Duplikat")

set_int = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set_int)

# Outputnya : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} Pada kode di atas, kita dapat melihat bahwa nilai yang diapit tanda kurawal “{}” akan dianggap sebagai set oleh program dan nilai duplikat di dalamnya akan dihapus. Pada kode di atas pun, nilai 1 sampai 10 yang duplikat telah dihapus. 

""" 
Terakhir, set adalah himpunan dalam matematika. Ini maknanya Anda dapat melakukan operasi union (gabungan) dan intersection (irisan) pada set. Python menyediakan method “.union()” dan “.intersection()” untuk tipe data set.

Method merupakan tindakan atau operasi yang dapat dilakukan oleh suatu objek. Saat ini, tidak apa-apa jika kamu belum memahami sepenuhnya. Anda akan mempelajari lebih detail mengenai method pada modul Object-Oriented Programming (OOP). Perhatikan contoh di bawah ini.
"""

# contoh
print("> Contoh Pembuktian Bahwa Set Dapat Melakukan Operasi Union dan Intersection")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}

Pada contoh di atas, kita melakukan operasi union atau penggabungan dua variabel bertipe data set, yakni variabel set1 dan variabel set2 dengan menggunakan method “.union()”. Hasilnya adalah tentu nilai gabungan dari kedua variabel. 

Terakhir, kita juga melakukan intersection atau irisan yang merupakan operasi dalam matematika untuk menemukan nilai atau elemen-elemen yang sama dalam dua atau lebih himpunan. Kita menggunakan method “.intersection()” untuk menjalankan operasi ini. Hasilnya adalah nilai 4 dan 5 yang memang berada pada variabel set1 dan variabel set2.
"""

#  ------------------------------------------------------- 4. Dictionary (dict) ---------------------------------------------------

"""

4. Dictionary
   Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan. Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. Pada Python, dictionary didefinisikan dengan kurawal {} dan tambahan definisi berikut.

    1. Setiap elemen pasangan key-value dipisahkan dengan koma (,).
    2. Key dan value dipisahkan dengan titik dua (:).
    3. Key dan value dapat berupa tipe variabel/objek apa pun.
    4. Key dapat berupa string, integer, atau tuple.
    5. Key tidak boleh sama.

    Perhatikan contoh di bawah ini.
"""

# contoh
print("> Contoh Implementasi Dictionary")

example_dict = {"nama": "Bagas", "umur": 20, "alamat": "Bandung", 'kode_pos' : 'Bagas Ganteng', 'jujur' : True}
print(example_dict, "Bertipe :" , type(example_dict))

# outputnya : {'nama': 'Bagas', 'umur': 20, 'alamat': 'Bandung', 'kode_pos': 'Bagas Ganteng', 'jujur': True} Bertipe : <class 'dict'>
""" 
Pada kode di atas, sintaks yang diapit tanda kurawal “{}” dan memiliki pasangan key-value akan dianggap sebagai data bertipe dictionary oleh program.

Dalam mengambil setiap nilai/elemen pada dictionary, Kita harus mengetahui key (kunci) untuk mengakses setiap value-nya (nilai). Hal ini berbeda dengan tipe data sebelumnya yang cukup mengharuskan Kita untuk menyebutkan indeksnya saja. 

Perhatikan contoh di bawah ini.
"""

# contoh
print("> Contoh Implementasi Dictionary")

example_dict = {"nama": "Bagas", "umur": 20, "alamat": "Bandung", 'kode_pos' : 'Ganteng', 'jujur' : True}
example_dict["nama"]
example_dict["kode_pos"]

print ("Maka Hasilnya akan seperti ini", example_dict["nama"], example_dict["kode_pos"] )

# outputnya : Maka Hasilnya akan seperti ini Bagas Ganteng tetapi jika kamu melakukan indeks dengan key yang tidak ada maka akan terjadi error, misalkan kamu menggunakan 0 pada indeks nya seperti ini example_dict[0] maka akan terjadi error KeyError: 0. Dalam kode di atas, Anda mengambil data pada dictionary dengan memanggil key yang ada.

# Beberapa hal yang bisa kamu gunakan dalam menggunakan dictionary.

# 1. Menambahkan data pada dictionary

# contoh
print("> Contoh Menambahkan Data Kepada Dictionary")

example_dict = {"nama": "Bagas", "umur": 20, "alamat": "Bandung", 'kode_pos' : 'Ganteng', 'jujur' : True}
example_dict["pekerjaan"] = "AI Specialist"
print(example_dict)

# outputnya : {'nama': 'Bagas', 'umur': 20, 'alamat': 'Bandung', 'kode_pos': 'Ganteng', 'jujur': True, 'pekerjaan': 'AI Specialist'}

# 2. Menghapus data pada dictionary

# contoh
print("> Contoh Menghapus Data Kepada Dictionary")

example_dict = {"nama": "Bagas", "umur": 20, "alamat": "Bandung", 'kode_pos' : 'Ganteng', 'jujur' : True}
del example_dict["umur"]
print(example_dict)

# outputnya : {'nama': 'Bagas', 'alamat': 'Bandung', 'kode_pos': 'Ganteng', 'jujur': True} maka key dan valuenya yang ada di dalam dictionary akan terhapus

# 3 Mengubah data pada dictionary

# contoh
print("> Contoh Mengubah Data Kepada Dictionary") 

example_dict = {"nama": "Bagas", "umur": 20, "alamat": "Bandung", 'kode_pos' : 'Ganteng', 'jujur' : True}
example_dict["umur"] = 21
example_dict["alamat"] = "Kp. Tembong"
print(example_dict)

# outputnya : {'nama': 'Bagas', 'umur': 21, 'alamat': 'Kp. Tembong', 'kode_pos': 'Ganteng', 'jujur': True} maka key dan valuenya yang ada di dalam dictionary akan terubah


# ======================================================= Casting Tipe Data (Konversi)================================================

"""

Setelah mengetahui berbagai tipe data pada Python, kita pun dapat melakukan konversi antar tipe data dengan menggunakan beberapa fungsi.

Fungsi merupakan blok kode yang dapat dipanggil untuk melakukan tugas tertentu. kita akan mempelajari fungsi lebih detail pada modul subprogram. Saat ini, kamu cukup memahami bahwa fungsi di bawah ini dapat melakukan operasi terhadap list, set, dan string.

Di bawah ini merupakan berbagai fungsi yang dapat digunakan untuk mengonversi data antar list, set, dan string.

"""

# Konversi Integer ke Float : Untuk melakukan konversi dari integer ke float cukup menggunakan fungsi float() dengan memasukkan nilai integer di dalamnya.

# contoh
print("> Contoh Konversi Integer ke Float")

example_int = 10
example_float = float(example_int)
print(example_float)

# outputnya : 10.0

# Konversi Float ke Integer : Untuk melakukan konversi dari float ke integer cukup menggunakan fungsi int() dengan memasukkan nilai float di dalamnya.

# contoh
print("> Contoh Konversi Float ke Integer")

example_float = 10.5
example_int = int(example_float)
print(example_int)

# outputnya : 10

# Konversi Integer ke String : Untuk melakukan konversi dari integer ke string cukup menggunakan fungsi str() dengan memasukkan nilai integer di dalamnya.

# contoh
print("> Contoh Konversi Integer ke String")

example_int = 10
example_str = str(example_int)
print(example_str)

# outputnya : 10

# Konversi String ke Integer : Untuk melakukan konversi dari string ke integer cukup menggunakan fungsi int() dengan memasukkan nilai string di dalamnya.

# contoh
print("> Contoh Konversi String ke Integer")

example_str = "10"
example_int = int(example_str)
print(example_int)

# outputnya : 10

# Konversi String ke Float : Untuk melakukan konversi dari string ke float cukup menggunakan fungsi float() dengan memasukkan nilai string di dalamnya.

# contoh
print("> Contoh Konversi String ke Float")

example_str = "10.5"
example_float = float(example_str)
print(example_float)

# outputnya : 10.5

# Konversi Float ke String : Untuk melakukan konversi dari float ke string cukup menggunakan fungsi str() dengan memasukkan nilai float di dalamnya.

# contoh
print("> Contoh Konversi Float ke String")

example_float = 10.5
example_str = str(example_float)
print(example_str)


# Konversi Ke Kumpulan Data (list dan tuple) : Untuk melakukan konversi dari string ke list atau tuple cukup menggunakan fungsi list() atau tuple() dengan memasukkan nilai string di dalamnya.

# contoh
print("> Contoh Konversi Ke Kumpulan Data (List dan tuple)")

print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))

"""
Output:
{1,2,3}
(5,6,7)
['h','e','l','l','o']
"""

# Konversi ke Dictioanry : Untuk Melakukan konversi ke Dictionary cukup menggunakan dict()

# contoh 

print(dict([[1,2],[3,4]]))

"""
Output:
{1:2, 3:4}

Pada kode di atas terdapat list berisi dua list yang berisi pasangan nilai, yakni [1,2] dan [3,4]. Lalu, list tersebut diubah menjadi dictionary dengan nilai 1 dan 3 sebagai key serta nilai 2 dan 4 sebagai value.

Konversi list dari beberapa tuple yang isinya pasangan nilai menjadi dictionary.
"""

# contoh 
print(dict([(3,26),(4,44)]))

"""
Output:
{3:26, 4:44}
Pada kode di atas terdapat list yang berisi dua tuple dengan pasangan nilai, yakni (3,26) dan (4,44). Setelah diubah menjadi dictionary, nilai 3 dan 4 menjadi key, sedangkan nilai 26 dan 44 menjadi value.
"""



