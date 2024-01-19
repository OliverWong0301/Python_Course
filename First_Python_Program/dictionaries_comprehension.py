# The syntax:
## {_ : _ for _ in _}

profile = dict(name = "Dieu Bang", age = 9, height = 130, weight = 32, email = "dieubang@yahoo.com")
uppercase_profile = {key.upper(): str(value).upper() for key, value in profile.items()} # str(value).upper() because int cant have attribute upper()
print(uppercase_profile)
# Just upper case the EMAIL key
uppercase_profile = {(key.upper() if key is "email" else key) : str(value).upper() for key, value in profile.items()}
print(uppercase_profile)


print("*** *** ***")
# Conditional logic with dictionaries
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_or_odd = {num : ("even" if num % 2 == 0 else "odd") for num in numbers}
print(even_or_odd)

even_or_odd = {num : ("odd" if num % 2 != 0 else "even") for num in range(1, 101)}
print(even_or_odd)

### ASCII 
char = {count : chr(count) for count in range(65, 91)}
print(char)