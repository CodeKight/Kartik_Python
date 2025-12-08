# Question:1
# get user age
# if age is greater than or equal to 16, ask if the user has license, 
# if yes print "You can drive", else print "You cannot drive"
# if age less than 16, print "You are not eligible to drive",
# do you want to get license, if yes print you can apply at the age of 18, 
# else print Uninterested.

# age = int(input("Enter Your Age:"))

# if age >= 16:
#     user_input = input("Do you have license ('yes'/'no'):").lower()
#     if user_input == 'yes':
#         print("You can drive!")
#     else:
#         print("You cannot drive!")

# if age < 16:
#     print("You are not eligible to drive!")
    
#     user_input = input("Do you want to get license ('yes'/'no'):").lower()
#     if user_input == 'yes':
#         print("You can apply at the age of 18")
#     else:
#         print("Unintrested")
        
#get a number from user and check if it is greater than 10

# num = int(input("Enter any Number:"))

# if num > 10:
#     print(f"{num} is greater than 10")
# else:
#     print(f"{num} is not greater than 10")

# # # get a number from user and check if it is even or odd
# if num % 2 == 0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is odd")
    
    
# # create a list of numbers
# # get the greater number from the list

# list_num =[1,2,33,44,55,44,33]
# max_num = list_num[0]  #assuming that the maxium value is at index 1

# if list_num[1] > max_num:
#     max_num = list_num[1]
# if list_num[2] > max_num:
#     max_num = list_num[2]
# if list_num[3] > max_num:
#     max_num = list_num[3]
# if list_num[4] > max_num:
#     max_num = list_num[4]
# if list_num[5] > max_num:
#     max_num = list_num[5]
# if list_num[6] > max_num:
#     max_num = list_num[6]

# print("The maxium number in List is:",max_num)

# print(max(list_num))
    



#create a list of username and password.
#get username for user. if username exist in the list print "username exist", else print "username not found"

# user_name = ["officialanilnepali@gmail.com","brocode@gmail.com"]
# password = ["firstgeneration","secondgeneration"]

# user_input = input(f"Enter the user name:")
# if user_input in user_name:
#     print("username exist")
# else:
#     print("user nae not found")

# my_list =[]
# print("Enter the list of items (sperated by commas)")
# while True:
#     item = input()
    
#     if item.lower()=="stop":
#         break
#     my_list.append(item)
# print(my_list)


# # Rock Paper Scissor Game:
# # get input form 2 user (r,p,s)
# # you can use nested if-else or other logic to determine the winner

# # user1 and user 2 input same--> Tie

# # r,p ---> p wins
# # r,s ---> r wins
# # p,s ---> s wins

user_1 = input("User 1 input--> Enter any one from options ('r','p','s')?:").strip().lower()
user_2 = input("User 2 input -->Enter any one from options ('r','p','s')?:").strip().lower()

if user_1 == user_2:
    print("Game Tie !")
else:
    if user_1 == 'r':
        if user_2 == 'p':
            print(f"User 2  wins in r,p ---> p wins")
        else:                                          #user 2 becomes s 
            print(f"User 1  wins in r,s ---> r wins")
            
    elif user_1 == 'p':
        if user_2 == 's':
            print(f"User 2  wins in p,s ---> s wins")
        else:                                          #user 2 becomes r
            print(f"User 1  wins in p,r ---> p wins") 
    
    elif user_1 == 's':
        if user_2 == 'r':
            print(f"User 2  wins in s,r ---> r wins")
        else:                                          #user 2 becomes p
            print(f"User 1  wins in s,p ---> s wins") 
    else:
        print("invalid input from user ")
    
    