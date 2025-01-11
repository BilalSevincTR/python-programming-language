"""
** Define a class called BankAccount.
** Each object created should have an attribute named "accountHolder".
   BankAccount("Bilal Sevinc")
** Each object created should have an attribute named "balance" that starts at 0.0.
** Each object created should have a "deposit" method that accepts an amount to deposit and adds it to the balance,
   then returns the updated balance.
** Each object created should have a "withdraw" method that accepts an amount to withdraw and subtracts it from the balance,
   then returns the updated balance.

    account = BankAccount("Bilal Sevinc")
    account.accountHolder => Bilal Sevinc
    account.balance => 0.0
    account.deposit(1000) => 1000.0
    account.withdraw(500) => 500.0
"""

class BankAccount:
    def __init__(self, accountHolder):
        self.accountHolder = accountHolder
        self.balance = 0.0

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
account = BankAccount("Bilal Sevinc")
account.deposit(1000)
print(account.get_balance())
account.withdraw(500)
print(account.get_balance())
account.withdraw(200)
print(account.get_balance())

# Output:

"""

1000.0
500.0
300.0

"""