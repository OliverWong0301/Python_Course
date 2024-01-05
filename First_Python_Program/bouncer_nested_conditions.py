# Ask for age
# 18 - 21 wristband
# 21+ drink, normal entry
# too young, sorry

print("How old are you?")
age = input()
if age:
    age = int(age)
    if age >= 21:
        print("Your have a normal entry")
    elif age >= 18:
        print("You need a wristband")
    else:
        print("Sorry kids, you are too young")
else:
    print("Please enter your age")