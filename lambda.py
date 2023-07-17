import functools

my_list = [1, 2, 3, 4, 5, 6]

rsult = functools.reduce(lambda x, y,: x * y, my_list)
print(rsult)

# print(functools.reduce(lambda x, y: x * y, my_list))


# name = input("what is your name?: ")

# print(functools.reduce(lambda x, y: x + " & " + y, name))


def calculate(x, y, fun):
    print(fun(x, y))


calculate(8, 9, lambda x, y: x + y)
calculate(18, 6, lambda x, y: x - y)
calculate(13, 5, lambda x, y: x * y)
calculate(26, 9, lambda x, y: x / y)
