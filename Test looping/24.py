nama = []
pembayaran = []

for i in range(5):
    nama.append(input(f"Nama siswa {i+1}: "))
    pembayaran.append(int(input(f"pembayaran {nama[i]}: ")))

print("\nRekapan Pembayaran: ")
for i in range(5):
    print(f"{i+1}. {nama[i]:<15}: {pembayaran[i]}")

print("\nJumlah Total pembayaran: ",sum(pembayaran))