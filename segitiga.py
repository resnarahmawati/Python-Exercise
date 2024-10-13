print('='*40)
print('     PROGRAM SEGITIGA SAMA KAKI')
print('='*40)

def segitiga():
    s = float(input('Masukkan Sisi : '))
    a = float(input('Masukkan Alas : '))
    t = float(input('Masukkan Tinggi : '))

    l = lambda a,t,: 1/2 * a * t
    k = lambda s: 3 * s
    print('LUAS SEGITIGA : ', l(a,t), 'cm2')
    print('KELILING SEGITIGA : ', k(s), 'cm2')

segitiga()
segitiga()
segitiga()