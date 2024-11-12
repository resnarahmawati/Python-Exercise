#volume (2 x phi x jari x tinggi) 
#luas permukaan ( phi x jari x jari + 2 x phi x jari x tinggi
print ("==============================")
print ("        PROGRAM TABUNG       ")
print ("==============================")

r = float(input('Masukkan Jari-jari :'))
t = float(input('Masukkan Tinggi : '))
phi = 3.14
v = 2 * phi * r * t
lp = (phi * r * r)+(2 * phi *r * t)

print('Volume : ', v, 'cm2')
print('Luas permukaan : ', lp, 'cm')