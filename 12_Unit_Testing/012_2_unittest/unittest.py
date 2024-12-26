print(f"\n{'Penerapan Unit Test dengan Library unittest':^150}")
'''
                                                                    Penerapan Unit Test dengan Library unittest

Sekarang mari kita pelajari cara implementasinya, materi kali ini akan menggunakan PyCharm sebagai IDE-nya. Silakan ikuti sembari menggunakan IDE Anda, seperti Visual Studio Code atau PyCharm. 

Tulis kode ini pada IDE PyCharm dan simpan kode ini dalam format .py. Lalu, jalankan pada Command Prompt di perangkat Anda.
'''

# Contoh penerapan unittest 
print("> Contoh penerapan unittest sebagai berikut:")
import unittest
 
class TestStringMethods(unittest.TestCase):
    # Ini adalah test case pertama (1)
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')
    
    # Test case kedua (2)
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())
    
    # Test case ketiga (3)
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')
    
if __name__ == '__main__':
    # Test Runner
    unittest.main()