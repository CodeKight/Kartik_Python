#Indexing: index or position starts form 0, can be used in String, List, Tuple. Used to Access or Get a single data in the given Index or position

a='mindrisers'
#m:0
# i=1
# n=2
# d=3

print(a[3])

b =  "I am a ( Programmer )"
#print out ( and )

print(b[7])  #⚠️Space is also couted
print(b[20])


myList=['a',  'b',  'c  ',5,'e','f']  #Space doesn't cout in list, only the no. of element is counted
print(myList[1])

#Access 5 from the list
print(myList[3])

#Upadate data by Indexing

myList[3]='d'
print(myList)

#Indexing in Tuple: Data can be acced but not changed

myTuple=('a',  'b',  'c  ',5,'e','f')
print(myTuple[2])
#myTuple[2]=5  Tuple doesn't suppor indexing assignment 






#Slicing: Used to get a subset fromt he given sequence, Include the starting index and exclude the end indes, form start to n-1 data is included 

myList=['a',  'b',  'c  ',5,'e','f']
#print form b to 5
print(myList[1:4])
myList[1:4]="abc"
print(myList)
myList[1:4]="abc","efg"
print(myList)

#Three Index:
myList=['a',  'b',  'c  ',5,'e','f']
print(myList[1:5:1])  #Third index is used to skip the index, 1 skip none, 2 skip 1, 3 skip 2 etc.
print(myList[1:5:2])
print(myList[1:5:3])
print(myList[1:])  #space reperesent start and right space repsent end
print(myList[:4])
print(myList[-1]) #neg index start form end, not zero



#todo
# colors=['red','blue','green','purple', 'yellow','orange']
# print out green using positive index
# print out yellow using neg index
# extract red,blue,green from the above sequence and assign to a  variable rgb


#numbers = [0, 10, 20, 30, 40, 50, 60 70, 80, 90]
# print out the sequenc3 with 3 interval 
# print out the reverse of the sequence number
# extract the data from even index and assign it to even variable 
# extract the data from odd index and assign it to odd variable 


#multiple  = [
#     [1,3,4],
#     [4,5,6],
#     [7,8,9]
# ]

#print out 5 fromm the above list 
#print out 9 fromm the above list 
#print out 4,5,6 fromm the above list 

#string = "PYTHON COURSE"
# chara = ['A', 'J','P','R','V' ]
# print out 'PYTHON' form the string variable 
# print out 'PY' form the above dtirng and assing it to a variable 
# replace the character "j" in chara with "PY"



#dict 
my_dict = {
    "name":"ram",
    "age":"500",
    "address":"kathmandu",
    "hobbies":["reading","watching movies", "go hiking", "playing_game"]
    
}

print(my_dict['name'])

#print age, address, hobbies
#'My hobby is____"
# print out read
# print out movies
# print out hiking
# print out playing game

