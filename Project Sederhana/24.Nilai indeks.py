def tentukan_indeks(nilai):
    if 80 <= nilai <= 100:
        return 'A'
    elif 70 <= nilai < 80:
        return 'B'
    elif 55 <= nilai < 70:
        return 'C'
    elif 40 <= nilai < 55:
        return 'D'
    else:
        return 'E'
    
def main():
    try:
        nilai = float(input("Masukkan nilai ujian mahasiswa: "))
        
        if nilai < 0 or nilai > 100:
            print("Nilai harus antara 0 dan 100.")
            return

        indeks = tentukan_indeks(nilai)
        
        print(f"Nilai: {nilai}")
        print(f"Indeks: {indeks}")

    except ValueError:
        print("Masukkan nilai yang valid (angka).")

if __name__ == "__main__":
    main()

