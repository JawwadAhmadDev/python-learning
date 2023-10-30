# methods = [i for i in dir(str) if "__" not in i]
# print(methods)


# name : str = "jawwad ahmad"
# print(f"Capitalize: {name.capitalize()}")
# print(f"Casefold: {name.casefold()}")
# print(f"Lower: {name.lower()}")
# print(f"Upper: {name.upper()}")
# print(f"Title: {name.title()}")


import re
# Whitespaces
name: str = "   Jawwad   Ahmad    "

# Removed from left side
# lstrip() method of string is used
print(f"Removed from left: '{name.lstrip()}'")

# Removed from right side
# rstrip() method of string is used
print(f"Removed from right: '{name.rstrip()}'")

# Removed from both sides
# strip() method of string is used
print(f"Removed from both sides: '{name.strip()}'")

# Removed from any place
# sub() method of re library is used to remove whitespaces
name1: str = re.sub(' {2,100}', ' ', name)
print(f"Removed from any place: {name1}")