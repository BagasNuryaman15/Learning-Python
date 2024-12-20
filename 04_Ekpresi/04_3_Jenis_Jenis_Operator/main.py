print(" Jenis Jenis Operator ".center(150, "+")+"\n")
''' 
                                                            Jenis-Jenis Operator
Selain ekspresi dengan beragam jenis, operator pun memiliki berbagai jenis yang dikelompokkan menjadi operator aritmetika, operator relational, operator logika, dan operator assignment.

                                                            Operator Aritmetika           
Jenis pertama adalah operator untuk melakukan operasi aritmetika. Perhatikan tabel di bawah ini untuk memahami contoh penerapan operator aritmetika. Asumsikan x bernilai 11 dan y bernilai 5. 

Operator	Nama	    Contoh	    Hasil
+	        Tambah	    x + y	    16
-	        Kurang	    x - y	    6
*	        Kali	    x * y	    55
/	        Bagi	    x / y	    2.2
//	        Bagi 	    x // y	    2       # (dibulatkan ke bawah)
%	        Modulus	    x % y	    1
**	        Pangkat	    x ** y	    125
'''

# Semua operator aritmetika di atas adalah jenis untuk melakukan operasi aritmetika yang sering dijumpai. Mari lihat penerapannya pada Python.

# Contoh Operator Aritmetika
print(" Contoh Operator Aritmetika ".center(40, "-") + "\n")

x = 11
y = 5

# Operator Penjumlahan (+)
print("> Operator Penjumlahan (+):")
print(f"Hasil dari {x} + {y} adalah {x + y}"+ "\n")

# Operator Pengurangan (-)
print("> Operator Pengurangan (-):")
print(f"Hasil dari {x} - {y} adalah {x - y}"+ "\n")

# Operator Perkalian (*)
print("> Operator Perkalian (*):")
print(f"Hasil dari {x} * {y} adalah {x * y}"+ "\n")

# Operator Pembagian (/)
print("> Operator Pembagian (/)")
print(f"Hasil dari {x} / {y} adalah {x / y} dan ingat ini adalah operator yang tidak dibulatkan"+ "\n")

# Operator Pembagian (//)
print("> Operator Pembagian (//)")
print(f"Hasil dari {x} // {y} adalah {x // y} dan ini adalah operator yang di bulatkan"+ "\n")

# Operator Modulus (%)
print("> Operator Modulus (%)")
print(f"Hasil dari {x} % {y} adalah {x % y}"+ "\n")

# Operator Pangkat (**)
print("> Operator Pangkat (**)")
print(f"Hasil dari {x} ** {y} adalah {x ** y}"+ "\n")
print("="*40 + "\n")

'''
                                                            Operator Relasional

Operator relasional merupakan operator perbandingan antara dua operan yang berupa integer, float, string, ataupun boolean. Hasil akhir dari operator ini adalah nilai bertipe boolean. Perhatikan tabel di bawah untuk memahami contoh penerapan operator relasional. Asumsikan kedua variabel bertipe numerik atau float dengan x bernilai 10 dan y bernilai 20.

Operator	Nama	                    Deskripsi                                                                               Contoh	    Hasil
==	        Sama dengan	                Menghasilkan True, jika kedua operan bernilai sama.                                     x == y	    False
!=          Tidak sama dengan           Menghasilkan True, jika kedua operan tidak sama.                                        x != y	    True
>	        Lebih besar dari	        Menghasilkan True, jika operan kiri lebih besar dari operan kanan.                      x > y	    False
<	        Kurang dari	                Menghasilkan True, jika nilai operan kiri kurang dari operan kanan.                     x < y	    True
>=	        Lebih besar sama dengan	    Menghasilkan True, jika operan kiri lebih besar atau sama dengan operan kanan.          x >= y	    False
<=	        Kurang dari sama dengan	    Menghasilkan True, jika operan kanan lebih besar atau sama dengan operan kiri.          x <= y	    True
'''

