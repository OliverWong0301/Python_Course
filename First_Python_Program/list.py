# List of Python == Array in other languages

# colors = ["Red", "Yellow", "Blue", "Green", "Pink", "Orange", "Purple"]
# print(f"The length of list of color is: {len(colors)}")

# nums = [1, 2, 3.5, 8, 12]

# FOR
# for x in nums:
#     print(x)

# for y in colors:
#     print(y)

# index = 0
# while index < len(colors):
#     print(f"{index+1} color is: {colors[index]}")
#     index += 1

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# # Define your code below:
# index = 0
# result = ""
# while index < len(sounds):
#     result += sounds[index]
#     index += 1
#     print(result.upper())

# for i in sounds:
#     result += i
#     print(result.upper())

# APPEND: add 1 single item
list = [1, 2, 3, 4, 5, 6, 7]
list.append(8)
print(list)

# EXTEND: add as many as you want
list.extend([8, 9, 10, 11, 12])
print(list)

# INSERT: Location in the list + content
list.insert(0, 0)
list.insert(len(list), "Final")
print(list)

# CLEAR
# list.clear()
# print(f"Current list is: {list}")

# POP
list.pop()
list.pop(0)
print(list)

# REMOVE
list.remove(8)
print(list)

# COUNT , REVERSE, SORT
print(list.count(2))
list.reverse()
print(list) # REVERSE can not run if it is inside the print order

# SORT
another_list = [9, 3, 4, 5.6, 6.8, 32, 10]
another_list.sort()
print(another_list) # SORT can not run if it is inside the print order

#JOIN (Applied for string)
name = ["Mr", "Hoang Tuan"]
print(". ".join(name))
print(" ".join(name))

print("\n***NEXT*** \n")

#SLICES
print(another_list[2:])
print(another_list[:2])
print(another_list[1:5])

# SWAPPING VALUE

name[0], name[1] = name[1], name[0]
print(name)

friends = ['ashley', 'matt', 'michael']
print([friend.capitalize() for friend in friends])
# OR
print([friend[0].upper() + friend[1:] for friend in friends])