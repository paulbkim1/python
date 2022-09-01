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

account1 = BankAccount(0.2, 200)
account2 = BankAccount(0.3, 500)
# account1.deposit(200).deposit(300).deposit(400).withdraw(300).yield_interest()

account1.deposit(100)
account1.deposit(200)
account1.deposit(300)
account1.withdraw(300)
account1.yield_interest()
account1.display_account_info()

account2.deposit(100)
account2.deposit(200)
account2.withdraw(300)
account2.withdraw(300)
account2.withdraw(300)
account2.withdraw(300)
account2.yield_interest()
account2.display_account_info()