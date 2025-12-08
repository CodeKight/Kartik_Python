#calulator using if-else


# implement while loop
# get two numbers from user
# get the operator from user(+,-,*,/)
# perform the operation based on the operator
# ask if the user want to continue the calculation, if yes repeat the process, else exit

# day 6 assignment modification 
# implement while loop in rock paper scissor game

# implement while loop in
# get two numbers form user
# get the greater number from the list


# #Calculator: 
# while True:
#     n1 = float(input("Enter first number: "))
#     n2 = float(input("Enter second number: "))
#     op = input("Enter operator (+ - * /): ")

#     if op == "+":
#         print("Result =", n1 + n2)
#     elif op == "-":
#         print("Result =", n1 - n2)
#     elif op == "*":
#         print("Result =", n1 * n2)
#     elif op == "/":
#         if n2 != 0:
#             print("Result =", n1 / n2)
#         else:
#             print("Error: Division by zero not allowed")
#     else:
#         print("Invalid operator!")

#     choice = input("Do you want to continue? (yes/no): ").lower()
#     if choice != "yes":
#         print("Exiting calculator...")
#         break






# #greater num1

# while True:
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))

#     if n1 > n2:
#         print("Greater number is:", n1)
#     elif n2 > n1:
#         print("Greater number is:", n2)
#     else:
#         print("Both numbers are equal")

#     choice = input("Check again? (yes/no): ").lower()
#     if choice != "yes":
#         print("Program ended!")
#         break

# while True:
#     user1=input("User1: Enter your move ")
#     user2=input("User2: Enter your move ")
#     if user1==user2:
#         print("Tie! Play Again. ")
#     elif user1=='r' and user2=='p':
#         print("Winner: user2")
#     elif user1=='r' and user2=='s':
#         print("Winner: user1")
#     elif user1=='p' and user2=='r':
#         print("Winner: user1")
#     elif user1=='p' and user2=='s':
#         print("Winner: user2")
#     elif user1=='s' and user2=='r':
#         print("Winner: user2")
#     elif user1=='s' and user2=='p':
#         print("Winner: user1")
#     choice=input("Do you want ot contiune?")
#     if choice!="yes":
#         break




while True:
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
 choice=input("Do you want ot contiune?")
 if choice!="yes":
  break