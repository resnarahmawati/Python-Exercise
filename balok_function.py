print('='*40)
print('         PROGRAM BALOK')
print('='*40)
def balok():
    p = float(input('Masukkan Panjang : '))
    l = float(input('Masukkan Lebar : '))
    t = float(input('Masukkan Tinggi : '))
    v = lambda p,l,t : p*l*t
    lp = lambda p,l,t : 2*(p*l)+(p*t)+(l*t)

    print('VOLUME\t\t : ',v(p,l,t),'cm')
    print('LUAS PERMUKAAN\t : ',(p,l,t),'cm')

balok()
balok()
balok()
