# -----------------------------------------------Tipe Data-----------------------------------------------
"""Tipe Data adalah jenis informasi yang dapat di simpan kedalam variable.  Tipe data adalah cara Python mengklasifikasikan data yang kita gunakan dalam program. Tipe data menentukan jenis nilai yang dapat disimpan dalam variabel, serta bagaimana Python memproses data tersebut. Di Python, ada beberapa tipe data dasar yang sering digunakan dalam berbagai aplikasi, termasuk dalam pengembangan AI dan Machine Learning."""

# =======================================1. Tipe Data String (str)================================== 
""" 
Tipe Data String sering digunakan untuk menulis sebuah kumpulan teks atau karakter dengan cirinya adalah di kelilingi oleh tanda kutip ganda (" Contoh ") dan tanda kutip tunggal (' Contoh '), String juga bersifat imutable (Tidak bisa diubah) setelah string dibuat isinya tidak dapat dirubah, Bisa menggunakan tanda kutip kosong dan bisa menggunakan spasi. Nah kita bisa menggunakan tanda kutip ganda dan tunggal secara bersamaan, namun perlu kalian ingat jika kalian mencampuri keduanya kalian akan kebingunan sendiri, maka disini saya akan memakai tanda kutip ganda saja (" "). Nah karaktersitiknya yaitu 1. Teks atau urutan karakter. 2. Dapat mencakup huruf, angka, simbol, dan spasi.
"""

# Contoh Tipe Data STRING (str)
nama = "Jajang"
pesan = 'Semangat DEK! Jangan Kau Leha Leha Mau Jadi Apa Kau!'
string_kosong = " "

print("Nama saya adalah", nama) # Output: Jajang
print("Nih Temen Temen dapat salam dari saya ", pesan) # Output: Semangat Dek! Jangan Kau Leha Leha Mau jadi Apa kau
print(string_kosong) # Output: (tidak ada output)

# Kita bisa menggunakan operasi aritmatika atau matematika kepada String namun penggunaannya sangat berbeda dari yang lainnya
# Menggabungkan String  (Concatenation): Gunakan tanda (+) untuk menggabungkan dua tipe data String.
nama_depan = "Jajang"
nama_belakang = "Sutisna"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)  # Output: Jajang Sutisna

# Mengulang String : Menggunakan tanda (*) untuk mengulangi string
salam = "nipon paint! "
pengulangan = salam * 7
print (pengulangan)

# Mengambil Karakter String hanya di bagian tertentu 
Kata = "Aku mah apa atuh"
print (Kata[2]) # Output u
print (Kata[-1]) # Output h karena min berarti mundur
kata_kata = Kata[2] + "" + Kata[-1] # Output gambungkan biar mantep jadi uh
print (kata_kata)

# Memotong String (Slicing) : Mengambil bagian dari string.

slicing = "Akumah apa atuh hirup ge dahar ranginang mang"
print (slicing[0:6]) # Output Akumah
print (slicing[7:10]) # Output apa
print (slicing[:31]) # Output Akumah apa atuh hirup ge dahar 

# Menghitung Panjang String : Dengan menggunakan fungsi len(value)
ngarang = "Aku adalah lelaki tengah malam, ibuku harimau bapak ku singa, aku sering kali di juluki menjadi raja dunia"
print(len(ngarang)) # Cobaan we ku nyalira nya cape

# Nah di Tipe Data String ada juga yang namanya Metode String yang dimana python memiliki banyak metode bawaan untuk memanipulasi sebuah Tipe Data String
# .upper (Value) - Mengubah teks String menjadi huruf Besar
upper = "Halow Mamng"
print (upper.upper()) # Output HALOW MAMANG

# .lower (value) - Mengubah String menjadi huruf kecil
lower = "MERENDAH KIEU Si eMaNg"
print(lower.lower())

# .capitalize() – Mengubah huruf pertama menjadi besar.
cap = "aku adalah aku"
print (cap.capitalize())

# .strip() – Menghapus spasi di awal dan akhir string.
strip = "              nyaan ieumah magic        "
print(strip.strip())

# .replace() – Mengganti bagian dari string.

re = "Aku sayang nanad"
print (re.replace("nanad", "jihyo"))

# 	.split() – Memecah string menjadi list berdasarkan pemisah tertentu.
impian = "AI,Machine Learning,Blockchain"
print (impian.split())



