'''
                                        Penanganan Kesalahan (Error Handling and Exception Handling)

Saat Anda membuat program, sering kali menemukan setidaknya dua jenis kesalahan berdasarkan kejadiannya.

    1. Kesalahan sintaks (syntax errors) atau sering disebut juga sebagai kesalahan penguraian (parsing errors). 
    2. Pengecualian (exceptions) atau sering disebut juga sebagai kesalahan saat beroperasi (runtime errors). 

Mari kita bahas satu per satu jenis kesalahan tersebut.

    1.  Kesalahan Sintaks (Syntax Errors)
        Kesalahan sintaks (syntax errors) adalah jenis kesalahan yang terjadi ketika Python tidak mengerti perintah Anda. Ini mengakibatkan pesan kesalahan muncul sebelum program tersebut berjalan. 

        Salah satu tipe kesalahan sintaks yang sering ditemui adalah kesalahan indentasi (IndentationError). Berikut contoh kodenya.

            if 9>10:
            print("Hello World!")

            ===========================================
            Output:
            File "/home/glot/main.py", line 2
                print("Hello World!")
                    ^
            IndentationError: expected an indented block
            ===========================================
        
        Pada contoh di atas, program memunculkan pesan error "IndentationError" karena seharusnya terdapat indentasi sebelum sintaks "print()". Perhatikan bahwa secara langsung Python menunjukkan baris indentasi dengan memberi tanda panah ke atas atau dikenal dengan caret "^".

        Tipe kesalahan yang sering dijumpai selanjutnya adalah kesalahan sintaksis (SyntaxErrors). Berikut contoh kodenya.

            i = 1
            while i<3
                print("Dicoding")
                i+=1

            ===================================
            Output:
              File "/home/glot/main.py", line 2
                while i<3
                         ^
            SyntaxError: invalid syntax
            ===================================

        Pada tipe kesalahan sintaksis (syntax errors) program akan memunculkan pesan error "SyntaxError". Program pun memberi petunjuk bahwa terdapat sintaks yang tidak valid berada di posisi i<3. Dapatkah Anda menemukan kesalahannya? Ya, kesalahannya adalah tidak terdapat tanda titik dua ":" setelah while statement.

        Jika kita tela'ah lebih dalam, kedua contoh tersebut memiliki tipe kesalahan yang berbeda. Contoh pertama menampilkan kesalahan indentation error dan kedua adalah syntax error. Kemudian setelah penyebutannya terdapat pesan detail kesalahan atau keterangan yang diberikan, misalnya sintaks yang tidak valid.

        Secara umum struktur kesalahan sintaks sebagai berikut.

            File "<file name>", line <nomor baris>
                <baris kode dengan kesalahan>
                            ^
            <tipe kesalahan>: <pesan kesalahan>
        
        Mari bedah satu per satu poin di atas.

        1. "<nama file>" merupakan file Python yang Anda eksekusi. Jika Anda menggunakan mode script melalui lokal komputer dan program Anda menghasilkan Error, pesan ini akan memunculkan nama script atau file Python Anda. 
        2. <nomor baris> merupakan nomor baris kode dalam file Anda yang mengalami kesalahan. 
        3. <baris kode> merupakan kode yang mengalami kesalahan dalam file Anda. 
        4. <tipe kesalahan> merupakan kelompok atau tipe kesalahan yang Anda alami, contohnya SyntaxError dan IndentationError.
        5. <pesan kesalahan> merupakan pesan detail kesalahan atau keterangan yang diberikan oleh program. Contohnya adalah “invalid syntax” dan “expected an indented block”.


    2.  Pengecualian (Exceptions)
        Pengecualian adalah kesalahan yang terjadi ketika Python mengerti perintah Anda, tetapi mendapatkan masalah saat mengikutinya. Umumnya, pengecualian bisa terjadi ketika aplikasi sudah mulai beroperasi.

        Jenis kesalahan ini paling sering ditemui ketika Anda membuat kode program yang kompleks. Meskipun kode atau ekspresi dari Python yang Anda tulis sudah benar, ada kemungkinan terjadi kesalahan ketika perintah tersebut dieksekusi. 

        Mari lihat contoh kode pengecualian di bawah ini.

            print(angka)

            
            Output:
            Traceback (most recent call last):
              File "/home/glot/main.py", line 1, in <module>
                print(angka)
            NameError: name 'angka' is not defined
            
        Contoh kode di atas merupakan tipe kesalahan yang menunjukkan bahwa program tersebut tidak mendefinisikan variabel "angka". Jenis kesalahan ini terjadi ketika Anda tidak melakukan deklarasi dan inisialisasi variabel, tetapi langsung memanggil variabel tersebut. Program juga menampilkan keterangan atau pesan detail setelah memberi tahu tipe kesalahannya. 

        Mari lihat contoh pengecualian selanjutnya.

            bukan_angka = '1'
            bukan_angka + 2
            
            
            output:
            traceback (most recent call last):
            File "/home/glot/main.py", line 2, in <module>
               bukan_angka + 2
            typeError: can only concatenate str (not "int") to str

        Pada contoh di atas, program memunculkan kesalahan karena variabel "bukan_angka" termasuk tipe data string. Di sisi lain, program berusaha melakukan operasi aritmetika yang mengharuskan kedua variabel atau operan bertipe data integer. Pesan tipe kesalahan yang dimunculkan adalah TypeError dengan keterangan atau pesan detailnya adalah "can only concatenate str (not "int") to str".

        Jika Anda telaah lebih dalam, struktur pengecualian hampir sama dengan struktur kesalahan sintaks. Namun, terdapat perbedaan di sana, pengecualian memberikan pesan "traceback (most recent call last)". 

        Pesan ini mengacu pada informasi yang ditampilkan ketika terjadi kesalahan atau pengecualian (exception). Pesan traceback ini menyediakan "jejak" dari kode yang dieksekusi sehingga Anda dapat melacak kembali jalur eksekusi program sebelum mencapai titik error.
    

    3. Penanganan Pengecualian
        Lalu, bagaimana menangani kesalahan atau pengecualian tersebut? Program Python yang Anda bangun dapat dilengkapi penanganan terhadap pengecualian dari tipe kesalahan yang Anda tentukan. Konsep ini dikenal dengan exceptions handling yang menggunakan pernyataan try-except untuk menangani pengecualian tersebut.

        Mari lihat jenis pengecualian yang berbeda dari contoh sebelumnya. Kali ini, pengecualiannya adalah kesalahan pembagian angka dengan nol.

            z = 0
            print(1/z)

            Output:
            Traceback (most recent call last):
              File "/home/glot/main.py", line 2, in <module>
                print(1/z)
            ZeroDivisionError: division by zero

        Pada contoh di atas, program memunculkan error karena melakukan operasi aritmetika pembagian dengan nilai nol. Kita tahu bahwa pembagian dengan nilai nol tidak bisa dilakukan karena tidak terdefinisikan (undefined). Perhatikan bahwa tipe pengecualian yang terjadi adalah "ZeroDivisionError".

        Kita bisa lakukan penanganan terhadap pengecualian tersebut dengan menggunakan pernyataan try-except. Berikut strukturnya

            try:
                # Blok kode yang mungkin saja terjadi pengecualian.
            expect:
                # Pertanyaan yang dioperasikan jika terjadi pengecualian.

        Anda bisa simpan kode yang dibuat di dalam "try" statement. Kode tersebut merupakan barisan kode yang mungkin terjadi pengecualian. Ada pun statement "except" adalah statement yang akan digunakan ketika pengecualian tersebut terjadi. 

        Sederhananya, program akan mencoba (try) mengeksekusi kode yang berada dalam try statement. Lalu jika terjadi pengecualian, kode yang berada pada except statement akan dieksekusi.

        Mari lihat penerapannya pada contoh berikut.
'''

