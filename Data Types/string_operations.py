name = "karri tirumala venkatesh"

# Remove white spaces in the string
name1 = name.strip()
print(name1)

# Capitalize first letter
name1 = name.capitalize()
print(name1)

# Capitalize first letter of each word
name1 = name.title()
print(name1)

# Split at space
first, middle, last = name.split(" ")
print(f"{first} {middle} {last}")