print('''
\033[94m
=============================
        ENERGI KINETIK
=============================
''')
def kinetik():
    m = float(input('Masukkan massa (kg) :'))
    v = float(input('Masukkan kecepatan (m/s) :'))
    ek = lambda m,v: 1/2 * m * v**2 
    print('ENERGI KINETIK: ',ek(m,v))

kinetik()
kinetik()
kinetik()