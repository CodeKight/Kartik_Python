# todo:
# get a user information(name, age, address)
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# address = input("Enter your address: ")
# def intro(name, age, address):
#     print(f"My name is {name}. I am {age} years old. My address is {address}")
# intro(name, age, address)


# get hobbies of users using args
# def hobbies(*args):
#     for hobby in args:
#         print(f"{hobby}")
# hobbies("cricket","basketball","running" , "football")



# other addition info like contact info using kwargs(phone, email, address)
# print out introduction of the user
# def addition_info(**kwargs):
#     for key, values in kwargs.items():
#        print(f"{key}:{values}")
# addition_info(phone = "986463733", email = "suraj@gmail.com", address = "ktm")


# print out introduction of the user
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# def intro(name, age, *args, **kwargs):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print("Hobbies")
#     print(f"{args}")
#     print("other information")
#     print(f"{kwargs}")
# intro(name, age, "cricket", "basketball",phone = "986463733", email = "suraj@gmail.com", address = "ktm" )




# create a dict of username and password {"ram":"ram123"}
# create a dict of username and initial_balance {"ram":"100000"}
# get username and password from user. check if it exist in the dictionary, if yes print "Login Success"
# show 2 choice, add balce, view balance, if user choice is add, get amount from user and add the value to the initial balance, if choice is view then show the initial balance to the user
# if user does not exist in the dictironay, print out a statement

# dict1 = {"suraj": "suraj123"}
# dict2 = {"suraj": 10000}
# username = input("Enter you name: ")
# password = input("Enter you password: ")
# for user in dict1:
#     if username == user and password == dict1[user]:
#         print("Login success")
#         choices = input("Enter your choice (add/view)balance:")
#         if choices.lower() == "add":
#             user_add = float(input("Enter the amount you want to add: "))
#             add = dict2["suraj"] + user_add
#             print("Your total balance is ", add)
#         elif choices.lower() == "view":
#             print("Your initial balancde is: ", dict2["suraj"])

#     else:
#         print("User doesnot exit")
