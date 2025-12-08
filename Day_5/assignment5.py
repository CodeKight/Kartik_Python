
# todo:
# colors = ["red","blue","green","purple","yellow","orange"]
# print out green from the list of colors using positive index
# print out yellow using negetive index
# extract red, blue, green from the above given sequence and assign it to new veriable rgb


colors = ["red","blue","green","purple","yellow","orange"]
print(colors[2])
print(colors[-2])
rgb=colors[:3]
print(rgb,'\n')




# number = [0, 10,20,30,40,50,60,70,80,90]
# print out the sequence with 3 interval
# print out the reverse of the sequence number
# extract the data from even index and assign it to even variable
# extract the data from odd index and assign it to odd variable

number = [0, 10,20,30,40,50,60,70,80,90]
print(number[0:10:3])
print(number[0::3])
print(number[-1:-11:-1])

even=number[0::2]
print(even)

odd=number[1::2]
print(odd,'\n')


# multiple = [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
# ]
# print out 5 from above list
# print out 9 from above list
# print out [4,5,6] from the sequence


multiple = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]

print(multiple[1][1])
print(multiple[2][2])
print(multiple[1],'\n')




# string = "PYTHON COURSE"
# chara = ['A','j','P','R','V']

# print out "PYTHON" from string variable
# print out "PY" from the above string and assign it to a veriable
# replace the character 'j' in chara  with "PY"


string = "PYTHON COURSE"
print(string[0:6])

py=string[0:2]
print(py)

chara = ['A','j','P','R','V']
chara[1]="PY"
print(chara,'\n')



# dict
# my_dict = {
#    "name":"ram",
#    "age":"500",
#    "address":"Kathmandu",
#    "hobbiess": ["reading","watching movies","go hiking","playing games"]
# }

# print(my_dict["name"])
# print age, address, hobbies
# "My hobby is ____"
# print out read
# print out movies
# print out hiking
# print out playing game


my_dict = {
   "name":"ram",
   "age":"500",
   "address":"Kathmandu",
   "hobbies": ["reading","watching movies","go hiking","playing games"]
}


# print(my_dict["name"])
# print age, address, hobbies
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["address"])
print(my_dict["hobbies"])


# "My hobby is ____"
print(f'  My hobby is {my_dict["hobbies"][0] } ')
print(f'  My hobby is {my_dict["hobbies"][1] } ')
print(f'  My hobby is {my_dict["hobbies"][2] } ')
print(f'  My hobby is {my_dict["hobbies"][3] } ')


# print out read
print(my_dict['hobbies'][0][0:4])

# print out movies
print(my_dict['hobbies'][0][0:4])

# print out hiking
print(my_dict['hobbies'][2][3:])

# print out playing game
print(my_dict['hobbies'][3][0:12])