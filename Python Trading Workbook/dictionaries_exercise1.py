def should_buy(product, price, valuations):
    if product in valuations :
        return (price < valuations[product])
    return False

valuations = {'banana':8, 'shell':4, 'coconut':13}

temp = should_buy('banana',7, valuations)
print(temp)
temp = should_buy('shell',6, valuations)
print(temp)
temp = should_buy('plum',3, valuations)
print(temp)