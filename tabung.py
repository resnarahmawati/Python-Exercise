print('='*40)
print('          PROGRAM TABUNG')
print('='*40)

phi = 3.14
r = float(input('Masukkan Jari-jari : '))
t = float(input('Masukkan Tinggi : '))
v = phi*r*r*t
lp = 2*phi*r*(r+t)

print('VOLUME : ',v)
print('LUAS PERMUKAAN : ',lp)