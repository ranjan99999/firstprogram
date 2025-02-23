print("hello world")
print("this is just demo the main picture is still remain")


def decorator(func):
    sum = 0

    def inner(x, y):
        return func(x, y)

    return inner


@decorator
def addition(x, y):
    print(x + y)


addition(4, 7)

my_string = "Exim is a profitable and stable  business "
repeating_char = ""
empty_list = {}
for item in my_string:
    if item in empty_list:
        empty_list[item] += 1
    else:
        empty_list[item] = 1

    if item not in repeating_char and empty_list[item] > 1:
        repeating_char += item
print(repeating_char)