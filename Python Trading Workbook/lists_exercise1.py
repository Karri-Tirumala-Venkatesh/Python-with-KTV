def crate_bananas(list1) :
    for i in range(len(list1)) :
        if(list1[i]>20) :
            list1[i]=20
    return list1

list1 = [18, 16, 24, 17, 22]
list1 = crate_bananas(list1)
print(list1)