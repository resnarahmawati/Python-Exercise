print('='*40)
print('          PROGRAM TABUNG')
print('='*40)

def tabung():
    phi = 3.14
    r = float(input('Masukkan Jari-jari : '))
    t = float(input('Masukkan Tinggi : '))
    v = lambda phi,r,t: phi*r*r*t
    lp = lambda phi,r,t: 2*phi*r*(r+t)

    print('VOLUME : ',v(phi,r,t))
    print('LUAS PERMUKAAN : ',lp(phi,r,t))

tabung()
tabung()