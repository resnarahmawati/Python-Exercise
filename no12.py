def tentukan_grade(nilai):
    if 90 <= nilai <= 100:
        return 'A'
    elif 80 <= nilai < 90:
        return 'B'
    elif 70 <= nilai < 80:
        return 'C'
    elif 60 <= nilai < 70:
        return 'D'
    else:
        return 'E'

def main():
    siswa = {}
    
    while True:
        nama = input("Masukkan nama siswa (atau ketik 'selesai' untuk berhenti): ")
        if nama.lower() == 'selesai':
            break
        
        try:
            nilai = float(input(f"Masukkan nilai untuk {nama} (0-100): "))
            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai harus antara 0 dan 100.")
        except ValueError as e:
            print(e)
            continue
        
        grade = tentukan_grade(nilai)
        siswa[nama] = {'nilai': nilai, 'grade': grade}
    
    print("\nDaftar Nilai dan Grade Siswa:")
    for nama, info in siswa.items():
        print(f"Nama: {nama}, Nilai: {info['nilai']}, Grade: {info['grade']}")

if __name__ == "__main__":
    main()
