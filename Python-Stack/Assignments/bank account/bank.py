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
        
        
        
account1 = BankAcount("0, 0.02")
account2 = BankAcount("100, 0.05")

account1.deposit(200).deposit(1523).deposit(8989).withdraw(1975).display_account_info()
account2.deposit(200).deposit(3434).withdraw(100).withdraw(100).withdraw(2244).withdraw(345).display_account_info()