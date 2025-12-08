# Function: like a variable but it hold block of code, task specific

# syntax
# def function_name():
#    statements


# create a function that prints the user introduction
# def introduction():
#    print(f"Name:Ram")

# introduction()

# def addition():
#    a = 10
#    b = 15
#    print(a + b)

# addition()

# parameter and arguments
# parameter: variable defined inside the parenthesis when decelaring function
# argument: variable inside the parenthesis when calling the function

# def addition(num1):   # parameter
#    print(num1 + 100)

# addition(15)   # argument


# Argument:
# positional argument: parameter accepts the argument in the given sequence(1st para -> 1st arg, 2nd para -> 2nd arg,....)
# def intro(name, age, address):
#    print(f"""Name:{name}
# Age: {age}
# Address:{address}""")

# intro("Ram","30","KTM")

# Keyword Argument: when calling function argrments are directly assigned to the parameter, does not care about the sequence of the argument
# def intro(name, age, address):
#    print(f"""Name:{name}
# Age: {age}
# Address:{address}""")

# intro(address = "Ktm", name = "Ram")

# Default Argument:  default values are assigned to the parameter when declerating function, when user send the argument to the parameter they are used but in case of missing arguments default valus are used
def intro(name="Default name", age="default age", address= " "):
   print(f"""Name:{name}
Age: {age}
Address:{address}""")

intro()


# todo:
# get user information like name, age, address,.....
# create a function that prints out the introduction of the user

# get two number from user.
# create a function that print out the addition of 2 numbers

# implement function in the simple calculator

# implement function in Celsius to Fahrenheit temperature converter

# get a number from user
# create a function to check if it is even or odd.

# create a function that takes a number from user and print out its square