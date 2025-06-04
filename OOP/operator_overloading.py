class Wallet:
    def __init__(self, cash=0):
        self.cash = cash
    def __str__(self):
        return f"Cash : {self.cash}"
    def __add__(self, other):
        # other - can be of any datatype
        # self - object (operand) on the left side of the operator
        # other - object (operand) on the right side of the operator
        return Wallet(self.cash + other.cash)


KTV = Wallet(500)
print(KTV)

KSN = Wallet(300)
print(KSN)


# for + operator we have __add__ function
KVR = KTV + KSN
print(KVR)