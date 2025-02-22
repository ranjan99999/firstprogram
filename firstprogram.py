print("hello world")
print("this is just demo the main picture is still remain")


def decorator(func):
    sum_default = 0

    def inner(x, y):
        return func(x, y)

    return inner


@decorator
def addition(x, y):
    print(x + y)


addition(4, 7)
print("the above result is based on the decorator")
# Above program is a decorator and it is for adding two number using decorator

