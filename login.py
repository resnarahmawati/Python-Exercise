USERNAME = 'resna1@gmail.com'
PASSWORD = '12345678'

username = input("Masukkan username\t: ")
password = input("Masukkan password\t: ")

if username != USERNAME:
    print("Username tidak tersedia")
elif username == USERNAME and password != PASSWORD:
    print("Password salah")
else: 
    print("Selamat datang" , username)

