# JARAK LENSA OBJEKTIF DAN LENSA OKULER
# d = fob + 4 fp + fok

print('''
======================================
JARAK LENSA OBJEKTIF DAN LENSA OKULER
======================================
''')
def jaraklensa():
    f_ob = float(input('Masukkan Jarak fokus lensa objektif :'))
    fp = float(input('Masukkan Jarak fokus lensa pembalik  :'))
    f_ok = float(input('Masukkan Jarak fokus lensa okuler :'))
    d = lambda f_ob,fp,f_ok: f_ob + 4 + fp + f_ok
    print('JARAK LENSA OBJEKTIF DAN LENSA OKULER:',d(f_ob,fp,f_ok))

jaraklensa()
jaraklensa()
jaraklensa()