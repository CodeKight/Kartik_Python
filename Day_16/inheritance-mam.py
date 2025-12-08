# Four pillors of Object Oriented Programming
# Inheritance
# Polymorphism
# Encapsulation
# Abstraction

# Inheritance: a child class can use the attributes and methods defined in the parent class in case they are not present in the child class itself
# new attributes and methods can be defined in child class
# if we define the methods with same name in both parent and child class the method is override
# Types of inheritance
class Car:
   def __init__(self, brand, color):
      self.brand = brand
      self.color = color
   
   def show(self):
      print(f"""BRAND: {self.brand}
COLOR: {self.color}""")

# c1 = Car("ABC","Black")
# c1.show()

class EV(Car):
   speed = None
   
   def get_speed(self, speed):
      self.speed = speed
      
   def show(self):
      print(f"""BRAND: {self.brand}
COLOR: {self.color}
SPEED: {self.speed}""")

ev1 = EV("EV","White")
ev1.get_speed("200/h")
ev1.show()


# create a class named Animal
# define different attributes like (leg, eye, ear, tail, ...)
# define method to get the data and a method to print out the animal detail
# create classes Dog and cat that inherits Animal class. define a method named sound, and override the detail method