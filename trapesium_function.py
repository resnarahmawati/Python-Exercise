print('='*40)
print('             PROGRAM TRAPESIUM')
print('='*40)

def trapesium():
    a = float(input('Masukkan sisi a : '))
    b = float(input('Masukkan sisi b : '))
    c = float(input('Masukkan sisi c : '))
    d = float(input('Masukkan sisi d : '))
    t = float(input('Masukkan Tinggi : '))
    l = lambda a,b,t: 1/2 * (a+b) * t
    k = lambda a,b,c,d: a+b+c+d
    print('LUAS : ',l(a,b,t),'cm')
    print('KELILING : ',k(a,b,c,d,'cm'))

trapesium()
trapesium()
trapesium()