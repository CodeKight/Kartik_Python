

# Ecommerse: function based
# create a dict that consists username, password, usertype(buyer,seller)
# [{"username":"ram","password":"123","usertype":"seller"},{"username":"shyam","password":"123","usertype":"buyer"}]
# create a dict that consists product list(name, description, price, seller_name:"ram")

# get username and password from user, check if it exists in the dictionary, if it exists get the usertype
# check if the usertype is buyer or seller,
   
   # if buyer: show choice 1. view all product 2. buy product 
      # if choice 1 show all product
      # if choice is 2. ask user what they want to buy, quantity and show the total price (price*quantity)
      
      
      
userDict=[
    {
        "username":"ram",
        "password":"123",
        "type":"seller"
    },
    {
        "username":"sam",
        "password":"456",
        "type":"buyer"
    },
    {
        "username":"hari",
        "password":"789",
        "type":"seller"
    }
    ]

product=[
    {
        "name":"Biscuit",
        "price":20,
        "seller":"ram"
    },
    {
        "name":"Chocolate",
        "price":10,
        "seller":"ram"
    },
    {
        "name":"noodles",
        "price":40,
        "seller":"hari"
    }
    ]

def login():
    username = input("Username: ")
    password = input("Password: ")
    is_login = False
    for i in userDict:
        if i['username'] == username and i['password'] == password:
            usertype = i['type']
            is_login = True
    
    if is_login:
        print("Login Success")
        if usertype == "seller":
            choice = input("""1. View my products
>>>""")
            if choice == "1":
                for pr in product:
                    if pr['seller'] == username:
                            print(f"{pr['name']} --> Rs.{pr['price']}")

        elif usertype == "buyer":
            choice = input("""1. View all products
2. Buy a product
>>>""")
            if choice == "1":
                for pr in product:
                    print(f"{pr['name']} --> Rs.{pr['price']}")
            elif choice == "2":
                for i in range(len(product)):
                    print(i, product[i]["name"], product[i]["price"])
                
                select = int(input("Enter product number to buy: "))
                quantity = int(input("Enter quantity: "))

                if 0 <= select < len(product):
                    total = product[select]["price"] * quantity
                    print(f"Total Price: Rs.{total}")
                else:
                    print("Invalid product selection!")

    else:
        print("Invalid username or password!")
login()



# todo:
# give user 2 choices "Login" or "Register"
# if register, get username from user, store the username in a file
# if login, get username from user and check if the name exist in the file


# choice = input("""1. Register
# 2. Login
# >>>>>>""")
# if choice == "1":
#     user = input("Enter your name: ")
#     file = open("file1.txt", "a")
#     write = file.write(user + "\n")
#     print("Registration successful!")
#     file.close()

# elif choice == "2":
#     username = input("Enter your name: ")
#     file = open("file1.txt", "r")
#     user = file.read().splitlines()
#     if username in user:
#         print(f"The name {username} exists in the file")
#     else:
#         print("username not found")
#     file.close()


def register():
    username = input("Enter your name: ")
    file = open("file1.txt", "a")
    write = file.write(username + "\n")
    print("Registration successful!")
    file.close()


def login():
    username = input("Enter username to login: ")
    try:
        file = open("file1.txt", "r")
        user = file.read().splitlines()
        if username in user:
            print(f"The name {username} exists in the file")
        else:
            print("username not found")
        file.close()
    except FileNotFoundError:
        print("No registered users found. Please register first.")

choice = input("""1. Login
2. Register
>>>>>>""")
if choice == "1":
    login()
elif choice == "2":
    register()
else:
    print("Invalid choice! Please select 1 or 2.")
