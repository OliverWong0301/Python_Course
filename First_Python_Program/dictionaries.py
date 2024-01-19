# Introduction of a complicated list which is contains a collection of value
## Shopping Cart

### Item1:
#### Name:
#### Quantity:
#### Price:

### Item2:
#### Name:
#### Quantity:
#### Price:

# So we use something called dictionaries which consists of key value pairs || SAME WITH OBJECT IN JAVASCRIPT

shopping_cart = {

    "name": "Chicken",
    "quantity": 8,
    "price": 20,
    "unitPrice": "USD",

}
print(shopping_cart)

print("******")

# Use dict() as add in into a variable
shopping_cart = dict(name = "Apple", price = 20, quantity = 6, unitPrice = "USD", expired = False)
print(shopping_cart)

print(f"The price of apple is: {shopping_cart["price"]}")

# Pull out the values out by .values()
for x in shopping_cart.values():
    print(x)

# Pull out the keys out by .keys()
for y in shopping_cart.keys():
    print(y)

# Access all items in the dictionary by .items()
print(shopping_cart.items())

# Pull out the key value pair in the dictionary by give 2 variables before .item()
for key, value in shopping_cart.items():
    print(key, ": ", value)
    print(f"{key}: {value}")

# Clear the dictionary by .clear()
shopping_cart.clear()
print(shopping_cart)

# Create keys values pair by another method {}.fromkeys()
## The keys must be put in [] as a list otherwise computer will iterate through every single alphabet of the string
## Example of a way of initial new dictionary with a same values but different keys
profile = {}.fromkeys(["name", "age", "scores", "email", "height"], "unknown")
print(profile)

## But for range, it is default as a list
numbers = {}.fromkeys(range(1, 11), "unknown")
print(numbers)

bio = profile.copy()
print(f"bio is: {bio}")