import functools

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rsult = reduce(lambda x, y,: x * y, my_list)
# print(rsult)

print(functools.reduce(lambda x, y: x * y, my_list))


name = input("what is your name?: ")
