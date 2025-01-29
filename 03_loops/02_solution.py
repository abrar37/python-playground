# Calculate the sum of even numbers up to a given number n.

num = 10
sum_val = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        sum_val += i

print("Sum of even numbers is:",sum_val)