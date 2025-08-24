# Latihan
#
# 1. Buat variabel berikut ini:
#    - nama       : string
#    - umur       : int
#    - tinggi     : float
#    - is_student : bool
# 2. Cetak semua nilai beserta tipe datanya.

nama = "Rofi"      # Variabel nama
umur = 22          # Variabel umur
tinggi = 170.5     # Variabel tinggi
is_student = False # Variabel is_student

print("Nama saya: " + nama)                         # Output: Nama saya: Rofi
print(type(nama))                                   # Output: <class 'str'>

print("Umur saya: " + str(umur) + " Tahun")         # Output: Umur saya: 22 Tahun
print(type(umur))                                   # Output: <class 'int'>

print("Tinggi badan saya: " + str(tinggi) +  " CM") # Output: Tingi badan saya: 170.5 CM
print(type(tinggi))                                 # Output: <class 'float'>

print(is_student > 2025)                            # Output: False
print(type(is_student))                             # Output: <class 'bool'>
