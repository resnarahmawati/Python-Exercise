print("="*40)
print("             KERUCUT")
print("="*40)

s = float(input('Masukkan garis pelukis (s) : '))
PHI = 3.14
t = float(input("masukan tinggi kerucut: "))
r = float(input("masukan jari-jari kerucut: "))

volume = PHI*r*r*t
LP = PHI*r*(r+s)

print("volume : ",volume, "cm3")
print("LP : " ,LP, "cm2")