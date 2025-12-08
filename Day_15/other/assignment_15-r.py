# OOP: Object Oriented Programming

# class : blueprint, stucture
# objects : real world entity, data created using class
# the variables defined inside the class are called attributes
# a class can have multiple objects
# the variable where the class are called, object
# class Car:
#    brand = "Toyota"  # brand, color, seats are attributes
#    color = "White"
#    seats = "5"

# c1 = Car()        # c1 is the object
# print(c1.brand)
# print(c1.color)
# print(c1.seats)

# c2 = Car()
# c2.brand = "ANC"
# c2.speed = "200/hr"
# print(c2.brand)
# print(c2.color)
# print(c2.seats)
# print(c2.speed)

# c3 = Car()
# print(c3.brand)
# print(c3.color)
# print(c3.seats)
# # print(c3.speed)

# print(Car)

# print(type("abc"))

# function defined inside a class is termed method

# class Student:
#    name = None
#    roll_no = None
#    address = None
#    contact = None
   
#    def get_info(self,sname, roll_no, address, contact):
#       self.uname = sname
#       self.roll_no = roll_no
#       self.address = address
#       self.contact = contact
   
#    def show_info(self):
#       print(f"""NAME: {self.uname} 
# ADDRESS: {self.address}
# ROLL NO: {self.roll_no}
# CONTACT: {self.contact}""")

# s1 = Student()
# s1.get_info("Ram","5","KTm","9874563210")
# s1.show_info()

# s2 = Student()
# s2.get_info("Shyam","10","KTm","987dsd4563210")
# s2.show_info()

# s3 = Student()
# s3.get_info("klsjflks","5","KTm","9874563210")
# s3.show_info()





# in above Student class:
# get information from user and show their info
# class student:
#    name = input("Enter your name: ")
#    roll_no = input("Enter your roll_no: ")
#    address = input("Enter your address: ")
#    contact = input("Enter your contact: ")

#    def show_info(self):
#         print(f"""NAME: {self.name} 
# ADDRESS: {self.address}
# ROLL NO: {self.roll_no}
# CONTACT: {self.contact}""")
# s1 = student()
# s1.show_info()
# s2 = Student()
# s2.name = "Shyam"
# s2.roll_no = "5"
# s2.address = "KTM"
# s2.contact = "983473492734"
# print(s2.name)
# print(s2.roll_no)
# print(s2.address)
# print(s2.contact)  





# create a class named Animal
# define different attributes like (leg, eye, ear, tail, ...)
# define method to get the data and a method to print out the animal detail
# class Animal:
#     leg = None
#     eye = None
#     ear = None
#     tail = None
#     horn = None
#     def get_data(self,leg,eye,ear,tail,horn):
#         self.leg = leg
#         self.eye = eye
#         self.ear = ear
#         self.tail = tail
#         self.horn = horn
    
#     def show_detail(self):
#         print(f"""Leg = {self.leg}
# Eye = {self.eye}
# Ear = {self.ear}
# Tail = {self.tail}
# Horn = {self.horn}""")


# s1 = Animal()
# s1.get_data(4,2,2,1,2)
# s1.show_detail()

class Animal:
    name = None
    leg = None
    eye = None
    ear = None
    tail = None
    horn = None
    def get_data(self):
        self.name = input("Enter the name of animal:")
        self.leg = int(input("Enter the number of legs:"))
        self.eye =  int(input("Enter the number of eyes:"))
        self.ear =  int(input("Enter the number of ears:"))
        self.tail =  int(input("Enter the number of tail:"))
        self.horn =  int(input("Enter the number of horn:"))
    
    def show_detail(self):
        print(f"""Name = {self.name}
Leg = {self.leg}
Eye = {self.eye}
Ear = {self.ear}
Tail = {self.tail}
Horn = {self.horn}""")


s1 = Animal()
s1.get_data()
s1.show_detail()



