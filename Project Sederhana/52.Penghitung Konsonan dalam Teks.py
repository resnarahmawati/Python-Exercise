def count_consonants(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

text = input("Masukkan teks: ")
print(f"Jumlah huruf konsonan adalah {count_consonants(text)}.")
