# Lists -> Container
numbers = []
print(numbers) # []
print(type(numbers)) # List

list1 = [10, 20, 30]
print(list1)

print(list1[0]) # Lists are 0 indexed ( Left to Right )
print(list1[-1]) # Lists are 0 indexed ( Right to Left )

list1.append(40)
print(list1)

n = len(list1) # Length of the List
print(n)