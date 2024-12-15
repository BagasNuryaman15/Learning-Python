import math
import time
import os
import sys

def clear_screen():
    # Membersihkan layar dengan perintah sesuai OS
    os.system('cls' if os.name == 'nt' else 'clear')

def spinning_donut():
    A = 0  # Sudut rotasi terhadap sumbu X
    B = 0  # Sudut rotasi terhadap sumbu Y

    while True:
        clear_screen()

        z = [0] * 1760
        b = [' '] * 1760

        for j in range(0, 628, 7):
            for i in range(0, 628, 2):
                sin_i = math.sin(i / 100)
                cos_i = math.cos(i / 100)
                sin_j = math.sin(j / 100)
                cos_j = math.cos(j / 100)
                
                sin_A = math.sin(A)
                cos_A = math.cos(A)
                sin_B = math.sin(B)
                cos_B = math.cos(B)

                h = cos_j + 2
                D = 1 / (sin_i * h * sin_A + sin_j * cos_A + 5)

                t = sin_i * h * cos_A - sin_j * sin_A
                x = int(40 + 30 * D * (cos_i * h * cos_B - t * sin_B))
                y = int(12 + 15 * D * (cos_i * h * sin_B + t * cos_B))
                o = int(x + 80 * y)

                N = int(8 * ((sin_j * sin_A - sin_i * cos_j * cos_A) * cos_B - sin_i * cos_j * sin_A - sin_j * cos_A - cos_i * cos_j * sin_B))

                if 1760 > o > 0 and D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

        # Menampilkan buffer
        sys.stdout.write("\033[H")  # Kembali ke pojok kiri atas
        for k in range(1760):
            sys.stdout.write(b[k])
            if k % 80 == 79:
                sys.stdout.write('\n')

        sys.stdout.flush()  # Memastikan output langsung ditampilkan

        A += 0.04
        B += 0.08
        time.sleep(0.03)  # Delay untuk animasi lebih stabil

if __name__ == "__main__":
    try:
        spinning_donut()
    except KeyboardInterrupt:
        print("\nDonat berputar dihentikan.")