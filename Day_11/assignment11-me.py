# todo:
# get a user information(name, age, address)
# get hobbies of users using args
# other addition info like contact info using kwargs(phone, email, address)
# print out introduction of the user
#-------------------------------------------------------------------------------------


def info(name, age, address, *args, **kwargs):
    print(f"""Name:{name} 
Age:{age} 
Address: {address}\n""")
    
    print("Hobbies: \n")
    for i in args:
      print(f" I like {i}")
    
    
    print("\nOther info is: \n")
    for key, value in kwargs.items():
        print(f"{key}:{value}")


name, age, address =input("Enter your name, age and address: ").split()
hobbies=[]
count=int(input("Enter your count: "))
for i in range (1,count+1):
    myHobby=input("Enter your hobby ")
    hobbies.append(myHobby)
    
kwargs={}
count2=int(input("Enter how many data: "))
for i in range(count2):
    key=input("Enter key")
    value=input("Enter value")
    kwargs[key]=value
    
print(kwargs)

info(name, age, address, *hobbies , **kwargs )






# create a dict of username and password {"ram":"ram123"}
# create a dict of username and initial_balance {"ram":"100000"}
# get username and password from user. check if it exist in the dictionary, if yes print "Login Success"
# show 2 choice, add balce, view balance, if user choice is add, get amount from user and add the value to the initial balance, if choice is view then show the initial balance to the user
# if user does not exist in the dictironay, print out a statement
#-------------------------------------------------------------------------------

# userDict={
#     "ram": "123",
#     "sam": "456",
#     "hari": "789"
# }

# # print(userDict)

# userBalance={
#     "ram": 1000,
#     "sam" : 2000,
#     "hari" : 300
# }

# # print(userBalance)

# username =input("Enter your username: ")
# password = input("Enter your password: ")


# def login_system():
#     if username in userDict:
#         if password in userDict[username]:
#             print("Login Successful!")
#             askBal = input("Do you want to add balance or view balance ")
#             if askBal.lower() == "view":
#                 print("Your balance is: ", userBalance[username])
#             elif askBal.lower() == "add":
#                 balAmount=int(input("Enter balance to add"))
#                 print("You current balance is: ", userBalance[username] + balAmount, "Now" )
                
#         else:
#             print("Wrong password!")
#     else:
#         print("Wrong Username")

# login_system()