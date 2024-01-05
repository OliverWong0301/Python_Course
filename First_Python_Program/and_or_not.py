# AND
a = 4
b = a
c = "correct"
d = "in"
if a and b == 4:
    print(c)
else:
    print(d + c)

# OR
print("What is the city that you are living in?")
city = input()
if city == "Los Angeles" or city == "San Francisco":
    print("You're living in California")
else:
    print("You're not living in California")        

# NOT
print("How old are you?")
age = int(input()) # Allow the input to be interger
if not ((age >= 0 and age <= 17) or age >= 65):
    print("You have to pay $10 ticket as you're an adult")
else:
    print("You have free ticket because you're either child or senior")