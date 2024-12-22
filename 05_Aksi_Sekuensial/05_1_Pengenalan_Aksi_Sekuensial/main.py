import datetime as dt 
print(" Pengenalan Aksi Sekuensial ".center(150, ('=')) + "\n")
'''
Selama Anda mempelajari beberapa materi pertama kelas ini, Anda telah membuat banyak program sederhana. Namun, program yang Anda buat masih terdiri dari satu atau dua baris kode saja. Ke depannya, Anda akan membuat kode program yang tidak hanya terdiri dari satu baris, tetapi bisa banyak baris dan lebih kompleks.Kali ini, Anda akan mempelajari cara komputer menjalankan kode program yang kompleks dan memiliki banyak baris. Ini adalah modal dasar Anda untuk paham hal tersebut. 

Dalam bahasa pemrograman Python, program yang Anda buat akan dijalankan secara sekuensial. Apa maksudnya? Kode yang Anda bangun akan berjalan sesuai dengan urutan perintahnya. Aksi sekuensial sendiri memiliki makna sebagai sederetan instruksi yang akan dijalankan oleh komputer berdasarkan urutan penulisannya. Dengan kata lain, program yang Anda bangun haruslah memiliki awal dan akhir. Jadi, ketika program tersebut dijalankan, bisa diketahui waktu berakhirnya. Simak kode di bawah ini untuk melihat implementasinya.
'''

# print("WELCOME MATE IN THE CLUB WE ARE SADLY".center(50))
# print("Tolong Masukan Data Diri Terlebih Dahulu".center(50) + '\n')

# nama = input("Sialahkan kawan masukan nama anda disini : ")
# mimpi = input("Masukan mimpi kamu menjadi apa \t\t : ")
# tahunLahir = int(input("Masukan Tahun Lahir Anda \t\t : "))

# umur = 2024 - tahunLahir

# print(f"""
# Selamat datang {nama} di Club Para Developer Pemula, Umur kamu per 2024 ini adalah {umur} Tahun. 
# Kamu diterima karena mimpimu yang sangat revolusioner""" + "\n")
# print("Terima Kasih telah bergabung dengan komunitas kami! Horassss!")

''' 
Output :
WELCOME MATE IN THE CLUB WE ARE SADLY       
Tolong Masukan Data Diri Terlebih Dahulu 

Selamat datang Bagas di Club Para Developer Pemula, Umur kamu per 2024 ini adalah 22 Tahun. 
Kamu diterima karena mimpimu yang sangat revolusioner

Terima Kasih telah bergabung dengan komunitas kami! Horassss!


    1. Komputer akan menjalankan kode pertama dengan menampilkan teks "WELCOME MATE IN THE CLUB WE ARE SADLY".

    2. Setelah berhasil, kode kedua akan dijalankan dengan menampilkan teks "Tolong Masukan Data Diri Terlebih Dahulu."

    3.Lalu, kode ketiga akan dijalankan. Program akan meminta Anda memasukkan nama sembari memunculkan teks "Silahkan kawan masukan nama anda disini : ".      Input ini akan disimpan pada variabel bernama "nama".

    4.Kemudian, kode keempat akan dijalankan. Program akan meminta Anda memasukkan mimpi sembari memunculkan teks "Masukan mimpi kamu menjadi apa : ". Input ini akan disimpan pada variabel bernama mimpi.

    5.Kemudian, kode kelima akan dijalankan. Program ini akan meminta Anda memasukan Tahun lahir sembari memunculkan teks "Masukan tahun lahir anda : ". Input ini akan disimpan pada variable tahunLahir.

    6.Setelah itu, variabel tahun_lahir akan dikalkulasikan untuk mengetahui umur Anda per tahun 2024. Hasil kalkulasi tersebut disimpan pada variabel umur.

    7. Program akan memunculkan teksSelamat datang {nama} di Club Para Developer Pemula, Umur kamu per 2024 ini adalah {umur} Tahun. 
    Kamu diterima karena mimpimu yang sangat revolusioner""" + "\n") Dengan {nama} dan {umur} merupakan nilai dari variabel dengan nama yang sama.
    
    8. Program ditutup dengan memunculkan teks "Terima Kasih telah bergabung dengan komunitas kami! Horassss!"

    Keseluruhan kode tersebut menggambarkan bahwa program akan dijalankan berdasarkan urutan perintahnya. Perlu diperhatikan bahwa terdapat program yang akan berubah hasilnya jika urutan baris instruksinya diubah. Ada juga program yang hasilnya TIDAK akan berubah jika urutan baris instruksinya diubah.
'''

# Mari kita pahami satu per satu. Simak kode di bawah ini untuk melihat contoh jika urutan baris diubah, TIDAK mengubah hasil eksekusi.
print("Contoh jika urutan baris di ubah")
a = 10
b = 15
 
result = a + b
print(f"Hasilnya adalah = {result}")
 
"""
Output:
25

Program di atas merupakan kode sederhana untuk melakukan operasi penjumlahan antar variabel a dan b. Nilai dari variabel a adalah 10 dan nilai dari variabel b adalah 15. Hasil dari operasi tersebut akan disimpan pada variabel "result". 
"""

# Sekarang mari kita ubah urutan inisialisasi variabel. 
print("Contoh mengubah urutan inisialisasi variabel.")

a = 15
b = 10

# Perhatikan bahwa urutan inisialisasi variabel a dan b sekarang diubah.
result = a + b
print(f"Hasilnya adalah = {result}")

"""
Output:
25

Program tersebut memunculkan hasil kalkulasi yang sama meskipun urutan inisialisasi variabel a dan b diubah.
"""

# Bagaimana dengan urutan instruksi yang mengubah hasil? Simak kode di bawah ini.
print("Contoh urutan instruksi yang mengubah hasil")

a = 15
b = 10

print(b//3)
print(a**2)

''' 
Output :
3 
225

Kode di atas merupakan program yang sama dengan kode sebelumnya. Namun, hasil yang didapat berbeda karena Anda mengubah urutan sintaks "print()". 

Sampai di sini Anda paham program yang akan mengubah hasil dan tidak akan mengubah hasil. Ini penting dipahami karena akan membantu menemukan kesalahan sintaks ketika Anda membuat program kompleks.
'''



