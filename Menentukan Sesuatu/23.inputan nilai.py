#buatlah program berupa inputan mapel,nilai uas,tugas
#tentukan grade 
#a>85
#b 70<85
#c 60<70
#d 0<60
mapel = input('Mata pelajaran : ')
nilaiuas = int(input('Masukkan nilai UAS : '))
tugas = int(input('Masukkan nilai tugas : '))
grade = nilaiuas+tugas
r = grade/2

print ('Mata Pelajaran',mapel)
if r >= 85:
    print('Grade A')

elif r >= 70 and r <85:
    print('Grade B')

elif r >= 60 and r < 70:
    print('Grade C')

elif r <=59:
    print('Grade D')
