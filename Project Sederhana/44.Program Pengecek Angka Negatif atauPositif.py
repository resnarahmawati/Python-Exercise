def check_number(num):
    if num > 0:
        return "Positif"
    elif num < 0:
        return "Negatif"
    else:
        return "Nol"

number = float(input("Masukkan angka: "))
print(f"{number} adalah angka {check_number(number)}.")
