#Absbraction: Data hiding the uncecessary events form user and only showing the necessay event 

class Bike:
    clutch = False
    brk = False
    acc = False
    
    def start(self):
      clutch = True
      acc = True
      print("Bike started. ")
    
b1=Bike()
b1.start()