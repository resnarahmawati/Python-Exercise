def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Masukkan angka: "))
if is_prime(number):
    print(number, "adalah bilangan prima.")
else:
    print(number, "bukan bilangan prima.")
