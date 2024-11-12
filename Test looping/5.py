total = 0
for y in range(1,6):
    total += y
    
    if y < 5:
        print(y, '+', end=' ')
    else:
        print(y, '=', end=' ')
        
print(total)