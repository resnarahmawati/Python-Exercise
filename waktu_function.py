print('='*40)
print('     PROGRAM MATEMATIKA WAKTU')
print('='*40)
def waktu():
    j = int(input('Masukkan Jarak : '))
    k = int(input('Masukkan kecepatan :'))
    w = lambda j,k: j / k
    print('Waktu : ',w(j,k))

waktu()
waktu()