print("=" * 150)
print(f"{'Library Text Processing':^150}")
print("=" * 150, "\n")
'''
                                                                Library Text Processing

Pertama adalah sekumpulan library yang bertujuan untuk melakukan pemrosesan teks dan menyederhanakan serta mempercepat tugas-tugas pemrosesan teks.
    1.  String
        String adalah salah satu modul bawaan Python yang tidak perlu dideklarasikan. Pada modul string ada fungsi-fungsi yang dapat dioperasikan pada variabel bertipe string seperti di bawah.
            a. upper(): Ubah setiap huruf dalam string menjadi huruf kapital. 
            b. lower(): Ubah setiap huruf dalam string menjadi huruf kecil.
            c. split(): Pisahkan teks berdasarkan delimiter (karakter pemisah).
            d. title(): Jadikan setiap awal kata kapital.
            e. zfill(): Tambahkan nol di awal string sebanyak nilai yang ada pada parameter.
        Contoh Penerapannya sih ada di materi tipe data string. Tapi tidak apa-apa saya akan mencontohkan kembali. 

            Sudah saya tulis ya di bawah liat aja biar tidak pusing.

    2. Regex (Regular Expression)
        Regex atau regular expression adalah sebuah cara untuk mencari teks berdasarkan pola tertentu. Umpamanya, ketika ingin mencari sebuah kata dalam kamus, misalnya arti dari kata parsing, kita akan mencari kata tersebut di halaman yang memiliki kata dengan awalan p, lalu pa. Regex bekerja dengan konsep yang sama.

        Pada regex, kita mencari sebuah kata atau kumpulan kata dengan memberikan pola yang diinginkan. Contoh umum regex adalah pada email. Kita dapat menggunakan regex untuk mengecek bahwa karakter @ ada pada email atau tidak.

        Contoh di bawah menunjukkan penggunaan regex. Pada variabel pattern di bawah, ^a berarti kita ingin mencari teks dengan awalan 'a', dan s$ berarti kita ingin mencari string berakhiran 's'.    
'''

# Disini kita akan melihat contoh penerapan dari modul string
print(" 1. String ".center(50, "-"), "\n")

# A. upper()
print("A. upper() : Contoh Penerapan upper")
textUpper = "Catatan Penting! Bahwa Satria Dirgantara Nuryaman Itu Sangat Ganteng Dan Kece Abieeezzzz"
print(textUpper.upper(), "\n")
# Output: CATATAN PENTING! BAHWA SATRIA DIRGANTARA NURYAMAN ITU SANGAT GANTENG DAN KECE ABIEEEZZZZ

# B. lower()
print("B. lower() : Contoh Penerapan lower")
textLower = "CIK ATUH JANG SING SOPAN ARI NGOMONG TEH BISI KA CENTANG"
print(textLower.lower(), "\n")
# Output: cik atuh jang sing sopan ari ngomong teh bisi ka centang

# C. split()
print("C. split() : Contoh Penerapan split")
textSplit = "Saya sedang belajar Python"
print(textSplit.split(), "\n")
# Output: ['Saya', 'sedang', 'belajar', 'Python']

# D. title()
print("D. title() : Contoh Penerapan title")
textTitle = "saya gak bisa pakai PyCharm kalau ada yang bisa bantu saya euy plis ieumah :("
print(textTitle.title(), "\n")
# Output: Saya Gak Bisa Pakai Pycharm Kalau Ada Yang Bisa Bantu Saya Euy Plis Ieumah :(

# E. zfill()
print("E. zfill() : Contoh Penerapan zfill")
textZfill = "123"
print(textZfill.zfill(5), "\n")
# Output: 00123

# Contoh Penerapan Regex (Regular Expression)
print(" 2. Regex(Reuguler Expression) ".center(50, "-"), "\n")

# Contoh Penggunaan Regex
import re # Import modul re

# Mencari kata yang diawali dengan 'a' dan diakhiri dengan 's'
pattern = '^a....*s$'
testString = 'aku sayang kamu aslina pisan ieumah slurrss'
result = re.match(pattern, testString)

if result:
    print("Kata yang diawali dengan 'a' dan diakhiri dengan 's' ditemukan")
else:
    print("Kata yang diawali dengan 'a' dan diakhiri dengan 's' tidak ditemukan")

# Output: Kata yang diawali dengan 'a' dan diakhiri dengan 's' ditemukan Perlu diperhatikan bahwa beberapa modul perlu diimpor terlebih dahulu untuk bisa digunakan. Pada contoh di atas, kita melakukan “import re” untuk mengimpor modul regex pada Python.
