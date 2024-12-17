# Decorator untuk validasi boolean
def validate_input(func):
    def wrapper(value):
        if not isinstance(value, int):
            return False
        return func(value)
    return wrapper

@validate_input
def is_positive(value):
    return value > 0

print("Is 5 positive:", is_positive(5))
print("Is 'abc' positive:", is_positive("abc"))
