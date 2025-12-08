# Accounting Program: implement file handling(2 file: userdata {"username":"password"} save in text file, userbalance)
# give user 2 choices "Login" or "Register"
# if register, get username, password from user, store the data in a file
# if login, get username, password from user and check if the userdata exist in the file

# show 2 choice, add balce, view balance, if user choice is add, get amount from user and add the value to the initial balance, if choice is view then show the initial balance to the user
# if user does not exist in the dictironay, print out a statement

import json

choice = int(input("1. Register 2. Login "))

if choice == 1:
    f = open("userFile.txt", 'a')
    username = input("Enter username: ")
    password = input("Enter password: ")

    user_detail = {username: {"password": password, "balance": 0}}
    json_user = json.dumps(user_detail)

    f.write(json_user + '-')
    f.close()
    print("Registered successfully!")

elif choice == 2:
    f = open("userFile.txt", 'r')
    username = input("Enter username: ")
    password = input("Enter password: ")

    a = f.read().split('-')
    f.close()

    login = False
    updated_data = []

    for i in a:
        if i != "":
            json_data = json.loads(i)

            # Check login
            if username in json_data and password == json_data[username]["password"]:
                login = True
                print("Login Success!")

                choices = int(input("1. Add Balance\n2. View Balance\n>>> "))

                if choices == 1:
                    amount = float(input("Enter amount to add: "))
                    json_data[username]["balance"] += amount
                    print("Balance Added!")
                    print("New Balance:", json_data[username]["balance"])

                elif choices == 2:
                    print("Your Balance:", json_data[username]["balance"])

            updated_data.append(json_data)

    if login:
        f = open("userFile.txt", 'w')
        for d in updated_data:
            f.write(json.dumps(d) + '-')
        f.close()

    else:
        print("User Not Found!")
        