# =======================================2. Tipe Data integer (int)================================== 
"""
Tipe Data Integer (int) sering digunakan untuk menuliskan sebuah angka bulat (tanpa desimal) baik poitif atau negatif asalkan tidak desimal maka akan bisa kalian gunakan dan jalankan. Tipe Data Integer juga sering disebut dengan Tipe Data Angka Satuan, nah Tipe Data Integer tidak boleh menggunaka String atau tanda kutip ganda karena itu akan membuat miss komunikasi antara kompeter dan syntax yang kita buat, maka hindarilah menggunakan tanda kutip ganda jika kamu ingin membuat sebuah Tipe Data Integer (int). Ciri cirinya bisa kita lihat yaitu 1. Bilangan Bulat: Tidak mengandung bagian desimal. 2. Rentang Luas: Python dapat menyimpan bilangan bulat dalam rentang yang sangat besar, dibatasi hanya oleh memori yang tersedia. 3. Operasi Matematika: Integer mendukung semua operasi aritmetika dasar seperti penjumlahan, pengurangan, perkalian, dan sebagainya.
"""

# Contoh Tipe Data Integer (int)
a = 10     # Integer positif
b = -3     # Integer negatif
c = 0      # Nol

print(a)   # Output: 10
print(b)   # Output: -3
print(c, type(c))   # Output: 0

# Operasi Dengan Integer (int)
# Penjumlahan (+)
plus = 100 + 67
print (plus)

# Pengurangan (-)
mins = 900 - 2233
print (mins)

# Perkalian (*)
kali = 100* 367
print (kali) 

# Pembagian Bulat (//)
bagi = 100 // 7
print (bagi) # Output 14 (Karena pembagian tanpa desimal)

# Pemangkatan (**)
pangkat = 3 ** 8
print (pangkat) # Output 6561 (3 pangkat 8)

#Modulus (%)
modulus = 10 % 3
print(modulus)  # Output: 1 (sisa hasil pembagian)

# Selain itu kita bisa mengkonversi suatu tipe data dan menjadikannya integer, berikut adalah caranya. 
# Konversi dari float ke integer
float_number = 3.7
int_number = int(float_number)  # Hasilnya: 3 (desimal dihilangkan)
print("Yang berawal dari memiliki tipe data float dan ada desimalnya sekarang lihat dibulatkan menjadi integer",int_number)

# Konversi dari string ke integer
string_number = "42"
cring_int = int(string_number)
print("Bukan sulap bukan sihir tapi dari string bisa jadi integer keren bukan ", cring_int, "Inilah Hasilnya geng", type(int_number))  # Output: 42



# =======================================3. Tipe Data FLoat================================== 
"""
Tipe Data Float adalah Tipe Data yang digunakan atau menuliskan sebuah angka yang desimal atau pecahan, ciri ciri Tipe Data ini adalah selalu menggunakan titik, ya namanya juga bilangan desimal atuh kang. Perlu kalian ingat juga float sama dengan integer bisa menggunakan negatif atau positif. Dapat mewakili nilai yang lebih besar atau lebih kecil dengan ketelitian tinggi. Digunakan dalam komputasi matematika dan statistik.
"""

# Contoh Tipe Data Float
a = 3.14     # Float positif
b = -0.75    # Float negatif
c = 0.0      # Float nol

print(a)     # Output: 3.14
print(b)     # Output: -0.75
print(c)     # Output: 0.0

# Operasi Math Float
# Sama saja seperti integer float dapat kita gabungkan dengan operasi matematika tetapi ada tambahana untuk float.

# Pembagian (/) inilah tambahanya

pembagian = 7.5 / 2.5
print(pembagian) # Output: 3.0

# Sama halnya dengan Tipe Data yang lain Float juga dapat mengkonversi
# Dari Integer ke Float
x = float(5)
print(x)  # Output: 5.0

# Dari String ke Float
y = float("3.14")
print(y)  # Output: 3.14

# Dari Boolean ke FLoat
z = float(True) # True menjadi 1.0
w = float(False) # False menjadi 0.0
print(z) # Output: 1.0
print(w) # Output: 0.0



# =======================================4. Tipe Data Boolean================================== 
"""
Tipe Data Boolean adalah Tipe Data yang hanya memeiliki dua nilai True (menyatakan kebenaran atau kondisi yang benar) dan False (menyatakan kebohongan atau kondisi yang salah). Tipe Data Boolean biasanya digunakan untuk perbandingan atau mewakili logika dalam program. Boolean sangat sering digunakan dalam perbandingan antara dua nilai, yang akan menghasilkan true atau false. Berikut adalah operator perbandingaan (assignment) yang menhasilkan nilai boolean 1. (==) Sama Dengan 2. (!=) Tidak Sama Dengan 3. (>) Lebih Besar Dari 4. (<) Lebih Kecil Dari 5. (>=) Lebih Besar Atau Sama Dengan 6. (<=) Lebih Kecil Atau Sama Dengan.
"""
# Contoh Tipe Data Booolean
benar = True
salah = False

print(benar)  # Output: True
print(salah)  # Output: False

# Contoh Boolean dalam operasi perbandingan (Assignment)

x = 10
y = 5

print(x > y)   # Output: True
print (y < x) # Output True
print(x == y)  # Output: False

