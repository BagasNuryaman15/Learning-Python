# --------------------------------------- Markle Tree Pada Tipe Data -------------------------------

"""

1.  Tipe Data None
    Tipe Data None adalah tipe data yang hanya memiliki satu nilai yaitu None. Tipe data None digunakan untuk menandai bahwa sebuah variabel tidak memiliki nilai apa pun. Tipe data None digunakan dalam beberapa kasus, seperti ketika sebuah variabel tidak memiliki nilai yang benar-benar diperoleh dari pengguna atau karena kesalahan pada program.

2.  Tipe Data Numeric
    Tipe Data Numeric adalah tipe data yang memiliki nilai numerik, yaitu bilangan bulat, bilangan desimal, dan bilangan kompleks. Tipe data numeric digunakan untuk menyimpan nilai numerik, seperti angka, desimal, dan bilangan kompleks. Tipe data numeric dibagi menjadi 2 yaitu : Int (Bilangan bulat) dan Float (Bilangan desimal).

3.  Tipe Data Boolean 
    Tipe Data Boolean adalah tipe data yang memiliki 2 nilai yaitu Benar (True) atau Salah (False). Tipe data Boolean digunakan untuk menyimpan nilai logika, yaitu nilai yang bernilai benar atau salah. Tipe data Boolean digunakan dalam beberapa kasus, seperti ketika sebuah variabel harus memiliki nilai benar atau salah. Tipe Data ini hanya satu yaitu : Bool

4.  Tipe Data Sequence 
    Tipe Data Sequence adalah tipe data yang memiliki nilai yang berupa kumpulan nilai yang berurutan. Tipe data sequence digunakan untuk menyimpan nilai yang berupa kumpulan nilai yang berurutan, seperti list, tuple, dan string. Tipe data sequence dibagi menjadi 3 yaitu : List, Tuple, dan String.

5.  Tipe Data Set 
    Tipe Data Set adalah tipe data yang memiliki nilai yang berupa kumpulan nilai yang tidak berurutan. Tipe data set digunakan untuk menyimpan nilai yang berupa kumpulan nilai yang tidak berurutan, seperti set, dan frozenset. Tipe data set dibagi menjadi 2 yaitu : Set dan Frozenset.

6.  Tipe Data Mapping
    Tipe Data Mapping adalah tipe data yang memiliki nilai yang berupa kumpulan nilai yang terdiri dari pasangan key dan value. Tipe data mapping digunakan untuk menyimpan nilai yang berupa kumpulan nilai yang terdiri dari pasangan key dan value, seperti dictionary. Tipe data mapping dibagi menjadi 2 yaitu : Dictionary dan Defaultdict.

7.  Tipe Data Binary
    Tipe Data Binary adalah tipe data yang memiliki nilai yang berupa kumpulan nilai yang terdiri dari bit. Tipe data binary digunakan untuk menyimpan nilai yang berupa kumpulan nilai yang terdiri dari bit, seperti bytearray, bytes, memoryview. Tipe data binary dibagi menjadi 3 yaitu : Bytearray, Bytes, dan Memoryview.

"""


# ======================================= 1. Tipe Data String (str) ======================================
print("Tipe Data String(str)".center(150, "="))

""" 
Tipe Data String sering digunakan untuk menulis sebuah kumpulan teks atau karakter dengan cirinya adalah di kelilingi oleh tanda kutip ganda (" Contoh ") dan tanda kutip tunggal (' Contoh '), String juga bersifat imutable (Tidak bisa diubah) setelah string dibuat isinya tidak dapat dirubah, Bisa menggunakan tanda kutip kosong dan bisa menggunakan spasi. Nah kita bisa menggunakan tanda kutip ganda dan tunggal secara bersamaan, namun perlu kalian ingat jika kalian mencampuri keduanya kalian akan kebingunan sendiri, maka disini saya akan memakai tanda kutip ganda saja (" "). Nah karaktersitiknya yaitu 1. Teks atau urutan karakter. 2. Dapat mencakup huruf, angka, simbol, dan spasi.
"""

# Pembatas
string = ("<Tipe Data String (str)>".center(50, "-"))
print (string)

