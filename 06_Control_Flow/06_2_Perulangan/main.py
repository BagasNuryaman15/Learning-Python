from typing import Counter

print("\n"," Perulangan ".center(150, "="))
# ============================================================= Perulangan =============================================================
'''
                                                                Perulangan

Dalam kehidupan sehari-hari, sering kali kita menemui situasi yang harus dilakukan berulang kali. Misalnya dalam skenario berikut. 

"Di suatu hari yang indah, ada seorang mahasiswa yang bernama bagas yang sedang mengerjakan soal UAS mata kuliah matematika. Bagas seorang yang tidak mengerti matemtika dia bodoh dalam hal itu, tetapi bagas sudah belajar pada malam harinya. Bagas mengerjakan UAS nya dengan tenang dan manly, UAS tersebut memiliki 5 soal yang harus di jawab oleh bagas dengan benar. Bagas telah mengerjakan 5 soal tersebut. Tetapi untuk memastikan jawabannya benar maka bagas harus mengcek semua jawaban bagas, apakah benar atau tidak?."

Pada skenario berikut, UAS memiliki 5 soal yang harus dijawab dengan benar oleh bagas. Setelah bagas mengerjakan ke 5 soal tersebut dia harus mengcek jawabannya kembali, untuk memastikan apakah jawaban dia benar atau salah, jika benar dia akan kumpulkan kepada pengawas lalu pulang, jika tidak bagas akan terus mengecek jawabannya hingga benar. 

Kita ilustrasikan dengan ilustrasi yang sederhana.

    ====================================================================================================================================

    Mengecek ke 5 soal dan jawaban --------------------> Apakah jawabannya benar? -----------------------> Jawabannya benar, bagas pulang
                    |                                              |
                    |                                              |
                    |                                              |
                    |                                              |
                    <------------------------------------------ Tidak   

    ====================================================================================================================================

Perhatikan pada diagram di atas, bagas akan selalu selalu melakukan aktivitas berulang untuk mengecek jawaban hingga kondisinya terpenuhi. Kondisi yang dimaksud adalah jawaban bagas yang benar. 

Dalam pemrograman, kita juga akan sering menemui masalah serupa yang mengharuskan untuk melakukan kode berulang. Contohnya menampilkan angka 1 hingga 10.

    print(1)                                    1
    print(2)                                    2       
    print(3)                                    3
    print(4)                                    4           
    print(5)                           Output : 5 
    print(6)                                    6   
    print(7)                                    7
    print(8)                                    8           
    print(9)                                    9           
    print(10)                                   10

Pada kode di atas, program menampilkan angka dari 1 hingga 10 menggunakan sintaks yang berulang. Terlihat tidak efektif, bukan? Itulah yang menjadi tujuan dari materi perulangan ini, Anda akan belajar untuk membuat kode program yang efektif dan mudah dibaca oleh programmer lain.

Dalam Python, ada beberapa sintaks atau statement untuk melakukan perulangan. 
'''
print(" Jenis Jenis Perulangan ".center(100, "-"), "\n")


print(" 1. Foor Loop ".center(100, "-"), "\n")
# ============================================================= For =============================================================
'''
                                                              for loop

For termasuk sintaks dalam Python yang bersifat definite iteration. Definite iteration adalah sebuah proses iterasi atau perulangan ketika jumlah pengulangannya ditentukan secara eksplisit sebelumnya.

Format dari perulangan for sebagai berikut.

    for <variable> in <iterable>:
        <statement(s)>

<iterable> merupakan segala object dalam Python yang dapat diiterasi seperti list, tuple, hingga string. Ada pula <variable> merupakan variabel yang akan mengambil elemen berikutnya dari <iterable> setiap kali iterasi berjalan.

Mari lihat penerapannya di bawah ini.
'''

print("> Contoh penerapan Foor Loop")
var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in var_list:
    print(f"Iterasi -----> {i}", "\n")
        

