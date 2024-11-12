total = 0

for y in range(1,6):
    total += y

    if y <5:
        print(y, end='\n')
    else:
        print(y,'__+ ',end=' \n')

print (total)