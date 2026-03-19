def classify_price(price) :
    if (price<8) :
        return "Good!"
    if price>12 :
        return "Bad!"
    return "Ok"

def check_and_classify_price(price) :
    print(price, end=" ")
    if price==4 :
        return "Really Bad!"
    return classify_price(price)

price = 9
x = check_and_classify_price(price)
print(x)