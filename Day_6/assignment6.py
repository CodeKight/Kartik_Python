
# todo: if-else practice problems
# get a number from user and check if it is greater than 10------------------------------------

# a=input("Enter a number")
# if a>10:
#     print("A is greater than 10")
# else:
#     print("A is less than 10")


# get a number from user and check if it is even or odd----------------------------------------

# b=input("Enter a numeber")
# if b%2==0:
#     print("Even")
# else:
#     print("Odd")


# create a list of username and password.{"username1":"password1","username2":"password2"}
# get username for user. if username exist in the list print "username exist", else print "username not found"-----------------------------

# userList={'Ram':'123','Shyam':'456','Hari':'111','Mohan':'789'}
# c=input("Enter the Username")
# if c in userList:
#     print("User Exist in the List")
# else:
#     print("User doesn't exist in the list")
    
    
    
# create the list of numbers
# get the greater number from the list----------------------------------------------------


numList=[1,72,3,1]
max=numList[0]

if numList[1]>max:
        max=numList[1]
if numList[2]>max:
        max=numList[2]
if numList[3]>max:
        max=numList[3]
print(max)


# Mark Calculator
# get mark of the student
# if mark is greater than or equal to 80 and less than 100 print "A+"
# if mark is greater than or equal to 70 and less than 80 print "A"
# if mark is greater than or equal to 60 and less than 70 print "B+"
# if mark is greater than or equal to 50 and less than 60 print "B"
# if mark is greater than or equal to 40 and less than 50 print "C"
# if mark is less than 40 print "Failed"

# f=int(input("Enter your marks"))

# if f>=80 and f<100:
#     print("You got A+")
# elif f>=70 and f<80:
#     print("You got A ")
# elif f>=60 and f<70:
#     print("You got B+")
# elif f>=50 and f<B:
#     print("You got B")
# elif f>=40 and f<50:
#     print("You got C")
# else:
#     print("You failed in Exam")
    



    
# ------------------------------------------------


# todo:
# get user age
# if age is greater than or equal to 16, ask if the user has license, if yes print "You can drive", else print "You cannot drive"
# if age less than 16, print "You are not eligible to drive", do you want to get license, if yes print you can apply at the age of 18, else print Uninterested.

# age=int(input("Enter your age"))
# if age>=16:
#     liscence=input("Do you have Liscence?")
#     if liscence=="yes" or liscence=="Yes" or liscence=="YES":
#         print("You can drive.")
#     else:
#         print("You cannot drive")
# else:
#     print("You are not eligible to drive")
#     interest=input("Do you want to get liscence")
#     if interest=="yes" or interest=="Yes" or interest=="YES":
#         print("You can appply after 16")
#     else:
#         print("Not interested")
        




# Rock Paper Scissor Game:---------------------------------------------------------
# get input form 2 user (r,p,s)
# you can use nested if-else or other logic to determine the winner

# user 1 = r, user2 = p:--->user2 wine
# user 1 = r, user2 = s:--->user1 wine

# user 1 = p, user2 = r:--->user1 wine
# user 1 = p, user2 = s:--->user2 wine

# user 1 = r, user2 = p:--->user2 wine
# user 1 = r, user2 = s:--->user1 wine

# user1 and user 2 input same--> Tie

# r,p ---> p wins
# r,s ---> r wins
# p,s ---> s wins



user1=input("User1: Enter your move ")
user2=input("User2: Enter your move ")
if user1==user2:
    print("Tie! Play Again. ")
elif user1=='r' and user2=='p':
        print("Winner: user2")
elif user1=='r' and user2=='s':
        print("Winner: user1")
elif user1=='p' and user2=='r':
        print("Winner: user1")
elif user1=='p' and user2=='s':
        print("Winner: user2")
elif user1=='s' and user2=='r':
        print("Winner: user2")
elif user1=='s' and user2=='p':
        print("Winner: user1")