print("> Contoh penerapan try statement", "\n")
z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.", "\n")

"""
Output:
Anda tidak bisa membagi angka dengan nilai nol.

Pada contoh di atas, program akan menjalankan try statement terlebih dahulu dengan mengeksekusi sintaks "print(1/z)". Kita tahu bahwa program tersebut akan mengalami error "ZeroDivisionError". Alih-alih program menampilkan pesan "ZeroDivisionError: division by zero", kita ingin program menampilkan teks "Anda tidak bisa membagi angka dengan nilai nol.”

Kita simpan pernyataan "ZeroDivisionError" setelah except statement. Dengan begini, kita memerintahkan program untuk mengeksekusi kode dalam except jika pengecualian "ZeroDivisionError" terjadi. Kode dalam except tersebut menampilkan pesan "Anda tidak bisa membagi angka dengan nilai nol."

Sebenarnya, struktur lengkap dari pernyataan try tidak hanya melibatkan except. Berikut adalah struktur lengkap pernyataan try.

    try:
        # Blok kode yang mungkin saja terjadi pengecualian.
    expect:
        # Pertanyaan yang dioperasikan jika terjadi pengecualian.
    else:
        # Pertanyaan yang dioperasikan jika TIDAK terjadi pengecualian.
    finally:
        # Pertanyaan yang dioperasikan setelah semua pertanyaan di atas terjadi.

Struktur lengkap seperti ini biasanya diterapkan ketika Anda membangun program atau aplikasi yang lebih kompleks. 

Pada try statement, program akan menjalankan blok kode yang mungkin terjadi pengecualian. Pada except statement, program akan mengeksekusi statement ini jika terjadi pengecualian. Pada else statement, program akan mengeksekusi statement ini jika tidak terjadi pengecualian. Pada finally statement, program akan mengeksekusi statement ini setelah semua pernyataan di atas terjadi.

Mari lihat contoh penerapannya di bawah ini, contoh tersebut merupakan program untuk menampilkan key dalam tipe data dictionary. Jenis pengecualian yang akan dilakukan adalah KeyError dan TypeError. Kita akan coba untuk mengakses value dictionary dari key yang tidak ada dan mencoba mengoperasikan value dictionary tersebut yang termasuk string dengan operasi aritmetika. Untuk pengingat, dictionary merupakan tipe data yang melibatkan key-value. 

Mari mulai dengan kondisi yang tidak menampilkan error.
"""

