def count_char(str, ch):
    return sum(1 for s in str if s == ch)


def remove_duplicates(str):
    result = sorted(set(str))
    result_str = "".join(result)
    return result_str


def add_numbers(*args):
    return sum(args)


def add_elements_to_array(array, *element):
    array += element
    return array


my_arry = [5, 6, 7, 8, 9]
array = add_elements_to_array(my_arry, 9, 10, "hello")
print(array, type(array))


print(add_numbers(7, 8, 6, 9, 5))

num = count_char("hello world", "l")
print(num)

result = remove_duplicates("abcdabcdf")
print(result)


my_list = [5, 6, 2, 8, 7]
print(sum(my_list))
