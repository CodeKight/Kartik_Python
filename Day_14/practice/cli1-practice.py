# Accounting Program: implement file handling(2 file: userdata {"username":"password"} save in text file, userbalance)
# give user 2 choices "Login" or "Register"
# if register, get username, password from user, store the data in a file
# if login, get username, password from user and check if the userdata exist in the file

# show 2 choice, add balce, view balance, if user choice is add, get amount from user and add the value to the initial balance, if choice is view then show the initial balance to the user
# if user does not exist in the dictironay, print out a statement


import json

choice = int(input("1. Register  2. Login "))

if choice == 1:
    username=input("Enter username: ")
    password = input("Enter password: ")
    f=open("userFile.txt","a")
    user_detail = {username:password} # *This is dictionary and cannot be stored in file. 
    json_data= json.dumps(user_detail)
    f.write(json_data+"-") #*
    print("Registered successfully! ")
    f.close()
    
elif choice == 2:
    username=input("Enter username: ")
    password=input("Enter password: ")
    f=open("userFile.txt","r")
    data=f.read().split("-")
    print(data)
    
#     login_status=False
#     for i in data:
#         if i!='':
#             json_data=json.loads(i)
#             if username in json_data and password == json_data[username]:
#                 print("Loging successful ")
#                 login_status =True
               
            

#     if login_status==False:
#         print("Invalid credential ")
        
    
    

# else:
#     print("Invalid choice ")
    
    