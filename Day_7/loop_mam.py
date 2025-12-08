# Loop
# continuous iteration, a block executing multiple times

# while loop: if the condition is true, then the block of code inside while loop is executed
# after the execution of all the statements inside while loop, the condition is checked again
# if the condition is still true, the block of code is executed again

# syntax:
# while contition:
#    print("Statement")

a = 0
b = 3

# while a < b:
#    print("Inside while loop")
#    print("A is smaller")
   
#    a += 1


# break : loop ends and read next statement that are present after loop
while a < b:
   if a == 2:
      break
   print("Inside while loop")
   print("A is smaller")
   a += 1

print("After break")

# continue : skips the current iteration and jumps to the next iteration
while a < b:
   a += 1
   if a == 2:
      continue
   print(a)



#calulator using if-else
# implement while loop
# get two numbers from user
# get the operator from user(+,-,*,/)
# perform the operation based on the operator
# ask if the user want to continue the calculation, if yes repeat the process, else exit

# day 6 assignment modification 
# implement while loop in rock paper scissor game

# implement while loop in
# get two numbers form user
# get the greater number from the list



# for loop