# Eg1:
string = 'hello'
print({char for char in string if char in 'aeiou'})
print(len({char for char in string if char in 'aeiou'}) == 5)


# Eg2:
ventures = 'sequoia'
print({char for char in ventures if char in "aeiou"})
print(len({char for char in ventures if char in "aeiou"}) == 5)