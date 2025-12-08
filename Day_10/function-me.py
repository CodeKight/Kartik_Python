#FUNCTION: like a variable but it holds a bolock of codes, it is task specific

#syntax
#  def function_name():
#      statements


#function that prints the user introduction

# def introduction():
#     print("Name:ram")
    
# introduction()

# def addition():
#     a=10
#     b=12
#     print(a+b)
    
# addition()

#Parameter and Arguments
# Paramenter: variable defined inside the parenthesis when declaring the function
# Arguments: value/ variable inside the parenthesis when calling the funciton

# def addition2(a,b): #Paramenter 
#     print(a+b)

# addition2(5,9) #Arguments


#Arguments: 

# Positional arguments: parameter accepts the arguments in the given sequences, 1st arg, 2nd arg, 3rd arg

# def intro(name, age, address):
#     print(f"""Name: {name}
# Age: {age} 
# Address: {address}""")
    
# intro("ram",22,"ktm")


#Keyword argument: when calling function arguments directly assigned the parameter, does not care about the sequence of the argument 



# def intro(name, age, address):
#     print(f"""Name: {name}
# Age: {age} 
# Address: {address}""")
    
# intro(address="ktm", name="Ram", age=44)


#Default Argument: defuult values are assigned tot he parameter when declaring funciton, when user send the argument tot he parameter they are used but in case of missing arguments default values are used


# def intro(name="Defualt name ", age="default age ", address="Default address"):  #you can also leave default value as blank 
#     print(f"""Name: {name}
# Age: {age} 
# Address: {address}\n""")
    
# intro(address="ktm", name="Ram")
# intro("ram", 22, address="ktm")

# intro()

# to do: 

print("\nTo do: ")
name=input("Enter name ")
age=input("Enter age ")
address=input("Enter address ")

def intro2(name, age, address):
   print(f"""Name: {name}
Age: {age}
Address: {address}""")

intro2(name, age, address)
