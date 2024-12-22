print("\n"," Percabangan Dan Ternary Operators ".center(150, "="), "\n")

'''
Control flow adalah sebuah cara untuk memberi tahu program mengenai instruksi yang harus dijalankan dan di mana harus memulai dan berakhir. Pada materi sebelumnya, Anda telah mempelajari aksi sekuensial. Python akan menjalankan kode Anda berdasarkan deretan instruksi yang dibuat secara sekuensial.

Dalam Python, program dapat berupa blok kode. Python sangat memperhatikan indentasi untuk membangun sebuah blok kode. Salah satu blok pemrograman adalah perulangan. Perulangan adalah satu dari beberapa control flow. 

Control flow memungkinkan program untuk berjalan berdasarkan jalur eksekusi. Control flow terbagi menjadi beberapa jenis, yakni kondisi tertentu (percabangan), mengulang blok kode secara berulang (perulangan), melewati sebagian kode dan berhenti di kode tertentu, hingga mendefinisikan fungsi. 

Kita akan mempelajari fungsi pada modul yang berbeda. Untuk menggantikannya, materi ini akan fokus menjelaskan error dan exception handling yang bertujuan untuk mengontrol dan merespons kejadian yang tidak diinginkan ketika program berjalan.

Mari kita mulai pembahasan kita dari Percabangan dan Ternary Operators terlebih dahulu.
'''

# =========================================================== Percabangan ======================================================================
'''
                                                              Percabangan

Dalam pemrograman, sebuah kode program dapat berjalan berdasarkan kondisi tertentu. Maknanya, Anda dapat memberikan instruksi berdasarkan "Jika-maka" (if-else). Misalnya dalam keadaan seperti berikut.

    1. Jika Anda tidak menyelesaikan kelas Memulai Pemrograman dengan Python, maka Anda tidak lulus dari kelas Memulai Pemrograman dengan Python.
    2. Jika jumlah variabel nama kurang dari dua, maka variabel tersebut tidak memenuhi kriteria kondisi.

Sebenarnya, kasus percabangan sering kita jumpai dalam kehidupan sehari-hari. Simak ilustrasi berikut.

"Setiap hari, Ibu selalu pergi ke pasar untuk membeli bahan makanan. Ibu selalu mengutamakan untuk membeli daging ayam di pasar. Jika daging ayam tidak tersedia, maka Ibu akan membeli tempe sebagai pengganti, lalu memasaknya."

    ==================================================================================================================================================

    Ibu pergi ke pasar ----------------------> Apakah Daging Ayam Tersedia ? ---> Iya (True) ---> Ibu membeli daging ayam ---> Ibu memasak daging ayam
                                                        |
                                                        |
                                                        |
                                                        Tidak (False) ---> Ibu membeli tempe ---> Ibu memasak tempe

    ==================================================================================================================================================

Layaknya ilustrasi di atas, setiap kondisi akan mengembalikan nilai true atau false. Dengan nilai boolean ini, Anda dapat menentukan instruksi selanjutnya. Misalnya, jika ayam tersedia (bernilai true), maka ibu akan membeli ayam dan memasaknya. Jika ayam tidak tersedia (bernilai false), maka ibu akan membeli tempe dan memasaknya.

Mari ubah ilustrasi di atas menjadi kode program Python. 
'''

print(" Percabangan ".center(150, ("-")), "\n")
# Ilustrasi di atas dapat dituliskan sebagai berikut.
print("> Contoh Percabangan ", "\n")

ketersediaan = "Daging Ayam"

if ketersediaan == "Daging Ayam":
    print("Ibu membeli daging ayam, lalu memasaknya", "\n")
else:
    print("Ibu membeli tempe, lalu memasaknya")

print("|" * 50, "\n")

