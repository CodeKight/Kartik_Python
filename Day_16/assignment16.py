# create a class named Animal
# define different attributes like (leg, eye, ear, tail, ...)
# define method to get the data and a method to print out the animal detail
# create classes Dog and cat that inherits Animal class. define a method named sound, and override the detail method




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
        
        

class Dog(Animal):
    def sound(self):
        print("Bark")
    
    def get_info(self, color):
      self.color=color

    def show_info(self):
        print("Color: ", self.color)
      
        
        
d1=Dog()
d1.get_info("White")
d1.show_info()
d1.sound()  
    
class Cat(Animal):
    def sound(self):
        print("Meow")
        
    def get_info(self, color):
     self.color=color

    def show_info(self):
        print("Color: ", self.color)
      
    


    
c1=Cat()
c1.get_info("Black")
c1.show_info()
c1.sound()