# Contoh Tipe Data STRING (str)
contoh_str = "= Contoh Tipe Data String (str)"
print (contoh_str)

# Contoh Penerapannya
nama = "Jajang"
pesan = 'Semangat DEK! Jangan Kau Leha Leha Mau Jadi Apa Kau!'
string_kosong = " "

# Outputnya
print("Nama saya adalah", nama) # Output: Jajang
print("Nih Temen Temen dapat salam dari saya ", pesan) # Output: Semangat Dek! Jangan Kau Leha Leha Mau jadi Apa kau
print(string_kosong) # Output: (tidak ada output)


# --------------------------------------- Menggunakan Operasi (aritmatika) ke dalam Tipe Data String (str) ---------------------------------
print("Menggunakan Operasi (aritmatika) le dalam Tipe Data String(str)".center(150, "*"))

# Menggabungkan String  (Concatenation): Gunakan tanda (+) untuk menggabungkan dua tipe data String.
Connect = "> Ini adalah contoh menggabungkan string (Concatenation)"
print (Connect)

# Contoh Penerapannya
nama_depan = "Jajang"
nama_belakang = "Sutisna"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)  # Output: Jajang Sutisna

# Mengulang String : Menggunakan tanda (*) untuk mengulangi string
loop = "> Ini adalah contoh mengulang string"
print (loop)
# Contoh Penerapannya
salam = "nipon paint! "
pengulangan = salam * 7
print (pengulangan) # Output nipon paint! nipon paint! nipon paint! nipon paint! nipon paint! nipon paint! nipon paint!

# Mengambil Karakter String hanya di bagian tertentu 
select = "> Ini adalah contoh mengambil karakter string"
print (select)

# Contoh Penerapannya
Kata = "Aku mah apa atuh"
print (Kata[2]) # Output u
print (Kata[-1]) # Output h karena min berarti mundur
kata_kata = Kata[2] + "" + Kata[-1] # Output gambungkan biar mantep jadi uh
print (kata_kata)

# Memotong String (Slicing) : Mengambil bagian dari string.
slice = "> Ini adalah contoh memotong string"
print (slice)

# Contoh Penerapannya
slicing = "Akumah apa atuh hirup ge dahar ranginang mang"
print (slicing[0:6]) # Output Akumah
print (slicing[7:10]) # Output apa
print (slicing[:31]) # Output Akumah apa atuh hirup ge dahar 

# Menghitung Panjang String : Dengan menggunakan fungsi len(value)
panjang = "> Ini adalah contoh menghitung panjang string"
print (panjang)

# Contoh Penerapannya
ngarang = "Aku adalah lelaki tengah malam, ibuku harimau bapak ku singa, aku sering kali di juluki menjadi raja dunia"
print(len(ngarang)) # Output Cobaan we ku nyalira nya cape loba kana 100+

# --------------------------------------------------------------------- Transform -----------------------------------------------------------------------
print("TRANSFORM VALUE".center(150, "*"))

""" 

Nah di Tipe Data String ada juga yang namanya Metode String yang dimana python memiliki banyak metode bawaan untuk memanipulasi sebuah Tipe Data String.

"""

# -------------------------------- Mengubah Huruf Besar/Kecil -----------------------------------
print("Mengubah Huruf Besar Atau Kecil".center(150, "-"))
'''
Dalam kategori ini terdapat beberapa metode yang dapat digunakan untuk mengubah string menjadi huruf kapital (UPPERCASE) atau huruf kecil (lowercase). Kedua metode ini, baik upper() maupun lower() adalah metode bawaan dari string Python. Perlu diingat bahwa jika terdapat karakter bukan huruf (seperti simbol atau angka) yang tidak memiliki opsi kapital sehingga karakter tersebut tidak diubah.
'''

# .upper (Value) - Mengubah teks String menjadi huruf Besar
upper = "> Ini adalah contoh mengubah teks string menjadi huruf besar"
print (upper)

# Contoh Penerapannya
upper = "Halow Mamng"
print (upper.upper()) # Output HALOW MAMANG

