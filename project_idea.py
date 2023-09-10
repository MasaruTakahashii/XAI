
```python
from datetime import datetime

class FinancialData:
    def __init__(self, account_number, transaction_date, transaction_type, amount):
        self.account_number = account_number
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type
        self.amount = amount

class FinancialDataManager:
    def __init__(self):
        self.financial_data = []

    def add_transaction(self, account_number, transaction_type, amount):
        # Generate current timestamp
        transaction_date = datetime.now()

        # Create FinancialData object
        data = FinancialData(account_number, transaction_date, transaction_type, amount)

        # Append the data to the list
        self.financial_data.append(data)

    def get_transactions_by_account(self, account_number):
        # Filter financial data based on account number
        transactions = [data for data in self.financial_data if data.account_number == account_number]

        # Sort transactions by date in descending order
        transactions.sort(key=lambda x: x.transaction_date, reverse=True)

        return transactions

    def get_total_amount_by_account(self, account_number):
        # Filter financial data based on account number
        transactions = [data for data in self.financial_data if data.account_number == account_number]

        # Calculate total amount
        total_amount = sum(transaction.amount for transaction in transactions)

        return total_amount
```

This code defines a FinancialDataManager class that can be used to manage financial transactions. It stores the financial data in a list and provides methods to add transactions, retrieve transactions by account number, and calculate the total amount for a specific account.

Transactions are represented using the FinancialData class, which contains attributes for the account number, transaction date, transaction type, and amount.

The add_transaction method accepts the account number, transaction type, and amount as parameters, and creates a FinancialData object with the current timestamp as the transaction date. It then appends the created object to the financial data list.

The get_transactions_by_account method takes an account number as a parameter and filters the financial data to retrieve transactions associated with that account. It then sorts the transactions by date in descending order and returns the result.

The get_total_amount_by_account method also takes an account number as a parameter and filters the financial data to retrieve transactions associated with that account. It then calculates the total amount by summing up the amounts of all transactions and returns the result.

This code can be a starting point for implementing a more comprehensive financial management system in a fintech startup.
