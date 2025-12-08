#OOP: Object orientied programming. 

#class : blue print, structure
# objects: real world entity, data created using class 



# class Car:
#     brand="Toyota"
#     color="White"
#     seats = "5"
    
# c1=Car()

# print(c1.brand)
# print(c1.color)
# print(c1.seats)


# c2=Car()

# c2.brand="Anc"
# c2.speed="20km/hr"
# print(c2.brand)
# print(c2.color)
# print(c2.seats)
# print(c2.speed)



# c3=Car()


# print(c3.brand)
# print(c3.color)
# print(c3.seats)
# #print(c3.speed)


# print(Car)

# print(type("abc"))



# class Student:
#     name= None
#     roll = None
#     address = None
#     contact = None
    
# s1 = Student()
# s1.name="Ram"
# s1.roll=33
# s1.address="ktm"
# s1.contact=938579347

# print(s1.name)
# print(s1.roll)
# print(s1.address)
# print(s1.contact)
 
 
 
  
# s2 = Student()
# s2.name="Ram"
# s2.roll=33
# s2.address="ktm"
# s2.contact=938579347

# print(s2.name)
# print(s2.roll)
# print(s2.address)
# print(s2.contact)
 
 
#Methods: functions defined inside object --------------------


class Student:
    name= None
    roll = None
    address = None
    contact = None
    
    def get_info(self,name,roll,address,contact):
        self.name=name
        self.roll=roll
        self.address=address
        self.contact=contact
    
    def show_info(self):
        print("Name: ", self.name)
        print("Roll: ", self.roll)
        print("Address: ", self.address)
        print("Contact: ", self.contact)
        


s1 = Student()
s1.get_info("Ram",33,"ktm",348743)
s1.show_info()

s1 = Student()
s1.get_info("Ram",33,"ktm",348743)
s1.show_info()