# .lower (value) - Mengubah String menjadi huruf kecil
lower = "> Ini adalah contoh mengubah teks string menjadi huruf kecil"
print (lower)

# Contoh Penerapannya
lower = "MERENDAH KIEU Si eMaNg"
print(lower.lower())

# .capitalize() – Mengubah huruf pertama menjadi besar.
capitalize = "> Ini adalah contoh mengubah huruf pertama menjadi besar"
print (capitalize)

# Contoh Penerapannya
cap = "aku adalah aku"
print (cap.capitalize())

# ------------------------------- Awalan dan Akhiran ---------------------------
print("Awal Dan Akhiran String".center(150, "-"))

''' 
Dalam kategori ini terdapat beberapa metode yang dapat digunakan untuk mengubah string menjadi huruf kapital (UPPERCASE) atau huruf kecil (lowercase). Kedua metode ini, baik upper() maupun lower() adalah metode bawaan dari string Python. Perlu diingat bahwa jika terdapat karakter bukan huruf (seperti simbol atau angka) yang tidak memiliki opsi kapital sehingga karakter tersebut tidak diubah.
'''

# .strip() – Menghapus spasi di awal dan akhir string.
strip = "> Ini adalah contoh menghapus spasi di awal dan akhir string"
print (strip)

# Contoh Penerapannya
strip = "              nyaan ieumah magic        "
print(strip.strip())

# Nah jika kalian ingin menghapus spasi atau whitespace dari kanan dan kiri saja maka kalian bisa menggunakan rstrip() dan lstrip()

# .starswith() - menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True.
print ("> Ini Adalah Contoh Menggunakan starwith()")
print ("Bagas Ganteng".startswith("Bagas"))

# Output : True, karena string yang bertuliskan Bagas memang ada pada awal kalimat Bagas Ganteng.  Jika awalan nya bukan string yang sama maka hasilnya akan False
# Nah ada juga yang mencari akhiran kata, kita bisa menggunakan endswith (). 

# ------------------------------- Memisah dan Menggabung String ---------------------------
print("Memisah Dan Menggabungkan String".center(150, "-"))

# .join() - Menggabungkan antara beberapa string.
print("> Ini Adalah Contoh Penggunaan .join()")

jion = ['Awal','Tengah','Akhir','120', ]
print(''.join(jion))

# Output : AwalTengahAkhir120 
# Pada kode di atas, kita menggabungkan string "Dicoding", "Indonesia", dan "!" yang telah disimpan pada variabel list. Perhatikan bahwa pada sintaks awal sebelum ".join()" kita menambahkan single quotes di sana. Single quotes ini bermaksud agar kita menentukan delimiter pada setiap kata/nilai yang ingin Anda gabungkan. Pada kode di atas, delimiter-nya adalah whitespace atau spasi.

# 	.split() – Memecah string menjadi list berdasarkan pemisah tertentu.
split = "> Ini adalah contoh memecah string menjadi list berdasarkan split()"
print (split)

# Contoh Penerapannya
impian = " AI MachineLearning Blockchain"
print (impian.split())

# Output : ['AI', 'MachineLearning', 'Blockchain'], Karena split() ini kebalikan dari join maka setiap string atau kata yang memiliki whitespace akan di pisahkan. Mengapa MachineLearning menyatu, karena dia tidak memiliki whitespace. Dan coba perhatikan string tersebut dimasukan ke dalam list.

# ----------------------------------- Mengganti Elemen String ----------------------------------
print("Mengganti Elemen String".center(150, "-"))

# .replace() – Mengganti bagian dari string.
replace = "> Ini adalah contoh mengganti bagian dari string"
print (replace)

# Contoh Penerapannya
re = "Aku sayang nanad"
print (re.replace("nanad", "jihyo"))

# Outputnya : Aku Sayang jihyo, karena string nanad telah digantikan dengan string jihyo.abs

# ------------------------------------------- Pengecekan String -------------------------------------
print("Pengecekan String".center(150, "-"))

# Kategori selanjutnya bertujuan untuk melakukan pengecekan pada string. Hasil dari kategori ini adalah mengembalikan nilai boolean True/False. 

