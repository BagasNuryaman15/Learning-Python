print("")
print(" Pengantar Unit Testing ".center(150, "="), "\n")
# ============================================================================= Unit Testing ==================================================================
'''
   
                                                                                Unit Testing

Sampai pada tahap ini, sudah banyak modul pemrograman Python yang telah dipelajari. Kita telah mengenal operasi-operasi dasar dalam Python, seperti perulangan, fungsi, hingga OOP pada Python.

Saat Anda membangun aplikasi menggunakan Python dan aplikasi yang dikembangkan semakin kompleks, dependensi akan muncul. Artinya, satu atau lebih fungsi digunakan oleh fungsi lain. Bahkan, ketika kita mulai membangun aplikasi dengan rekan kita, kita membuat fungsi yang digunakan oleh rekan, ataupun sebaliknya.

Pada saat membuat fungsi baru ataupun mengubah fungsi yang sudah ada, tentunya perlu dipastikan bahwa fungsionalitas aplikasi yang sebelumnya tidak terganggu dengan adanya perubahan baru tersebut. Bagaimana jika fungsionalitas bukan hanya lima atau sepuluh, tetapi lebih dari itu? Tentu menyulitkan sekali untuk mengeceknya satu per satu setiap kita melakukan perubahan.

Di sinilah kita butuh pengujian (test) untuk fungsi-fungsi tersebut. Pengujian sebenarnya dapat dibedakan menjadi dua tipe, yaitu manual dan otomatis. 
    1. Manual testing adalah proses pengujian yang dilakukan oleh seseorang yang ditunjuk sebagai tester atau bahkan developer lainnya.

                        Feedback
        Developer <----------------------> Tester or Developer
                        Request Review
        (Membuat Fungsi)                    (Menguji Fungsi)
        Tanpa sadar, sebenarnya ketika Anda menjalankan program pertama kali lalu mengecek bahwa output-nya sesuai atau tidak, itu merupakan pengujian manual.
    
    2. Testing otomatis merupakan hal yang sebaliknya. Ini adalah pengujian yang dilakukan secara otomatis terhadap kode-kode yang kita bangun berdasarkan rencana pengujian (test plan).

        Rencana pengujian terdiri dari bagian aplikasi yang ingin diuji, urutannya, dan tanggapan atau output yang diharapkan. Alur pengujian otomatis secara umum dimulai dari menyusun rencana pengujian, lalu membangun kode tes dan menjalankan kode tes tersebut. Jika kode tes gagal, kita perlu memperbarui kode; jika kode tes berhasil, kita melaju ke pengujian selanjutnya hingga selesai.
        
    Tidak hanya sekadar manual dan otomatis, dalam dunia testing yang begitu luas, Anda akan menemui berbagai jenis testing. Beberapa di antaranya adalah unit testing dan integration testing. Unit testing adalah pengujian yang dilakukan pada unit terkecil dari kode, seperti fungsi atau metode. Sedangkan integration testing adalah pengujian yang dilakukan pada beberapa unit yang saling berinteraksi.

    Integration testing adalah pengujian yang bertujuan untuk menguji suatu sistem sebagai satu kesatuan. Bayangkan Anda sedang mengecek lampu motor, tentu hal pertama yang dilakukan adalah menyalakan motor. Lalu, Anda melihat lampu motor tersebut yang sempat menyala, tetapi perlahan mati. Anda kemudian bertanya, mengapa lampunya mati?

    Kejadian yang dijelaskan di atas erat dengan konsep integration testing karena dengan menyalakan motor, kita dapat menguji seluruh bagian motor lain, seperti lampunya.

    Unit testing adalah pengujian yang lebih spesifik dan fokus terhadap bagian-bagian kecil. Bayangkan ketika mengecek lampu motor dan ternyata ia tidak menyala, Anda perlu mengecek lampu tersebut; apakah rusak? Atau ada kabel dari lampu tersebut yang tidak berfungsi? Hal-hal yang lebih spesifik tersebut adalah unit testing. Dalam pemrograman, bagian-bagian kecil tersebut berupa fungsi, kelas, dan sebagainya.

    Pada materi ini, kita akan mempelajari unit testing menggunakan salah satu library bawaan Python, yaitu unittest. Unit test adalah proses pengujian perangkat lunak yang memastikan setiap unit/fungsi dari program teruji. Jika fungsionalitas dari aplikasi yang kita bangun terdiri dari prosedur-prosedur dan fungsi-fungsi yang kita tulis, kita perlu melakukan unit test untuk setiap prosedur atau fungsi yang ada.

    Layaknya sebuah framework pengujian, library unittest mendukung beberapa hal esensial berikut.

    1.  Pengujian secara otomatis.
    2.  Kode awal proses (setup) dan akhir proses (shutdown) yang dapat digunakan ulang.
    3.  Penyatuan sejumlah pengujian dalam sebuah koleksi.
    4.  Terpisahnya framework pengujian dari framework pelaporan (reporting).

    Library unittest mendukung sejumlah konsep penting yang berorientasi objek, antara lain berikut.

    1. Test fixture merepresentasikan persiapan yang dibutuhkan untuk melakukan satu pengujian atau lebih serta proses pembersihannya (cleanup). Beberapa contohnya adalah menyiapkan basis data pengujian, direktori pengujian, atau mengaktifkan sebuah proses server.

    2. Test case adalah sebuah unit dari pengujian ketika ia mengecek sejumlah respons dari sebagian kelompok masukan. Library unittest menyediakan basis class dan TestCase yang akan digunakan untuk membuat kasus pengujian baru.

    3. Test suite adalah sebuah koleksi dari kasus-kasus pengujian, koleksi dari test suite itu sendiri, atau gabungan keduanya. Hal ini berguna untuk mengumpulkan pengujian-pengujian yang akan dieksekusi bersama.

Test runner adalah komponen yang akan mengatur (orchestrates) eksekusi dari pengujian-pengujian dan menyediakan keluaran untuk pengguna. Dalam hal ini, runner dapat menggunakan tampilan grafis, tampilan tekstual, atau mengembalikan nilai spesial yang menyatakan hasil dari pengujian.
'''