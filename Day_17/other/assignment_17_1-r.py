# create a class named login.
# the class should have email and password attribute
# the attributes should not be accessable through object
# define a method that print out the user info (email, password)
# create 3 objects
class login:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
    def show_info(self):
        print(f"""Email : {self.__email}
Password : {self.__password}""")

l1 = login('suraj@gmail.com', 'suraj123')
l2 = login('hari@gmail.com', 'hari123')
l3 = login('parbat@gmail.com', 'parbat123')
l1.show_info()
l2.show_info()
l3.show_info()



# create a class Bank
# the class should have accountnumber and balance attribute
# the attributes should not be accessable through object
# define a method that print out the user_details (accountnumber, balance)
# create 3 objects
class Bank:
    def __init__(self, accountnumber, balance):
        self.__accountnumber = accountnumber
        self.__balance = balance
    def user_detail(self):
        print(f"""Accountnumber : {self.__accountnumber}
Balance : {self.__balance}""")

l1 = Bank(145633234555, 1000000)
l2 = Bank(654356753677, 550000)
l3 = Bank(786344444556, 400000)
l1.user_detail()
l2.user_detail()
l3.user_detail()