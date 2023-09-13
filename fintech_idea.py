
```python
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def execute(self):
        if self.sender.get_balance() >= self.amount:
            self.sender.withdraw(self.amount)
            self.receiver.deposit(self.amount)
            print("Transaction successful")
        else:
            print("Transaction failed: Insufficient funds")

# Usage
account1 = Account("1234567890", 1000)
account2 = Account("9876543210", 500)

transaction = Transaction(account1, account2, 200)
transaction.execute()

print("Account 1 balance:", account1.get_balance())
print("Account 2 balance:", account2.get_balance())
```

This code represents a basic implementation of bank account transactions in a fintech application. It includes two classes: `Account` for managing account balances and performing deposit/withdraw operations, and `Transaction` for executing transfers between accounts.

The `Account` class has an account number and balance as attributes. It provides methods to deposit into and withdraw from the account, as well as to retrieve the current balance.

The `Transaction` class takes a sender account, receiver account, and transaction amount as parameters in its constructor. The `execute` method checks if the sender has sufficient funds and performs the transaction by withdrawing from the sender's account and depositing into the receiver's account.

Finally, the code demonstrates a sample usage by creating two accounts, initiating a transaction between them, and printing the updated balances for verification.
