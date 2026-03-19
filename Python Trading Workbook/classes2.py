class Trade :
    def __init__(self, price : int, volume : int) : 
        # We can explicitly even mention arguments - datatype
        self.price = price
        self.volume = volume

    def __repr__(self): # Representation of the Object -> returns str
        # return "Trade("+str(self.price)+" @ " + str(self.volume)+"$)"
        return f"Trade({self.price} @ {self.volume}$)" # 'f' strings..
    
    
t1 = Trade(8,3)
# If we don't use the __repr__ function, it gives a bad representation.
print(t1)