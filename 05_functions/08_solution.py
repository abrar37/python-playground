# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwrgs(**kwargs):
    # print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")



print_kwrgs(name="Hulk", power="Speed")
print_kwrgs(name="Hulk")
print_kwrgs(name="Hulk", power="Speed", enemy="Thanos")
