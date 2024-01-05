# Normal conditional statement
print("What is your name?")
name = input()

if name == "Hoang Tuan":
    print(f"Hello Sir, {name}")
elif name == "Hoang Quang":
    print(f"Hello bitch, you're not Sir Hoang Tuan")
else:
    print(f"Hello bastard, you're totally not Sir Hoang Tuan")


# Multi elif
color = input("What is your favorite color?")
if color == "red":
    print("You're hornie")
elif color == "yellow":
    print("You're betrayal")
elif color == "blue":
    print("You're peaceful")
elif color == "green":
    print("You're hopeful")
else:
    print("You're a monster")

# True or False, Yes or No, Have or Don't have
print("What is your favorite animal")
animal = input()

if animal:
    print("What a lovely: " + animal + " in the animal world")
else:
    print("You didn't fill in anything!!!")