# Contoh Boolean dalam Operasi Logika: Operasi logika digunakan untuk melakukan perhitungan berdasarkan nilai Boolean (True atau False). Operasi ini penting untuk membuat keputusan dalam pemrograman.
"""
> Python memiliki tiga Operator Logika Utama:
1. and (Dan)
2. or (Atau)
3. not (Kebalikan)
"""

# Operator Logika and
"""
> Operator Logika and (dan)
Penjelasannya adalah: 
1. and mengembalikan True hanya jika semua Kondisi dalah True
2. Jika salah satu kondisi False, maka hasilnya False
"""
# Pembatas
ands = "Ini adalah Logika and (Dan)"
print (ands)

# Contoh kasusanya adalah di bawah ini
a = True
b = False 

print (a and b) # Output False karena salah satu kondisi false

# Contoh lebih rinci 
x = 10
b = 15
z = 1
j = 90

print (x < b and z < j) # Output True (Karena kedua kondisi memang benar)
print (x > j and z < b) # Outputnya False (Karena salah satu kondisi salah)
print ( x > b and z > j) # Outputnya False (Karena keduanya sama sama salah)

# Operator Logika or
"""
> Operator Logika or (Atau)
Penjelasannya :
1. or akan mengembalikan True jika seidaknya ada satu dari kondisi adalah True, begitupun dengan sebaliknya
2. Mengembalikan False hanya jika semua kondisi adalah False. Begitupun sebaliknya
"""

# Pembatas biar gak bingung euy
ora = "Ini adalah Logika or (Atau)"
print (ora)

# Contoh Kasus dari or 
a = True
b = False

print(a or b)  # Output: True

# Contoh Lebih Rinci
c = 100
d = 78
f = 56 
h = 304

print (c > f or d < h) # Output True (Karena kedua kondisi benar)
print (f < d or f > h) # Output True (Karena salah satu kondisi benar)

# Operator Logika not 
"""
> Operator Logika not (sebaliknya)
1. Jika True, hasilnya menjadi False.
2. 	•	Jika False, hasilnya menjadi True.
"""

# Batas deui soalna bingung pisan abi
nota = "Ini adalah Logika not (Sebaliknya)"
print (nota)

# Contoh Logika not 
a = True
b = False
print(not a)  # Output: False karena (not) merupakan negasi atau kebalikan dari kondisi sebenarnya
print(not b)  # Output: True



# ========================================5. Tipe Data List====================================
"""
Tipe Data List adalah Salah satu tipe data yang digunakan untuk menyimpan sekumpulan item (atau elemen) dalam satu variabel. Yang dimana bisa mengelompokan berbagai jenis Tipe Data seperti  string, integer, float dan boolean bahkan Tipe Data lainnya kedalam satu variable.  List bisa berisi data yang terurut dan dapat diubah, yang artinya kita bisa menambah, menghapus, atau mengubah item di dalamnya. List ditandai dengan tanda kurung siku [], dan setiap elemen di dalamnya dipisahkan dengan koma. 
"""

# Contoh Tipe Data List
# List berisi angka
angka = [1, 2, 3, 4, 5]
print(angka)  # Output: [1, 2, 3, 4, 5]

# List dengan berbagai tipe data
data = [1, 3.14, "Hello", True]
print(data)  # Output: [1, 3.14, 'Hello', True]

# Elemen dalam list bisa diakses menggunakan indeks. Indeks dimulai dari angka 0 untuk elemen pertama.
data_mahasiswa = ["Nanad", "Bagas", "Vathur", "Enep", "Reza", "Faisal", "Firhan", "Putra", "Zaelaniaja"]
print(data_mahasiswa[0])  # Output: Nanad
print(data_mahasiswa[1])  # Output: Bagas
print(data_mahasiswa[2])  # Output: Vathur
print(data_mahasiswa[6])  # Output: Firhan

# Mengubah Elemen dalam List: Karena list bersifat mutable (dapat diubah), kita bisa memodifikasi elemen dalam list.
nama_siswa = ["Nanad", 100, "Bagas", "Ayah", "Mamah"]
nama_siswa[0] = "Nanad Mirip Moncong Onta" # Output Nanad Miirip Moncong Onta
nama_siswa[2] = "Bagas si ganteng kalem" # Output Bagas si ganteng kalem
nama_siswa[4] = "Sultan" # Output Sultan
nama_siswa[3] = "Kalem" # Output Kalem
print(nama_siswa)

# Menambah Elemen dalam List: Untuk menambah elemen di dalam list, kita bisa menggunakan metode append() untuk menambahkan elemen di akhir list, atau insert() untuk menyisipkan elemen pada posisi tertentu.

# Menambahkan elemen ke akhir list
nama_siswa.append ("Jajang_guru")
print(nama_siswa)

# Menyisipkan elemen pada indeks tertentu
nama_siswa.insert(1, "Bener Pisan")
print(nama_siswa)

print((5 > 3) or (2 * 2 == 5) and not (10 < 20))
