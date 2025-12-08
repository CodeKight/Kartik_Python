#Identical Operatior: Check if the values are equal and also allocated location
#is: if the values are identical, output: True, False otherwiese
a = 10
b=10

c='Ram'
d='Rams'

print(a is b)
print(id(a))
print(id(b))

print(c is d )
print(id(c))
print(id(d))

#not is: if values are identical, output : False , True otherwise

print(a is not b)
print(id(a))
print(id(b))

