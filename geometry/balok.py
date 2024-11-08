print("="*40)
print("BALOK")
print("="*40)

p = float(input("masukan panjang balok: "))
l = float(input("masukan lebar: "))
t = float(input("masukan tinggi: "))
k = 4*l*t
v = p*l*t
lp = 2*(p*l)+(p*t)+(l*t)

print("volume : ",v, " cm3")
print("luas permukaan : ",lp, " cm2")
print("keliling : ",k, " cm2")