# Class -> a custom type
# Functions in a Class -> Methods
# Methods -> need to be given an extra argument -> 'self'
# self -> is the actual instance

class Person :
    def __init__(self, name): # Constructor
        self.name = name
        self.rno = 214

    def talk(self): # 'self' -> is used to identify -> Which particular person ?
        print(f"Hello {self.name} {self.rno}!")

karri = Person("Karri") # Constructor
print(type(karri))
karri.talk() # No argument here
print(karri.name)

'''
tirumala = Person()
tirumala.talk()
'''