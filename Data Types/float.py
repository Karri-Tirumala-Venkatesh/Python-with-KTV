x = 22.1
y = 7.5

# 29.6 is rounded to 30
z = round(x+y)
print(z)

# Roundoff to 2 decimals
z = round(x/y, 2)
print(z)

# Roundoff to 3 decimals
z = x/y
print(f"{z:.3f}")
