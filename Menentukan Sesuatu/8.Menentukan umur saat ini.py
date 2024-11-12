import datetime as dt

print('Silahkan Masukkan tanggal, Bulan, dan Tahun lahir anda')
tanggal = int(input('Tanggal :'))
bulan = int(input('Bulan: '))
tahun = int(input('Tahun lahir: '))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f'Tanggal lahir anda adalah: {tanggal_lahir}')

hari_ini = dt.date.today()
print(f'Hari ini tanggal: {hari_ini}')
umur_hari = hari_ini-tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days %365)//30

print(f'Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan')
