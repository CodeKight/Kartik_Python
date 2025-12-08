# a = 10
# b = 5
# print(type(a))
# print(a.__add__(b))

# x = "abc"
# y = "xyz"
# print(x.__add__(y))

# polymorphism: poly - multiple, morph- form: takes multiple form depending on the objects
class Dog:
   def sound(self):
      print("Woof!")

class Cat:
   def sound(self):
      print("Mew!")

class Cow(Cat):
   def sound(self):
      print("Moo")


d1 = Dog()
c1 = Cat()
cow1 = Cow()

d1.sound()
c1.sound()
cow1.sound()