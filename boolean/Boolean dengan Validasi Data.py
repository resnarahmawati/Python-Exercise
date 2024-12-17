# Validasi data input menggunakan boolean
def validate_user_data(name, age):
    if not isinstance(name, str):
        return False
    if not isinstance(age, int):
        return False
    if age < 0:
        return False
    return True

print("Validasi data ('Alice', 25):", validate_user_data("Alice", 25))
print("Validasi data (123, -5):", validate_user_data(123, -5))