"""
Output:
Iritasi -----> 1
Iritasi -----> 2
Iritasi -----> 3
Iritasi -----> 4
Iritasi -----> 5
Iritasi -----> 6
Iritasi -----> 7
Iritasi -----> 8
Iritasi -----> 9
Iritasi -----> 10


Kode di atas merupakan program yang bertujuan untuk menampilkan angka dari 1 hingga 10 berdasarkan variable list yang sudah diinisialisasikan sebelumnya. Perhatikan bahwa program di atas sebenarnya sama dengan program pada contoh sebelumnya. Jika contoh sebelumnya menggunakan sintaks "print()" yang berulang, program di atas menggunakan sintaks atau statement for.

Pada program di atas, kita melakukan perulangan untuk menampilkan angka dari 1 hingga 10 yang sebelumnya telah diinisialisasikan pada variabel "var_list". Setiap iterasi atau perulangan yang berjalan, "i" akan mengambil elemen dari "var_list" satu per satu. Lalu, blok kode "print(i)" akan dijalankan dengan nilai "i" adalah nilai yang sudah diambil sebelumnya.

Anda juga bisa menggunakan tipe data string sebagai object <iterable>, silakan ubah variable "var_list" di atas dengan string apa pun yang Anda inginkan. Hasilnya program akan menampilkan setiap huruf dari string tersebut.

Anda juga dapat melakukan perulangan berdasarkan panjang suatu nilai dengan menggunakan fungsi "range()".
"""

# Contoh penggunaan range pada for loop
print("> Contoh penggunaan range() pada foor loop")

for a in range(5):
    print(a, "\n")

'''
Output: 
0
1
2
3
4

Jika Anda perhatikan lebih baik, program di atas menampilkan angka dari 0 hingga 4 padahal kita menentukannya 5. Mengapa itu terjadi? Pada dasarnya, "range()" adalah fungsi bawaan dalam Python yang akan menghasilkan urutan bilangan dimulai dari indeks ke-0.

Sintaksis umum dari fungsi "range()" sebagai berikut.

    range(start,stop,step)

Berikut adalah penjelasan detail terkait fungsi "range()".

    1. "Start" merupakan nilai awal dari urutan bilangan yang bersifat opsional, jika Anda tidak memasukkannya, nilai awal akan dianggap 0. 
    2. "Stop" merupakan nilai batas yang wajib dimasukkan. Urutan akan berhenti sebelum mencapai nilai "stop" (eksklusif). 
    3. "Step" merupakan nilai penambahan antara setiap dua bilangan dalam urutan yang bersifat opsional. Jika nilai tersebut tidak diberikan, secara default nilai yang dimasukkan adalah 1.

Di bawah ini contoh implementasinya. 

    for i in range(1,10,2):
    print(i)

    Output:
    1
    3
    5
    7
    9
    
Pada program di atas, kita menampilkan bilangan ganjil yang dimulai dari 1 hingga 10. Perhatikan bahwa program di atas mendefinisikan nilai "1" sebagai "start", nilai "10" sebagai "stop", dan nilai "2" sebagai "step". Ingat bahwa "stop" bersifat eksklusif, yang artinya nilai terakhirnya tidak akan disertakan. 

Dengan begitu, program di atas akan menampilkan kode dari 1 hingga 10 dengan setiap bilangan ke-2 dan kelipatannya akan dilewati atau tidak dicetak.
'''



# ============================================================= While ============================================================
print(" 2. While Loop ".center(100, "-"), "\n")
'''
                                                                While
While termasuk sintaks dalam Python yang bersifat indefinite iteration. Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.

Format dari perulangan while sebagai berikut.

    while kondisi:
        # blok pertanyaan yang akan diulang selama kondisi bernilai True.

Kondisi merupakan ekspresi yang akan dievaluasi dan menghasilkan nilai true atau false. Selama hasil evaluasi bernilai true, program akan terus berjalan hingga menghasilkan nilai false.

Berikut implementasinya.
'''

# Contoh penerapan while loop
print("> Contoh penerapan while loop")

