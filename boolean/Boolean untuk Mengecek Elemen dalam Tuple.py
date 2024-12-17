# Boolean dengan tuple
options = ("yes", "no", "maybe")
user_input = "yes"

is_valid_option = user_input in options
print(f"Apakah '{user_input}' opsi valid:", is_valid_option)
