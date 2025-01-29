# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

given_number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(given_number, "x", i, "=", given_number * i)
