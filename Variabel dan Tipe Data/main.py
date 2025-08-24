#-----------------------------------------------------------------
#
# Belajar Python Itu Menyenangkan
#
# Pertemuan ke : 2
# Tentang      : Variabel dan Tipe Data
#
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#
# A. Apa itu Variabel?
#
# Variabel adalah tempat menyimpan data di dalam program.
#
# - Variabel memiliki nama dan nilai.
# - Nilai variabel bisa berupa angka, teks, atau tipe data lain.
#
# Contoh:
nama_lengkap = "Rofi" # menyimpan teks
umur = 22     # menyimpan angka
#
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#
# B. Aturan Penamaan Variabel
#
# - Boleh: huruf, angka, underscore
# - Tidak boleh: diawali angka, ada spasi, atau pakai simbol aneh
#
# Contoh benar:
nama_depan = "Rofi"
usia = 22

# Contoh salah:
# nama depan = "Rofi"
# 2usia = 22
#
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#
# C. Tipe Data Dasar di Python
#
# 1. String (teks)
#    - Digunakan untuk menyimpan kata atau kalimat.
#    - Ditulis diantara tanda kutip ('') atau ("")
#
# Contoh:
nama_lengkap = "Rofi"     # Variabel
print(nama_lengkap)       # Output: Rofi
print(type(nama_lengkap)) # Output: <class 'str'>

#    Operasi string:
hobi = "Membaca"      # Variabel
print(hobi + " Buku") # Menggabungkan string
print(hobi.upper())   # Ubah jadi huruf besar semua
print(hobi.lower())   # Ubah jadi huruf kecil semua

# 2. Integer (bilangan bulat)
#    - Angka tanpa koma.
#    - Bisa digunakan untuk operasi aritmatika.
#
# Contoh:
umur = 20         # Variabel
print(umur + 2)   # Output: 22
print(type(umur)) # Output: <class 'int'>

# 3. Float (bilangan desimal)
#    - Angka dengan koma (desimal)
#
# Contoh:
tinggi_badan = 170.5      # Variabel
print(tinggi_badan)       # Output: 170.5
print(type(tinggi_badan)) # Output: <class 'float'>

# 4. Boolean (True/False)
#    - Hanya punya dua nilai: True atau False.
#    - Biasanya digunakan dalam logika dan kondisi.
#
# Contoh:
lulus = True       # Variabel
print(lulus)       # Output: True
print(type(lulus)) # Output: <class 'bool'>

nilai = 75         # Variabel
print(nilai > 60)  # Output: True
#
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#
# D. Konversi Tipe Data
#
# Kadang kita perlu mengubah tipe data.
#
# Contoh:
#
# 1. Tipe data int ke float
angka_bilangan_bulat = 10                            # Variabel
angka_bilangan_desimal = float(angka_bilangan_bulat) # Mengubah tipe data dari int ke float
print(angka_bilangan_desimal)                        # Output: 10.0
print(type(angka_bilangan_desimal))                  # Output: <class 'float'>

# 2. Tipe data float ke int
angka_bilangan_desimal = 10.0                       # Variabel
angka_bilangan_bulat = int(angka_bilangan_desimal)  # Mengubah tipe data dari float ke int
print(angka_bilangan_bulat)                         # Output: 10
print(type(angka_bilangan_bulat))                   # Output: <class 'int'>

# 3. Tipe data int ke string
umur = 22                                           # Variabel
print("Umur saya tahun ini adalah: " + str(umur))   # Output: Umur saya tahun ini adalah: 22
#
#-----------------------------------------------------------------