# Abstraction: data hiding: hiding the unnecessary events from the user and only showing the necessary event

class Bike:
   clutch = False
   brek = False
   acc = False
   
   def start(self):
      clutch = True
      acc = True
      print("Bike started")


b1 = Bike()
b1.start()