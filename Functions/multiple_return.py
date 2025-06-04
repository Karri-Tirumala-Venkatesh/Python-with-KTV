# functions returning multiple values

def get_student():
    name = input("Name : ")
    roll_no = int(input("Roll Number : "))
    return name, roll_no
# return (name, roll_no) - this is returning a tuple
# return [name, roll_no] - this is returning a list

# here we are returning a tuple - collection of values
# List is mutable, values of individual element of the List can be changes
# Tuple is immutable, we cannot change individual values

name, rno = get_student()
print(f"{name} - {rno}")

# A visible tuple
student = get_student()
print(f"{student[0]} - {student[1]}")