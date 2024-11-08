print('='*40)
print('          PROGRAM DEBIT')
print('='*40)
def debit():
    v = int(input('Masukkan Volume : '))
    w = int(input('Masukkan waktu :'))
    d = lambda v,w: v / w
    print('DEBIT : ',d(v,w))

debit()
debit()
debit()