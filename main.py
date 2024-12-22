# 1. Buatlah program Faktorial dengan menggunakan fungsi rekursif.
print(" Aplikasi Menghitung Faktorial ".center(40, "="), "\n")
def faktorial(nilai):
    if nilai == 0 or nilai == 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

# Pemanggilan fungsi faktorial melalui Input User
nilai = int(input("Masukkan bilangan: "))
hasil = faktorial(nilai)
print(f"Faktorial dari {nilai} adalah {hasil}", "\n\n")

# 2. Buatlah program untuk menghitung faktor faktornya.
print(" Aplikasi Mencari Faktor Bilangan ".center(40, "="),"\n")
def cari_faktor(n):
    faktor = []  # List untuk menyimpan faktor-faktor
    for i in range(1, n + 1):  # Periksa semua angka dari 1 hingga n
        if n % i == 0:  # Jika n dibagi i tanpa sisa
            faktor.append(i)  # Tambahkan i ke dalam list faktor
    return faktor

# Meminta input dari pengguna
n = int(input("Masukkan bilangan: "))
print(f"Faktor-faktor dari {n} adalah {cari_faktor(n)}")