# -isupper() : akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kapital (uppercase). Sebaliknya, jika ada satu huruf saja yang kecil/tidak uppercase, nilai False akan dikembalikan.

# Contohnya
print("> Contoh Penerapan (.isupper())")
print("BAGAS NURYAMAN".isupper())

# Output : True, Karena String di atas memeiliki value yang dimana value nya berupa teks yang UPPPER semuanya. 

# Nah ada juga yang namanya .islower() Kebalikan dari .isupper().

# -.isalpha() : Metode ini mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet. Jika ada satu huruf lain yang bukan alfabet, seperti angka, nilai False akan dikembalikan.

# Contohnya
print("> Contoh Penerapan (.isalpha())")
print("bagas ganteng".isalpha())

# Output : True , Karena Value String memang benar hanya menggunakan alphabet saja, tetapi jika kita menambahkan angka atau Huruf Besar pada awal kalimat maka akan False.

# -isalnum() : Metode isalnum() mengembalikan nilai True jika karakter dalam string adalah alfanumerik, yaitu hanya huruf atau hanya angka atau berisi keduanya. Jika tidak, nilai False akan dikembalikan.

# Contohnya
print("> Contoh Penerapan (.isalmun())")
print("Limbangan150902".isalnum())

# Ouput : True, karena value tersebut memiliki teks dengan angka, tetapi jika kamu menambahkan whitespace (spasi) pada keduanya maka .isalmun() akan menganggap bahwa itu kedua kalimat yang berbeda maka akan di kembalikan False

# -isdecimal() : Metode isdecimal() akan mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik. Jika tidak, nilai False akan dikembalikan.

# Contohnya
print("> Contoh Penerapan (.isdecimal())")
print("124".isdecimal())

# Output : True, karena hanya berupa angka/numerik. Uniknya namanya saja yang desimal tetapi ketika kita menambahkan sebuh titik pada salah satu titik maka akan dianggap itu adalah bukan angka atau numerik.

# -isspace() : Metode isspace() akan mengembalikan nilai True jika string hanya berisi whitespace, seperti spasi, tab, newline, atau karakter whitespace lainnya.

# Contohnya
print("> Contoh Penerapan (.isspace())")
print("                 ".isspace())

# Output : True, Karena hanya sebuah whitespace

# -istitle() : Metode istitle() mengembalikan nilai True jika string berisi huruf kapital pada setiap kata pertamanya. Jika tidak, nilai False dikembalikan.

# Contohnya
print("> Contoh Penerapan (.istitle())")
print("Belajar Machine Learning".istitle())

# Output : True, Karena memiliki huruf kapital maka di anggap itu sebuah title.

# ------------------------------------------ Formatting pada String --------------------------------------
print("Formating Pada String".center(150, "-"))

# -zfill() : Metode zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu. Tujuan dari metode ini adalah membantu untuk memastikan bahwa sebuah angka atau nilai memiliki panjang tetap, terutama ketika ingin menyimpan nilai dalam format yang konsisten.

# Contohnya 
print("> Contoh Penerapan (.zfill())")
teks = "126"
contoh_zfill = teks.zfill(5)
print(contoh_zfill)

'''
Output : 126
    1. Variabel teks menyimpan nilai string berupa "126". Perlu dipahami bahwa kata "Code" hanya memiliki 3 huruf atau sederhananya panjang kata "126" adalah 3.
    2. Variabel tambah_number menyimpan nilai variabel teks dengan memanggil metode zfill(5).  Angka 5 tersebut merupakan parameter untuk menentukan panjang yang diinginkan oleh string. Sederhananya, kita memastikan bahwa panjang kata "126" haruslah 5 dan bukan 3. Jadi, program akan menambahkan angka 0 di depan kata "126" untuk memastikan bahwa panjangnya adalah 5.

    Metode zfill() ini berguna ketika ingin memastikan bahwa angka atau nilai dalam string memiliki panjang tetap dan sesuai dengan format yang diinginkan. Metode zfill() dapat diterapkan untuk menetapkan nomor nota atau nomor antrian.
'''

