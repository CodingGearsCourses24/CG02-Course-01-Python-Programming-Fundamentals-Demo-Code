# Functions - Parameters - Adv
# *args & **kwargs (keyword arguments)


def print_args(*args):
    print(args)


def print_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
    if len(kwargs):
        for item in kwargs:
            print("{} is the capital of {}".format(kwargs[item], item))


print_args(1, 2, 3, 4, 5)

print_kwargs(USA="Washington DC", Japan="Tokyo")
