def day_of_week(number):
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    return days[number - 1] if 1 <= number <= 7 else "Angka tidak valid."

day = int(input("Masukkan angka (1-7): "))
print("Hari:", day_of_week(day))
