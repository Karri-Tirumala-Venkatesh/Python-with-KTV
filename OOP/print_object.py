class  Student:
    
    def __init__(self, name, rno):
        if name =="":
            raise ValueError("Missing Name")
        if rno>224:
            raise ValueError("Invalid Roll Number")
        self.name = name
        self.rno = rno

    def __str__(self):
        return f"{self.name} - {self.rno}"


def get_student():
    name = input("Name : ")
    rno = int(input("Roll Number : "))
    return Student(name, rno)

student = get_student()
# __str__ method is automaticall called when the object is to be represented as a string
# here the print function wishes the object as a string
print(student)