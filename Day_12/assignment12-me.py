

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
      
      
      
# userDict=[{
#     "username":"ram",
#     "password":"123",
#     "type":"seller"
# },{
#     "username":"sam",
#     "password":"456",
#     "type":"buyer"
# },{
#     "username":"hari",
#     "password":"789",
#     "type":"seller"
# }]

# product=[{
#     "name":"noodles",
#     "price":"20"
    
# },{
#     "name":"noodles",
#     "price":"20"
    
# },{
#     "name":"noodles",
#     "price":"20"
    
# }]



# def login(name):
#     for i in userDict:
#         is_status=False
#         if i[username]==username in userDict and i[password] in userDict:
#             is_status =True
        
            
        
        
        
# login(username, password)
        
        
        
        

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
      
  
  
      

# userDict=[
#     {
#         "username":"ram",
#         "password":"123",
#         "type":"seller"
#     },
#     {
#         "username":"sam",
#         "password":"456",
#         "type":"buyer"
#     },
#     {
#         "username":"hari",
#         "password":"789",
#         "type":"seller"
#     }
#     ]

# product=[
#     {
#         "name":"Biscuit",
#         "price":"20",
#         "seller":"ram"
#     },
#     {
#         "name":"Chocolate",
#         "price":"20",
#         "seller":"ram"
#     },
#     {
#         "name":"noodles",
#         "price":"20",
#         "seller":"hari"
#     },
#      {
#         "name":"Kurkure",
#         "price":"15",
#         "seller":"hari"
#     }
    
#     ]

# def login():
#     username = input("Username: ")
#     password = input("Password: ")
#     is_login = False
#     for i in userDict:
#         if i['username'] == username and i['password'] == password:
#             usertype = i['type']
#             is_login = True
    
#     if is_login:
#         print("Login Success")
#         if usertype == "seller":
#             choice = input("""1. View my products
# >>>""")
#             if choice == "1":
#                 for i in product:
#                    if i["seller"]==username:
#                        for j in i:
#                            print(j, ":", i[j])
                           
                           
#         elif usertype == "buyer":
            
#             choice = input("""1. View all products
# 2. Buy a product
# >>>""")
#             if choice == "1":
#                 for i in product:
#                        for j in i:
#                            print(j, ":", i[j])
                           
#             elif choice == "2":
#                product_name = input("Enter the product name: ")
#                for i in product:
#                   if i["name"] == product_name:
#                    print("Found:", i)
#                    qty=int(input("Enter the quantity: "))
#                    price = int(i["price"])*qty
#                    print("Price: ", price)
#                    break
#             else:
#                print("Product not found")

#     else :
#         print("No user mathcing")

# login()



#Function Based:----------------------------------------------------- 



userDict = [
    {"username": "ram", "password": "123", "type": "seller"},
    {"username": "sam", "password": "456", "type": "buyer"},
    {"username": "hari", "password": "789", "type": "seller"}
]

product = [
    {"name": "Biscuit", "price": "20", "seller": "ram"},
    {"name": "Chocolate", "price": "20", "seller": "ram"},
    {"name": "noodles", "price": "20", "seller": "hari"},
    {"name": "Kurkure", "price": "15", "seller": "hari"}
]


#Functions: 

def seller_menu(username):
    print("\n Seller Menu: ")
    choice = input("1. View my products\n >>> ")

    if choice == "1":
        view_seller_products(username)


def view_seller_products(username):
    print("\n Your Products: ")
    for p in product:
        if p["seller"] == username:
            for key in p:
                print(key, ":", p[key])
            print()


def buyer_menu():
    print("\n Buyer Menu: ")
    choice = input("1. View all products\n 2. Buy a product\n >>> ")

    if choice == "1":
        view_all_products()

    elif choice == "2":
        buy_product()

    else:
        print("Invalid choice!")


def view_all_products():
    print("\n All Products: ")
    for p in product:
        for key in p:
            print(key, ":", p[key])
        print()


def buy_product():
    product_name = input("Enter the product name: ")

    for p in product:
        if p["name"] == product_name:
            print("Found:", p)

            qty = int(input("Enter the quantity: "))
            price = int(p["price"]) * qty

            print("Price:", price)
            return

    print("Product not found!")


def login():
    username = input("Username: ")
    password = input("Password: ")

    for user in userDict:
        if user["username"] == username and user["password"] == password:
            print("\nLogin Success!\n")

            if user["type"] == "seller":
                seller_menu(username)

            elif user["type"] == "buyer":
                buyer_menu()

            return

    print("No user matching!")



#Main call: 

login()
