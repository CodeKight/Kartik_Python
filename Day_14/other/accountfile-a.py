# # # Accounting Program: 
# # # implement file handling(2 file: userdata {"username":"password"} save in text file, userbalance)
# # # give user 2 choices "Login" or "Register"
# # # if register, get username, password from user, store the data in a file
# # # if login, get username, password from user and check if the userdata exist in the file

# # # show 2 choice, add balce, view balance,
# # if user choice is add,
# # get amount from user and add the value to the initial balance,
# # if choice is view then show the initial balance to the user
# # # if user does not exist in the dictironay, print out a statement

import json   # dictionary format is changed in json format and viseversa

choice1 = int(input("1. Register 2. Login: "))


if choice1 == 1:
   f = open("accountfile.txt", 'a')
   username = input("Enter your username: ")
   password = input("Enter the password: ")

   # Creates a dictionary
   user_detail = {username: password}

   # python dict to → json string
   json_user = json.dumps(user_detail)

   # Writing JSON into file with a separator "-"
   f.write(json_user + "-")
   f.close()

   # create balance file entry (initial balance = 0)
   fb = open("balancefile.txt", "a")
   
   user_balance = json.dumps({username:0})
   fb.write(user_balance+ "-")
   fb.close()

   print("Registered successfully")


elif choice1 == 2:
   f = open("accountfile.txt", 'r')
   username = input("Enter your username: ")
   password = input("Enter the password: ")

   # read all user entries
   a = f.read().split('-')
   f.close()

   login_success = False

   for i in a:
       if i != "":    # avoid empty strings
           json_data = json.loads(i)

           # check username + password
           if password == json_data.get(username):
               print("Login Success")
               login_success = True
               break

   if login_success == False:
       print("User does not exist or wrong password!")
   else:

       while True:
           print("\n1. Add Balance")
           print("2. View Balance")
           print("3. Exit")

           ch = int(input("Enter your choice: "))

           if ch == 1:
               amt = float(input("Enter amount to add: "))

               fb = open("balancefile.txt", "r")
               balance_list = fb.read().split("-")
               fb.close()

               new_data = ""
               for b in balance_list:
                   if b != "":
                       dic = json.loads(b)
                       # update this user's balance
                       if username in dic:
                           dic[username] += amt
                       new_data += json.dumps(dic) + "-"

               # rewrite updated balances
               fb = open("balancefile.txt", "w")
               fb.write(new_data)
               fb.close()

               print("Amount added successfully!")

           elif ch == 2:
               fb = open("balancefile.txt", "r")
               balance_list = fb.read().split("-")
               fb.close()

               for b in balance_list:
                   if b != "":
                       dic = json.loads(b)
                       if username in dic:
                           print(username,"Your is Balance:", dic[username])

           elif ch == 3:
               print("Thank you!")
               break

           else:
               print("Invalid choice!")

else:
   print("Invalid option!")
