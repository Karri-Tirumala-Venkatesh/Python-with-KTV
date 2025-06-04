class Person:
    def __init__(self, name) :
        self.name = name

class Student(Person): # Student is a child class and it inherits from the Person Super Class
    def __init__(self, name, rno) :
        super().__init__(name) # Making usage of Parent class functionality
        self.rno = rno

student = Student("KTV", 214)
print(student.name)
