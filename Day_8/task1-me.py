#Task 1:

# 1. Write a program that converts a temperature from Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32.
# myTemp=int(input("Enter a temperatur in Celcius "))
# F = (myTemp * 9/5) + 32
# print("The temperature in Farenheit is: ", F)


# 2.Write a program that asks for the user's age as input (string), converts it to an integer, and calculates what their age will be in 10 years.
# myAge=input("Enter your age: ")
# intAge=int(myAge)
# print("Your age after 10 years will be: ", intAge+10)


# 3.Write a program that takes a decimal number as input and prints both the integer part and the decimal part separately.
# myNum=float(input("Enter a decimal num "))
# intPart=int(myNum)
# decPart=myNum-intPart
# print("Integer part: ", intPart)
# print("Decimal part: ", decPart)



# 4.Create a program that calculates the average of five numbers entered by the user.
# num1=int(input("Enter number1: "))
# num2=int(input("Enter number2: "))
# num3=int(input("Enter number3: "))
# num4=int(input("Enter number4: "))
# num5=int(input("Enter number5: "))
# Avg=num1+num2+num3+num4+num5
# print("The Average: ", Avg/5)


# 5.Build a simple tip calculator: ask for the bill amount and tip percentage, then calculate the tip and total.
# Bill = float(input("Enter the bill amount: "))
# Tip = float(input("Enter the tip percent: "))
# Bill += Bill*Tip/100
# print("Total bill: ", Bill)

# 6.Use //= to repeatedly divide a number by 2 until it becomes 1. How many divisions did it take? Print it out
# myNum = float(input("Enter a number: "))
# count = 0
# while myNum > 1:
#     myNum//=2
#     count+=1
    
# print("It took ", count, "division")


# 7.Create a program that checks if a number is between 1 and 100
# numCheck = int(input("Enter a number: "))
# if numCheck in range (1,101):
#     print("The number fall betwee 1 to 100. ")
# else:
#     print("The number is beyond 100. ")


# 8.Write a program that checks if a user's input contains the word "Python".
# myWord = input("Enter a word: ")
# if "Python".lower() in myWord:
#     print("It contains Python ")
# else:
#     print("It doesn't contain Python")


# 9.Ask for a sentence and check if it contains any vowels (a, e, i, o, u).
# mySen=input("Enter a sentence. ")
# if 'a' in mySen or 'e' in mySen or 'i' in mySen or 'o' in mySen or 'u' in mySen:
#     print("Yes, it contains vowel")
# else:
#     print("It doesn't contain vowel. ")

# 10.Write a program that determines if a triangle is valid (sum of any two sides must be greater than the third side).
# Side1=int(input("Enter the side 1: "))
# Side2=int(input("Enter the side 2: "))
# Side3=int(input("Enter the side 3: "))

# if Side1+Side2>=Side3 and Side1+Side3>=Side2 and Side2+Side3>=Side1:
#     print("Triangle is valid.")
# else:
#     print("Trianlge is not valid")

# 11. Build a mini-quiz: ask 3 questions and count how many correct answers the user gets.
# Que1=input("What is the color of the sky? ")
# Que2=input("What is the capital city of nepal? ")
# Que3=int(input("How many hours is there in a day? "))
# count=0

# if Que1.lower()=='blue':
#     count+=1
# if Que2.lower()=='ktm':
#     count+=1
# if Que3==24:
#     count+=1
# print("Correct ans: ", count)


# 12. Calculate the sum of numbers from 1 to n (n is the user input)
# myNum=int(input("Enter the value of n: "))
# sum=0
# for i in range(1,myNum+1):
#     sum+=i
    
# print(sum)
    

# 13. Write a program that keeps asking for a password until the correct one is entered.
# myPass=None
# while myPass!="pass":
#     myPass = input("Enter your password: ")
#     if myPass!="pass":
#      print("Wrong password!")
#      print("Try Again!")
#      print()
#     else:
#         print("Correct password! ")
# print("This is outside of the block. ")
    

# 14. Write a program that counts how many vowels are in a string.
# myStr=input("Enter a string: ")
# count=0
# for i in myStr:
#     if i.lower() in "aeiou":
#         count+=1
      
# print("There are ", count, "Vowel in the String. ")