# -.rjust() : Metode rjust() berguna untuk merapikan pencetakan teks. Dengan metode rjust() ini, Anda dapat membuat teks menjadi rata kanan sehingga tampilannya lebih rapi.

# Contohnya
print("> Contoh Penerapan (.rjust())")
print("Ini Akan Bergeser ketengah karena .rjust(100)".rjust(100))

'''
Output : Value tersebut bergeser dari kiri ke kanan, nah perlu di ingat bahwa ketika kita menggunakan rjust() maka rumusnya adalah hitung dulu ada berapa indeks dari variable value kita.
    contoh : Jika kita telah mengetahui bahwa "apa" adalah 3 karena tidak memiliki whitespace maka kita akan mengatur .rjust(5), hasilnya value tersebut akan bergeser 2 spasi dari kiri ke kanan. 
    
    Rumusnya (.rjust(Selera inimah Boy) - lens). !Noted, Ini juga bisa kita gunakan untuk .zfill()
'''

# -.ljust() : Ini adalah kebalikannya dari .rjust()

# Gausah di Contohin lahya

# -.center() : Metode center() menjadikan teks rata tengah. Metode ini akan menambahkan whitespace di sebelah kiri dan kanan secara default. Anda juga bisa mengganti whitespace tersebut dengan karakter lain.

# Contohnya
print("> Contoh Penerapan (.center())")
print("Teks Ini Akan Berada Di Tengah Tanpa Mengatur .rjust atau .ljust".center(160))

# Output : Maka Value tersebut akan otomatis berada di tengah tanpa perlu mengatur .ljust() dan .rjust() karena .center() telah memiliki nilai tersebut.abs

# --------------- Noted! -----------------
# Sekali lagi, kita harus ingat bahwa zfill(), rjust(), ljust(), dan center() berfungsi sama, yakni memastikan panjang teks sesuai dengan yang diminta.

# ----------------------------------------------------- String Literals ---------------------------------------
print("String Literals".center(150, "-"))

'''
Umumnya, string ditulis dengan mudah di Python, diapit oleh tanda petik tunggal. Namun, dalam kondisi tertentu, dibutuhkan petik tunggal di tengah string (misalnya, struktur kepemilikan dalam bahasa Inggris your's Cat atau penyebutan Jum'at pada hari dalam bahasa Indonesia).

    Misalnya kita menuliskan : contoh_1 = 'Where Your's Phone'

    Python akan salah mengira bahwa string berakhir setelah huruf r dan selebihnya merupakan kode yang invalid. Namun, Python memperbolehkan untuk menggunakan petik dua seperti kita menggunakan petik tunggal. Dalam kasus sebelumnya, kita cukup mengetik seperti berikut.

    contoh_1 = "Where Your's Phone"

    Dalam contoh di atas, Python mengenali bahwa petik tunggal adalah bagian tidak terpisahkan dari string tersebut. Bagaimana jika kita memerlukan kedua jenis petik dalam string tunggal? Python menyediakan escape character.

    ! Escape character memungkinkan kita untuk menggunakan karakter yang sebelumnya tidak bisa dimasukkan dalam string. Umumnya diawali dengan backslash (\) dan diikuti karakter tertentu yang diinginkan. Contohnya, untuk petik tunggal kita dapat menambahkan \'.

    contoh_1 = 'Where Your\'s Phone'

    Python mengetahui bahwa pada your\'s, sebelum petik terdapat backslash (\) yang menandakan petik tunggal sebagai bagian dari string dan bukan akhir dari string. Escape character \' dan \" memungkinkan kita untuk memasukkan karakter ' dan '' dalam bagian string. Beberapa contoh escape character lainnya sebagai berikut. 

    1. \' Single quote
    2. \" Double quote
    3. \t Tab
    4. \n Newline (line break)
    5. \\ Backslash
'''

# Contoh Keseluruhan Penggunaan
print("> Contoh Penerapan String Literals")
print('Helo, siapakah namamu?\n\'Namaku adalah Jajang\'\nOh, Halo Jajang senang berkenalan denganmu.\t Jajang pun senang')


