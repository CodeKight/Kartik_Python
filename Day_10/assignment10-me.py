

# todo:
# get user information like name, age, address,.....
# create a function that prints out the introduction of the user

print("\nTo do: ")
name=input("Enter name ")
age=input("Enter age ")
address=input("Enter address ")

def intro2(name, age, address):
 try:
   print(f"""Name: {name}
Age: {age}
Address: {address}""")
 except: 
     print("Invalid input")

intro2(name, age, address)



# get two number from user.
# create a function that print out the addition of 2 numbers

a=int(input("Enter a numb"))
b=int(input("Enter another numb"))

def add(a,b):
  try:
    print(a+b)
  except: 
      print("Invalid inpuy")
    
add(a,b)

# implement function in the simple calculator



num1=int(input("Enter a number"))
num2=int(input("Enter another number"))
op=input("Enter operation")

def calc(a,b,op):
  try:  
    if op=='+':
        print(num1+num2)
    elif op=='-':
        print(num1-num2)
    elif op=='*':
        print(num1*num2)
    elif op=='/':
        print(num1/num2)
    else:
        print("Invalid operator")
  except:
      print("Invalid input")
      
calc(num1, num2, op)


# implement function in Celsius to Fahrenheit temperature converter



myTemp=int(input("Enter a temperatur in Celcius "))
def fah(c):
    try:
     
      F = (myTemp * 9/5) + 32
      print("The temperature in Farenheit is: ", F)

    except:
        print("Invalid Number")
        
fah(myTemp)



# get a number from user
# create a function to check if it is even or odd.


b=input("Enter a numeber")
def EO(num):
    try:
        if b%2==0:
          print("Even")
        else:
          print("Odd") 
    
    except:
        print("Invalid input")
 
EO(b)

# create a function that takes a number from user and print out its square

sq=int(input("Enter a num"))

def square(a):
    
 try: 
         print("a*a")
 except:
    print("Invalid Input")
   
square(sq)


try:
    
    
except:
    print("Invalid input")