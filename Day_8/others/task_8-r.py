# 1. Write a program that converts a temperature from Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32.
# temp = float(input("Enter the temperature in celcius: "))
# fahrenhite = (temp * 9/5) + 32
# print(f"The Temperature from Celsius to Fahrenheit is {fahrenhite}°F")


# 2.Write a program that asks for the user's age as input (string), converts it to an integer, and calculates what their age will be in 10 years.
# user = input("Enter your age: ")
# user = int(user)
# age = user + 10
# print("Ypur age after 10 year is ", age)


# 3.Write a program that takes a decimal number as input and prints both the integer part and the decimal part separately.
# num = float(input("Enter the number: "))
# integer_part = int(num)
# decimal_part = num-integer_part
# print("The integer part is ", integer_part)
# print("The decimal part is ", decimal_part)


# 4.Create a program that calculates the average of five numbers entered by the user.
# i = 1
# total = 0
# while i<=5:
#     num = float(input("Enter the number: "))
#     total += num 
#     i+=1
# average_number = total/5
# print("The average of 5 number is: ",average_number)


# 5.Build a simple tip calculator: ask for the bill amount and tip percentage, then calculate the tip and total.
# bill_amt = float(input("Enter the bill amount: "))
# tip_percentage = float(input("Enter the tip percentage: "))
# tip_amt = (tip_percentage * bill_amt)/100
# total_bill_amt = tip_amt + bill_amt
# print("The total bill amount is :", total_bill_amt )
# print("The total tip amount is :", tip_amt )


# 6.Use //= to repeatedly divide a number by 2 until it becomes 1. How many divisions did it take? Print it out
# num = int(input("Enter the number: "))
# count = 0
# while num >1:
#     num //=2
#     count+=1
# print("Number of divisions:", count)


# 7.Create a program that checks if a number is between 1 and 100
# num = int(input("Enter the number: "))
# for i in range(1, 101):
#     if num == i:
#         print(f"{num} is between 1 and 100")
#         break
    

# 8.Write a program that checks if a user's input contains the word "Python".
# user = input("Enter the your statement: ")
# if "python" in user:
#     print("Yes! The python word exist")
# else:
#     print("No, The python word doesnot exist")


# 9.Ask for a sentence and check if it contains any vowels (a, e, i, o, u).
# sentence = input("Enter your sentence: ")
# for vowels in "aeiouAEIOU":
#     if vowels in sentence:
#         print("Yes! It contains the vowels")
#         break


# 10.Write a program that determines if a triangle is valid (sum of any two sides must be greater than the third side).
# len = float(input("Enter the length of a triangle: "))
# bredth = float(input("Enter the bredth of a triangle: "))
# height = float(input("Enter the height of a triangle: "))
# if len+bredth>height and len+height>bredth and height+bredth>len:
#     print("The triangle is valid ")
# else:
#     print("THe triangle isnot valid ")


# 11. Build a mini-quiz: ask 3 questions and count how many correct answers the user gets.
# count = 0
# quiz1 = input("What is the capital city of Nepal? ")
# if quiz1.lower()=="kathmandu":
#     count+=1
# quiz2 = input("What is 5 + 7?")
# if quiz2=="12":
#     count+=1
# quiz3 = input("How many hours are there in a day?")
# if quiz3=="24":
#     count+=1
# print(f"You have {count} correct answer.")


# 12. Calculate the sum of numbers from 1 to n (n is the user input)
# n = int(input("Enter the number: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print("The sum of the number is: ", sum)


# 13. Write a program that keeps asking for a password until the correct one is entered.
# while True:
#     user = input("Enter the correct password: ")
#     if user.lower() == "roma123":
#         print("You have entered correct password")
#         break
#     else:
#         print("Try again to enter correct password")


# 14. Write a program that counts how many vowels are in a string.
# string = input("Enter the word: ").lower()
# count = 0
# for vowels in string:
#     if vowels in "aeiou":
#         count+=1
# print(f"There are {count} vowels")