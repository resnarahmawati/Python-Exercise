baris = 5

for i in range(baris):
    print("*"*i)
    i += 1
    if i>4:
        print("*"*7)
no = 1
for no in range(baris):
    print("*"*baris)
    baris -= 1