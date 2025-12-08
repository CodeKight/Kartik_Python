
class Student: 
 
    
    def __init__(self, name, roll, address, contact):
      self.__name=name
      self.__roll=roll
      self.address=address
      self.contact=contact
      
    def __show_info(self):
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Address: ", self.address)
        print("Contact: ", self.contact)
        
    def norMethod(self):
        self.__show_info()
        
        
s1=Student("Ram", 33, "ktm", 3495734)
s1.norMethod()
# print(s1.__name)  CAnnot be accessed bec of incapsulation, its private 
# print(s1.__roll)
        