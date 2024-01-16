# Take evens and odds but by transforming them into string
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(["Evens: " + str(num) for num in numbers if num % 2 == 0])
print(["Odds: " + str(num) for num in numbers if num % 2 != 0])

# Take events and odds even they are still interger
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# With else
print([num * 2 if num % 2 == 0 else num / 2 for num in numbers])
print([num * 3 if num % 2 != 0 else num * 5 for num in numbers])

# With .join() + string
string = "This is so exciting"
print("".join([char for char in string if char not in "aeiou"]))
print(" ".join([char for char in string if char not in "aeiou"]))
print(".".join([char for char in string if char not in "aeiou"]))