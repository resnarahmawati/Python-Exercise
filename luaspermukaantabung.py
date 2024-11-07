print ('='*40)
print ('    LUAS PERMUKAAN TABUNG')
print ('='*40)

PHI = 3.14
r = int(input('Masukkan Jari-jari : '))
t = int(input('Masukkan Tinggi : '))
lp = PHI*r*r + 2*PHI*r*t
print (f'Luas permukaan : ',lp,'cm2')