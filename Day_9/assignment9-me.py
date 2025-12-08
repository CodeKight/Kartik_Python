# implement exception handling 
# in calculator

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



# in program that converts a temperature from Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32.

try:
 myTemp=int(input("Enter a temperatur in Celcius "))
 F = (myTemp * 9/5) + 32
 print("The temperature in Farenheit is: ", F)

except:
    print("Invalid Number")
    



# in program that determines if a triangle is valid (sum of any two sides must be greater than the third side).

try:
 Side1=int(input("Enter the side 1: "))
 Side2=int(input("Enter the side 2: "))
 Side3=int(input("Enter the side 3: "))

 if Side1+Side2>=Side3 and Side1+Side3>=Side2 and Side2+Side3>=Side1:
    print("Triangle is valid.")
 else:
    print("Trianlge is not valid")
except:
    print("Invalid number entry")


# in a program that checks if a number is between 1 and 100

try:
 numCheck = int(input("Enter a number: "))
 if numCheck in range (1,101):
    print("The number fall betwee 1 to 100. ")
 else:
    print("The number is beyond 100. ")
except:
    print("Invalid number format")

# in grade calculation program

try:
    f=int(input("Enter your marks"))

    if f>=80 and f<100:
        print("You got A+")
    elif f>=70 and f<80:
        print("You got A ")
    elif f>=60 and f<70:
        print("You got B+")
    elif f>=50 and f<B:
        print("You got B")
    elif f>=40 and f<50:
        print("You got C")
    else:
        print("You failed in Exam")
except:
    print("Wrong data")
    
    

# in simple tip calculator

try:
 Bill = float(input("Enter the bill amount: "))
 Tip = float(input("Enter the tip percent: "))
 Bill += Bill*Tip/100
 print("Total bill: ", Bill)
 
except:
    print("Invalid Number")