print("> Contoh penerapan Struktur Lengkap try statement", "\n")

var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")
    
"""
Output:
rata-rata adalah 1.0
Kode ini dieksekusi jika tidak ada exception.
Kode ini dieksekusi terlepas dari ada atau tidaknya exception.

Pada contoh di atas, langkah pertama yang dilakukan adalah melakukan inisialisasi variable "var_dict" dengan nilai dictionary. Lalu, kita mencoba mengakses value dari key "rata_rata". Program di atas tidak menimbulkan error karena kita memberikan sintaks yang benar untuk mengakses value berdasarkan key, yakni var_dict['rata_rata'].

Perlu diperhatikan bahwa else statement ikut dieksekusi disebabkan pengecualian tidak terjadi (Error Exception tidak ada). Selain itu, finally statement akan selalu dieksekusi baik jika ada pengecualian ataupun tidak.

Bagaimana membangkitkan KeyError dan TypeError? Perhatikan langkah berikut.

    1. Untuk membangkitkan KeyError, ubah kode "print(f"rata-rata adalah {var_dict['rata_rata']}") " dengan kode " print(f"rata-rata adalah {var_dict['ratarata']}")  ". Anda bisa langsung copy-paste kode tersebut. 

        1. Dengan mengubah kode tersebut, program akan menampilkan KeyError. Hal ini terjadi karena kita mengakses key "ratarata", padahal seharusnya adalah "rata_rata".
        2. Perhatikan bahwa else statement tidak dieksekusi, karena exception atau pengecualian terjadi. Hal ini dibuktikan dengan tidak adanya teks "Kode ini dieksekusi jika tidak ada exception".

    2. Untuk membangkitkan TypeError, ubah kode "print(f"rata-rata adalah {var_dict['rata_rata']}") " dengan kode " print(f"rata-rata adalah {var_dict['rata_rata']/2}")  ". Anda bisa langsung copy-paste kode tersebut. 

        1. Dengan mengubah kode tersebut, program akan menampilkan TypeError. Hal ini terjadi karena kita melakukan operasi aritmetika terhadap value dari key "rata_rata" yang merupakan tipe data string.
        2. Perhatikan bahwa else statement tidak dieksekusi, karena exception atau pengecualian terjadi. Hal ini dibuktikan dengan tidak adanya teks "Kode ini dieksekusi jika tidak ada exception".
"""

