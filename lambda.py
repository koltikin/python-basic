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


class Apple:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"color: {self.color}, weight: {self.weight}"

    def __repr__(self):
        return f"color: {self.color}, weight: {self.weight}"


apple1 = Apple("red", 240)
apple2 = Apple("green", 180)
apple3 = Apple("red", 100)
apple4 = Apple("red", 150)
apple5 = Apple("green", 200)

apple_list = [apple1, apple2, apple3, apple4, apple5]
# print(apple1)
# print(apple_list)


def fillter(l1, fun):
    result_list = []
    for item in l1:
        if fun(item):
            result_list.append(item)

    print(result_list)
    return result_list


fillter(apple_list, lambda item: item.color.lower() == "red")
fillter(apple_list, lambda item: item.weight > 150)
