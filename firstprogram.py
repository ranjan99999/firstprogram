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


my_dict = {"a":"ranjan","b":123,"c":"shiv","d":98990 ,"e":"God"}
for index , item in my_dict.items():
    if isinstance(item,str):
        my_dict[index] = item[::-1]
print(my_dict)