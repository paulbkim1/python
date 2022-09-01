class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
    def display_account_info(self):
        print(f"Balance: {self.balance} int_rate: {self.int_rate}")
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=100)
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawal(self):
        self.account.withdraw()
    def display_user_balance(self):
        self.account.display_account_info()

User.make_deposit(100)
User.display_user_balance()
# person1 = User.a