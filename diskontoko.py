HARGA_BARANG_SATU = 48000
HARGA_BARANG_DUA = 3000
HARGA_BARANG_TIGA = 15000
HARGA_BARANG_EMPAT = 20000

total = HARGA_BARANG_SATU + HARGA_BARANG_DUA + HARGA_BARANG_TIGA + HARGA_BARANG_EMPAT
diskon = 10750
bayar = total - diskon

print('Buku : ',str(HARGA_BARANG_SATU))
print('Penghapus : ',str(HARGA_BARANG_DUA))
print('Pensil 1 lusin : ',str(HARGA_BARANG_TIGA))
print('Pengserut Pensil: ',str(HARGA_BARANG_EMPAT))
print('Total : ', str(total))
print('Diskon : ', str(diskon))
print('Jumlah Bayar : ', str(bayar))
print('SELAMAT ANDA MENDAPATKAN DISKON 12,5%')