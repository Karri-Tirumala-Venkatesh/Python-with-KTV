def mystery_box_value(products, valuations) :
    dict1 = {}
    for product in products :
        dict1[product] = products[product]*valuations[product]
    return dict1

products = {'banana' : 200, 'shell':300, 'coconut':100}
valuations = {'banana' : 8, 'shell':4, 'coconut':13}

dict1 = mystery_box_value(products, valuations)
print(dict1)