# args: it is used instead of parameters, accepts multiple arguments, * is used to define args, args accepts tuple datatype

# get a numbers and add them
# def addition(*args):
#    print(args[2])
#    sum = 0
#    for i in args:
#       sum += i
#    print(sum)

# addition(5,10,5,10,20,30,50,80,20,10)


# kwargs: multiple keyword data accepts, ** is used to define kwargs, accepts dictionary datatype
# def intro(**kwargs):
#    print(kwargs)
#    for key, values in kwargs.items():
#       print(f"{key}:{values}")


# intro(name = "Ram",age = "30",addresss ="KTM", phone = "985252555", gender = "male", abc = "20",xyz = "skjdfksjdf")

# def intro(name,age,*args,**kwargs):
#    print(f"Name: {name}")
#    print(f"Age: {age}")
#    print(f"Args: {args}")
#    print(f"Kwargs: {kwargs}")


# intro("Ram","30","skjdf","klskjdf", address = "KTM",phone = "985252555", gender = "male", abc = "20",xyz = "skjdfksjdf")

# todo:
# get a user information(name, age, address)
# get hobbies of users using args
# other addition info like contact info using kwargs(phone, email, address)
# print out introduction of the user


# return: return the values back to the line the function was called, it also ends the function so the statements writtrn after return is not executed
# sum = 100      # global variable

# def addition(*args):
#    sum = 0     # local variable: variable defined inside function, can only be used inside function
#    for i in args:
#       sum += i
#    return sum
#    print("abc")

# a = addition(5,10,5,10,20,30,50,80,20,10)
# print(a)

# print(a * 3)

z = 100        # global varaiable: can be access anywhere in the program, if tried to change it from inside function we have to define it is a global variable

# def addition(*args):
#    # global z
#    # z = 0     # local variable: variable defined inside function, can only be used inside function
#    # for i in args:
#    #    sum += i
#    print(z)
#    z += 1
   
#    return z

# # print(z)
# a = addition(5,10,5,10,20,30,50,80,20,10)
# print(a)


#------------------further extended----------------------------------

# create a dict of username and password {"ram":"ram123"}
# create a dict of username and initial_balance {"ram":"100000"}
# get username and password from user. check if it exist in the dictionary, if yes print "Login Success"
# show 2 choice, add balce, view balance, if user choice is add, get amount from user and add the value to the initial balance, if choice is view then show the initial balance to the user
# if user does not exist in the dictironay, print out a statement

userdata = {"ram":"ram123","shyam":"shyam123","hari":"hari123"}
userbalance = {"ram":100000,"shyam":50000,"hari":30000}

def add_balance(uname):
   initial = userbalance[uname] 
   amount = int(input("Enter an amount to add: "))
   total = amount + initial
   return total

def view_balance(uname):
   balance = userbalance[uname]
   # print(f"YOur balance is {balance}")
   return balance


def login(name, passw):
   if passw == userdata[name]:
      choice = input("""Login Succuss
   1. Add balance
   2. View Balance
   >>>""")
      if choice == "1":
         total = add_balance(name)
         print(f"Your new balance is {total}")
      elif choice == "2":
         blc = view_balance(name)
         print(f"Your balance is {blc}")
         
   else:
      print("Invalid Credentials")


username = input("Username: ")
password = input("Password: ")

login(username, password)






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