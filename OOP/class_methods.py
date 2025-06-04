import random

class Lottery:

    codes=["abc","def", "ghi"]
    # Now this becomes a class variable shared by all the objects in common

    # cls - reference to the class
    @classmethod
    def code(cls, name):
        c = random.choice(cls.codes)
        print(f"{name} - {c}")

# Just we are creating containers with attributes and Methods
# Class Name . Class Method
Lottery.code("KTV")