'''
                                                            Raise Exception

Jika sebelumnya kita menangani kesalahan yang TIDAK DISENGAJA, kali ini kita akan mempelajari cara menangani kesalahan yang DISENGAJA. Umumnya, ketika membuat kode program kita ingin membatasi program tersebut dengan kondisi tertentu.

Perlu diingat bahwa umumnya, raise digunakan bersamaan dengan if-else statement.

Misalnya, Anda ingin membuat kode program untuk menampilkan angka dari 1 hingga 10 berdasarkan input atau masukan pengguna. Namun, dalam program tersebut kita ingin mengontrol dengan cara berikut: jika user memberikan input berupa bilangan negatif, program akan memunculkan pesan error dengan keterangan "Bilangan negatif tidak diperbolehkan".

Mari lihat penerapannya di bawah ini. Asumsikan user memasukkan input berupa bilangan "-1".

    var = -1
    if var < 0:
        raise ValueError("Bilangan negatif tidak diperbolehkan")
    else:
        for i in range(var):
            print(i+1)
        
    Traceback (most recent call last):
      File "/home/glot/main.py", line 3, in <module>
        raise ValueError("Bilangan negatif tidak diperbolehkan")
    ValueError: Bilangan negatif tidak diperbolehkan

    Pada contoh di atas, kita menggunakan percabangan untuk melakukan evaluasi jika nilai variabel "var" adalah bilangan negatif (kurang dari 0), program akan menampilkan error dengan teks "Bilangan negatif tidak diperbolehkan". Selain itu, program akan mengeksekusi else statement jika nilai dari variabel "var" bukanlah bilangan negatif (lebih besar atau sama dengan 0).

    Ke depannya, Anda bisa mengontrol flow program yang Anda bangun dengan melibatkan error dan exceptions handling. Terutama ketika Anda membangun program yang lebih kompleks.
'''

input_user = int(input("Silahkan masukan bilangan negatif guys: "), "\n")

if input_user < 0:
    raise ValueError("HEI BADZINGAN BILANGAN NEGATIF TIDAK DIPERBOLEHKAN")
else :
    print("Keren Bingit Luhk")

'''
Output: 

Traceback (most recent call last):
  File "/cloudide/workspace/Learning-Python/06_Control_Flow/06_3_Penanganan_Kesalahan/main.py", line 236, in <module>
    else :
        ^^^
ValueError: HEI BADZINGAN BILANGAN NEGATIF TIDAK DIPERBOLEHKAN

Pada contoh di atas, kita menggunakan percabangan untuk melakukan evaluasi jika nilai variabel "var" adalah bilangan negatif (kurang dari 0), program akan menampilkan error dengan teks "Bilangan negatif tidak diperbolehkan". Selain itu, program akan mengeksekusi else statement jika nilai dari variabel "var" bukanlah bilangan negatif (lebih besar atau sama dengan 0).

Ke depannya, Anda bisa mengontrol flow program yang Anda bangun dengan melibatkan error dan exceptions handling. Terutama ketika Anda membangun program yang lebih kompleks.
'''
