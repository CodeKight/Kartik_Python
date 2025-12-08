# todo: if-else practice problems
# get a number from user and check if it is greater than 10
number = int(input("Enter the number: "))
if number >= 10:
    print("It is greater than 10")
else:
    print("It is smaller than 10")

# get a number from user and check if it is even or odd
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("It is even")
else:
    print("It is odd")

# create a list of username and password.{"username1":"password1","username2":"password2"}
# get username for user. if username exist in the list print "username exist", else print "username not found"
users = [
    {"username1": "password1"},
    {"username2": "password2"},
    {"username3": "password3"},
    {"username4": "password4"},
]

username = input("Enter the username: ")

found = False

for user in users:
    if username in user:   # ✔ checks keys inside dictionaries
        found = True
        break

if found:
    print("username exist")
else:
    print("username not found")


# get two numbers form user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# get the greater number from the list
if num1>num2:
    print("The greater number is :" ,num1)
else:
    print("The greater number is :" ,num2)

# Mark Calculator
# get mark of the student
marks = int(input("Enter the marks: "))
# if mark is greater than or equal to 80 and less than 100 print "A+"
if marks >= 80 and marks<100:
    print("A+")
# if mark is greater than or equal to 70 and less than 80 print "A"
if marks >= 70 and marks<80:
    print("A")
# if mark is greater than or equal to 60 and less than 70 print "B+"
if marks >= 60 and marks<70:
    print("B+")
# if mark is greater than or equal to 50 and less than 60 print "B"
elif marks >= 50 and marks<60:
    print("B")
# if mark is greater than or equal to 40 and less than 50 print "C"
elif marks >= 40 and marks<50:
    print("C")
# if mark is less than 40 print "Failed"
else:
    print("Failed")
# get user age
age = int(input("Enter your age: "))
# if age is greater than or equal to 16, ask if the user has license, if yes print "You can drive", else print "You cannot drive"
if age>=16:
    license = input("Do you have license(yes/no): ")
    if license == "yes":
        print("You can drive")
    else:
        print("you can't drive")

else:
    print("you cannot drive")
# if age less than 16, print "You are not eligible to drive", do you want to get license, if yes print you can apply at the age of 18, else print Uninterested.
age = int(input("Enter your age: "))
if age<16:
    print("You are not eligible to drive")
    license = input("Do you want to get license?: ")
    if license == "yes":
        print("You can apply at the age of 18")
    else:
        print("Not interested")
else:
    print("You are eligible")


# Rock Paper Scissor Game:
# get input form 2 user (r,p,s)
player1 = input("Enter your choise: ")
player2 = input("Enter your choise: ")
# you can use nested if-else or other logic to determine the winner
if player1 == player2:
    print("It's a tie! 🤝")

elif player1 == "rock":
    if player2 == "scissor":
        print("Player 1 Wins! Rock beats Scissor")
    else:
        print("Player 2 Wins! Paper beats Rock")

elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 Wins!  paper beats rock")
    else:
        print("Player 2 Wins! Scissor cuts Paper")

elif player1 == "scissor":
    if player2 == "paper":
        print("Player 1 Wins! scissor beats paper")
    else:
        print("Player 2 Wins! Rock beats Scissor")

else:
    print("Invalid input")
