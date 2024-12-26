'''
                                                                                Pengecekan Style Guide PEP8

Sampai dengan saat ini, Anda tentu sudah menuliskan kode pemrograman Python cukup banyak, termasuk di antaranya kode yang Anda tulis mengalami kesalahan sintaksis atau indentasi. Lalu, bagaimana agar ke depannya bisa mencegah hal tersebut terjadi?

Semua itu bergantung pada kode editor yang Anda gunakan untuk menulis kode Python, terkadang ada beberapa kode editor yang sudah dilengkapi dengan fitur pengecekan kemungkinan kesalahan dan memformat kode sesuai arahan gaya penulisan (style guide) PEP8, seperti PyCharm. Ada juga kode editor, seperti Visual Studio Code yang menyediakan plugin tambahan untuk membantu pengecekan kemungkinan kesalahan dan memformat kode.

PEP atau Python Enhancement Proposals merupakan panduan yang telah menjadi acuan untuk perkembangan Python. Salah satu panduan tersebut membahas mengenai arahan gaya penulisan (style guide) yang baik dan benar ketika Anda ingin membangun kode menggunakan Python. Panduan tersebut adalah PEP8 yang berjudul "Style Guide for Python Code".

Tujuan dari panduan ini agar kode Anda lebih mudah dibaca dan dipahami oleh programmer lain serta menghindari kemungkinan kesalahan yang akan muncul.

Pada materi kali ini, kita akan mempelajari beberapa aplikasi yang dapat Anda gunakan dengan memanggil perintah atau sebaiknya diintegrasikan ke editor kode yang Anda pakai. Tujuannya untuk membantu Anda mengecek kemungkinan kesalahan dan kesesuaian dengan PEP8.

    1.  Lint
        Lint adalah proses pengecekan kode atas kemungkinan terjadi kesalahan (error), termasuk dalam proses ini adalah mengecek kesesuaian terhadap arahan gaya penulisan kode (style guide) PEP8. Aplikasi yang digunakan untuk proses ini disebut linter. 

        Integrasi linter dengan editor kode Anda akan membuat efisien dalam menulis kode Python. Pertimbangan ini karena keluaran atau output dari aplikasi linter hanya berupa teks singkat berupa keterangan dan kode Error atau Warning atau Kesalahan Konvensi Penamaan (Naming Conventions).

        Lint atau linting akan meminimalkan kode Anda mengalami error, salah satu contohnya karena kesalahan indentasi di Python. Sebelum kode Anda diproses oleh interpreter Python dengan IndentationError, lint akan memberitahukannya lebih dahulu ke Anda.

        Berikut akan dibahas tiga jenis aplikasi linter, silakan dicermati dahulu. Tidak harus semuanya diinstal/dicoba, hanya paket yang menurut Anda sesuai kebutuhan saja yang digunakan. Untuk menginstalnya, silakan buka terminal Anda dan jalankan kode di bawah ini sesuai yang Anda pilih.

            Catatan: Output ketiga aplikasi ini kemungkinan mirip, tetapi pada kondisi tertentu akan ada output atau fitur yang mungkin sesuai dengan kebutuhan Anda menulis kode.

        1.  Pycodestyle (sebelumnya bernama pep8)
            Pycodestyleadalah aplikasi open source (berlisensi MIT/Expat) untuk membantu mengecek kode terkait gaya penulisan kode dengan konvensi PEP8. Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.

                pip install pycodestyle
        
        2.  Pylint
            Pylintadalah aplikasi open source (berlisensi GPL v2) untuk melakukan analisis kode Python, mengecek untuk kesalahan (error) pemrograman, memaksakan standar penulisan kode dengan mengecek penulisan kode yang tidak baik, serta memberikan saran untuk refactoring sederhana. Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.

                pip install pylint

        3.  Flake 8
            Flake8adalah aplikasi open source (berlisensi MIT) yang membungkus sejumlah kemampuan aplikasi lain, seperti pycodestyle, pyflakes, dan (skrip/fitur) lainnya. Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.
                pip install flake8

    Selanjutnya, mari kita masuk ke pembahasan cara kerja ketiganya. Pastikan Anda sudah menginstal aplikasi yang disebutkan sebelumnya. 

    1.  Masuk ke kode editor Anda, misalnya Visual Studio Code.
    2.  Buat sebuah file bernama kalkulator.py dan masukkan kode berikut.
        class Kalkulator:
            """kalkulator tambah kurang"""
            def __init__(self, _i):
                self.i = _i
            def tambah(self, _i): return self.i + _i
            def kurang(self, _i):
            return self.i - _i

        Pada kode di atas, kita membuat kelas bernama Kalkulator. Kelas ini memiliki dua metode, yaitu tambah dan kurang. Atribut yang dimiliki kelas ini hanyalah variabel "i".

        Berdasarkan PEP8, kode tersebut masih perlu diperbaiki dan ada blok kode yang akan menghasilkan error. Kita akan mengetahuinya nanti.

    3.  Mari kita jalankan file atau script tersebut dengan aplikasi yang telah diinstal. Buka kembali terminal Anda, pastikan membuka direktori tempat file atau script Anda berada.
        a.  Pycodestyle
            Untuk menguji menggunakan pycodestyle, jalankan kode berikut.
                pycodestyle kalkulator.py

            Output yang akan dihasilkan adalah ini :
            kalkulator.py:1:2: E111 indentation is not a multiple of 4
            kalkulator.py:1:2: E113 unexpected indentation
            kalkulator.py:2:13: E117 over-indented
            kalkulator.py:5:13: E301 expected 1 blank line, found 0
            kalkulator.py:7:13: E112 expected an indented block
            kalkulator.py:7:31: W292 no newline at end of file

            Gambar di atas adalah tampilan terminal ketika Anda menjalankan script menggunakan pycodestyle.

        b.  pylint
            Untuk menguji menggunakan pylint, jalankan kode berikut.
                pylint kalkulator.py
            Output yang dihasilkan adalah berikut.

            ************* Module kalkulator
            kalkulator.py:1:1: E0001: Parsing failed: 'unexpected indent (kalkulator, line 1)' (syntax-error)

            Gambar di atas adalah tampilan terminal ketika Anda menjalankan script menggunakan pylint

        c.  flake8
            Untuk menguji menggunakan flake8, jalankan kode berikut.
                flake8 kalkulator.py 
            Outputnya :
            kalkulator.py:1:2: E999 IndentationError: unexpected indent

    Pesan dari ketiga aplikasi tersebut ternyata beragam, tetapi ada satu kesamaan, yakni ketiganya menunjukkan pola yang sama di awal pesan berupa nama file diikuti dengan baris dan kolom.

    Mari perbaiki kodenya, silakan ganti dengan kode berikut.

        class Kalkulator:
            """kalkulator tambah kurang"""
            def __init__(self, _i):
                self.i = _i

            def tambah(self, _i): return self.i + _i

            def kurang(self, _i):
                return self.i - _i

    Pada kode di atas, kita telah melakukan beberapa perbaikan. Pertama adalah kita menambahkan new line (garis baru) pada setiap penulisan setelah blok fungsi, sekarang setiap fungsinya dipisahkan oleh satu baris kosong. Kedua, kita menambahkan indentasi pada metode "kurang". 

    Kemudian jalankan kembali file tersebut menggunakan ketiga aplikasi yang sebelumnya digunakan.

    Jika diproses menggunakan pycodestyle dan flake8, itu tidak akan memunculkan pesan seperti gambar di bawah ini. Hal ini berarti menjelaskan kodenya sudah lebih baik.

    Namun, ketika Anda menjalankannya menggunakan pylint, beberapa pesan peringatan muncul. Hal ini karena kita perlu menambahkan dokumentasi pada setiap fungsi dan kelas yang dibangun. Tidak apa-apa, itu merupakan peringatan untuk membuat kode kita lebih sempurna.
'''