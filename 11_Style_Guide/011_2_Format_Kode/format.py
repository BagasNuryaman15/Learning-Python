print("\n")
print(" Memforamt Kode ".center(150, "="), "\n")
'''
Jika proses lint atau linting hanya melakukan pengecekan, kali ini adalah arahan gaya penulisan kode agar bisa sesuai dengan PEP8. Kita akan kembali menggunakan beberapa aplikasi yang nantinya akan diinstal. 

Proses memformat kode akan sama dengan cara melakukan proses linting, yaitu kita akan mengeksekusi script. Perbedaannya adalah output yang dihasilkan. Jika proses linting menghasilkan pesan dengan menunjukkan baris dan kode yang mengalami kesalahan, proses memformat kode akan memberikan pesan berupa kode yang telah diperbaiki. Ini artinya Anda tidak perlu mengubah kode secara manual.

Berikut adalah tiga jenis aplikasi untuk memformat kode, silakan dicermati dahulu. Tidak harus semuanya diinstal, hanya paket yang menurut Anda sesuai kebutuhan saja yang digunakan.

    1.  black
        black adalah proyek open source yang dikembangkan di repository Python Software Foundation (PSF) dengan lisensi MIT. Untuk mendapatkan gambaran, versi online (tidak resmi) ada di https://black.now.sh.

        Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.
            pip install black

    2.  YAPF (Yet Another Python Formatter)
        YAPF adalah proyek open source yang dikembangkan di repository Google dengan lisensi Apache.

        Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.
            pip install yapf

    3.  autopep8
        autopep8 adalah proyek open source (berlisensi MIT) yang termasuk paling awal untuk memformat kode dengan bantuan lint pycodestyle.

        Untuk instalasi, silakan buka terminal Anda dan jalankan kode berikut.
            pip install autopep8
        
    Selanjutnya, mari kita masuk ke pembahasan cara kerja ketiganya. Kita akan menggunakan kode yang sama seperti sebelumnya, yaitu kalkulator.py. Pastikan Anda sudah menginstal aplikasi yang disebutkan sebelumnya.

    1.  Buka script kalkulator.py dan salin kode berikut.

        class Kalkulator:
            """kalkulator tambah kurang"""
            def __init__(self, _i):
                self.i = _i
            def tambah(self, _i): return self.i + _i
            def kurang(self, _i):
                return self.i - _i
    
    Contoh di atas merupakan kode kalkulator yang sama seperti materi sebelumnya, saat kita mendefinisikan kelas kalkulator dengan dua metode, yaitu tambah dan kurang serta satu atribut objek.

    2.  Mari jalankan file atau script tersebut dengan aplikasi yang telah kita instal. Buka kembali terminal Anda, pastikan membuka direktori tempat file atau script Anda berada.

        a.  Untuk black, jalankan kode berikut.
                black kalkulator.py
            Ketika Anda menjalankan perintah di atas, kode yang berada di dalam kalkulator.py akan mengalami perubahan. Silakan cek kembali kode dalam file Anda.

        b.  Untuk YAPF, jalankan kode berikut.
                yapf kalkulator.py
            Ketika Anda menjalankan perintah di atas, tidak akan mengubah kode Anda secara langsung, seperti black. Namun, yapf akan memberikan saran kode melalui terminal.
                class Kalkulator:
                    """kalkulator tambah kurang"""

                    def __init__(self, _i):
                        self.i = _i

                    def tambah(self, _i):
                        return self.i + _i

                    def kurang(self, _i):
                        return self.i - _i

            Gambar di atas adalah tampilan layar terminal menunjukkan saran kode yang telah diperbaiki oleh yapf.

        c.  Untuk autopep8, jalankan kode berikut.
            Cara kerja autopep8 dapat seperti yapf yang akan memberi saran kode ke layar terminal atau seperti black yang akan mengubah langsung isi file kalkulator.py.

            Jika Anda ingin autopep8 memberikan saran kode, silakan jalankan kode berikut.
                autopep8 kalkulator.py
            Ketika dijalankan, layar akan memunculkan saran kode yang telah diperbaiki seperti pada gambar berikut.
                class Kalkulator:
                    """kalkulator tambah kurang"""

                    def __init__(self, _i):
                        self.i = _i

                    def tambah(self, _i):
                        return self.i + _i

                    def kurang(self, _i):
                        return self.i - _i
            Jika Anda ingin mengubah kode file secara langsung, silakan jalankan kode berikut dan periksa kembali file kode Anda.

                autopep8 --in-place --aggressive --aggressive kalkulator.py

    Setelah mempelajari kedua mekanisme: pengecekan gaya penulisan (style guide) dan proses memformat kode, Anda tinggal fokus dengan penulisan indentasi dalam kode Python. Untuk format sisanya, aplikasi-aplikasi yang telah kita pelajari di atas dapat membantu.

    Jika Anda menulis dengan editor kode yang sangat sederhana, anggap saja seperti notepad di Windows atau pico/nano di Linux, dalam menuliskan kode Python cukup perhatikan indentasi untuk setiap baris pernyataan (statement). Setelah selesai menuliskan kodenya, simpan kodenya sebagai file .py, lalu eksekusi perintah linter atau langsung eksekusi perintah aplikasi untuk memformat kode. Hasilnya, kode Anda sudah dirapikan sesuai arahan gaya penulisan PEP8 juga dilakukan pengecekan terhadap kemungkinan kesalahan (jika Anda lakukan linting).

    Untuk Anda yang mengikuti instalasi editor kode PyCharm dalam materi awal, secara bawaan sudah menggunakan fitur inspeksi dengan kemampuan yang kurang lebih sama. Namun jika Anda mau, bisa juga menambahkan aplikasi lint yang sudah dijelaskan sebagai tambahan dari bawaan. Demikian juga untuk fitur format ulang kode juga tersedia secara bawaan di aplikasi PyCharm.
'''