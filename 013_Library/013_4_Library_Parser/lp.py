print("\n")
print(" Library Parser ".center(150, "="), "\n")

'''
                                                                    Library Parser

Library parser pada Python menyediakan fasilitas untuk menguraikan kode Python menjadi struktur data yang dapat diproses dan dianalisis. Anda dapat menggunakan Getopt atau ArgParse. 

Argument parser bermanfaat jika kita ingin membuat program atau skrip kecil yang langsung menerima parameter pada saat pemanggilan program. Hal ini biasa digunakan dalam pemanggilan aplikasi atau skrip di CLI/terminal *nix-based, misalnya Linux dan MacOS. Contoh perintah dimaksud adalah berikut.

    python panggildicoding.py -o
    python panggildicoding.py --output
    python panggildicoding.py -o output.txt
    python panggildicoding.py --output output.txt
    python panggildicoding.py -h
    python panggildicoding.py --help

Dengan menggunakan argument parser, kita dapat membuat program yang lebih interaktif dan mudah digunakan oleh pengguna.
'''
# Contoh Penerapan Library Parser
print("> Contoh Penerapan Library Parser \n")
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()
 
if args.output:
   print("Halo, ini merupakan sebuah output dari lp.py")

'''
    Jadi, pada saat dijalankan, ada beberapa hal yang perlu diperhatikan, yaitu berikut.

    1. Berkas lp.py dapat menerima parameter -o atau --output.
    2. Jika kita memanggil berkas tanpa parameter -o, berkas tidak akan menampilkan apa pun.
    3. Jika kita memanggil dengan -o atau --output, berkas akan menampilkan Halo, ini merupakan sebuah output dari lp.py.
    4. Jika kita memanggil --help, tampil help dengan penjelasan "tampilkan output".
'''