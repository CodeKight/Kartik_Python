# Indexing: index or position starts from 0 : string, list, tuple . Used to access/get a single data in the given index/position

# string
# a = "mind risers"

# # m:0
# # i:1
# # n:2
# # d:3
# # :4
# # r:5

# print(a[3])

# b = "I am a ( programmer )."
# # print out ( and )
# print(b[7])


# # list, tuple
my_list = ["a fgf dfg","b","c",5,"e","f"]

# # "a": 0
# # "b":1
# # "c":2

# # access and printout 5 from the list
print(my_list[-3])

# my_list[3] = "d"
# print(my_list)


# my_tuple = ("a fgf dfg","b","c",5,"e","f")
# print(my_tuple[3])



# Slicing: used to get a subset from the given sequence, include the start index but exclude the end index(start index ko data batw end - 1 index samma ko data are included)
# variable[start_index : end_index]

my_list = ["a","b","c",5,"e","f"]
# print b to e from above list
print(my_list[2:])

# my_list[1:5] = "abc","sldkjf"
# print(my_list)

# variable[start_index : end_index : step]

print(my_list[0:5:2])

# todo:
# colors = ["red","blue","green","purple","yellow","orange"]
# print out green from the list of colors using positive index
# print out yellow using negetive index
# extract red, blue, green from the above given sequence and assign it to new veriable rgb

# number = [0, 10,20,30,40,50,60,70,80,90]
# print out the sequence with 3 interval
# print out the reverse of the sequence number
# extract the data from even index and assign it to even variable
# extract the data from odd index and assign it to odd variable

# multiple = [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
# ]
# print out 5 from above list
# print out 9 from above list
# print out [4,5,6] from the sequence

# string = "PYTHON COURSE"
# chara = ['A','j','P','R','V']
# print out "PYTHON" from string variable
# print out "PY" from the above string and assign it to a veriable
# replace the character 'j' in chara  with "PY"


# dict
my_dict = {
   "name":"ram",
   "age":"500",
   "address":"Kathmandu",
   "hobbiess": ["reading","watching movies","go hiking","playing games"]
}

print(my_dict["name"])
# print age, address, hobbies
# "My hobby is ____"
# print out read
# print out movies
# print out hiking
# print out playing game