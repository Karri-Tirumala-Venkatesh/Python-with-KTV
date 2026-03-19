class Trade :
    def __init__(self, price : int, volume : int) :
        self.price = price
        self.volume = volume

    def __repr__(self):
        return f"Trade({self.price} @ {self.volume}$)"


class TradeTracker :
    def __init__(self) :
        self.list1 =[]
    
    def add_trade(self, trade : Trade) : # Class - type Argument
        self.list1.append(trade)
    
    def get_buy_trades(self) :
        list2 = []
        for trade in self.list1 :
            if(trade.volume > 0) :
                list2.append(trade)
        print(list2)
    
    def get_average_traded_price(self) :
        average = 0
        for trade in self.list1 :
            average += trade.price
        average = average / len(self.list1)
        print(average)
    
tracker = TradeTracker()
tracker.add_trade(Trade(7,4))
tracker.add_trade(Trade(10,-3))
tracker.get_buy_trades()
tracker.get_average_traded_price()