def stack_total(num) :
    answer=0
    while num>0:
        answer = answer+num
        num = num-1 # num-=1
    return answer

print(stack_total(4))
print(stack_total(6))