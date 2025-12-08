# for loop

# iterable: sequential data type list, tuple, string, dictionary, set
# my_list = [1, 2, 3, 4, 5,8,4,"aisdjf"]
# iteration: repeating a block of code for multiple times, proceess of iteration over a sequence
# iterator: a variable used to iterate over a sequence


# for iterator in iterable:
   #  print(statements)
   
# for i in range(5,50):
#    print("Hello",i)

# list of hobbies
# hobbies = ["reading", "coding", "gaming", "sleeping"]
# implement for loop to print each hobbies

# todo:
# create a dictionary with names and age 
# user = {"ram":25,"shyam":30,"hari":22}
# get names from user
# check if name exist in the dictionary, if exist print the age of the person, else print user not found
# print the oldest person from dictionary(optional)
# dict = {
#     "ram":23,
#     "hari":12,
#     "ashish":27,
# }
# names = input("Enter your name: ")
# for dictonary in dict:
#     if names == dictonary:
#         print(f"The age of {names} is ", dict[names])

# using chatgpt
# oldest = max(dict, key=dict.get)
# print(f"The oldest person is {oldest} with age {dict[oldest]}")       


# create a dictioanry with username and password
# get username and password from user
# check if username exist in the dictionary and check if the password match, if match print "login successful", else print "invalid password"

# dict = {
#     "suraj" : "suraj123", 
#     "hari" : "hari123", 
#     "ashsih" : "ashsih123", 
# }
# username = input("Enter the name: ")
# password = input("Enter the password: ")
# for name in dict:
#     if username == name:
#         if password == dict[name]:
#             print("login successful")
            
#         else:
#             print("invalid password")

# assignment using for loop
# get a number from user and print the multiplication table of the number using for loop
user = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{user} * {i} = { i*user} ")

