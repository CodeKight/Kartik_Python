# Identical Operator: check of the values are equal, and also allocated location

a = 10
b = 15
# is: if the values are identical, output : True, false otherwise
print(a is b)
print(id(a))
print(id(b))

# is not: if values are identical , output: False, True otherwise
print(a is not b)
print(id(a))
print(id(b))