# Simple nested list with simple access
nested = [[1, 2, 3], ["Oliver", "Ginny", "Chang"]]
print(nested[0][2])
print(nested[1][-1])

# Print every single item from a nested list by using 2 loop
for index in nested:
    for val in index:
        print(val)

# Example for running an airbnb and here are the coordinates of the location:
coords = [[10.234, 9.688], [28.666, 3.9], [100.8, 18.7979]]
[[print(val) for val in index] for index in coords]
print([index for index in nested])

# Another example
board = [[index for index in range(1, 4)] for valx3 in range(1, 4)]
print(board)

x_and_o = [["X" if index % 2 != 0 else "O" for index in range(1, 4)] for valx3 in range(1, 4)]
print(x_and_o)

