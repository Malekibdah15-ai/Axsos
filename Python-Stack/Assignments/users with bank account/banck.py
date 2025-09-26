class BankAcount:
    def __init__(self, balance=0, int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate
        print(f"DEBUG: balance type is {type(self.balance)}") 
        
    def deposit(self, amount):
         self.balance += amount
         print(f"Deposited ${amount}. New balance: ${self.balance}")
         
         return self
         
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"withdrow {amount}. new balance: ${self.balance}")
            
        else:
          print("insufficent funds: charging a $5 fee")
          self.balance -=5
        return self
    
    def display_account_info(self):
        print(f"balance: ${self.balance}")
        
        return self
            
    def yield_interest(self):
        self.balance = self.balance * self.int_rate
        if self.balance > 0:
            print(f"Applied interest. New balance: {self.balance}")
        


class User:

    def __init__(self, name):
        self.name = name
        self.account = BankAcount(int_rate=0.02, balance=0)


    def make_Deposit(self, amount):
        self.account.deposit(amount)
      
        return self
    
    def make_withdrawal(self, amount):
        self.account.deposit(amount)
        
        return self
   

    def display_balance(self):
        print(f"User: {self.name},balance {self.account.balance}" )
       
        return self
    
    
user1 = User("Malek")


user1.make_Deposit(1000).make_Deposit(1000).make_Deposit(1000).make_withdrawal(800).display_balance()