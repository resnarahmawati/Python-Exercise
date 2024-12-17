numbers = list(map(float, input("Masukkan angka (pisahkan dengan spasi): ").split()))
average = sum(numbers) / len(numbers)
print(f"Rata-rata angka adalah {average:.2f}.")
