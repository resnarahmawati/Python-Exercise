total = 0
w = 2
while w in range(12):
    total += w
    
    if w < 10:
        print(w, '+', end=' ')
    else:
        print(w, '=', end=' ')
    w = w + 2
        
print(total)