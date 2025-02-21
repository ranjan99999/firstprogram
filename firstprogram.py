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
