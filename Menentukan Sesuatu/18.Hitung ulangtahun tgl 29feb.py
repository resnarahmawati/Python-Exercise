def hitung_ulang_tahun(tahun_lahir, tahun_akhir):
    # Memastikan tahun akhir lebih besar dari tahun lahir
    if tahun_akhir <= tahun_lahir:
        return 0

    # Hitung berapa kali ulang tahun di tahun kabisat
    ulang_tahun_count = 0
    for tahun in range(tahun_lahir + 1, tahun_akhir + 1 ):
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            ulang_tahun_count += 1
    
    return ulang_tahun_count

tahun_lahir = int(input('Masukkan Tahun lahir: '))
tahun_akhir = 2024
ulang_tahun_count = hitung_ulang_tahun(tahun_lahir, tahun_akhir)
print(f"Jumlah ulang tahun yang bisa dirayakan sejak tahun {tahun_lahir} hingga {tahun_akhir}: {ulang_tahun_count}")
