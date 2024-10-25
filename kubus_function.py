print('==========================')
print('       RUMUS KUBUS        ')
print('--------------------------')
def kubus():
    rusuk = float(input("Rusuk\t: "))
    luas = lambda rusuk: 4 * rusuk ** 2
    volume = lambda rusuk: rusuk ** 3
    print('Luas: ',luas(rusuk))
    print('Volume:',volume(rusuk))
kubus()
kubus()