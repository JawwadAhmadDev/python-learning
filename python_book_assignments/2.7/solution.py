# 2-7. Stripping Names: Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

name : str = """\tJawwad\n\t\tAhmad"""

# using lstrip() method
name1 : str = name.lstrip()
print(f"Using lstrip method: {name1}")

#  using rstrip() method
name2 : str = name.rstrip()
print(f"Using rstrip method: {name2}")

# using strip() method
name3 : str = name.strip()
print(f"Using strip method: {name3}")
