def cek_huruf(huruf):
    
    vokal = 'AEIOUaeiou'

    
    if huruf.isalpha() and len(huruf) == 1:
        if huruf in vokal:
            return 'Vokal'
        else:
            return 'Konsonan'
    else:
        return 'Bukan huruf'

input_huruf = input("Masukkan sebuah huruf (A-Z atau a-z): ")

print(cek_huruf(input_huruf))
