
# if-else statement: conditional statement, it uses operators that returns boolean values, if condition is true, the block of code inside is executed
# else: if the condition are all false then this block is automatically executed
# elif: it takes conditions just like if, a if statement can have multiple elif statements
# if contional_statement:
#    print("Statuement")
#    print("Statuement")
#    print("Statuement")
#    print("Statuement")

a = 10
b = 10
if a > b:         # in case a is greater than b the block of code inside if will be executed
   print("A is greater than B")
elif a == b:
   print("A is equal to B")
elif a < b:
   print("A is less than B")
elif a >= b:
   print("A is greater than or equal to B")
else:
   print("B is greater than A")

print("This is outside of if block")

# todo: if-else practice problems
# get a number from user and check if it is greater than 10

# get a number from user and check if it is even or odd

# create a list of username and password.{"username1":"password1","username2":"password2"}
# get username for user. if username exist in the list print "username exist", else print "username not found"

# create the list of numbers 
# get the greater number from the list

# Mark Calculator
# get mark of the student
# if mark is greater than or equal to 80 and less than 100 print "A+"
# if mark is greater than or equal to 70 and less than 80 print "A"
# if mark is greater than or equal to 60 and less than 70 print "B+"
# if mark is greater than or equal to 50 and less than 60 print "B"
# if mark is greater than or equal to 40 and less than 50 print "C"
# if mark is less than 40 print "Failed"


# nested if-else:
a = 10
b = 10
c = 50
if a > b:         # in case a is greater than b the block of code inside if will be executed
   if a > c:
      print("A is greater.")

elif a == b:
   if a == c:
      print("A, B, C are equal")
   
   elif a >= c:
         print("A and C are equal")

   else:
      print("A and B are equal")

else:
   print("B is greater than A")
   if b > c:
      print("B is also greater than C")
   elif b < c:
      print("C is greater than B")

# todo:
# get user age
# if age is greater than or equal to 16, ask if the user has license, if yes print "You can drive", else print "You cannot drive"
# if age less than 16, print "You are not eligible to drive", do you want to get license, if yes print you can apply at the age of 18, else print Uninterested.


# Rock Paper Scissor Game:
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