import sys


def hello(*args):
    print(type(args))
    print("hello", args[2], args[1], args[0])  # *args is a tuple


hello("ziay", 32, 1990)


def hi(**kwargs):
    print(type(kwargs))  # **kwargs is a dictionary
    # print(
    # f"hello {kwargs['first_name']}, you are {kwargs['age']}, you are a {kwargs['major']}")

    # for valu in kwargs.values():
    #     print(valu)

    # for keys in kwargs.keys():
    #     print(keys)


#     for key, value in kwargs.items():
#         print(key + ": " + str(value))


# hi(first_name="ziya", age=32, major="programmer")

print(sys.executable)
