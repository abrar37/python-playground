# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):

    # print(*args)
    # print(args)

    # for i in args:
    #     print(i)

    return sum(args)

# print(sum_all(1, 3, 5))
print(sum_all(3, 5, 1, 9, 8, 7))