# Pada dasarnya, ini adalah operator yang membandingkan dua nilai dengan hasil akhir bertipe boolean. Mari lihat penerapannya pada Python.

# Contoh Operator Relasional
print(" Contoh Operator Relasional ".center(40, "-") + "\n")

x = 10
y = 20

# Operator Sama dengan (==)
print("> Operator Sama dengan (==):")
print(f"Hasil dari {x} == {y} adalah {x == y}"+ "\n")

# Operator Tidak sama dengan (!=)
print("> Operator Tidak sama dengan (!=):")
print(f"Hasil dari {x} != {y} adalah {x != y}"+ "\n")

# Operator Lebih besar dari (>)
print("> Operator Lebih besar dari (>):")
print(f"Hasil dari {x} > {y} adalah {x > y}"+ "\n")

# Operator Kurang dari (<)
print("> Operator Kurang dari (<):")
print(f"Hasil dari {x} < {y} adalah {x < y}"+ "\n")

# Operator Lebih besar sama dengan (>=)
print("> Operator Lebih besar sama dengan (>=):")
print(f"Hasil dari {x} >= {y} adalah {x >= y}"+ "\n")

# Operator Kurang dari sama dengan (<=)
print("> Operator Kurang dari sama dengan (<=):")
print(f"Hasil dari {x} <= {y} adalah {x <= y}"+ "\n")
print("="*40 + "\n")

'''
Pada kode di atas, Anda telah menerapkan seluruh operasi menggunakan operator relasional. Jika kita lihat lebih detail, seluruh output tersebut memiliki hasil yang sama dengan tabel sebelumnya. Sebagaimana telah dijelaskan sebelumnya, operator relasional dapat menggunakan operan bertipe integer, string, ataupun float. Kode di atas telah menggunakan operan bertipe integer, Anda juga bisa mengubahnya dengan operan bertipe float. 

Namun, berbeda halnya dengan operan bertipe string. Anda dapat melihat tabel di bawah untuk contoh penerapannya. Asumsikan x bernilai "Bagas" dan y bernilai "Ganteng".

Operator    Relasional	Deskripsi	                                                                                                 Contoh	    Hasil
==          Menghasilkan True, jika kedua string memiliki nilai yang identik/sama persis.                                            x == y	    False
!=          Menghasilkan True, jika kedua string memiliki nilai yang tidak sama.                                                     x != y	    True
>           Menghasilkan True, jika karakter pertama dalam string kiri lebih besar dari karakter pertama dalam string kanan.	     x > y	    False
<           Menghasilkan True, jika karakter pertama dalam string kiri lebih kecil dari karakter pertama dalam string kanan.	     x < y	    True
>=          Menghasilkan True, jika huruf pertama pada string pertama memiliki nilai unicode dengan urutan yang lebih tinggi atau sama dibandingkan huruf pertama pada string kedua.                                                                                                           x >= y	  False
<=          Menghasilkan True, jika huruf pertama pada string pertama memiliki nilai unicode dengan urutan yang lebih rendah atau sama dibandingkan huruf   pertama pada string kedua.                                                                                                           x <= y	    True
'''

# Contoh Operator Relasional Terhadap String
print(" Contoh Operator Relasional Terhadap String ".center(70, "-") + "\n")

x = "Bagas"
y = "Ganteng"

# Operator Sama dengan (==)
print("> Operator Sama dengan (==):")
print(f"Hasil dari {x} == {y} adalah {x == y}"+ "\n")

# Operator Tidak sama dengan (!=)
print("> Operator Tidak sama dengan (!=):")
print(f"Hasil dari {x} != {y} adalah {x != y}"+ "\n")

# Operator Lebih besar dari (>)
print("> Operator Lebih besar dari (>):")
print(f"Hasil dari {x} > {y} adalah {x > y}"+ "\n")

