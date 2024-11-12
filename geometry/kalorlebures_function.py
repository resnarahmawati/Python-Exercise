print('''
=============================
       KALOR LEBUR ES
=============================
''')
def kalor():
    m = float(input('Masukkan massa benda:' ))
    l = float(input('Masukkan kalor lebur es (dalam Joule per kilogram):'))
    Q2 = lambda m,l: m * l
    print('KALOR LEBUR ES : ', Q2(m,l))

kalor()
kalor()
kalor()