'''
Output :
Ibu membeli daging ayam, lalu memasaknya

Kode di atas merupakan program percabangan. Jika variabel "ketersediaan" bernilai "Daging ayam", maka akan mengembalikan string "Ibu membeli daging ayam, lalu memasaknya". Kita bisa asumsikan variabel "ketersediaan" sama seperti ketersediaan bahan makanan dari pasar yang ibu kunjungi. Jika pasar tersebut menyediakan "Daging ayam", variabel tersebut bernilai "Daging ayam".

    ==================================================================================================

    Ketersediaan = "Daging Ayam" -------------------------------------> Pasar menyediakan "Daging ayam"

    ==================================================================================================

Jika daging ayam tidak tersedia di pasar, maknanya variabel "ketersediaan" akan bernilai kosong atau bernilai bahan makanan lain. Dengan begitu, jika variabel "ketersediaan" tidak memiliki nilai "Daging ayam", variabel ketersediaan tidak lagi memenuhi kondisi "if ketersediaan == 'Daging ayam'". Jadi, program akan mengembalikan teks atau string "Ibu membeli dan memasak tempe".

Ingat bahwa Python adalah bahasa pemrograman case-sensitive, hal ini berlaku juga pada percabangan. Buktikan sendiri dengan mengubah "Daging ayam" menjadi "Daging Ayam". Apakah output program masih sama?

Dalam ilustrasi di atas, kita paham bahwa percabangan melibatkan if dan else statement. Anda dapat mengasumsikan statement sebagai instruksi. Selain if dan else statement, sebenarnya Python masih memiliki satu statement lagi yang sering digunakan, yakni elif. Mari kita pelajari satu per satu.
'''


#
# =========================================================== If Statement ======================================================================
print(" If Statement ".center(45, ("-")), "\n")
'''
                                                                If

If adalah statement Python yang akan mengecek nilai variabel di dalamnya memenuhi kriteria suatu kondisi atau tidak. Jika memenuhi kriteria, kondisi tersebut bernilai true. Jika tidak memenuhi kriteria, kondisi akan bernilai false. Jika kondisi if bernilai true, kode yang berada dalam blok kode if akan dieksekusi.
    ======================================================================

    if kondisi:
        # Blok kode yang akan dieksekusi jika kondisi bernilai benar(True)
    
    ======================================================================

Perlu diingat bahwa if merupakan blok kode. Jadi, Anda perlu memperhatikan indentasi untuk menjalankan kode, seperti yang ditunjukkan gambar.
'''

# Mari tinjau implementasi if pada kode di bawah ini.
print("> Contoh If Statement ", "\n")
nilai = 100

if nilai >= 80:
    print("Lulus dengan nilai", nilai, "\n")

'''
Output :
Lulus dengan nilai 100

Pada kode di atas, program akan mengecek nilai dari variabel "nilai". Kondisi yang harus terpenuhi adalah "if score >= 80" atau bisa diartikan nilai dari variabel "nilai" harus bernilai lebih besar sama dengan "80". Program lalu mengecek variabel dan mengevaluasi nilainya berdasarkan kondisi yang harus dipenuhi. 

Pada kode di atas, dikarenakan variable nilai mengandung int 100 maka kondisi sudah terpenuhi alias benar (True) dikarenakan kondisinya adalah jika variable nilai lebih besar sama dengan 80 maka benar(True). Jadi, kode yang berada dalam blok kode if akan dieksekusi yang menghasilkan output Lulus dengan nilai 100.

Hal lain yang perlu diperhatikan adalah Python menganggap setiap nilai kosong (zero) dan null sebagai False. Sebaliknya, nilai yang tidak kosong (non-zero) dan tidak null (non-null) akan bernilai True. Untuk lebih mengetahui maksudnya, mari lihat kode berikut. 
'''

print("> Contoh nilai kosong ")
print('''
if x:
    print("Ini True")

Output nya kosong bukan :)
''')

x = ""

if x: 
    print("Ini True") 

'''
Output :

Outputnya kosong. Pada baris pertama kode program di atas, variabel "x" diinisialisasikan dengan string kosong "". Kemudian if statement mengevaluasi variabel "x" dan menghasilkan nilai salah (False). Hal ini terjadi karena variabel "x" berisi string kosong dan Python mengevaluasinya sebagai False. Sebab hasil kondisinya adalah False, blok kode dalam if tidak dijalankan.

Beberapa nilai yang dianggap sebagai false oleh Python sebagai berikut.

    1. Nilai yang sudah didefinisikan bernilai salah: None dan False.
    2. Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
    3. Urutan (sequence) dan koleksi (collection) yang kosong: "", (), {}, set(), range(0).

Selain nilai di atas, Python akan menganggap semua nilai sebagai true.

Tolong Kalian Liat ini :

    Terakhir, if statement memiliki versi one-liner-nya. Ini memungkinkan Anda untuk membuat kode if dalam bentuk single statement atau satu baris, tanpa perlu memperhatikan indentasi dan membuat blok kode.
'''