# Operator Kurang dari (<)
print("> Operator Kurang dari (<):")
print(f"Hasil dari {x} < {y} adalah {x < y}"+ "\n")

# Operator Lebih besar sama dengan (>=)
print("> Operator Lebih besar sama dengan (>=):")
print(f"Hasil dari {x} >= {y} adalah {x >= y}"+ "\n")

# Operator Kurang dari sama dengan (<=)
print("> Operator Kurang dari sama dengan (<=):")
print(f"Hasil dari {x} <= {y} adalah {x <= y}"+ "\n")

print("="*40 + "\n")


''' 
                                                            Operator Logika
Operator logika merupakan jenis operator untuk melakukan operasi logika dengan kedua operannya bertipe boolean. Hasil akhir dari operasi ini adalah nilai bertipe boolean. Perhatikan kode di bawah ini untuk memahami contoh penerapannya, asumsikan bahwa p bernilai True dan q bernilai False.

    Operator	Deskripsi	                                                                            Contoh	   
    and (&)     Logika yang hanya menghasilkan True jika kedua operan bernilai True.                    p and q = False, p & q = False
    or  (|)     Logika yang menghasilkan True jika salah satu dari kedua operan bernilai True.          p or q = True, p | q = True
    not	(~)     Logika yang bertujuan untuk membalikkan nilai logika dari operannya.                    not p = False, ~p = False

Operator AND hanya akan menghasilkan nilai True jika kedua operannya bernilai True. Operator OR akan menghasilkan nilai True jika salah satunya bernilai True. Operator NOT hanya akan membalikkan nilai logika; jika True, False yang akan dikembalikan, begitupun sebaliknya.  

    1. Operator AND (&)
                                                p               q               p and q
                                                True            True            False
                                                True            False           False
                                                False           True            False
                                                False           False           False

    Pada tabel di atas, operator AND hanya akan menghasilkan nilai TRUE jika kedua operan, yakni P dan Q bernilai TRUE. Sisanya akan menghasilkan nilai FALSE.

    2. Operator OR (|)
                                               p                q               p or q
                                               True             True            True 
                                               True             False           True
                                               False            True            True
                                               False            False           False

    Pada tabel di atas, operator OR akan menghasilkan nilai TRUE jika salah satu dari kedua operan, yakni P dan Q bernilai TRUE. Sisanya akan menghasilkan nilai FALSE.

    3. NOT (~)
                                               p                not p
                                               True             False
                                               False            True
    
    Pada tabel di atas, operator NOT akan membalikkan nilai boolean dari operan aslinya atau disebut sebagai negasi.
'''

# Mari lihat penerapannya pada Python.
# Contoh Operator Logika
print(" Contoh Operator Logika  ".center(70, "-") + "\n")

# Contoh Operator Logika AND (&)
print("="*40)
print("> Contoh Operator Logika AND (&):"+ "\n")

print("+ Ini ketika dua kondisi True(Benar)")
groupAnd = [[True, False], [False, True]]
print(f"  Hasil dari {groupAnd[0][0]} and {groupAnd[1][1]} adalah {groupAnd[0][0] and groupAnd[1][1]}"+ "\n")

print("+ Ini ketika salah satu kondisi False(Salah)")
print(f"  Hasil dari {groupAnd[0][1]} and {groupAnd[1][1]} adalah {groupAnd[0][1] and groupAnd[1][1]}"+ "\n")

print("+ Ini ketika kedua kondisi False(Salah)")
print(f"  Hasil dari {groupAnd[0][1]} and {groupAnd[1][0]} adalah {groupAnd[0][1] and groupAnd[1][0]}")
print("="*40 + "\n")

# Contoh Operator Logika OR (|)
print("="*40)
print("> Contoh Operator Logika OR (|):"+ "\n")

print("+ Ini ketika dua kondisi True(Benar)")
groupOr = [[True, False], [False, True]]
print(f"  Hasil dari {groupOr[0][0]} or {groupOr[1][1]} adalah {groupOr[0][0] or groupOr[1][1]}"+ "\n")

