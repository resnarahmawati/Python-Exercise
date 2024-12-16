baris = 5
char = 'a'
for i in range(baris):
    print(char * 5)
    char = chr(ord(char)+1)