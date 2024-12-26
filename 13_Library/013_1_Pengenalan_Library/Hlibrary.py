print("=" * 150)
print(f"\n{'Pengenalan Library ':^150}", "\n")
print("=" * 150, "\n")
'''
                                                                    Pengenalan Library

Dalam pengembangan program atau aplikasi, kita tidak akan lepas dari peran package atau library. Sebagaimana yang sudah dijelaskan dalam materi-materi sebelumnya, package adalah sebuah direktori yang berisi satu atau lebih modul yang terkait dan saling berhubungan, sedangkan library adalah koleksi dari banyaknya modul dan paket yang saling terkait dan dapat digunakan berulang kali. 

Pada materi ini, kita akan mempelajari berbagai library yang telah dikembangkan oleh banyak pengembang dan dapat digunakan kembali oleh kita. Jumlah library Python sangat banyak yang terbagi menjadi Python Standard Library dan Python External Library.

    1. Python Standard Library adalah jenis library yang telah terinstal secara otomatis ketika kita melakukan instalasi Python. Anda tidak perlu melakukan instalasi kembali jika ingin menggunakannya. Beberapa contoh Python Standard Library adalah “os”, “datetime”, “re”, serta lainnya yang dapat Anda baca lebih lengkap pada laman berikut.

    2. Python External Library adalah kumpulan kode yang telah dikembangkan oleh orang lain atau komunitas dan disediakan dalam bentuk paket atau modul yang dapat diimpor. Jenis library ini mengharuskan Anda untuk melakukan instalasi agar dapat digunakan. External library ini dikembangkan oleh individu atau organisasi di luar tim inti pengembang Python. 

Untuk melakukan instalasi library eksternal, Anda dapat melakukan beberapa cara, seperti menggunakan PIP dan conda.

    1.  PIP
        PIP adalah package manager resmi dari Python yang dapat digunakan untuk mengunduh, menginstal, menghapus, dan mengelola package Python dari Python Package Index (PyPI) dan repositori lainnya. PyPI merupakan repositori online yang menyediakan ribuan package dari Python dan siap digunakan oleh para pengembang.

        Selain mengelola paket, Anda juga bisa membuat lingkungan virtual dalam Python menggunakan PIP. Hanya saja, pip cenderung difokuskan untuk mengelola instalasi paket dibanding lingkungan virtual. Lingkungan virtual memungkinkan kita untuk membuat sebuah lingkungan terisolasi yang terpisah satu sama lain. Kita akan bahas lebih dalam terkait lingkungan virtual pada materi conda.

        Kabar baiknya, pip biasanya telah terpasang secara otomatis jika Anda menggunakan Python 2 untuk versi 2.7.9 ke atas atau Python 3 untuk versi 3.4 ke atas. Maka dari itu, silakan periksa bahwa pip telah terpasang dengan menjalankan perintah berikut.

            pip --version

    2.  Conda
        Selain pip yang termasuk package manager resmi dari Python, ada juga conda yang merupakan package manager dan environment manager untuk Python. Conda memungkinkan kita untuk membuat dan mengelola lingkungan (environment) terisolasi atau terpisah satu sama lain. Dengan terisolasinya setiap lingkungan tersebut, kita diuntungkan untuk mencegah konflik yang terjadi antar proyek. 

        Contohnya ketika Anda memiliki proyek machine learning dengan versi Python yang digunakan adalah Python 3.9. Di sisi lain, Anda memiliki proyek web development A dengan versi Python yang digunakan adalah Python 3.8. Ada pula proyek web development B dengan versi Python yang digunakan sama-sama menggunakan Python versi 3.8.

        Dengan adanya lingkungan yang terisolasi, Anda bisa menyesuaikan semua library, modul, hingga versi Python sesuai dengan kebutuhan masing-masing proyek. Conda sendiri dapat diinstal melalui Anaconda dan Miniconda. Anaconda merupakan sistem distribusi perangkat lunak yang di dalamnya mencakup Conda. Ketika menginstal Anaconda, Anda pun dapat menggunakan beberapa library dan plugin tambahan melalui Anaconda tersebut. Miniconda adalah versi ringan dari Anaconda. Miniconda hanya berisi conda dan beberapa package dasar yang diperlukan untuk menjalankannya.

        Conda sendiri hadir dalam dua bentuk utama: “conda” sebagai package dan environment manager serta “conda-forge”, yakni sebuah repositori berisi ribuan paket yang disediakan oleh komunitas Conda.

        Kelebihan Conda adalah sifat tidak terbatasnya pada bahasa pemrograman Python. Conda juga mendukung paket-paket dalam bahasa pemrograman lain, seperti R.

        Kali ini, kita akan menginstal conda melalui sistem terdistribusi Anaconda, silakan ikuti langkah-langkah berikut.

            1.  Kunjungi laman berikut: https://www.anaconda.com/download.
            2.  Silakan scroll ke bawah dan Anda akan menjumpai “Anaconda Installer” yang tersedia untuk tiga sistem operasi, yakni Windows, Linux, dan Mac. Silakan unduh Anaconda sesuai dengan sistem operasi Anda.
            3.  Setelah mengunduh, lakukan instalasi dengan menjalankan file installer yang telah Anda unduh.
            4.  Akan muncul tampilan berikut, lalu pilih “Next”
            5.  Anda akan diarahkan pada License Agreement. Pilih “I Agree”.
            6.  Lalu Anda diharuskan untuk memilih tipe instalasi. Pilih “Just Me” untuk saat ini, kemudian klik “Next”.
            7.  Selanjutnya, Anda perlu menentukan lokasi instalasi. Silakan sesuaikan dengan kebutuhan Anda. Saat ini biarkan default saja dan pilih “Next”.
            8.  Anda akan diarahkan ke menu opsi “Advanced Installation”. Anda bisa membiarkan secara default atau jika ingin mengatur Anaconda3 sebagai default Python, Anda bisa mencentangnya. Setelah selesai, klik Install.
            9.  Proses instalasi akan berjalan. Jika sudah selesai, klik Finish.
        Terakhir, Anda memeriksa bahwa conda telah terinstal. Silakan buka “Anaconda Prompt” dengan klik windows button atau sistem pencarian sesuai sistem operasi Anda dan ketik “Anaconda Prompt”.

        Pada terminal tersebut, jalankan kode berikut.
                conda -V
        Anda akan melihat versi conda yang telah terinstal, seperti pada gambar berikut.


        Anda juga bisa membuka Anaconda Navigator dengan klik windows button atau sistem pencarian lainnya yang sesuai dengan sistem operasi dan ketik “Anaconda Navigator”.

        Berikut adalah tampilan dari Anaconda Navigator.
            
'''