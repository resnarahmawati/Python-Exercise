print('='*40)
print('           PROGRAM BOLA')
print('='*40)

def bola():
    phi = 3.14
    r = float(input('Masukkan JAri-jari : '))
    v = lambda phi,r: 4/3*phi*r*r*r
    lp = lambda phi,r: 4*phi*r*r

    print('VOLUME : ',v(phi,r),'cm')
    print('LUAS PERMUKAAN\t : ',lp(phi,r),'cm')

bola()
bola()