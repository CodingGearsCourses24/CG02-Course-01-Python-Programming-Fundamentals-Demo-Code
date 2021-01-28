# Functions - Parameters - Adv


def print_message_format2(message="No Message", number=999, level="ERROR", *others):
    print(level + ":" + str(number) + ":" + str(message))
    print(others)
    print(type(others))


message1 = "This is great!"
print_message_format2(message1, 100, "High", 1, 2, 3, 4, 5, "etc")
print_message_format2(message1, 100, "High", 1, 2, "etc")


