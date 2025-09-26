class User:

    def __init__(self, name):
        self.name = name
        self.balance = 0


    def make_Deposit(self, amount):
        self.balance = self.balance + amount
        print(f"deposited ${amount} to {self.name}'s account")
        
    
    def make_withdrawal(self, amount):
        self.balance = self.balance -amount
        print(f"withdrowal ${amount} from {self.name}'s account")
   

    def display_balance(self):
        print(f"User: {self.name},Balance : {self.balance}" )
       



user1 = User("Malek")
user2 = User("Ahmad")
user3 = User("batata")

user1.make_Deposit(300)
user1.make_Deposit(100)
user1.make_Deposit(2000)
user1.make_withdrawal(500)
user1.display_balance()

user2.make_Deposit(500)
user2.make_Deposit(400)
user2.make_withdrawal(200)
user2.make_withdrawal(100)
user2.display_balance()

user3.make_Deposit(1000)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.display_balance()















