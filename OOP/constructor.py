class  Student:
    # initialization method : Constructor
    # self -> gives reference to current object which is just created
    def __init__(self, name, rno):
        if name =="":
            raise ValueError("Missing Name")
        if rno>224:
            raise ValueError("Invalid Roll Number")
        self.name = name
        self.rno = rno

# Attributes are accessed through '.'

def get_student():
    name = input("Name : ")
    rno = int(input("Roll Number : "))
    student = Student(name, rno) # Initializing attributes through constructor
    return student
        
# OR return Student(name, rno)

student = get_student()
print(f"{student.name} - {student.rno}")