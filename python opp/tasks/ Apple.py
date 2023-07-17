class Apple:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"color: {self.color}, weight: {self.weight}"


def filter_green_apple(ListApple):
    resultGreen = []
    for item in ListApple:
        if item.color.upper() == "GREEN":
            resultGreen.append(item)
    return resultGreen


def filter_heavy_apple(ListApple):
    resultheavy = []
    for item in ListApple:
        if item.weight > 200:
            resultheavy.append(item)
    return resultheavy


def predicate(apple_list, fun):
    result = fun(apple_list)
    return result


def print_list_item(l1):
    for apple in l1:
        print(apple)


apple1 = Apple("Green", 100)
apple2 = Apple("red", 250)
apple3 = Apple("RED", 350)
apple4 = Apple("Green", 100)
apple5 = Apple("Green", 300)

list_apple = [apple1, apple2, apple3, apple4, apple5]
Green_Apple_list = predicate(list_apple, filter_green_apple)
heavy_Apple_list = predicate(list_apple, filter_heavy_apple)

print_list_item(Green_Apple_list)
print("--------------------------------------")
print_list_item(heavy_Apple_list)
