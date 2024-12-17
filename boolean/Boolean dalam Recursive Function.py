# Boolean dengan rekursi
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

print("Is 'radar' palindrome:", is_palindrome("radar"))
print("Is 'hello' palindrome:", is_palindrome("hello"))
