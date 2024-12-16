
def menu():
    print("=== Menu Geometri ===")
    print("1. Luas dan Keliling Persegi")
    print("2. Luas dan Keliling Persegi Panjang")
    print("3. Luas dan Keliling Segitiga")
    print("4. Luas dan Keliling Lingkaran")
    print("5. Keluar")
    return input("Pilih menu (1-5): ")

def luas_keliling_persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    luas = sisi ** 2
    keliling = 4 * sisi
    print(f"Luas Persegi: {luas}")
    print(f"Keliling Persegi: {keliling}")

def luas_keliling_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas Persegi Panjang: {luas}")
    print(f"Keliling Persegi Panjang: {keliling}")

def luas_keliling_segitiga():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    sisi1 = float(input("Masukkan panjang sisi 1: "))
    sisi2 = float(input("Masukkan panjang sisi 2: "))
    sisi3 = float(input("Masukkan panjang sisi 3: "))
    luas = 0.5 * alas * tinggi
    keliling = sisi1 + sisi2 + sisi3
    print(f"Luas Segitiga: {luas}")
    print(f"Keliling Segitiga: {keliling}")

def luas_keliling_lingkaran():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    luas = 3.14 * (jari_jari ** 2)
    keliling = 2 * 3.14 * jari_jari
    print(f"Luas Lingkaran: {luas}")
    print(f"Keliling Lingkaran: {keliling}")

def main():
    while True:
        pilihan = menu()
        if pilihan == '1':
            luas_keliling_persegi()
        elif pilihan == '2':
            luas_keliling_persegi_panjang()
        elif pilihan == '3':
            luas_keliling_segitiga()
        elif pilihan == '4':
            luas_keliling_lingkaran()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
        input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()