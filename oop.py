#Object-Oriented Programming (OOP)
#Basic: Create a class called Car with attributes brand and color.
# Instantiate an object of the Car class and print its attributes.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
details = Car('Wagon', 'white')
print(details.brand)
print(details.color)
#Intermediate: Add a method called start_engine to the Car class that 
# prints a message saying the engine of the car has started. Create an instance of Car and call the method.
class Car:
    def __init__(self ,color,brand):
        self.color=color
        self.brand=brand
    def start_engine(self):
        print(f" the engine of the car has started{self.color}")
        
    
 
#Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
#Deposit an amount.
#Withdraw an amount (only if sufficient balance exists).
#Print the account balance.
class BankAcoount:
      def  __init__(self, account_number,balance=0):
          self.account_number=account_number
          self.balance=balance
        
      def deposit(self, amount): #deposit an amount into the account
          if amount>0:
              self.balance +=amount
              print(f" deposit{amount}.current balance:{self.balance}")
          else:
              print("deposit amount must be positive.")
      def withdraw(self,amount):
          if amount>0:
              if self.balance>=amount:
                  self.balance-=amount
                  print(f"withdrew{amount}.current balance:{self.balance}")
              else:
                  print("insuffient balance.")
          else:
               print("withdraw amount must be positive")
      def print_balance(self):
          print(f"account{self.account_number} balance:{self.balance}")
account=BankAcoount('12345', 100000)
account.deposit(50000)

account.withdraw(20000)
            
                  
                      
            
          
           
# Challenge: Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. The Library class should have methods to:
#Add a book to the library.
#Remove a book from the library.
#Check if a book is available by title.
#Borrow a book (mark it as unavailable if it’s available).
#Return a book (mark it as available again if it was borrowed).