counter = 1
while counter <= 7: 
    print(counter, "\n")
    counter += 1

'''
Output:
1
2
3
4
5
6
7

Pada contoh di atas, kita menggunakan perulangan "while" untuk menampilkan angka 1 hingga 7. Variabel "counter" diinisialisasi dengan nilai 1 sebelum perulangan dimulai. Ini artinya perulangan akan dimulai dari 1 berdasarkan nilai variabel tersebut. Perulangan lalu berjalan dengan mengevaluasi variabel "counter" yang memiliki nilai "1". Hasil dari evaluasi tersebut bernilai true sehingga blok kode di dalamnya akan dijalankan.

Perhatikan bahwa kita menggunakan jenis ekspresi uner untuk melakukan increment. Increment adalah pola untuk menambahkan suatu variabel dengan nilai tetap. Dengan hal ini, setiap perulangan bernilai true maka variabel "counter" akan terus ditambah dengan nilai "1". Pada perulangan di atas, nilai variabel "counter" akan bertambah hingga nilainya adalah "7". Ketika nilai variabel "counter" menyentuh "7" maka hasil evaluasi akan bertambah menjadi "8", tetapi angka 8 tersebut tidak memenuhi kondisi "<=7" sehingga kode print() tidak akan dijalankan dan hanya akan memunculkan angka hingga 7.

Namun, Anda harus berhati-hati untuk tidak melakukan infinite loop, yakni sebuah kondisi ketika perulangan tidak berhenti karena tidak memenuhi kondisi yang diinginkan. Contohnya adalah ketika melakukan perulangan, kita tidak memberikan increment yang menyebabkan variabel atau counter tidak akan memenuhi kondisi while.

    counter = 1
    while counter <= 5:
        print(counter)

Pada contoh di atas, kita melakukan perulangan while, tetapi tidak melakukan increment di baris akhir kode. Hal ini menyebabkan program akan terus berjalan dan akhirnya berhenti karena run time exceeded atau waktu berjalan melebihi yang ditentukan. 

Jika Anda menjalankan kode di atas pada IDE seperti notebook, program akan terus berjalan dan harus dihentikan dengan menekan CTRL + C.
'''



# ============================================================= For Bersarang ============================================================
print(" 3. For Bersarang (nested loop) ".center(100, "-"), "\n")
'''
                                                                For Bersarang

Ketika Anda membuat perulangan, sering kali menemukan perulangan dalam perulangan atau disebut sebagai nested loop. 

Format dari nested loop sebagai berikut.

    for variable_luar in itarable_luar:
        for variable_dalam in itarale_dalam:
            # blok pertanyaan yang akan diulang

Anda dapat asumsikan bahwa ada dua perulangan, yakni "perulangan luar" dan "perulangan dalam". Program akan melakukan "perulangan luar" terlebih dahulu, lalu akan melakukan "perulangan dalam". "variabel_luar" akan mengambil nilai dari "iterable_luar", sedangkan "variabel_dalam" akan mengambil nilai dari "iterable_dalam".
'''

# Mari kita lihat implementasi dari for bersarang.
for i in range(1, 4):
    for j in range(1, 3):
        print(f"Ini adalah loop_luar = {i} dan loop_dalam --> {j}")

