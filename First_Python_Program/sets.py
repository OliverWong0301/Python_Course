### SETS
## Sets are like formal mathematical sets
## Set do not have duplicated values
## Elements in sets aren't ordered
## You can not access sets by index because they don't have order
## Sets can be useful if you need to keep track of a collection of elements and you don't wanna care abt ordering, keys, values and duplicates

# Creating a set by set()
s = set({1, 4, 5})

# Creating a set by simply put {}
s = {1, 8, 5}

s = {1, 3, 5}

print(s)

# Access each element by loops:
for i in s:
    print(i)

# Change a list into a set in case of the list has too many elements and might be duplicated (In this case there are 2 Tokyo):
cities = ['Los Angeles', 'Tokyo', 'Kyoto', 'Singapore', 'Bali', 'Bangkok', 'London', 'San Francisco', 'Paris', 'Berlin', 'Roma', 'Shanghai', 'Toronto', 'Sydney', 'Tokyo']
print(cities)
print(len(cities))
print(set(cities))
print(len(set(cities)))
