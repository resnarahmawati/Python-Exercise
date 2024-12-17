# Validasi input menggunakan boolean
def is_valid_email(email):
    return "@" in email and "." in email

email = "example@example.com"
print("Is email valid:", is_valid_email(email))
