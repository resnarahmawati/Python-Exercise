print('='*40)
print('         PROGRAM LIMAS SEGITIGA')
print('='*40)

def limas():
    luas = int(input('Masukkan Luas : '))
    tinggi = int(input('Masukkan tinggi : '))
    v = lambda l,t:  1/3*l*t
    print('VOLUME\t : ',v(luas,tinggi), ' cm')

limas()
limas()
limas()