

#2. ANIMAL TUPLE:
print("\nANIMALS TUPLE:\n")

myAnimals=('Cow', 'Dog','Apple', 'Horse','Bufallo','Tiger')
#myAnimals[2]='Tiger'   #Tuple is immutable
print(myAnimals)

myList=list(myAnimals)
print(myList)

myList[2]='Tiger'
print(myList)


# mySet=set(myAnimals)    #⚠️The Set doesn't support Indexing and Assignment
# print(mySet)
# mySet[5]='Tiger'
# print(mySet)


#3. CHECK RABIT IN ANIMALS
print("\nCHECK RABIT IN ANIMALS:\n")

print('Cow' in myAnimals)
print('Rabbit' in myAnimals)


#4. CHECH X IN Y:
print("\nCHECH X IN Y:\n")
x = [1,2,3,4]
y = [1,2,3,4,5,[1,2,3,4]]

print(x in y)
print( x[0] in y)
print( x[1] in y)
print( x[2] in y)
print( x[3] in y)




#1. TAKE A USER AS INPUT AND CHECK IF IT IS PRESENT IN THE LIST
print("\nCHEK USER IN THE LIST:\n")
myUsers=['Ram','Sam','Hari','Mohan']
enterUser=input('Enter a Username\n')
print(enterUser in myUsers)
