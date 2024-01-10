# for x in range(1, 10):
    #print(x)

# for letter in "hello pussy":
    #print(letter)

# for num in range(0, 100, 5):
#     print(num)

# x = 0
# for num in range(10, 21):
#     if num % 2 != 0:
#         x =+ num
#         print(x)

# times = input("How many times do i have to tell you to clean up your room? ")
# times = int(times)

# for x in range(times):
#     print(f"Time {x+1}: CLEAN UP YOUR ROOM")

# for x in range(1, 21):
#     if x == 4 or x == 13:
#         print(f"X = {x}: Unlucky number")
#     elif x % 2 != 0:
#         print(f"X = {x}: Odd number")
#     else:
#         print(f"X = {x}: Even number")

for x in range(1, 21):
    if x == 4 or x == 13:
        stateMent = "Unlucky number"
    elif x == 6 or x == 8:
        stateMent = "Chinese lucky number"
    elif x == 7 or x == 9:
        stateMent = "Western lucky number"
    elif x % 2 != 0:
        stateMent = "Odd number"
    else:
        stateMent = "Even number"
    print(f"X = {x}: {stateMent}")