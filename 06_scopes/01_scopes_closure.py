username = "abrar_11"

def func():
    # username = "ahmad_22"
    print(username)

# func()
# print(username)



x = 99

def func2():
    global x  # global keyword change the value or global variable
    x = 22

# func2()
# print(x)


#--- closure ---
def f1():
    x = 57
    def f2():
        print(x)

    return f2


result = f1()
# result()

def uper(num):
    def actual(x):
        return x ** num
    return actual

f = uper(2)
print(f(3))
