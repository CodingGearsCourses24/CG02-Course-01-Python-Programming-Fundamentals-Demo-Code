# Strings - find & replace
# find - returns the index of the first occurrence of the substring

message1 = "GlobalETraining .com is our registered domain. " \
         "We offer subscription based access to our online courses at a low price!"


search_domain_name = message1.find("GlobalETraining.com")
search_low_price = message1.find("low price")

print(search_domain_name)
print(search_low_price)

if search_domain_name == -1 or search_low_price == -1:
    print("The message is not approved! Please check the domain name and the string \"low price\"")

ip_address_from_meta_string1 = "10-10-21-23"
ip_address_from_meta_string2 = "    10-10-21-23"
ip_address_from_meta_string3 = "10-10-21-23    "
ip_address_from_meta_string4 = "   10-10-21-23   "
ip_address_reformatted1 = ip_address_from_meta_string2.replace("-", ".")
ip_address_reformatted2 = (ip_address_from_meta_string2.replace("-", ".")).strip()

print(ip_address_reformatted1)
print(ip_address_reformatted2)
