# in above Student class:
# get information from user and show their info




class Student: 
    name=None
    roll=None
    address=None
    contact=None
    
    def get_info(self, name, roll, address, contact):
      self.name=name
      self.roll=roll
      self.address=address
      self.contact=contact
      
    def show_info(self):
        print("Name: ", self.name)
        print("Name: ", self.roll)
        print("Name: ", self.address)
        print("Name: ", self.contact)
        
        
name=input("Enter your name")
name=int(input("Enter your roll"))
name=input("Enter your address")
name=int(input("Enter your contact"))
s1= Student()
s1.get_info(name, roll, address, contact)
s1.show_info()
        
      
      
      
    
      
# create a class named Animal
# define different attributes like (leg, eye, ear, tail, ...)
# define method to get the data and a method to print out the animal detail


class Animal: 
    leg=None
    eye=None
    ear=None
    tail=None
    def get_info(self, leg, eye, ear, tail):
      self.leg=leg
      self.eye=eye
      self.ear=ear
      self.tail=tail
      
    def show_info(self):
        print("leg: ", self.leg)
        print("eye: ", self.eye)
        print("ear: ", self.ear)
        print("tail: ", self.tail)
        
        
leg=int(input("Enter no. of leg"))
eye=int(input("Enter no. of eye"))
ear=input("Enter no. of ear")
tail=int(input("Enter no. tail"))
s1= Animal()
s1.get_info(leg, eye,ear, tail)
s1.show_info()
        
    