'''
Output : 
'Namaku adalah Jajang'
Oh, Halo Jajang senang berkenalan denganmu.      Jajang pun senang

Mengapa bisa begitu ya karena kita menggunakan \n(Line Break), \' (Single Quote) dan \t(Tab)
'''

# -------------------------------------------- Raw String ------------------------------------
print("Raw String".center(148,'-'))

'''
Python juga menyediakan cara untuk mencetak string sesuai dengan apa pun input atau teks yang diberikan. Metode ini dinamakan raw strings. Umumnya, ia digunakan untuk regex atau beberapa implementasi lain yang sangat bergantung pada keberadaan backslash. Untuk mengimplementasikan raw strings, sisipkan huruf r sebelum pembuka string.

    Liat Contoh Di Bawah :
'''

# Contohnya
print("> Contoh Penerapan Raw String(r)")
print(r"Where\'\tWhere\'\t")

# Output : Where\'\tWhere\'\t, Maka Perhatikan bahwa escape character (\') dan (\t) ikut tercetak pada teks tersebut. Hal ini karena raw string akan mencetak string sesuai dengan apa pun input atau teks yang diberikan. Jadi ketika kita menggunakan raw string kita tidak lagi memerlukan escape karakter tetapi kekurangannya hanya bisa bergungsi satu baris saja tidak multicolumn.

print("> Contoh Yang Benar Untuk Penggunaan Raw String (r)")
print(r"Where's my phone, anyone can u help me to find my phone's ")

# Output : Where's my phone, anyone can u help me to find my phone's, Bisa kita lihat dengan jelas kita tidak lagi memerlukan escape karakter disini, tetepi memiliki kekurangan tidak bisa menggunakan enter atau multiple-column.





print(" ".center(150,'-'))
# ======================================= 2. Tipe Data integer (int) ================================== 
print(" Tipe Data Integer (str) ".center(150))
"""

Tipe Data Integer (int) sering digunakan untuk menuliskan sebuah angka bulat (tanpa desimal) baik poitif atau negatif asalkan tidak desimal maka akan bisa kalian gunakan dan jalankan. Tipe Data Integer juga sering disebut dengan Tipe Data Angka Satuan, nah Tipe Data Integer tidak boleh menggunaka String atau tanda kutip ganda karena itu akan membuat miss komunikasi antara kompeter dan syntax yang kita buat, maka hindarilah menggunakan tanda kutip ganda jika kamu ingin membuat sebuah Tipe Data Integer (int). Ciri cirinya bisa kita lihat yaitu 1. Bilangan Bulat: Tidak mengandung bagian desimal. 2. Rentang Luas: Python dapat menyimpan bilangan bulat dalam rentang yang sangat besar, dibatasi hanya oleh memori yang tersedia. 3. Operasi Matematika: Integer mendukung semua operasi aritmetika dasar seperti penjumlahan, pengurangan, perkalian, dan sebagainya.

"""


# Pembatas
contoh_int = "= <Tipe Data Integer (int)>"
print (contoh_int)

# Contoh Tipe Data Integer (int)
contoh_int = "= Contoh Tipe Data Integer (int)"
print (contoh_int)

# Contoh Penerapannya
a = 10     # Integer positif
b = -3     # Integer negatif
c = 0      # Nol

# Outputnya
print(a)   # Output: 10
print(b)   # Output: -3
print(c, type(c))   # Output: 0

# --------------------------------------- Menggunakan Operasi (Math) ke dalam Tipe Data Integer (Int)---------------------------------
print(" Menggunakan Operasi Matematika (artimatika) ".center(70, '-'))
# Penjumlahan (+)
plus = "> Ini adalah contoh penjumlahan (+)"
print (plus)

# Contoh Penerapannya
plus = 100 + 67
print (plus)

# Pengurangan (-)
minus = "> Ini adalah contoh pengurangan (-)"
print (minus)

# Contoh Penerapannya
mins = 900 - 2233
print (mins)

# Perkalian (*)
kali = "> Ini adalah contoh perkalian (*)"
print (kali)

# Contoh Penerapannya
kali = 100* 367
print (kali) 

