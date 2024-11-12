print(40*"=")
print("  KONVERSI ANGKA KE ROMAWI 1 - 10")
print(40*"=")


input = int(input("masukan angka 1-10 = "))
angka_romawi = {
    1:"I",
    2:"II",
    3:"III",
    4:"IV",
    5:"V",
    6:"VI",
    7:"VII",
    8:"VIII",
    9:"IX",
    10:"X"
}
hasil_romawi = angka_romawi[input]
print(f"Angka romawi nya adalah {hasil_romawi}")