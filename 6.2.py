import re
def is_palindrome(s):
    cleaned = re.sub(r'[^A-Za-zА-Яа-я0-9]', '', s).lower()
    return cleaned == cleaned[::-1]
assert is_palindrome("level") == True 
assert is_palindrome("Лёша на полке клопа нашёл") == True  
assert is_palindrome("Hello") == False 
assert is_palindrome("12321") == True 
assert is_palindrome("!!!???") == True 
print("Все тесты прошли успешно!")
