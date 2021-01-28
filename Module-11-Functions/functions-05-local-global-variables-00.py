# Variables - local & global

message = "1: Hello Python!!"


def print_message1():
    print(message)


def print_message2():
    message = "2: Hello Python!!"
    print(message)


def print_message3():
    global message
    message = "3: Hello Python!!"
    print(message)


print_message1()
print_message2()
print_message3()
print_message1()