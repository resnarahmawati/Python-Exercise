print('='*40)
print('         PROGRAM KERUCUT')
print('='*40)
def kerucut():
    s = float(input('Masukkan garis pelukis (s) : '))
    r = float(input('Masukkan Jari-jari : '))
    phi = 3.14
    t = float(input('Masukkan Tinggi : '))

    v = lambda r,phi,t: 1/3*phi*r*r*t
    la = lambda r,phi: phi*r*r
    selimut = lambda r,phi: phi *r*r
    lp = lambda s,r,phi: phi*r*(s+r)

    print('VOLUME : ',v(r,phi,t),'cm')
    print('LUAS ALAS : ',la(r,phi),'cm')
    print('SELIMUT : ',(r,phi),'cm')
    print('LUAS PERMUKAAN : ',lp(s,r,phi),'cm')

kerucut()
kerucut()