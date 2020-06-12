
def is_palindrome(data):
    if data == "".join(list(data)[::-1]):
        return 1
    else:
        return 0


result = is_palindrome("Deleveled")

if result:
    print("palindrome")
else:
    print("Not a palindrome")