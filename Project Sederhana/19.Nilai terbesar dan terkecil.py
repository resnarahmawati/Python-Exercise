#ada inputan 3 Angka, tentukan nilai terbesar dan terkecil 

x = int(input("Masukkan bilangan pertama: "))
y = int(input("Masukkan bilangan kedua: "))
z = int(input("Masukkan bilangan ketiga: "))


if (x >= y) and (x >= z):
    terbesar = x
elif (y >= x) and (y >= z):
    terbesar = y
else:
    terbesar = z

if (x <= y) and (x <= z):
    terkecil = x
elif (y <= x) and (y <= z):
    terkecil = y
else:
    terkecil = z

print(f"Nilai terbesar adalah: {terbesar}")
print(f"Nilai terkecil adalah: {terkecil}")
