#ARGS_KWARGS:

#Args: Accepts multiple arguments, is used to define args 



# def addition(*args):
#     print(args[1])
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
      
# addition(10,20,30,10)


#kwargs: multiple keyworkd 

# def intro(**kwargs):
#     for key,value in kwargs.items():
#      print(key,":",value)
     
# intro(name="ram", age="40", address="ktm", phone=797997, gender="male", )




# def intro(name, age, *args, **kwargs):
    # for key,value in kwargs.items():
    #  print(key,":",value)
    
#     print(name)
#     print(args)
#     print(kwargs)
     
# intro("ram", "40", "ktm", "apple", phone=797997, gender="male", course="python" )


#get a user information (name, age)
# get hobbies of users using argrs
# other addition info like contact info using kwargs(phone, email, address)
# print out introduction of the user 


#Return:

# def addition(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
#     print("abc") #won't excute, statement after return is not executed, the flow goes to the place of call when return is encountered 
       
# a= addition(10,20,30,10)
# print(a*2)



#Global variable: 

a=10 #global variable 
b=20 
def addition(*args):
    global b  #use global keyword to change the global varible locally, bec, global var can only be acced locally not change without the use of global keyword . 
    print(a) #can be accessed inside the function
    z=0 #local variable 
    global y
    sum=0
    for i in args:
        sum+=i
    # return sum
    print("abc") #won't excute, statement after return is not executed, the flow goes to the place of call when return is encountered 
    b+=1
print(b)  #Global variable changed locally and printed outside 
# print(z)  Cannot acces the local outside the block 
# a= addition(10,20,30,10)
# print(a*2)