totalharga = float(input("Masukkan total belanja Anda : "))
totaldiskon = totalharga * 5 / 100
totalyangharusdibayarkan = totalharga - totaldiskon

if totalharga >= 100000:
    print(" SELAMAT ANDA MENDAPATKAN DISKON 5%")

print(' TOTAL DISKON : ', (totaldiskon))
print(' TOTAL HARGA SETELAH DISKON : ', (totalyangharusdibayarkan) )
