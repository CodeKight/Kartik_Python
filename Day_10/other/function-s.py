# Question 1:
# get user information like name, age, address,.....
# create a function that prints out the introduction of the user

# #creating function with 3 parameters name 
# def user_intro(name,age,address):
#     print(f"Hi! my name is:{name}.\nI am {age} years old.\nI live in {address}.\n")
    
# #calling function with the arguments of user information     
# user_intro("Anil Nepali",23,"Basundhara")


#Question 2:
# get two number from user.
# create a function that print out the addition of 2 numbers

# try:
#     num_1 = int(input("Enter the first num:"))
#     num_2 = int(input("Enter the second num:"))

#     def add():
#         print(f"The addition between {num_1} and {num_2} is :{(num_1 + num_2)}")
#     add()
# except ValueError:
#     print("Invalid literal for int() with base 10")


#Question 3:
# # implement function in the simple calculator
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero!"

# def calculator(num1, num2, op):
#     if op == "+":
#         return add(num1, num2)
#     elif op == "-":
#         return subtract(num1, num2)
#     elif op == "*":
#         return multiply(num1, num2)
#     elif op == "/":
#         return divide(num1, num2)
#     else:
#         return "Invalid operator"

# # taking input
# try:
#     n1 = float(input("Enter first number: "))
#     n2 = float(input("Enter second number: "))
#     operator = input("Enter operator (+, -, *, /): ")

#     result = calculator(n1, n2, operator)
#     print(f"The {operator} between num 1 and num 2 is: {result}")

# except ValueError:
#     print("Please enter valid numbers!")
# calculator(10,20,operator)

#function with argument
# def add(a,b):
#     print(a+b)
# add(8,6)

# # implement function in Celsius to Fahrenheit temperature converter
# unit = input("Is this temperature is in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter the Temperatrue:"))
# if unit.upper()=="C":
#     temp = round((9*temp)/5 + 32,2)
#     print(f"The temperature in fahrenheit is :{temp}°F")
# elif unit.upper()=="F":
#     temp = round((temp-32)*5/9,2)
#     print(f"The temperature in celsius is :{temp}°C")
# else:
#     print(f"{unit} is an Invalid unit of a measurement")
# def convert_temperature():
#     try:
#         unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").strip()
#         temp = float(input("Enter the Temperature: "))

#         if unit.upper() == "C":
#             result = round((9 * temp) / 5 + 32, 2)
#             print(f"The temperature in Fahrenheit is: {result}°F")

#         elif unit.upper() == "F":
#             result = round((temp - 32) * 5 / 9, 2)
#             print(f"The temperature in Celsius is: {result}°C")

#         else:
#             print(f"{unit} is an invalid unit of measurement")

#     except ValueError:
#         print("Invalid temperature input! Please enter a number only.")
# convert_temperature()






# get a number from user
# create a function to check if it is even or odd.

# try:
#     num = int(input("enter any number:"))
#     def check_odd_even():
#         if num%2==0:
#             print(f"{num} is even number.")   
#         else:
#             print(f"{num} is odd number.")  
#     check_odd_even()
# except ValueError:
#     print("ValueError: invalid literal for int() with base 10: 'uu'")   

# create a function that takes a number from user and print out its square

# def square(num=int(input("enter any number"))):
#     print(num)
# square()