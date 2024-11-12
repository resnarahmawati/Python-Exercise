print ('='*40)
print ('    LUAS PERMUKAAN TABUNG')
print ('='*40)

def lptabung():
    PHI = 3.14
    r = int(input('Masukkan Jari-jari : '))
    t = int(input('Masukkan Tinggi : '))
    lp = lambda r,t: PHI*r*r + 2*PHI*r*t
    print (f'Luas permukaan : ',lp(r,t),'cm2')

lptabung()
lptabung()