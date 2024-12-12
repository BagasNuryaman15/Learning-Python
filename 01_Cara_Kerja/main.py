# ---------------------------------------What Is Python?----------------------------------------
import time
start_time = time.time()
print ("Apa itu Python?. Python adalah bahasa perogramaan high level lenguage (Bahasa Pemrogramaan Tingkat Tinggi) yang dirancang mudah untuk dipelajari dan digunakan. Pyhton ini didirikan oleh Guido Van Rosuum dan dirilis pada tahun 1991. Python dikenal karena sintaksnya yang sederhana, sehingga memudahkan pemula sekaligus cukup kuat untuk proyek-proyek besar. Python ini disebut karena kecepatannya untuk mengolah data yang cepat, tidak membutuhkan file compiled karena Python adalah bahasa pemrogramaan yang interpreted. Nah apa sih inrepreted itu")

# Menjelaskan apa itu Interpreted dan Interpreter Python
print ("Interpreted Language adalah bahasa yang kode sumbernya dijalankan langsung barris demi baris oleh sebuah program khsusus yang disebut interpreter. Berbeda dengan bahasa yang dikompilasi seperti C atau C++, yang harus dikompilasi menjadi kode mesin sebelum dijalankan, bahasa interpreted tidak melalui proses kompiilasi terlebih dahulu.")

# Menjelaskan apa itu interpreter di Python
print ("Apa itu Interpreter Python?. Interpreter Python adalah program yang membaca dan menjalankan kode Python secara langsung. Interpreter menerjamahkan setiap baris kode Python menjadi intruksi yang dapat dihapami oleh mesin atau sistem operasi")

# Cara Kerja Interpreter Python
print ("Nah disini cara kerja dari interpreter Python adalah Membaca kode sumber Python yang bisa kamu tuliskan di file yang berujung (.py) nanti file tersebut akan di terjamahkan oleh interpreter baris demi baris. Lalu interpreter menerjamahkan setiap baris menjadi kode mesin (bahasa yang dimengerti oleh komputer yaitu binary code), lalu tahap akhir adalah interpreter memunculkan hasil dari kode kode tersebut menjadi sebuah nilai yang sudah kita tuliskan dan menampilkannya di layar anda sendiri atau bisa dibilang tahapan terakhir ini bisa dibilang dengan exsekusi.")

# Contoh lainmya dari cara kerja Python
print ("Kita pasti mengetahui sebelum membuat sebuah kode untuk kita tuliskan dan menjadikannya intruksi kepada komputer maka kita perlu sebuah file yang berujung (.py) nah itu bisa disebut dengan Source Code yaitu suatu file yang berisikan tentang kode intruksi untuk mengoperasikan sistem komputer. Nah setelah kamu menuliskan sebuah kode di file tersebut maka kamu akan melihat hasilnya kan dan kamu akan menjalankannya. Nah dari proses kamu menjalankan lalu muncul feedback atau tampil di komputer kamu, dibelakangnya terjadi sebuah proses yang bernama interpreter atau interpreted language yang dimana interpreter adalah semacam terjamaah kode kita menjadi sebuah kode yang dapat dikenali oleh komputer kita, nah kalau di Python penerjemah nya tuh Python itu sendiri atau interpreter Python lalu dieksekusi dan dimunculkan atau dijalankan diterminal.")

# Perbedaan antara Interpreted dan Compiled
print ("Nah compiled merupakan program khusus seperti Interpreted tetapi compiled ini digunakan oleh bahasa permorgramaan C++ dan masih banyak lagi. Perbedaanya dengan Interpreted adalah jika interpreted langsung diterjemaahkan dari baris ke baris dan dieksukusi secara langsung, nah jika Compiled memerlukan sebuah kompilasi terlebih dahulu sebelum di eksekusi jadi, misalkan kita punya sebuah file maka file tersebut akan di kompiilasi terlebih dahulu menjadi file baru atau masuk kedalam file yang berujung .exe atau bisa disebut executable yang dimana didalam nya ada kode binary. ")

# Rule Penulisan atau Penjalanan kode di Python 
print ("Di Python ini menampilkan sebuah kode secara berurutan atau dieksekusi sesuai awal dan akhir sebuah kode, jadi kita tidak bisa secara acak menuliskan sebuah kode karena Pyhton menerjamaahkan secara baris per baris dan mengeksekusi nya juga baris perbaris sampai muncul di sebuah layar atau terminal.")

# Contoh 
print ("Contoh jika ingin kita menuliskan terlebih dahulu hello dan setelahnya world maka terminal atau layar akan menampilkan terlebih dahulu hello nya dan di baris kedua world nya. Tetapi jika ingin menambahkan atau menampilkan kode secara bersamaan maka kita harus menulisnya bersamaan juga contoh hello world")

print ("Hello")
print ("World")
print ("Hello World") # Maka hasilnya akan sejajar tidak seperti pada contoh diatas yang hasilnya akan saling bertumpukan.

# Rule baris pada Python 
print ("Baris kosong tidak akan mempengerauhi ke program kita dan tidak akan di eksekusi jadi langsung ke kode yang kita buat")

# Comentar pada Python
print ("Komentar juga tidak akan di eksekusi seperti contoh nya # pada setiap Title yang sudah saya buat di atas dengan mengugnakan komentar atau (#), dan komentar juga kita bisa gunakan untuk mengasih komentar pada sisi variable nya nanti saya coba contohkan dibawah. Komentar juga berguna untuk kita yang ingin membuat atau ngasih informasi agar kita tidak lupa, dan bisa memberikan informasi apa yang kita sedang kerjakan atau bisa memberikan sebuah informasi bahwa ada beberapa content dalam projek kita. Tidak hanya menggunakan (#) tapi kita juga bisa menggunakan comment multi line dengan menggunakan Tanda Kutip 2 garis sebanyak tiga klai)")

a = 10 # A ini merupakan variable dan 10 merupakan sebuah value nya

b = 12 # Sama seperti di atas

print(a)
print(b)

# Python juga bisa kita gunakan untuk compiled sebuah file jadi kita bisa gunakan bytcode juga dengan cara dibawah ini
print ("Perlu kita ketahui terlebih dahulu bytcode sama seperti file .exe. Cara kerjnya adalah merubah source code yang berisi syntax dalam bahasa inggris lalu kita harus melewati proses compile dan akan menjadi sebuah file dengan format bytcode. Apa sih keunggulan compile ke bytcode, seperti yang sudah dijelaskan padda materi di atas bahwa compile itu bisa lebih cepat di eksekusi karena dia menerjamaahkan terlebih dahulu ke dalam sebuah file lalu semua file tersebut akan di tampilkaan beda halnya dengan interpreter yang menerjamaahkan dengan satu baris per baris.")

print ("Cara compiled nya dengan kita menuliskan di terminal (python3 -py_compile main.py)")

# Test Kecepatan Compile dan Interpreted
print(time.time() - start_time, "Detik")

# Terbukti bahwa compile itu lebih cepat


