# PERCEPATAN RATA-RATA
# a= V2 - V1 / t2 - t1

print('''
=============================
    PERCEPATAN RATA-RATA
=============================
''')

def percepatan():
    v1 = float(input('Masukan kecepatan 1: '))
    v2 = float(input('Masukan Kecepatan 2: '))
    t1 = float(input('Masukan waktu 1: '))
    t2 = float(input('Masukan waktu 2: '))
    a = lambda v1,v2,t1,t2: v1 - v2 / t2 - t1
    print('PERCEPATAN RATA-RATA:', a(v1,v2,t1,t2))

percepatan()
percepatan()
percepatan()