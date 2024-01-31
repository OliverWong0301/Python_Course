# # How parameters work as the inputs of the fucntion

# # Square nums example:
# num = int(input("Fill in your number to square it: "))

# def square(num):
#     return num * num

# print(square(num))

# # Happy birthday example:
# name = input("What is the name Sir? ")

# def happy_birthday(name):
#     print("\nHappy Birthday to you!!! " * 2)
#     print(f"Happy Birthday to {name}")
    
# happy_birthday(name)
# # print(happy_birthday(name)) ===> will lead to another print of the execute print in the function and it leads to print out the None value

# # 2 parameters:
# a = int(input("Give the value of a: "))
# b = int(input("Give the value of b: "))

# def add(a, b):
#     return f"Sum of a & b is: {a + b}"

# print(add(a, b))

# Common mistakes as putting the return in incorrect place

def sum_odd_numbers(numbers):
    total = 0 # This variable is called local scope, which is declared inside the function and you can not access it outside of the function
    for num in numbers:
        if num % 2 != 0:
            total += num
            #return total: wrong place which return 1
        #return total: wrong place which retrun 1
    return total #correct place

print(sum_odd_numbers([1,2,3,4,5,6,7,8]))

# return can replace else if there is only 2 conditions:
num = int(input("Fill in your number to see it is odd? ")) # This is called global scope, which you can use anywhere incld inside the function

def is_odd(num):
    if num % 2 != 0:
        return True
    return False #instead of else:
                                # return False
print(is_odd(num))

# Default parameters: by giving behind it =
def exponent(num1, num2=2):
    return num1 ** num2
print(exponent(3)) 

# a default parameter can be a function

# An example of using the global scope by method global standing right before the variable name happens inside the function
total = 0
def sum_it_up():
    global total
    total += 1
    return total

print(sum_it_up())

# An example of using local scope from a parents function by a child function (nested) || using nonlocal method
def outer():
    count = 10
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

print(outer())