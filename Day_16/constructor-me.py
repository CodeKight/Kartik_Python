#Constructor: 

class Student: 
 
    
    def __init__(self, name, roll, address, contact):
      self.name=name
      self.roll=roll
      self.address=address
      self.contact=contact
      
    def show_info(self):
        print("Name: ", self.name)
        print("Roll: ", self.roll)
        print("Address: ", self.address)
        print("Contact: ", self.contact)
        
        
name=input("Enter your name")
roll=int(input("Enter your roll"))
address=input("Enter your address")
contact=int(input("Enter your contact"))
s1= Student(name, roll, address, contact)
s1.show_info()

print("\n",s1.name)
print(s1.roll)
print(s1.address)
print(s1.contact)
        


#Four pillers of Object Orientied Programming

# Inheritence
# Polymorphism
# Encapsulation
# Abstraction


#Inheritence: a child class can be used 

class Car:
    def __init__(self, brand, color):
        self.brand=brand
        self.color=color
    
    def show_info(slef):
        print(f""" Brand: {self.brand}
Color: {self.color}""")
        

class  EV(Car):
    def show(self):
        print

        
    