'''
Output :
Ini adalah loop_luar = 1 dan loop_dalam --> 1
Ini adalah loop_luar = 1 dan loop_dalam --> 2
Ini adalah loop_luar = 2 dan loop_dalam --> 1
Ini adalah loop_luar = 2 dan loop_dalam --> 2
Ini adalah loop_luar = 3 dan loop_dalam --> 1
Ini adalah loop_luar = 3 dan loop_dalam --> 2

Pada contoh implementasi di atas, kita melakukan perulangan for luar dengan variabel "i" yang mengulang dari 1 hingga 3. Lalu melakukan perulangan "j" yang akan mengulang dari 1 hingga 3 juga.

            for i in range(1, 4) ------------------------------------------------------------------------
            ---- for j in range(1, 3)                                                                    = Outer Loop
Inner Loop  = ---- print(f"Ini adalah loop_luar = {i} dan loop_dalam --> {j}")---------------------------


Output :
                        ----Ini adalah loop_luar = 1 dan loop_dalam --> 1
                        |   Ini adalah loop_luar = 1 dan loop_dalam --> 2
 Hasil Outer Loop ----> |   Ini adalah loop_luar = 2 dan loop_dalam --> 1 ------> Hasil Inner Loop
                        |   Ini adalah loop_luar = 2 dan loop_dalam --> 2
                        |   Ini adalah loop_luar = 3 dan loop_dalam --> 1
                        ----Ini adalah loop_luar = 3 dan loop_dalam --> 2
    
Output dari sebelah kiri dihasilkan dari perulangan for luar, sedangkan output dari sebelah kanan dihasilkan dari perulangan for dalam. Perhatikan lebih detail bahwa "perulangan luar" atau outer loop akan dilanjutkan jika "perulangan dalam" atau inner loop telah selesai. Semua perulangan tersebut dilakukan hingga kedua perulangan menghasilkan false dan berhenti.
'''



# ========================================================== Kontrol Perulangan ============================================================
print("\n")
print(" 4. Kontrol Perulangan ".center(100, "-"), "\n")
'''
                                                                Kontrol
                                                               Perulangan

Selain membuat perulangan, kita juga dapat mengontrol perulangan dengan menggunakan beberapa pernyataan di antaranya sebagai berikut.

    1. Break
    Break statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya. Jika Anda memiliki perulangan yang bertingkat seperti for bersarang, break akan menghentikan perulangan sesuai dengan tingkatan atau letak perulangannya berada.
    2. Continue
    Continue statement adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya. Continue seolah mengabaikan pernyataan    (statement) yang berada antara continue hingga akhir blok.
    3. Else Setelah For Pada Python juga dikenal else setelah for yang berfungsi untuk perulangan bersifat pencarian. Else setelah for ini bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan.
    4. Else setelah While Berbeda dengan else setelah for, pada statement else setelah while, blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah. 
    5. Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun. Dengan kata lain, pass digunakan untuk menghindari error saat Anda belum menulis kode di dalam blok tertentu (seperti di dalam fungsi, loop, atau kondisi), tetapi Anda ingin kode tersebut tetap ada.
    6. List comprehension adalah cara yang lebih singkat dan elegan untuk membuat list baru dengan cara mengiterasi elemen dari iterable lain (seperti list, tuple, string, atau range), dan menerapkan operasi atau kondisi tertentu pada elemen-elemen tersebut. Secara umum, list comprehension memungkinkan Anda membuat list baru dalam satu baris kode, yang sebelumnya mungkin memerlukan beberapa baris menggunakan loop biasa.

    Sintaks dasar list comprehension adalah sebagai berikut:

       [expression for item in iterable if condition]

    •	expression: Ini adalah ekspresi yang akan diterapkan pada setiap elemen dari iterable.
	•	item: Variabel yang mewakili setiap elemen dari iterable.
	•	iterable: Objek yang dapat diiterasi (seperti list, string, atau range).
    •   Kalau kondisi pasti sudah kalian tau lah ya.
'''

# =================== Break Statement =================
# Contoh Break statement
print(" 1. Break Statement ".center(50, ("-")), "\n")
print("> Contoh penggunaan break statment", "\n")

for i in range(1, 3):
    for j in range(1, 11):
        print(f"Loop Luar = {i} -----> Loop Dalam = {j}")
        if j == 5:
            break # Ini artinya untuk menghentikan perulangan Loop Dalam jika Loop dalam == 5

