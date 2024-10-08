print('='*40)
print('         PROGRAM BALOK')
print('='*40)

p = float(input('Masukkan Panjang : '))
l = float(input('Masukkan Lebar : '))
t = float(input('Masukkan Tinggi : '))
v = p*l*t
lp = 2*(p*l)+(p*t)+(l*t)

print('VOLUME : ',v)
print('LUAS PERMUKAAN : ',lp)