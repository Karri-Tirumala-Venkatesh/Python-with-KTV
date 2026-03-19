prices = [4, 5, 8, 9, 11, 13, 16]
for price in prices :
    print(price, end=" ")
    if price<6 :
        if price%2==0 :
            print("Really Good!")
        else :
            print("Good")
    elif price<10 :
        print("Good")
    elif price>14 :
        print("Really Bad!")
    elif price>=10 :
        if price>10 and price%2!=0 : # 'and' / 'or' keywords
            print("Really Bad!")
        else :
            print("Bad")

# We can combine multiple print statements, by merging the conditions, using 'and' / 'or' keywords
