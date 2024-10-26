print('='*40)
print('    PROGRAM KONVERSI SUHU ')
print('='*40)
def suhu():
    c = int(input('Masukkan suhu dalam celcius : '))
    r = lambda c: (4/5)* c
    f = lambda c: (9/5)* c + 32
    k = lambda c: c + 273
    print('Reamur : ', r(c),)
    print('Fahrenheit : ', f(c))
    print('Kelvin : ',k(c))

suhu()
suhu()