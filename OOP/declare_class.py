class  Student:
    ...

# Attributes are accessed through '.'

def get_student():
    student = Student() # Creating an object of the class
    student.name = input("Name : ")
    student.rno = int(input("Roll Number : "))
    return student

student = get_student()
print(f"{student.name} - {student.rno}")