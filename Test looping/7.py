total = 0
w = 1
while w in range(6):
    total += w
    
    if w < 5:
        print(w, '+', end=' ')
    else:
        print(w, '=', end=' ')
    w = w + 2
        
print(total)