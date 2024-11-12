print('='*40)
print('     PROGRAM PERSEGI')
print('='*40)
def persegi():
    sisi = int(input('Sisi\t\t: '))

    luas = lambda s: s * s
    keliling = lambda s: 4 * s

    print('Luas\t\t: ',luas(sisi), 'cm2')
    print('Keliling\t: ',keliling(sisi), 'cm')

persegi()
persegi()
persegi()
persegi()