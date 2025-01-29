# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = 20
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Tickes price for you is $", price)

# Direct concatenation of the string and the variable
print("Tickes price for you is $" + str(price))

# Alternatively, use of f-string
print(f"Tickets price for you is ${price}") 
    