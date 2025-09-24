class User:
    
    def __init__(self, name):
        self.name = name
        self.balance = 0
        
    def make_Deposit(self, amount):
        self.balance = self.balance + amount
        print(f"deposited ${amount} to {self.name}'s account" )
      
        return self
    
    def make_withdrow(self, amount):
        self.balance = self.balance - amount
        print(f"withdrow {amount} from {self.name}'s account")
        
        return self
    def display_balance(self):
        print(f"User: {self.name} balance {self.balance}")
        return self
    
user1 = User("Malek")


user1.make_Deposit(1000).make_Deposit(1000).make_Deposit(1000).make_withdrow(800).display_balance()