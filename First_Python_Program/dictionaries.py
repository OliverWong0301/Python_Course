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