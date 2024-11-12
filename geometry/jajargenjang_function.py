print('='*40)
print('         PROGRAM JAJAR GENJANG')
print('='*40)

def jajargenjang():
    a = float(input('Masukkan alas : '))
    t = float(input('Masukkan Tinggi : '))
    p = float(input('Masukkan Panjang : '))
    le = float(input('Masukkan Lebar : '))
    l = lambda a,t,: a * t
    k = lambda p,le: 2 * (p+le)

    print('LUAS JAJAR GENJANG : ', l(a,t,),'cm')
    print('KELILING JAJAR GENJANG : ', k(p,le),'cm')

jajargenjang()
jajargenjang()

  