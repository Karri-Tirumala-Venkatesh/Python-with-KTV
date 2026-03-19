# Dictionary : Container
# Key - Value Pairs

dictionary1 = {}
print(dictionary1) # {}
print(type(dictionary1)) # Dict

d = {'a':1, 'b':2, 'c':3} # Key shall be unique
print(d['a'])

d['z']=-1
d['a']=0
for i in d :
    print(d[i])

# Checking if a Key is in a Dictionary :
print('a' in d) # True
print('a' not in d) # False

# Iterating over the Key - Value Pairs :
for i in d.items():
    print(i) # Prints the tuples

for key, value in d.items():
    print(key, value)