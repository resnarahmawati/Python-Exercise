def travel_time(distance, speed):
    return distance / speed

distance = float(input("Masukkan jarak (km): "))
speed = float(input("Masukkan kecepatan (km/jam): "))
print(f"Waktu tempuh: {travel_time(distance, speed):.2f} jam.")
