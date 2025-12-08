#File handling: process of creating, edinting, manipulating the files programetically

#to open a file: 

# open(path, mode)

#read mode ( 'r' )
# f= open("C:/Users/USER/OneDrive/Desktop/file.txt", 'r')
# a = f.read()
# print(a)

  
#Write into a file ( 'w' ): if file doesn't exist new file is created , if file exist then the existing data is overwritten by new data
# f= open("C:/Users/USER/OneDrive/Desktop/file.txt", 'w')
# f.write("file is new file ")



#append mode( 'a' ): if file exist new data are added at the end of the file, if file doesn't exist, new file is created. 

# f= open("C:/Users/USER/OneDrive/Desktop/file.txt", 'a')
# f.write("This is append  ")


#to do: 
# get username form usser 
# give user two choice
# if register, username should be stored in file, 
# if login , get username and check if name exist in the file. 


username=input("Enter your username: ")
choice=int(input("1. Register 2. Login "))

if choice==1:
    f= open("C:/Users/USER/OneDrive/Desktop/userFile.txt", 'a')
    f.write(username)
    print("Registered successfully")
elif choice==2:
  f= open("C:/Users/USER/OneDrive/Desktop/userFile.txt", 'r')
  a = f.read()
  if username in a:
    print("Login Successfully! ")
  else:
    print("Couldn't find username. ")

else: 
  print("Invalid Choice. ")

    





