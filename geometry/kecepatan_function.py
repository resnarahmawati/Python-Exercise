print('='*40)
print('     PROGRAM MATEMATIKA KECEPATAN')
print('='*40)
def kecepatan():
    j = int(input('Masukkan Jarak : '))
    w = int(input('Masukkan waktu :'))
    k = lambda j,w: j / w  
    print('KECEPATAN : ',k(j,w))

kecepatan()
kecepatan()