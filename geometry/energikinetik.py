print('''
\033[94m
=============================
        ENERGI KINETIK
=============================
''')

m = float(input('Masukkan massa (kg) :'))
v = float(input('Masukkan kecepatan (m/s) :'))
ek = 1/2 * m * v**2 

print('ENERGI KINETIK: ', round(ek))