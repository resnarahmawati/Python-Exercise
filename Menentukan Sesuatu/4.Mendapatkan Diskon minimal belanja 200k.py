
HARGA_BARANG_SATU = 20000
HARGA_BARANG_DUA = 50000
HARGA_BARANG_TIGA = 40000
HARGA_BARANG_EMPAT = 120000

total = HARGA_BARANG_SATU + HARGA_BARANG_DUA + HARGA_BARANG_TIGA + HARGA_BARANG_EMPAT
diskon = 17250
bayar = total - diskon

print('Barang 1 : ',str(HARGA_BARANG_SATU))
print('Barang 2 : ',str(HARGA_BARANG_DUA))
print('Barang 3 : ',str(HARGA_BARANG_TIGA))
print('Barang 4 : ',str(HARGA_BARANG_EMPAT))
print('Total : ', str(total))
print('Diskon : ', str(diskon))
print('Jumlah Bayar : ', str(bayar))
print('SELAMAT ANDA MENDAPATKAN DISKON 7,5% JIKA MINIMAL BELANJA 200K')