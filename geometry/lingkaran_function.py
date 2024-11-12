print('='*40)
print('         PROGRAM LINGKARAN')
print('='*40)

def lingkaran():
    phi = 3.14
    r = float(input('Masukkan Jari-jari : '))
    l = lambda phi,r:phi * r * r
    k = lambda phi,r:2 * phi * r
    d = lambda r:2 * r

    print('LUAS LINGKARAAN : ', l(phi,r))
    print('KELILING LINGKARAN : ', k(phi,r))
    print('DIAMETER LINGKARAN : ', d(r))

lingkaran()
lingkaran()
lingkaran()
lingkaran()