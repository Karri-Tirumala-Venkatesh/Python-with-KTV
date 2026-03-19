def add(x=1, y=2) :
    # x, y only exist in this function
    return x+y

z= add(5,3)
print(z)

z= add(5)
print(z)

z= add()
print(z)