print("+ Ini ketika salah satu kondisi True(Benar)")
print(f"  Hasil dari {groupOr[0][1]} or {groupOr[1][1]} adalah {groupOr[0][1] or groupOr[1][1]}"+ "\n")

print("+ Ini ketika kedua kondisi False(Salah)")
print(f"  Hasil dari {groupOr[0][1]} or {groupOr[1][0]} adalah {groupOr[0][1] or groupOr[1][0]}")
print("="*40 + "\n")

# Contoh Operator Logika NOT (~)
print("="*40)
print("> Contoh Operator Logika NOT (~):"+ "\n")

print("+ Ini ketika kondisi True(Benar)")
groupNot = [True, False]
print(f"  Hasil dari not {groupNot[0]} adalah {not groupNot[0]}"+ "\n")

print("+ Ini ketika kondisi False(Salah)")
print(f"  Hasil dari not {groupNot[1]} adalah {not groupNot[1]}")
print("="*40 + "\n")



''' 
                                                            Operator Assignment
Operator selanjutnya adalah assignment. Operator ini bertujuan untuk melakukan proses assignment atau pemberian nilai pada suatu variabel dengan nilai tetap. Perhatikan tabel di bawah ini untuk memahami contoh penerapan operator assignment. Asumsikan x bernilai 11 dan y bernilai 5.

    Operator	Contoh	                Eksekusi
    =	        x = 11	                x bernilai 11
    +=	        x += 1	                x bernilai 12
    -=	        x -= 1	                x bernilai 10
    *=	        x *= 2	                x bernilai 22
    /=	        x /= 2	                x bernilai 5.5
    //=	        x //= 2             	x bernilai 5
    %=	        x %= 2	                x bernilai 1
    **=	        x **= 2             	x bernilai 121

    Sederhananya, seluruh operator di atas setara dengan x = x <operator> y. Biasanya, Anda akan sering menjumpai operator assignment ini pada perulangan (Anda akan mempelajarinya nanti). Perulangan pada pemrograman berarti Anda membuat sebuah program yang akan terus berulang hingga berakhir karena suatu kondisi. Salah satu caranya agar dapat terus berulang adalah dengan menambahkan operator assignment. 
'''

# Contoh Operator Assignment 
print(" Contoh Operator Logika  ".center(70, "-") + "\n")
# Contoh Operator Assignment (=)
print("="*40)

x = 11
y = 5

print("> Contoh Operator Assignment (=):")

x = y
print(f"  Hasil dari x = {y} adalah {x}" + "\n")

# Contoh Operator Assignment (+=)
print("> Contoh Operator Assignment (+=):")

x += 1
print(f"  Hasil dari x += 1 adalah {x}" + "\n")

# Contoh Operator Assignment (-=)
print("> Contoh Operator Assignment (-=):")

x -= 1
print(f"  Hasil dari x -= 1 adalah {x}"+ "\n")

# Contoh Operator Assignment (*=)
print("> Contoh Operator Assignment (*=):")

x *= 2
print(f"  Hasil dari x *= 2 adalah {x}" + "\n")

# Contoh Operator Assignment (/=)
print("> Contoh Operator Assignment (/=):")

x /= 2
print(f"  Hasil dari x /= 2 adalah {x}" + "\n")

# Contoh Operator Assignment (//=)
print("> Contoh Operator Assignment (//=)")

x //= 2
print(f"  Hasil dari x //= 2 adalah {x}" + "\n")

# Contoh Operator Assignment (%=)
print("> Contoh Operator Assignment (%=)")

x %= 2
print(f"  Hasil dari x %= 2 adalah {x}" + "\n")

# Contoh Operator Assignment (**=)
print("> Contoh Operator Assignment (**=):")

x **= 2
print(f"  Hasil dari x **= 2 adalah {x}" + "\n")
print("="*40 + "\n")









