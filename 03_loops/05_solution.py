# Given a string, find the first non-repeated character

input_str = "Betty Botter Bought Some Butter"

for char in input_str:
    if input_str.count(char) == 1:
        print("First non-repeated character is:", char)
        break
