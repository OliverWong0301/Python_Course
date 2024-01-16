# List comprehension contains looping
nums = [1, 2, 3]
count = [x * 10 for x in nums]
print(count)

# List comprehension vs looping (tradiontional style)
numbers = [1, 3, 5, 7, 9]
doubled_numbers = []

for x in numbers:
    doubled_number = x * 2
    doubled_numbers.append(doubled_number)

print(doubled_numbers)

### Or use contain loop
doubled_numbers = [x * 2 for x in numbers]
print(doubled_numbers)

# With String
name = "Oliver"
print([char.upper() for char in name])

string = ["oliver", "chang", "ginny", "cindy"]
print([char[0].upper() for char in string])
print([char[0].upper() + char[1:] for char in string])

# With Range
print([num * 10 for num in range(1, 6)])

# With boolean - Please note that in Python: 0, empty string, empty list, empty object are equal to False
print([bool(val) for val in [0, [], ""]])

# Convert a list of num => string
print([str(x) for x in numbers])

# Another funny example
my_num = [1, 2, 3, 4, 5, 6]
print([str(x) + " * Hello" for x in my_num])