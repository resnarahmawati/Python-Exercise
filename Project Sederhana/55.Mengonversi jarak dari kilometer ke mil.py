def km_to_miles(km):
    return km * 0.621371

km = float(input("Masukkan jarak dalam kilometer: "))
print(f"{km} kilometer sama dengan {km_to_miles(km):.2f} mil.")
