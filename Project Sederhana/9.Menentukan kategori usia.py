print('*'*40)
print('     PROGRAM KATEGORI USIA')
print('*'*40)
usia = int(input('Masukkan usia Anda: '))

if 0 <= usia <= 12:
    print('kategori: Anak-anak')
elif 13 <= usia <= 19:
    print('kategori: Remaja')
elif 20 <= usia <= 64:
    print('kategori: Dewasa')
elif usia >= 65:
    print('kategori: Lansia')