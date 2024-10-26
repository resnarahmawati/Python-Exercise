print('''
=============================
       KALOR JENIS ES
=============================
''')
def kalor():
    m = float(input('Masukan massa benda:'))
    c = float(input('Masukankalor jenis es (dalam Joule per kilogram per derajat Celsius) :'))
    t = float(input('Masukan perubahan suhu es:'))
    Q = lambda m,c,t:  m * c * t
    print('KALOR JENIS ES:',Q(m,c,t))

    