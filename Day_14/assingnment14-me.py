# Accounting Program: implement file handling(2 file: userdata {"username":"password"} save in text file, userbalance)
# give user 2 choices "Login" or "Register"
# if register, get username, password from user, store the data in a file
# if login, get username, password from user and check if the userdata exist in the file

# show 2 choice, add balce, view balance, if user choice is add, get amount from user and add the value to the initial balance, if choice is view then show the initial balance to the user
# if user does not exist in the dictironay, print out a statement

import json   # dictionary format is changed in json format and viseversa

choice=int(input("1. Register 2. Login "))

if choice==1:
   f= open("userFile.txt", 'a')
   username=input("Enter your username: ")
   password=input("Enter the password: ")
   user_detail = {username:password}
   json_user = json.dumps(user_detail) # dict convert json format
   f.write(json_user+'-')
   print("Registered successfully")

elif choice == 2:
   f= open("userFile.txt", 'r')
   username=input("Enter your username: ")
   password=input("Enter the password: ")
   a = f.read().split('-')  # list_datatype {"sdf":"asdf"}
   for i in a:
      if i != '':
         json_data = json.loads(i)    # json converted into dict
         if password == json_data.get(username):
            print("Login Success")
            choice=int(input("1. View Balance  2. Add Balance"))
            if choice==1:
                  f= open("userBal.txt", 'a')
                  username=input("Enter your name: ")
                  balance=input("Enter initial bal: ")
                  user_bal = {username:balance}
                  json_user = json.dumps(user_bal) # dict convert json format
                  f.write(json_user+'-')
                  print("Balance added successfully")
               
               
            elif choice ==2:
            
                f= open("userBal.txt", 'r')
                username=input("Enter your username: ")
                addBal =int(input("Enter your balance to add: "))
                a = f.read().split('-')  # list_datatype {"sdf":"asdf"}
                for i in a:
                    if i != '':
                        json_data = json.loads(i)    # json converted into dict
                        oldBal= json_data.get(username)
                        newBal = oldBal+addBal
                        print("New Balance is: ", newBal)
             
            else:
                print("Invalid choice")
                                   
                
               
            
            # show 2 choice, add balce, view balance, if user choice is add, get amount from user and add the value to the initial balance, if choice is view then show the initial balance to the user
            # if user does not exist in the dictironay, print out a statement
            
            
            
         else:
            print("User data not found")
