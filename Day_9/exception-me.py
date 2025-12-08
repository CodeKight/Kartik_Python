#EXCEPTION_HANDILING: runtime error

# try:
#     print(a+10)
#     a=int(input("Enter a number"))
 
# except NameError:
#     print("A is not defined")
# except ValueError:
#     print("Invalid Input")
# except:
#     print("Something went wrong")
    
    
# Implement exception handling in calculator

# try:
#  num1=int(input("Enter a number"))
#  num2=int(input("Enter another number"))
#  op=input("Enter operation")
# except:
#     print("Invalid Input")

# try:
#  if op=='+':
#     print(num1+num2)
#  elif op=='-':
#     print(num1-num2)
#  elif op=='*':
#     print(num1*num2)
#  elif op=='/':
#     print(num1/num2)
# except:
#     print("Invalid operaton")


try:
 num1=int(input("Enter a number"))
 num2=int(input("Enter another number"))
 op=input("Enter operation")
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
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Invalid Input")





