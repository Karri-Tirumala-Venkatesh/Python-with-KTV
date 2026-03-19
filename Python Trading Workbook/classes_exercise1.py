class Trade :
    def __init__(self, price, volume):
        self.price = price
        self.volume = volume
        
    def is_buy(self) :
        return self.volume>0

t1 = Trade(4,2)
print(t1.is_buy())