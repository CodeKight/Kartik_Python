# Ecommerse: function based
# create a dict that consists username, password, usertype(buyer,seller)
# [{"username":"ram","password":"123","usertype":"seller"},{"username":"shyam","password":"123","usertype":"buyer"}]
# create a dict that consists product list(name, description, price, seller_name:"ram")

# get username and password from user, check if it exists in the dictionary, if it exists get the usertype
# check if the usertype is buyer or seller,
   # if seller: show choices 1. view my product
   # if buyer: show choice 1. view all product 2. buy product 
      # if choice 1 show all product
      # if choice is 2. ask user what they want to buy, quantity and show the total price (price*quantity)

userdata =[
    {"username":"ram","password":"ram123","usertype":"seller"},
    {"username":"shyam","password":"shyam123","usertype":"buyer"},
    {"username":"hari","password":"hari123","usertype":"buyer"},
    {"username":"gita","password":"gita123","usertype":"seller"},
]
# create a dict that consists product list(name, description, price, seller_name:"ram")
productdata = [
    {
        "name": "Laptop",
        "description": "A high-performance laptop suitable for gaming and work.",
        "price": 85000,
        "seller_name": "ram"
    },
    {
        "name": "Mouse",
        "description": "Wireless optical mouse",
        "price": 1200,
        "seller_name": "gita"
    },
    {
        "name": "Headphones",
        "description": "Noise-cancelling over-ear headphones",
        "price": 4500,
        "seller_name": "gita"
    },
    {
        "name": "Mobile Phone",
        "description": "Latest smartphone with AMOLED display",
        "price": 75000,
        "seller_name": "ram"
    },
]

# get username and password from user, check if it exists in the dictionary, if it exists get the usertype
# check if the usertype is buyer or seller,
   # if seller: show choices 1. view my product
   # if buyer: show choice 1. view all product 2. buy product 
      # if choice 1 show all product
      # if choice is 2. ask user what they want to buy, quantity and show the total price (price*quantity)

def login(name, passw):
    for user in userdata:
        if user["username"] == username and user["password"] == password:
            print(f"login success and you are {user["usertype"]}")

username = input("Enter your name: ")
password = input("Enter your password: ")

def seller(username):
    choice = input("Enter your choice 1:") 
    if choice == "1":
        for p in productdata:
           if p["seller_name"] == username:
                print(p)
    else:
        print("something went wrong")


def buyer():
    choice = input("Enter your choice: ")
    if choice == "1":
        for p in productdata:
            print(p)

    elif choice == "2":
        for i in range(len(productdata)):
            p = productdata[i]
            print(i, p["name"], p["price"])
        select = int(input("Enter product number to buy: ")) - 1
        quantity = int(input("Enter quantity: "))

        if 0 <= select < len(productdata):
            total = productdata[select]["price"] * quantity
            print(f"Total Price: Rs.{total}")
        else:
            print("Invalid product selection!")
login(username, password)

