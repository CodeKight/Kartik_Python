# File Handling -  process of creating, editing, manipulating the files programatically

# to open file
# open("path","mode")

# read mode('r'): file has to exist
# f = open("C:/Users/ittra/Desktop/file1.txt",'r')
# a = f.read()
# print(a)

# write mode('w'): if file does not exist new file is created and write the data, if file exist new data overrides the old data
# f = open("D:/Teach/kartik/file1.txt",'w')
# f.write("FIle file file file")


# append mode('a'): if file exist new data are added at the end of the file, if file doesnot exist new file is created
f = open("D:/Teach/kartik/file1.txt",'a')
f.write(" New data")


# todo:
# give user 2 choices "Login" or "Register"
# if register, get username from user, store the username in a file
# if login, get username from user and check if the name exist in the file