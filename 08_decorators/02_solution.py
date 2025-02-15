# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.


def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key} = {value}" for key, value in kwargs.items())
        print(f"Calling: {func.__name__} with {args_value} and with kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper


@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting} {name},")


greet("Jack", greeting="Hi")