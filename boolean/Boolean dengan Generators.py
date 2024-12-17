# Generator dengan boolean
numbers = range(10)

even_numbers = (n for n in numbers if n % 2 == 0)
print("Apakah ada bilangan genap:", any(even_numbers))
