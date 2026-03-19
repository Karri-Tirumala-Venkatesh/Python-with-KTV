def count_bananas(list1):
    sum =0
    for list2 in list1 :
        for i in list2 :
            sum+= i
    return sum

list1 = [[25,25,25,25], [40,45,10], [90]]
x = count_bananas(list1)
print(x)