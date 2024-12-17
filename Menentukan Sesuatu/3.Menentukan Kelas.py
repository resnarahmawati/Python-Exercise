print('='*40)
print('       MENENTUKAN KELAS X PPLG')
print('='*40)

nama = input('Masukkan Nama Lengkap : ')
nilai = int(input('Masukkan No Absen (se jurusan) : '))

print(nama)
if 1 <= nilai <= 36:
    print(f'X PPLG 1')
elif 37 <= nilai <= 72:
    print(f'X PPLG 2')
elif nilai >= 73:
    print(f'BUKAN KELAS X PPLG')