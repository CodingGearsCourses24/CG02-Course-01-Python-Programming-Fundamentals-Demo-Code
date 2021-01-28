# Binary Files

import pickle

phone_number_list = [["John", "111-111-1111"], ["Peter", "222-222-222"], ["Mouse", "333-333-3333"]]

# Write to binary file
with open("phone.bin", "wb") as bfile_handler:
    pickle.dump(phone_number_list, bfile_handler)

# Read from binary file
with open("phone.bin", "rb") as bfile_handler2:
    plist = pickle.load(bfile_handler2)
    print(type(plist))
    print(plist)