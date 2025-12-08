

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
        "price":"20",
        "seller":"ram"
    },
    {
        "name":"Chocolate",
        "price":"20",
        "seller":"ram"
    },
    {
        "name":"noodles",
        "price":"20",
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
                pass

        elif usertype == "buyer":
            choice = input("""1. View all products
2. Buy a product
>>>""")
            if choice == "1":
                pass
            elif choice == "2":
                pass
    else:
        print("No user mathcing")

login()