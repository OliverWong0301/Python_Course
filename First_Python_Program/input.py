print("How many Kilometers did you complete running today?")
kms = input()
miles = float(kms) / 1.60934
print(f"Ok, you've just said {kms}")

# round(thing to round, how many decimal points)
# or miles = round(miles, 2) then print line just need {miles}
print (f"And that is equal to {round(miles, 2)}")

