# () : tuple - [] : list

# This is a list:
numbers = [1, 2, 3]
print(numbers)

## You can change the list because it is mutable:
numbers = ["hello", 1, 38, "handsome"]
print(numbers)

# BUT THIS IS A TUPLE
numbers = (1, 2, 3)
print(numbers)

## Since it was a tuple, it is immutable and you can't change it
# numbers.append(1)
# numbers.pop()

# Example: on unchanging data
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
for i in months:
    print(f'This month is: {i}')


print('*** *** ***')
# Tuple also can be used as keys in dictionaries but list can not
hotel_location = {

    (39.39, 79.79): "Tokyo",
    (100, 2003): "Los Angeles",
    (68, 98.999): "London"

}

print(hotel_location[(68, 98.999)])

### ALL items() returns tuple