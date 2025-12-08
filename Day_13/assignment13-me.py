#to do: 
# get username form usser 
# give user two choice
# if register, username should be stored in file, 
# if login , get username and check if name exist in the file. 
#-----------------------------------------------------------------------------------------------


# username=input("Enter your username: ")
# choice=int(input("1. Register 2. Login "))

# if choice==1:
#     f= open("C:/Users/USER/OneDrive/Desktop/userFile.txt", 'a')
#     f.write(username)
#     print("Registered successfully")
# elif choice==2:
#   f= open("C:/Users/USER/OneDrive/Desktop/userFile.txt", 'r')
#   a = f.read()
#   if username in a:
#     print("Login Successfully! ")
#   else:
#     print("Couldn't find username. ")

# else: 
#   print("Invalid Choice. ")

    



# Accounting Program: implement file handling
# give user 2 choices "Login" or "Register"
# if register, get username, password from user, store the data in a file
# if login, get username, password from user and check if the userdata exist in the file
# show 2 choice, add balce, view balance, if user choice is add, get amount from usfer and add the value to the initial balance, if choice
#is view then show the initial balance to the user
# if user does not exist in the dictironay, print out a statement
#----------------------------------------------------------------------------------------------------------------------------------------

userBalance={
    "ram": 1000,
    "sam" : 2000,
    "hari" : 300
}


username=input("Enter your username: ")
password=input("Enter the password: ")
choice=int(input("1. Register 2. Login "))


def Account():
 if choice==1:
     f= open("C:/Users/USER/OneDrive/Desktop/userFile.txt", 'a')
     f.write(username)
     f.write(password)
     print("Registered successfully")
 elif choice==2:
   f= open("C:/Users/USER/OneDrive/Desktop/userFile.txt", 'r')
   a = f.read()
   if username in a and password in a:
     print("Login Successfully! ")
     askBal = input("Do you want to add balance or view balance? ")
     if askBal.lower() == "view":
        print("Your balance is: ", userBalance[username])
     elif askBal.lower() == "add":
        balAmount=int(input("Enter balance to add: "))
        print("You current balance is: ", userBalance[username] + balAmount, "Now" )
     else:
        print("Invalid choice. ")         
   else:
    print("Wrong username or password! ")

 else: 
   print("Invalid Choice. ")
   
Account()



