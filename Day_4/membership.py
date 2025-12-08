#Membership operator: Used to check if a value or data exists in a sequential datatype(string and group datatype)
#Outpu in boolean


#in : if a data or value exists in a sequential datatype , Output: True otherwise False

seq= "membership"

print('m' in seq)
print('z' in seq)

my_list=['membership','operatiod','used',15]
print('membership' in my_list)
print(15 in my_list)


#not in: if a data or valur exists in sequence datatype, Output: False, other wiese TRue 

print('\n','membership' not in my_list)
print(15 not in my_list)