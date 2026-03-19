def biggest_bunch(list1):
    answer = -1
    for list2 in list1 :
        for i in list2 :
            if i>answer :
                answer = i
    return answer

list1 = [[25,25,25,25], [40,45,10], [90]]
x = biggest_bunch(list1)
print(x)