print("> Contoh One-liner If Statement ")
nama = "Bagas"

print('''
if name == "Bagas": print("Bagas memang ganteng gileee abiee") 
''')
if nama == "Bagas": print("Bagas memang ganteng gileee abiezzz", "\n")
print("|" * 50, "\n")

'''
Output :
Bagas memang ganteng gileee abiezzz

Kode program di atas merupakan program yang sama dengan contoh pertama sebelumnya. Perhatikan bahwa kode "print()" disimpan setelah tanda titik dua ":". Program tidak menganggap itu sebagai kesalahan sehingga dapat menghasilkan output yang diharapkan, yakni teks/string "Bagas memang ganteng gileee abiezzz".
'''



# =========================================================== Else Statement ======================================================================
print(" Else Statement ".center(45, ("-")), "\n")
'''
                                                                Else

Else adalah statement yang menjadi jalan keluar saat kondisi atau hasil evaluasi if statement bernilai false. Maksudnya adalah program akan menjalani blok kode if terlebih dahulu dan jika hasilnya adalah false, program akan menjalankan else statement sebagai jalan keluar atau kondisi terakhir.

Jika kita gabungkan if dan else, struktur berikut akan dihasilkan.

    if kondisi:
        # Blok kode yang akan dieksekusi jika kondisi bernilai benar(True)
    else:
        # Blok kode yang akan dieksekusi jika kondisi bernilai salah(False)

Perhatikan gambar di atas, secara sekuensial program akan menjalankan kondisi if statement terlebih dahulu. Jika hasil kondisi adalah true, blok kode dalam if statement akan dieksekusi. Namun, jika kondisi if statement bernilai false, else statement akan dijalankan dan blok kode dalam else statement akan dieksekusi. 

Else termasuk statement bersifat opsional. Umumnya, else statement digunakan ketika memiliki kondisi terakhir saat semua kondisi tidak terpenuhi. Mari tinjau penerapannya dalam kasus Pembuatan SIM di indonesia yang di batasi usia.
'''

print("> Contoh Else Statement", "\n")
umur = 16

if umur >= 18:
    print(f"selamat kamu bisa mengikuti pembuatan SIM, di karenakan umur kamu {umur} tahun")
else:
    print(f"Maaf kamu belum bisa mengikuti pembuatan SIM, di karenakan umur kamu {umur} tahun", "\n")

''' 
Output :

Maaf kamu belum bisa mengikuti pembuatan SIM, di karenakan umur kamu 16 tahun

Pada kode diatas, program akan mengecek umur dari variabel "umur". Kondisi yang harus terpenuhi adalah "if age >= 18" atau bisa diartikan umur dari variabel "umur" harus bernilai lebih besar sama dengan "18". Program lalu mengecek variabel dan mengevaluasi nilainya berdasarkan kondisi yang harus dipenuhi. kamu juga bisa menggunakan input untuk lebih mudah di pahami, tetapi pada contoh kali ini saya malas untuk menggunakan input. 

Apabila Anda memiliki pertanyaan seperti “bagaimana jika kondisi else statement tidak terpenuhi?” Jawabannya adalah kondisi else statement sudah pasti terpenuhi karena merupakan jalan keluar terakhir dalam suatu percabangan. Anda harus menggunakan else statement sebagai kondisi terakhir dalam percabangan dan bukan kondisi ke-2, kondisi ke-3, dan seterusnya. 

Jika ingin menambah kondisi baru, seperti kondisi ke-2, kondisi ke-3, dan seterusnya, jangan gunakan else statement. Untuk hal itu, Anda bisa menggunakan elif statement.
'''



