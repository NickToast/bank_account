#New BankAccount class
class BankAccount:
    bank_accounts_info = []
    #BankAccount should have a balance: when instance is created, if an amount is given, the balanced of the account should initially be set to that amount; otherwise start at $0
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.bank_accounts_info.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self
    
    def display_account_info(self):
        print("===================")
        print(f"Balance: ${self.balance}")
        print("===================")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = round(self.balance + (self.balance * self.int_rate), 2)
            return self

    @classmethod
    def all_balances(cls):
        for account in cls.bank_accounts_info:
            print(BankAccount.bank_accounts_info)
            # print(f"Bank Accounts Interest Rate: {cls.bank_accounts_info[0][cls.int_rate]}")
            # print(f"Bank Account Balance: ${cls.bank_accounts_info[1][cls.balance]}")
            #Not too sure how to do this part come back to it later

user1 = BankAccount(0.08, 500)
user2 = BankAccount(0.05, 100)
# user1.display_account_info()

user1.deposit(123.45).deposit(543.21).deposit(100.00).withdraw(100.00).yield_interest().display_account_info()

user2.deposit(500.00).deposit(250.00).withdraw(50.00).withdraw(75.00).withdraw(145.50).withdraw(50.69).yield_interest().display_account_info()

#Bonus: Use a classmethod to print all instances of a Bank Account's info
# BankAccount.bank_accounts_info
BankAccount.all_balances()
