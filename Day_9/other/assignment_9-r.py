# implement exception handling 
# in calculator
# while True:
#     try:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#         operator = input("Enter the operator: ")
#         if operator == "+":
#             print("The sum is: ", num1 + num2)
#         elif operator == "-":
#             print("The difference is: ", num1 - num2)
#         elif operator == "*":
#             print("The multiply is: ", num1 * num2)
#         elif operator == "/":
#             print("The division is: ", num1 / num2)
#         else:
#             print("invalid operator")
#     except:
#         print("invalid inputs")
#     repeat = input("Do you want to continue the calculation? ")
#     if repeat != "yes":
#         print("Thankyou for using this calculator")
        # break


# in program that converts a temperature from Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32.
# try:
#     temp = float(input("Enter the temperature in celcius: "))
#     fahrenhite = (temp * 9/5) + 32
#     print(f"The Temperature from Celsius to Fahrenheit is {fahrenhite}°F")
# except ValueError:
#     print("please enter the correct value")


# in program that determines if a triangle is valid (sum of any two sides must be greater than the third side).
# try:
#     len = float(input("Enter the length of a triangle: "))
#     bredth = float(input("Enter the bredth of a triangle: "))
#     height = float(input("Enter the height of a triangle: "))
#     if len+bredth>height and len+height>bredth and height+bredth>len:
#         print("The triangle is valid ")
#     else:
#         print("THe triangle isnot valid ")
# except ValueError:
#     print("please enter the correct value")


# in a program that checks if a number is between 1 and 100
# try:
#     num = int(input("Enter the number: "))
#     for i in range(1, 101):
#         if num == i:
#             print(f"{num} is between 1 and 100")
#             break
# except:
#     print("something went wrong! please enter the correct input")


# in grade calculation program
# try:
#     grade = float(input("Enter your marks: "))
#     if grade>90 and grade<100:
#         print("A+")
#     elif grade>80 and grade<90:
#         print("A")
#     elif grade>70 and grade<80:
#         print("B+")
#     elif grade>60 and grade<70:
#         print("B")
#     elif grade>50 and grade<60:
#         print("C+")
#     elif grade>50 and grade<60:
#         print("C")
#     elif grade>40 :
#         print("D+")
#     else:
#         print("fail")
# except ValueError:
#     print("invalid input")


# in simple tip calculator
# try:
#     bill_amt = float(input("Enter the bill amount: "))
#     tip_percentage = float(input("Enter the tip percentage: "))
#     tip_amt = (tip_percentage * bill_amt)/100
#     total_bill_amt = tip_amt + bill_amt
#     print("The total bill amount is :", total_bill_amt )
#     print("The total tip amount is :", tip_amt )
# except ValueError:
#     print("invalid inputs")