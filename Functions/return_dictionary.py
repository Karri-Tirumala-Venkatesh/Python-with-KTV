# functions returning multiple values

def get_student():
    temp = {}
    temp["name"] = input("Name : ")
    temp["roll_no"] = int(input("Roll Number : "))
    return temp

# Dictionaries - Mutable, similar to lists

student = get_student()
print(f"{student['name']} - {student['roll_no']}")
# As we are using a dictionary, we need not remember, the ordering of return values
# inside of double quotes, make use of single quotes for clarity