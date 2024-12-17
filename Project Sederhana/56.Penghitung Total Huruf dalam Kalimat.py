text = input("Masukkan kalimat: ")
letter_count = sum(1 for char in text if char.isalpha())
print(f"Jumlah huruf dalam kalimat adalah {letter_count}.")
