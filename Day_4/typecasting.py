#typecasting: process of changing the datatype from string to int, int to string(type conversion)

a = "15"
b="20"

print(a +b)
print(type(a))
print(type(b))

#to integer- int()

c = int(a)
d = int(b)
print(c+d)

#to float- float()

e=float(c)
print(e)

#to string- str()
f=str(e)
print(f)
print(type(f))


#to list- list()
data = "mindriser345" #only string can be converted into list, not int or float
my_list=list(data)
print(my_list)


data=('123','apple','ball')
my_list=list(data)
print(my_list)

#to tuple- tuple()
my_tuple=tuple(my_list)
print(my_tuple)

#to set- set()

data=('123','apple','ball','apple')
my_set=set(data)
print(my_set)

#to dictionary- dict()
intro=(('name','ram'),('address','sanepa'),('age',23))
my_dicts=dict(intro)
print(my_dicts,'\n')


#input:


name=input("What is your name")

print(f"Your name is {name}")
print(type(name))



name=int(input("What a number"))

print(f"Your name is {name}")
print(type(name))


#assignment:







