totalharga = int(input(" Masukkan total belanja Anda : "))
totaldiskon = int(input(" Masukkan Diskon : "))
totalyangharusdibayarkan = totalharga - totaldiskon

if totalharga >= 100000:
    print(" SELAMAT ANDA MENDAPATKAN DISKON ",totaldiskon)

print(' TOTAL DISKON : ', (totaldiskon))
print(' TOTAL HARGA SETELAH DISKON : ', (totalyangharusdibayarkan))
