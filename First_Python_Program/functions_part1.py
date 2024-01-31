# METHODS ARE A DIFFERENT STYLE OF FUNCTION
# print() is a built-in function

## Eg1:
def happy_birthday():
    print("\nHappy Birthday to you\n" * 10)
happy_birthday()

## Eg2 (high level):
name = input('What is your name? ')

def say_hello(name):
    print(f'\nHello to {name}\n' * 3)
    
say_hello(name)