# =========================================================== Elif Statement ======================================================================
print(" Elif Statement ".center(45, ("-")), "\n")
'''
                                                                Elif
Elif merupakan kependekan dari else if dan alternatif untuk if bertingkat atau switch case. Elif statement berada pada posisi setelah if. Anda dapat menambahkan elif statement lebih dari satu karena tidak dibatasi dan opsional.

Struktur keseluruhan percabangan jika kita gabungkan antara if, elif, dan else adalah berikut.

    if kondisi:
        # Blok kode yang akan dieksekusi jika kondisi1 bernilai benar(True)
    elif kondisi:
        # Blok kode yang akan dieksekusi jika kondisi1 bernilai benar(True)
    else:
        # Blok kode yang akan dieksekusi jika kedua kondisi bernilai salah(False)

Perhatikan gambar di atas, secara sekuensial program akan menjalankan if statement terlebih dahulu. Jika kondisinya bernilai true, blok kode di dalamnya akan dieksekusi. Jika kondisinya false, elif statement akan dijalankan. 

Jika kondisi elif statement menghasilkan true, blok kode di dalamnya akan dieksekusi. Kondisi else statement akan dijalankan dan kode di dalamnya akan dieksekusi jika semua kondisi sebelumnya salah atau menghasilkan false.
'''

# Mari tinjau penerapannya pada kasus penilaian tugas siswa. 
print("> Contoh Elif Statement", "\n")
nilai = 30

if nilai >= 90 and nilai <= 100:
    print("Selamat KING!, Kamu berhak mendapatkan nilai A")
elif nilai >= 70 and nilai <= 89:
    print("Selamat Pangeran, Kamu mendapatkan nilai B")
elif nilai >= 50 and nilai <= 69:
    print("Tetap Semangat dan terus belajar, Kamu mendapatkan nilai C")
elif nilai >= 30 and nilai <= 49:
    print("Walaweeee cok, Ini nilai apa tempe", "\n")
else:
    print("Gausah kuliah jang, mancing we sana dahar jeung asin nya")

print("|" * 50, "\n")

'''
Output :
walaweeee cok, Ini nilai apa tempe

Program di atas merupakan contoh dari penerapan if, else dan elif statement. Program akan mengecek nilai dari variabel "nilai". 

    1. Kondisi pertama yang harus terpenuhi adalah "if score >= 90 and score <= 100" atau bisa diartikan nilai dari variabel "nilai" harus bernilai lebih besar sama dengan "90" dan kecil sama dengan "100". Jika kondisi terpenuhi, program akan menampilkan teks "Selamat KING, Kamu berhak mendapatkan nilai A".

    2. Kondisi kedua yang harus terpenuhi adalah "elif score >= 70 and score <= 89" atau bisa diartikan nilai dari variabel "nilai" harus bernilai lebih besar sama dengan "70" dan kecil sama dengan "89". Jika kondisi terpenuhi, program akan menampilkan teks "Selamat Pangeran, Kamu mendapatkan nilai B".

    3. Kondisi ketiga yang harus terpenuhi adalah "elif score >= 50 and score <= 69" atau bisa diartikan nilai dari variabel "nilai" harus bernilai lebih besar sama dengan "50" dan kecil sama dengan "69". Jika kondisi terpenuhi, program akan menampilkan teks "Tetap Semangat dan terus belajar, Kamu mendapatkan nilai C".  

    4. Kondisi keempat yang harus terpenuhi adalah "elif score >= 30 and score <= 49" atau bisa diartikan nilai dari variabel "nilai" harus bernilai lebih besar sama dengan "30" dan kecil sama dengan "49". Jika kondisi terpenuhi, program akan menampilkan teks "Walaweeee cok, Ini nilai apa tempe".

    5. Kondisi kelima yang harus terpenuhi adalah "else" atau bisa diartikan jika semua kondisi sebelumnya salah atau menghasilkan false maka else ini yang akan di eksekusi, program akan menampilkan teks "Gausah kuliah jang, mancing we sana dahar jeung asin nya".
'''


