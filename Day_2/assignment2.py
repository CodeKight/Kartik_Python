#'List' of Hobbies and Display them in a sentence.

print('\nLIST:\n')
myList=['Singing','Dancing','Painting','Hiking']
print(myList)

print(f'I like {myList[0]}.')
print(f'I like {myList[1]}.')
print(f'I like {myList[2]}.')
print(f'I like {myList[3]}.\n')


#'Dictionary' of your info and Display it

print('DICTIONARY:\n')
myDictionary={
    'Name':'Jilani',
    'Age':22,
    'Address':'Sanepa',
    'Hobby':'Exploring'
}
print(myDictionary,'\n')
print(f'My Info:\n Name: {myDictionary['Name']}\n Age: {myDictionary['Age']}  \n Address:{myDictionary['Address']} \n Hobby:{myDictionary['Hobby']}\n')


#Swaping two numbers.

  #Using Third Variable:
  
print('SWAP:')
print('Swap using third variable:\n')
a=10
b=20
print(f"Before swap a: {a} and b: {b}")


c=a
a=b
b=c
print(f"After swap a: {a} and b: {b}\n")

  #Without using third variable
  
print('Swap without using third variable:\n')
a=40
b=50
print(f"Before swap a: {a} and b: {b}")
a=a+b
b=a-b
a=a-b
print(f"After swap a: {a} and b: {b}\n")

  
# MORE:
    
# 1- print(myList+'\n')  #Gives Error. '\n' can only be concatinated with Strings, not Lists
#   Correct way to do it is:


# print('MORE:')

# print(myList, '\n')        #By using Comma
# print(str(myList) +'\n' )  #By Typecasting
# for items in myList:       #By using 'for-in' loop
#   print(items)
  
  
# 2- print('\n'LIST)  is not going to next line in



#by MAM:




#By Mam:

a = 50
b=60
print('BEfore',a,b)

a,b=b,a

print('BEfore',a,b)



my_dict = {
   2:"dia",
   1:"ram", 
   3:"ram",
   "age":50,
   2 : "shyam",
   "hobbies":["reading","coding","gaming"]
   }

print(my_dict['hobbies'][0])