'''
Output :

Loop Luar = 1 -----> Loop Dalam = 1
Loop Luar = 1 -----> Loop Dalam = 2
Loop Luar = 1 -----> Loop Dalam = 3
Loop Luar = 1 -----> Loop Dalam = 4
Loop Luar = 1 -----> Loop Dalam = 5
Loop Luar = 2 -----> Loop Dalam = 1
Loop Luar = 2 -----> Loop Dalam = 2
Loop Luar = 2 -----> Loop Dalam = 3
Loop Luar = 2 -----> Loop Dalam = 4
Loop Luar = 2 -----> Loop Dalam = 5

Pada kode di atas, kita melakukan perulangan untuk menampilkan bilangan 1 hingga 3 pada "perulangan luar" atau for pertama. Lalu, kita membuat perulangan kedua untuk menampilkan bilangan dari 1 hingga 11. Namun, pada perulangan kedua atau "perulangan dalam" tersebut, kita akan melakukan break jika bertemu angka 5. Alhasil, perulangan dalam hanya akan menampilkan angka hingga 1 sampai 5 saja. Program akan berhenti karena ada statement break yang diberikan jika bertemu angka 5.
'''

# Contoh lainnya sebagai berikut.
print("\n")
print("> Contoh penggunan break statement dengan string(str)", "\n")

for huruf in "Bagas Ga Ganteng":
    if huruf == " ":
        break
    print('Huruf saat ini: {}'.format(huruf))

'''
Output :
Huruf saat ini: B
Huruf saat ini: a
Huruf saat ini: g
Huruf saat ini: a
Huruf saat ini: s

Pada contoh di atas, program akan berhenti jika bertemu huruf " " (spasi) yang berada pada teks "Bagas Ga Ganteng". Ini menunjukan bahwa BAGAS tuh GANTENG ABIEZZ! 
'''




# ================== Continue Statement =================
print("\n")
print(" 2. Continue Statement ".center(50, ("-")), "\n")
print("> Contoh penggunaan continue statment", "\n")

# Contoh Penerapan Break Statement
for h in "Bagas Jelek Ganteng".split():
    if h == "Jelek":
        continue
    print(f"Iterasi Huruf Saat Ini = {h}")

''' 
Output :

Iterasi Huruf Saat Ini = Bagas
Iterasi Huruf Saat Ini = Ganteng

Pada contoh di atas, kita membuat perulangan yang sama dengan contoh sebelumnya. Namun, sekarang kita menambahkan split() kepada string yang menyebabkan huruf dalam string menjadi kelompok list, dan kita menggunakan continue untuk membuat program melanjutkan dan melewati kata "Jelek". 
'''



# ================== Else setelah for =================                                                
print("\n")
print(" 3. Else setelah for ".center(50, ("-")), "\n")
print("> Contoh penggunaan Else setelah for", "\n")

# Contoh penerapan Else setelah for
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num == 10:
        print("Oh ini dia ada angkanya, program dihentikan!")
        break # Loop dihentikan karena angka 10 ditemukan

else: 
    print("Waduh kak mohon maaf angka tidak di temukan nih") # Hanya dijalankan jika tidak ada `break`

'''
Output :

Waduh kak mohon maaf angka tidak di temukan nih

Pada contoh di atas, kita membuat program untuk melakukan pencarian terhadap bilangan 10. Jika bilangan 10 tersebut merupakan elemen atau nilai yang berada pada list, program akan berhenti dan menampilkan teks "Oh ini dia ada angkanya, program dihentikan!".

Namun, pada contoh di atas angka 10 bukan merupakan elemen dari list maka program akan menampilkan teks "Waduh kak mohon maaf angka tidak di temukan nih". Apa jadinya jika program menemukan angka? Silakan ganti "if num == 10" dengan "if num == 2" atau angka lain yang merupakan nilai yang berada dalam list.

Perlu diperhatikan oleh Anda, if dan else pada contoh tersebut berkaitan walaupun berbeda blok. Pada else setelah for, statement else tidak akan dieksekusi saat if pernah sekali saja benar. Dengan kata lain, break dalam if tidak akan terjadi untuk memicu else setelah for. Jadi pada intinya break tidak akan mempengaruhi else karena else setelah for mempunyai sifat Digunakan untuk menjalankan sesuatu setelah semua iterasi pada loop for selesai tanpa break. Sangat berguna, misalnya, untuk mengecek apakah semua item dalam iterasi telah diproses.
'''



