# File Handling in Accounting Assingment: 
# ----------------------------------------------------------------------------------

import json

choice = int(input("1. Register  2. Login "))

#Register: 
if choice == 1:
    f = open("userFile.txt", "a")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = {username: password}
    f.write(json.dumps(user) + "-")
    f.close()
    print("Registered Successfully")

#Login: 
elif choice == 2:
    f = open("userFile.txt", "r")
    username = input("Enter username: ")
    password = input("Enter password: ")
    users = f.read().split("-")
    f.close()

    login_ok = False

    for u in users:
        if u != "":
            d = json.loads(u)
            if username in d and d[username] == password:
                login_ok = True
                break

    if not login_ok:
        print("User data not found")
        exit()

    print("Login Success")

    #Balance Option: 
    ch = int(input("1. View Balance  2. Add Balance "))

    #Read existing file: 
    try:
        f = open("userBal.txt", "r")
        bal_list = f.read().split("-")
        f.close()
    except:
        bal_list = []

    balance_dict = {}

    for b in bal_list:
        if b != "":
            d = json.loads(b)
            balance_dict.update(d)

    #Show balance: 
    if ch == 1:
        if username in balance_dict:
            print("Your Balance is:", balance_dict[username])
        else:
            print("Your Balance is: 0")

    #Add balance: 
    elif ch == 2:
        if username in balance_dict:
            oldBal = int(balance_dict[username])
            addBal = int(input("Enter amount to add: "))
            newBal = oldBal + addBal
            print("New Balance is:", newBal)

        else:
            initBal = int(input("No balance. Enter initial balance: "))
            print("Initial Balance is:", initBal)

    else:
        print("Invalid Choice")

else:
    print("Invalid Choice")



#File Handling in Ecommerce Assingment. 
#-------------------------------------------------------------------------

# import json

# userFile = "userFile.txt"
# productFile = "productFile.txt"

# #Login or register:
# print("1. Register\n2. Login")
# choice = input("Enter choice: ")

# #Register: 
# if choice == "1":
#     print("=== REGISTER ===")
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     usertype = input("Enter type (seller/buyer): ")

    
#     with open(userFile, "a") as uf:
#         uf.write(json.dumps({username: {"password": password, "type": usertype}}) + "-")

  
#     if usertype == "seller":
#         pname = input("Enter product name: ")
#         price = input("Enter price: ")
#         with open(productFile, "a") as pf:
#             pf.write(json.dumps({"name": pname, "price": price, "seller": username}) + "-")

#     print("Registration complete.\n")

# #Login: 
# print("=== LOGIN ===")
# uname = input("Username: ")
# upass = input("Password: ")


# f = open(userFile, "r")
# u_data = f.read().split("-")
# f.close()

# userDict = []

# for u in u_data:
#     if u != "":
#         d = json.loads(u)
#         for key in d:
#             value = d[key]
#             if isinstance(value, dict):
#                 userDict.append({"username": key, "password": value["password"], "type": value["type"]})
#             else:
#                 userDict.append({"username": key, "password": value, "type": "buyer"})

# logged_in = False
# for user in userDict:
#     if uname == user["username"] and upass == user["password"]:
#         logged_in = True
#         uType = user["type"]
#         break

# if not logged_in:
#     print("Invalid credentials")
#     exit()

# print("Login successful!\n")


# #Load prduct: 
# f = open(productFile, "r")
# p_data = f.read().split("-")
# f.close()

# product = []
# for p in p_data:
#     if p != "":
#         d = json.loads(p)
#         product.append(d)


    
#     #Seller menu: 
#     print("1. View My Products\n2. Add More Product")
#     choice = input("Enter choice: ")

#     if choice == "1":
#         print("\nYour Products:")
#         for p in product:
#             if p["seller"] == uname:
#                 print("Name:", p["name"], "| Price:", p["price"])

#     elif choice == "2":
#         pname = input("Enter new product name: ")
#         price = input("Enter price: ")
#         with open(productFile, "a") as pf:
#             pf.write(json.dumps({"name": pname, "price": price, "seller": uname}) + "-")
#         print("Product added successfully.")


# #Buyer menu: 

#     elif uType == "buyer":
#      print("1. View All Products\n2. Buy Product")
#      choice = input("Enter choice: ")

#     if choice == "1":
#         print("\nAll Products:")
#         for p in product:
#             print("Name:", p["name"], "| Price:", p["price"], "| Seller:", p["seller"])

#     elif choice == "2":
#         pname = input("Enter product name to buy: ")
#         qty = int(input("Enter quantity: "))
#         found = False
#         for p in product:
#             if p["name"] == pname:
#                 total = int(p["price"]) * qty
#                 print("\nProduct:", pname)
#                 print("Seller:", p["seller"])
#                 print("Quantity:", qty)
#                 print("Total Price:", total)
#                 found = True
#                 break
#         if not found:
#             print("Product not found.")
