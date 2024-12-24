print(" Functions Anonim (Lambada Expression) ".center(150, "="), "\n")
'''
                                                                                    Functions Anonim (Lambada Expression

Terakhir, mari kita pelajari cara membuat fungsi tanpa mendeklarasikan def. Cara ini dikenal dengan ekspresi lambda yang digunakan untuk membuat fungsi tanpa perlu menyebutkan def ketika membuatnya. Anda bisa mengasumsikan fungsi anonim ini sebagai fungsi one-liner. Secara umum, struktur fungsi anonim sebagai berikut.

    functions = lambada args: ret_val

    Kita akan menggunakan ekspresi lambda untuk melakukan operasi layaknya def didefinisikan.

    def func(args):
        return ret_val

    ini setara dengan: 
    func = lambada args: ret_val

    Nama fungsi (func) setara dengan nama variabel yang digunakan untuk menyimpan ekspresi lambda, args adalah argumen yang dibutuhkan untuk dioperasikan, dan ret_val merupakan nilai yang kita kembalikan (return).

    Perhatikan contoh di bawah ini. Mari kita ubah contoh fungsi mencari luas persegi panjang menjadi fungsi anonim.
'''

# Contoh penerapan Lambada Expression
print("> Contoh Penerapan Lambada Expression\n")

# Contoh
pembagian = lambda angka1, angka2: angka1 // angka2
hasil = pembagian(24, 2)
print(hasil, "\n")

'''
    Output: 
    12

    Pada contoh kode di atas, kita membuat fungsi dengan nama "pembagian" yang menjadi nama variabel. Argumen yang digunakan adalah angka1 dan angka2, kita mendefinisikan ini tepat setelah pernyataan lambda. Lalu, kita menambahkan isi fungsi, yaitu angka1 // angka2 dan hasilnya merupakan return value. Terakhir, pemanggilan pada fungsi anonim sama seperti biasanya.

    Isi fungsi dalam lambda dapat Anda ganti menjadi sebuah nilai, alih-alih variabel. Hal ini karena umumnya bertujuan untuk melakukan operasi sederhana dan perlu melibatkan fungsi yang tidak terlalu kompleks hingga perlu menggunakan def. 

    Silakan ganti panjang*lebar dengan nilai integer yang Anda mau untuk mengetahui maksud dari pernyataan di atas. 

    Sebuah fungsi lambda dapat menerima argumen dalam jumlah berapa pun, tetapi hanya mengembalikan satu nilai ekspresi. Dalam contoh di atas, Anda bisa menambahkan argumen selain panjang dan lebar, tetapi hanya bisa menggunakan satu operasi, yaitu angka1 // angka2.
'''


# ============================================================================ Variabel Global dan Lokal ==========================================================
print(" Variable Global dan Lokal ".center(70, "-"), "\n")
'''
                                                                                Variabel Global dan Lokal

Dalam Python, ada konsep "scope" yang mengatur jangkauan variabel dan fungsi dalam suatu program. Konsep ini lebih dikenal sebagai scope variable yang mengacu pada wilayah di dalam program tempat variabel dapat diakses dan digunakan.

Ada dua jenis scope yang umum dijumpai, khususnya ketika Anda membuat fungsi dan program yang lebih kompleks.

    1.  Variable Global
        Suatu variabel yang didefinisikan di luar fungsi atau blok kode apa pun dan dapat diakses dari seluruh bagian program. Mari lihat penerapannya di bawah ini, asumsikan bahwa kita membuat sebuah fungsi penjumlahan dengan satu nilai yang sudah ditetapkan, yaitu 10.
'''

# Contoh dari Variable Global seperti yang sudah di bahas pada materi di atas
print("~ 1. Variable Global \n> Contoh penerapan Variable Global\n")

# Contoh 
angka = 180

def add(b):
    hasil = angka ** b
    return hasil

bilanganPertama = add(3)
print(f"Hasilnya akan seperti ini:\n= {bilanganPertama}\nIni adalah contoh variable global\n")

'''
    Output:
    5832000

    Pada contoh di atas, kita mendeklarasikan variabel a dan menginisialisasikannya dengan nilai 180. Pada tahap ini, kita menetapkan bahwa variabel a merupakan variabel global dan dapat digunakan pada seluruh bagian program yang kita buat.

    Selanjutnya, fungsi penjumlahan didefinisikan dan akan menjumlahkan variabel a yang telah dibuat dengan bilangan yang dapat kita tentukan. Pada contoh di atas, kita mempangkatkan variabel a bernilai 180 dengan nilai 3 dan hasilnya adalah 583200.
'''

'''
    2.  Variable Lokal
        Variabel ini didefinisikan dalam suatu fungsi atau blok kode tertentu. Jenis ini hanya dapat diakses dari dalam fungsi atau blok kode tempat variabel tersebut didefinisikan. Mari lihat contohnya di bawah ini, asumsikan bahwa kita membuat fungsi untuk penjumlahan yang menerima dua bilangan untuk dijumlahkan. Namun, kali ini setiap dua bilangan tersebut dioperasikan akan dikurangi oleh lokal variabel bernilai 10.
'''

# Contoh dari Variable Lokal seperti yang sudah di bahas pada materi di atas
print("~ 2. Variable Lokal \n> Contoh Variable Lokal\n")

# Contohnya 
def kacau(a, b):
    lokal_Rrq = 10
    result = a + b - lokal_Rrq
    return result

bilangan1 = kacau(10, 50)
print(f"Maka hasilnya akan dikurangi oleh Variable Lokal = {bilangan1}")

'''
    Output :
    50

    Pada contoh di atas, kita mendefinisikan fungsi penjumlahan bernama "kacau" dengan dua parameter, yakni a dan b. Dalam fungsi tersebut, kita mengoperasikan penjumlahan antara a dan b lalu dikurangi variabel lokal bernama "lokal_Rrq" dengan nilai 10.

    Ingat bahwa variabel lokal hanya dapat diakses dari dalam fungsi atau blok kode tempat variabel tersebut didefinisikan. Silakan coba cetak ke layar "lokal_Rrq" menggunakan fungsi print(). Salin dan tempel kode berikut ke dalam program di atas tepat setelah perintah print(bilanganPertama).

        print(lokal_Rrq)

    Apa output yang dikeluarkan? Program akan menampilkan pesan error bahwa "lokal_var is not defined". Hal ini karena variabel tersebut kita definisikan dalam fungsi dan hanya dapat digunakan dalam fungsi tersebut.
'''