# Pembagian Bulat (//)
bagi = "> Ini adalah contoh pembagian bulat (//)"
print (bagi)

# Contoh Penerapannya
bagi = 100 // 7
print (bagi) # Output 14 (Karena pembagian tanpa desimal)

# Pemangkatan (**)
pangkat = "> Ini adalah contoh pemangkatan (**)"
print (pangkat)

# Contoh Penerapannya
pangkat = 3 ** 8
print (pangkat) # Output 6561 (3 pangkat 8)

#Modulus (%)
modulus = "> Ini adalah contoh modulus (%)"
print (modulus)

# Contoh Penerapannya
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



# ======================================= 3. Tipe Data FLoat ================================== 
print(" Tipe Data Float ".center(150, '-'))
"""
Tipe Data Float adalah Tipe Data yang digunakan atau menuliskan sebuah angka yang desimal atau pecahan, ciri ciri Tipe Data ini adalah selalu menggunakan titik, ya namanya juga bilangan desimal atuh kang. Perlu kalian ingat juga float sama dengan integer bisa menggunakan negatif atau positif. Dapat mewakili nilai yang lebih besar atau lebih kecil dengan ketelitian tinggi. Digunakan dalam komputasi matematika dan statistik.
"""

# Pembatas
print
contoh_float = "= <Tipe Data Float>"
print (contoh_float)

# Contoh Tipe Data Float
contoh_float = "= Contoh Tipe Data Float"
print (contoh_float)

# Contoh Penerapannya
a = 3.14     # Float positif
b = -0.75    # Float negatif
c = 0.0      # Float nol

# Outputnya
print(a)     # Output: 3.14
print(b)     # Output: -0.75
print(c)     # Output: 0.0

# --------------------------------------- Menggunakan Operasi (aritmatika) ke dalam Tipe Data Float---------------------------------
print("Operasi Matematika Untuk Tipe Data Float".center(80,'-'))
# Sama saja seperti integer float dapat kita gabungkan dengan operasi matematika tetapi ada tambahana untuk float.

# Pembagian (/) inilah tambahanya
bagi = "> Ini adalah contoh pembagian (/) inilah tambahanya"
print (bagi)

# Contoh Penerapannya
pembagian = 7.5 / 2.5
print(pembagian) # Output: 3.0

# Sama halnya dengan Tipe Data yang lain Float juga dapat mengkonversi
print("> Contoh Konversi Float")
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

# Pembatas
contoh_boolean = "= <Tipe Data Boolean>"
print (contoh_boolean)

# Contoh Tipe Data Booolean
contoh_boolean = "= Contoh Tipe Data Booolean"
print (contoh_boolean)

# Contoh Penerapannya
benar = True
salah = False

# Outputnya
print(benar)  # Output: True
print(salah)  # Output: False

# # --------------------------------------- Menggunakan Operasi (aritmatika) ke dalam Tipe Data Boolean (bool)---------------------------------

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

# ------------------------------------------------------------- Operator Logika and (Dan) ---------------------------------------
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
contoh = "> Contoh Lebih Rinci"
print (contoh)

x = 10
b = 15
z = 1
j = 90

# Outputnya
print (x < b and z < j) # Output True (Karena kedua kondisi memang benar)
print (x > j and z < b) # Outputnya False (Karena salah satu kondisi salah)
print ( x > b and z > j) # Outputnya False (Karena keduanya sama sama salah)

# ------------------------------------------------------------- Operator Logika or (Atau) ---------------------------------------
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
contoh = "> Contoh Lebih Rinci"
print (contoh)

c = 100
d = 78
f = 56 
h = 304

# Outputnya
print (c > d or f > h) # Output True (Karena salah satu kondisi benar)
print (c > f or d < h) # Output True (Karena kedua kondisi benar)
print (f < d or f > h) # Output True (Karena salah satu kondisi benar)

# ------------------------------------------------------------- Operator Logika not (negasi/Sebaliknya) ---------------------------------------
"""

> Operator Logika not (sebaliknya)

Penjelasannya :

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



# ======================================== 5. Tipe Data List====================================
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