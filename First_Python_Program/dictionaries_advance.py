# POP to delete a pair values:

profile = dict(name = "John", age = 28, email = "john_ivy@gmail.com", scores = 99)
print(profile)

# Must turn the keys to string in pop()
profile.pop("email")
print(profile)

## popitem() to delete the last pair values in the dictionary
profile.popitem()
print(profile)

# UPDATE keys and values in a dictionary with another set of key value pairs
bio = dict(name = "Oliver", age = 38, email = "oliverwong0301@gmail.com", scores = 100, height = 170, nickname = "Bi")
bio1000 = {} # This meansan empty dictionary # This is for reference, we don't apply it here, we use the bio1 variable below:
bio1 = {

    "city": "San Francisco"

}
bio1.update(bio)
bio.update(bio1)
print(bio1)
print("******")
print(bio)



