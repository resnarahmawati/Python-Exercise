print('='*40)
print('         PROGRAM PERSEGI PANJANG')
print('='*40)

def persegi_panjang():
    p = int(input('Masukkan Panjang : '))
    l = int(input('Masukkan lebar : '))
    luas = lambda p,l: p*l
    print('Luas : ',luas(p,l),'Cm2')

persegi_panjang()
persegi_panjang()