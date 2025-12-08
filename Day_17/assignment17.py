# create a class named login.
# the class should have email and password attribute
# the attributes should not be accessable through object
# define a method that print out the user info (email, password)
# create 3 objects

class Login:
    __email=None
    __password=None
    def info(self, email, password):
      self.__email=email
      self.__password=password
      
    def show_info(self):
        print(self.__email)
        print(self.__password)
        

l1=Login()
l1.info("ram@gmail.com", "ram123")
l1.show_info()

l2=Login()
l2.info("sam@gmail.com", "sam123")
l2.show_info()

l3=Login()
l3.info("hari@gmail.com", "hari123")
l3.show_info()
    

# create a class Bank
# the class should have accountnumber and balance attribute
# the attributes should not be accessable through object
# define a method that print out the user_details (accountnumber, balance)
# create 3 objects


class Bank:
    __accountnumber = None
    __balance = None

    def details(self, accountnumber, balance):
        self.__accountnumber = accountnumber
        self.__balance = balance

    def show_details(self):
        print(self.__accountnumber)
        print(self.__balance)


b1 = Bank()
b1.details("11111", 5000)
b1.show_details()

b2 = Bank()
b2.details("22222", 7500)
b2.show_details()

b3 = Bank()
b3.details("33333", 10000)
b3.show_details()
