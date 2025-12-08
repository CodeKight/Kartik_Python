#  String alphabet, characters

text = 'Hello, \tworlds\''
print(text)

text="Hello, \"world\""  #The data is reassigned or overrided, that's why this data is overwritten by the next string.

text = ''' hello 
world'''

print(text)

#boolean

is_true = True
print(is_true)

a= None


#List: []  

my_list = ['Ram','San', '20', 'Raju']
print(my_list)

my_list[0]=66
print(my_list)

my_list.append("Sita")
print(my_list)

#Tuple: ()

my_tuple = ('Ram','San', '20', 'Raju')
print(my_tuple)
print(type(my_tuple))
#my_tuple.append("Sanu")  #cannot append, not mutable 
print(my_tuple)



#set {}
my_set = {'set', 'Ram','San', '20', 'Raju'}
print(my_set)
#print(my_set[1])  #index cannot be accesed, its unordered


#Dictionary {}
my_dict={'ram':'bca', 'age':22, 1:5}

my_dict={'ram':'bca', 
         'age':22, 
         1:5,
         2:'bca',
         'age':33,
         'hobbies':['dancing','singing','painting'],
         '1.5':'mark',
         5:'4.5',
         'e':5 }

print(my_dict)
print(my_dict['age'])
print(my_dict[2])


#create a list of your hobbies and print it out as a proper sentwence "I like hobby1. I like hobby2, hobby3"
#create a dictionary containing your infor. print it out your info