# ============================================================ Ternary Operators ===================================================================
print(" Ternary Operators ".center(150, ("-")), "\n")
'''
                                                                Ternary Operators

Ternary operators termasuk conditional expressions pada Python. Conditional expressions adalah bentuk ekspresi yang bertujuan untuk mengevaluasi kondisi dan mengembalikan nilai berdasarkan hasil evaluasinya. Anda bisa asumsikan bahwa ternary operators ini merupakan versi one-liner dari if dan else. 

Untuk memahaminya perhatikan ilustrasi berikut.

    ======================================================================

    -------------------------- if else statemnt --------------------------
    if kondisi:
        # Blok kode yang akan dieksekusi jika kondisi bernilai benar(True)
    else:
        # Blok kode yang akan dieksekusi jika kondisi bernilai salah(False)

    -------------------------- Ternary Operators --------------------------

    Blok_kode_jika_benar: if kondisi else blok_kode_jika_salah 

    ======================================================================

Ternary operators dibangun dengan menempatkan "blok kode jika benar" pada posisi awal, lalu diikuti oleh "if statement" serta "kondisi"-nya. Kemudian "else statement" ditempatkan di akhir beserta dengan "blok kode jika salah".
'''

# Mari lihat implementasinya.
print("> Contoh Ternary Operators", "\n")
nilai = 30

print("Kamu sangat jelek dan bodo guoablok") if nilai <= 30 else print("Sealamat king daripada mendapatkan nilai 30 wkwkkw", "\n")

'''
Output :

Kamu sangat jelek dan bodo guoablok

Kode program di atas menampilkan pesan teks "Ya Allah, kamu meni bodo" jika kondisi bernilai true dan ketika kondisi salah maka akan menampilkan pesan teks "Sealamat king daripada mendapatkan nilai 30 wkwkkw". Jika kita transformasikan menjadi bentuk blok, berikut adalah kodenya.

    if nilai <= 30:
        print("Kamu sangat jelek dan bodo guoablok")
    else:
        print("Sealamat king daripada mendapatkan nilai 30 wkwkkw")

Kode di atas merupakan program yang sama dengan contoh sebelumnya. Program akan menampilkan pesan teks "Kamu sangat jelek dan bodo guoablok" jika kondisi bernilai true dan menampilkan pesan teks "Selamat king daripada mendapatkan nilai 50 wkwkkw" jika kondisi bernilai false. Silakan telaah secara perlahan untuk memahami maksudnya. 

Perlu diingat bahwa tujuan dari one-liner bukanlah sekadar untuk memudahkan kode dibaca karena hanya dibuat dalam satu baris, melainkan untuk membuat kode menjadi lebih singkat dan jelas.

Opsi lain dari ternary operators adalah melibatkan tuple.

   -------------------------- Ternary Tuples --------------------------

    (Blok_kode_jika_benar): (blok_kode_jika_salah, blok_kode_jika_benar)[kondisi]

Perhatikan bahwa pada ternary tuples kita menggunakan indeks ke-0 tuples sebagai kode jika kondisi salah, sedangkan indeks ke-1 sebagai kode jika kondisi benar. 

Atau sederhananya begini 

    tuple[condition]

    1. condition adalah ekspresi yang menghasilkan True atau False.
    2. Jika condition bernilai True, maka elemen dengan indeks 1 yang dipilih.
	3. Jika condition bernilai False, maka elemen dengan indeks 0 yang dipilih.
'''

# Mari lihat implementasi ternary tuples di bawah ini.
print("> Contoh Ternary Tuples", "\n")
KTP = "Ada"

# Tuple ternary untuk kategori nilai
category = ("Antum harus membuat KTP terlebih dahulu ya!", "Silahkan antum bisa langsung pinjol")[KTP == "Ada"]  # Jika KTP == ada, pilih "Silahkan antum bisa langsung pinjol", jika tidak, pilih "Antum harus membuat KTP terlebih dahulu ya!"
print(category) 

'''
Output :

Silahkan antum bisa langsung pinjol

Kode program di atas menampilkan pesan teks "Silahkan antum bisa langsung pinjol" jika kondisi bernilai True dan menampilkan pesan teks "Antum harus membuat KTP terlebih dahulu ya!" jika kondisi bernilai false. Jika kita ubah menjadi blok kode IF, berikut penerapannya.

    if KTP == "Ada":
        print("Silahkan antum bisa langsung pinjol")
    else:
        print("Antum harus membuat KTP terlebih dahulu ya!"

Perlu diingat oleh Anda, ternary tuples sebaiknya dihindari terutama untuk kode dan klausa true/false yang kompleks. Komunitas Python sendiri menganggap bahwa cara ternary tuples ini kurang "pythonic" atau "tidak Python banget!" karena cukup membingungkan untuk meletakkan kondisi saat True atau False.
'''


