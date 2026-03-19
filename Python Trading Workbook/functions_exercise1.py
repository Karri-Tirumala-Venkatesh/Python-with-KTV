def classify_price(price, threshold1=8, threshold2=12) :
    print(price, end=" ")
    if (price<threshold1) :
        return "Good!"
    if price>threshold2 :
        return "Bad!"
    return "Ok"
    
price = 18
x = classify_price(price, threshold2=20, threshold1=11)
print(x)

price = 9
x = classify_price(price, 10)
print(x)