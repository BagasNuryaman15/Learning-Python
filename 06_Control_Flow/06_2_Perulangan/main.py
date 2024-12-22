from typing import Counter


print("\n"," Perulangan ".center(150, "="))
# ================================================================================= Perulangan =============================================================
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
        print(f"Ini adalah variable_luar = {i} dan variable_dalam --> {j}")

'''
Output :
Ini adalah variable_luar = 1 dan variable_dalam --> 1
Ini adalah variable_luar = 1 dan variable_dalam --> 2
Ini adalah variable_luar = 2 dan variable_dalam --> 1
Ini adalah variable_luar = 2 dan variable_dalam --> 2
Ini adalah variable_luar = 3 dan variable_dalam --> 1
Ini adalah variable_luar = 3 dan variable_dalam --> 2

Pada contoh implementasi di atas, kita melakukan perulangan for luar dengan variabel "i" yang mengulang dari 1 hingga 3. Lalu melakukan perulangan "j" yang akan mengulang dari 1 hingga 3 juga.

            for i in range(1, 4) ------------------------------------------------------------------------
            ---- for j in range(1, 3)                                                                    = Outer Loop
Inner Loop  = ---- print(f"Ini adalah variable_luar = {i} dan variable_dalam --> {j}") ------------------

    
Output dari sebelah kiri dihasilkan dari perulangan for luar, sedangkan output dari sebelah kanan dihasilkan dari perulangan for dalam. Perhatikan lebih detail bahwa "perulangan luar" atau outer loop akan dilanjutkan jika "perulangan dalam" atau inner loop telah selesai. Semua perulangan tersebut dilakukan hingga kedua perulangan menghasilkan false dan berhenti.
'''





