print('='*40)
print('     PROGRAM MATEMATIKA JARAK')
print('='*40)

k = int(input('Masukkan kecepatan : '))
w = int(input('Masukkan waktu :'))
j = lambda k,w: k*w
print('JARAK : ',j(k,w))