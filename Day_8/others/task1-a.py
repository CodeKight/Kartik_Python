# # 1. Write a program that converts a temperature from Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32.print("-------------------------------------------------------------")
# print("      Temperature Convertor      ")
# print("-------------------------------------------------------------")


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

# print("-------------------------------------------------------------")


# 2.Write a program that asks for the user's age as input (string), converts it to an integer,
# and calculates what their age will be in 10 years.
# user_age = str(input("Enter your age: "))
# user = int(user_age)
# age = user + 10
# print("Ypur age after 10 year is ", age)


# 3.Write a program that takes a decimal number as input and prints both the integer part 
# and the decimal part separately.

# 4.Create a program that calculates the average of five numbers entered by the user.

# 5.Build a simple tip calculator: ask for the bill amount and tip percentage, then calculate the tip and total.
# 6.Use //= to repeatedly divide a number by 2 until it becomes 1. How many divisions did it take? Print it out
# 7.Create a program that checks if a number is between 1 and 100

# num = int(input("Enter any number between 1 to 100:"))

# # for i in range(1,100):
# if num in range(1,100):
#     print(f"The number {num} is between 1 to 100: ")
# elif num < 0:
#     print(f"The {num} is less than 0 and not between 1 to 100")
# elif(num >100):
#     print(f"The {num} is greater than 100 and not between 1 to 100")
# else:
#     print("invalid input")

# 8.Write a program that checks if a user's input contains the word "Python".
# word = input("Enter the word:")
# if word == "Python".lower():
#     print(f"user input is correct")
# else:
#     print("Invalid user input")

# 9.Ask for a sentence and check if it contains any vowels (a, e, i, o, u).
# sentence = input("Enter the Sentence:")
# vowels = ['a', 'e', 'i', 'o', 'u']

# found_vowels = []  #creating empty list

# for char in sentence:
#     if char.lower() in vowels:
#         found_vowels.append(char)

# if found_vowels:
#     print("Vowels in sentence are:", found_vowels)
# else:
#     print("char a,e,i,o,u are not found")

# 14. Write a program that counts how many vowels are in a string.

# count = 0

# for char in sentence:
#     if char.lower() in vowels:
#         count += 1

# print("Total number of vowels:", count)

        
# # 10.Write a program that determines if a triangle is valid (sum of any two sides must be greater than the third side).
# a = int(input("Enter side a: "))
# b = int(input("Enter side b: "))
# c = int(input("Enter side c: "))

# # Check triangle validity
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("The triangle is valid.")
# else:
#     print("The triangle is NOT valid.")

# 11. Build a mini-quiz: ask 3 questions and count how many correct answers the user gets.
# score = 0       #Initialize score as 0
# total_questions = 3  # Define total questions

# #Q1
# print("Q1: Which programming language has rich frameworks?:")
# ans = input().strip().lower() 

# if ans == "python":
#     score += 1         #every time answer is corrected score update by 1
#     print("Correct!")
# else:
#     print("Wrong answer")

# #Q2
# print("Q2: Which is the Backend Framework of Python")
# ans2 = input().strip().lower()

# if ans2 == "django":  # Fixed: should be lowercase to match .lower()
#     score += 1
#     print("Correct!")
# else:
#     print("Wrong answer")
    
# #Q3
# print("Q3: List is Mutable or Immutable?:")
# ans3 =input().strip().lower()

# if ans3 == "Mutable":
#     score += 1
# else:
#     print("Wrong answer")

# print(f"Your score: {score}/{total_questions}")

# 12. Calculate the sum of numbers from 1 to n (n is the user input)
# n = int(input("Enter the number till you want sum: "))
# sum = n*(n+1)/2
# print(sum)

# total = 0
# for i in range(1,n+1):
#     total += i
# print(total)
    
# 13. Write a program that keeps asking for a password until the correct one is entered.
# password = "mindrises.com"
# while True:
#     user_input = input("Enter the password:")
#     if user_input == password:
#         print("congrulation you Guess it")
#         break
#     else:
#         print("not matched")

