# Encapsulation: data hiding concept(disabling the access of attributes and methods through objects), attributes and methods are encapsulated in a single unit,
# '__' double underscore is used infront of attributes and methods to make them private
# to access private attibutes and methods normal/non private methods should defined inside the class


# objects are unable to access the private attributes and methods

class Student:
   def __init__(self,name,roll_no, address,contact):
      self.__name = name
      self.__roll_no = roll_no
      self.address = address
      self.contact = contact
   
   
   def __show_info(self):
      print(f"""NAME: {self.__name} 
ADDRESS: {self.address}
ROLL NO: {self.__roll_no}
CONTACT: {self.contact}""")
   
   def call_met(self):
      self.__show_info()

s1 = Student("Ram","24","KTM","093849823894")
s1.call_met()

# create a class named login.
# the class should have email and password attribute
# the attributes should not be accessable through object
# define a method that print out the user info (email, password)
# create 3 objects

# create a class Bank
# the class should have accountnumber and balance attribute
# the attributes should not be accessable through object
# define a method that print out the user_details (accountnumber, balance)
# create 3 objects