# ================== Else setelah while =================   
print("\n")
print(" 4. Else setelah while ".center(50, ("-")), "\n")
print("> Contoh penggunaan Else setelah while", "\n")

# Contoh penerapan Else setelah for
target = 5
guess = 0
attempts = 0
max_attempts = 3
guessed_correctly = False  # Flag untuk menandai jika angka telah ditebak

while guess != target:
    if attempts >= max_attempts:
        print(f"Program dihentikan! Anda telah mencoba sebanyak {attempts} kali.")
        break
    
    guess = int(input("Tebak angka (1-10): "))
    attempts += 1
    
    if guess == target:
        print(f"Selamat! Anda menebak dengan benar dalam {attempts} percobaan.")
        guessed_correctly = True  # Tandai bahwa angka telah ditebak
        break
    elif guess > 1000:
        print("Angka terlalu besar, coba angka di bawah 1000.")
    else:
        print("Silahkan coba lagi sampai berhasil.")
        quest = input("Apakah ingin melanjutkan [y/n]? ").lower()
        if quest == "n":
            print(f"Program dihentikan! Anda telah mencoba sebanyak {attempts} kali.")
            break
else:
    if not guessed_correctly:
        print(f"Anda telah mencapai batas percobaan ({max_attempts}) tanpa menebak angka yang benar.")

'''
Kapan Blok else Dieksekusi?

Blok else pada while dieksekusi jika loop berhenti karena kondisi menjadi False, bukan karena perintah break.
	•	Kasus: Menebak dengan benar
	    •	Jika Anda menebak angka dengan benar (guess == target), program akan masuk ke perintah break.
	    •	Karena ada break, blok else tidak akan dijalankan.
	    •	Namun, jika else tetap dieksekusi, itu terjadi karena break tidak benar-benar menghentikan eksekusi else.
	•	Kasus: Mencapai batas percobaan
	    •	Jika Anda mencapai batas percobaan tanpa menebak angka dengan benar (attempts >= max_attempts), loop dihentikan oleh break.
	    •	Blok else juga tidak dijalankan karena ada break.

while tersebut masih bernilai benar walaupun program keluar karena "break". 
'''


# ================== Pass Statement ================== 
print("\n")
print(" 5. Pass Statement ".center(50, ("-")), "\n")
print("> Contoh penggunaan Pass Statment", "\n")

# Contoh penerapan pass statement
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

"""
Output:


Program di atas tidak menampilkan apa pun karena jika kondisi terpenuhi, program tidak akan melakukan apa pun.

Statement pass digunakan dalam situasi-situasi ketika Python memerlukan adanya pernyataan, tetapi tidak memiliki tindakan yang perlu dilakukan pada saat itu. Biasanya itu adalah kondisi ketika Anda membutuhkan placeholder untuk menunjukkan bahwa tidak ada operasi yang perlu dilakukan. Hal ini dapat membantu kita mengatur struktur kode secara rapi dan memungkinkan penambahan implementasi di kemudian hari.
"""



# ================== List Comprehension ==================
print("\n")
print(" 6. List Comprehension ".center(50, ("-")), "\n")
print("> Contoh penggunaan List Comprehension", "\n")

# Contoh penerepan List Comprehension yang umum tanpa kondisi
print("= Contoh Dengan Non Kondisi", "\n")
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat, "\n")

'''
Output:
[1, 4, 9, 16]
'''

# Contoh penerapan List Comprehension dengan kondisi
print("= Contoh Dengan Kondisi", "\n")
penggabungan = [(angka1, angka2) for angka1 in range(3) for angka2 in range(1, 4)]
for angka1, angka2 in penggabungan:
    print(f"Iterasi Perulangan Luar -----> {angka1} dan Iterasi Perulangan Dalam {angka2}")

 





