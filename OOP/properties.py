class  Student:
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno # Calls the setter method

    def __str__(self):
        return f"{self.name} - {self.rno}"

    # Function Overloading :

    # Getter
    @property
    def rno(self): 
        return self._rno
    
    # Setter
    @rno.setter # Same name as that of the property
    def rno(self, n): 
        # If we dont want the user to do so, we can have a ValueError
        if n>224:
            raise ValueError("Invalid Roll Number")
        self._rno = n

    # Getter
    @property
    def name(self): 
        return self._name
    
    # Setter
    @name.setter
    def name(self, n): 
        if n =="":
            raise ValueError("Missing Name")
        self._name = n

def get_student():
    name = input("Name : ")
    rno = int(input("Roll Number : "))
    return Student(name, rno)

student = get_student()
student.rno = 230 # Python automatically recognizes the Setter
# student._rno = 250 -> No setter is involved
print(student)

# Anywhere, if we use underscore infront of any attribute name, we do not pass through the getter and setter