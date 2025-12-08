#=============== READ   WRITE   APPEND
#                READ+  WRITE+  APPEND+ =======================



#how to read a file: If you try to open and read the file that doesn't exist then it gives error. 

#Raad: 
# try: 
#  f=open("myFile.txt","r")
#  d= f.read()
#  print(d)

# except: 
#     print("File doesn't exist. ")


# #Write: 
f=open("myFile.txt","w")
f.write("This is my file")
f.seek(20)
f.write("Lion")

#Open: 
# f=open("myFile.txt","a")
# d=f.write("\nThis is appened ")
# print(d)


#read +
#write +
#append + 

#read +: the file must exist at first otherwise it gives error. In read and read + mode the file must exist. 
#it works like append mode, it doesn't erase the existing data of a file. 

# try: 
#  f=open("myFile.txt","r+")
#  d=f.read()
#  print(d)
# except:
#     print("File doesn't exist. ")

# f.write("\ncherryf ")
# print(f.read())
# # print(d)


#write + mode: seek(*index) is mandatory in w+ mode if you want to read a file also 

# f=open("appleFile.txt","w+")
# f.write("Apple is red in color. ")
# f.seek(0)       #The cursor move to the end and nothing is printed, so to bring back the cursor at the begining, we use seek() method

# print(f.read())
# f.write("Green is leaf ")
# f.write("Yellow ")
# f.write("Yellow ")
# f.write("Yellow ")


# #append + mode: 
# f=open("manFile.txt","a+")
# f.write("\nThis is the guava file3 ")
# f.seek(4)
# # print(f.read())
# f.write("Wrinting at the end. ")  # *Append mode always  write at the end despite of the cursor position .





# | Mode | Can Read | Can Write | Preserves Old Data? | Behavior on open                                                                       |
# | ---- | -------- | --------- | ------------------- | -------------------------------------------------------------------------------------- |
# | `r`  | ✅        | ❌         | ✅                   | Must exist, reads only, content is preserved                                           |
# | `r+` | ✅        | ✅         | ✅                   | Must exist, can read and write, writing **overwrites from pointer**, preserves rest    |
# | `a`  | ❌        | ✅         | ✅                   | Creates if missing, writes **always at end**, preserves old data                       |
# | `a+` | ✅        | ✅         | ✅                   | Creates if missing, can read and write, writing **always appends**, preserves old data |
# | `w`  | ❌        | ✅         | ❌                   | Creates if missing, **clears file on open**, writing starts at beginning               |
# | `w+` | ✅        | ✅         | ❌                   | Creates if missing, **clears file on open**, can read/write, writing starts at pointer |
 