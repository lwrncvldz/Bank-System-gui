import uuid
from datetime import datetime

class Transaction:
    """Represents a single transaction"""
    def __init__(self, transaction_type, amount, description="", balance_after=0, timestamp=None):
        self.id = str(uuid.uuid4())[:8]
        self.type = transaction_type  # "deposit", "withdraw", "transfer_out", "transfer_in"
        self.amount = float(amount)
        self.description = description
        self.balance_after = float(balance_after)
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __repr__(self):
        return f"Transaction({self.type}, ${self.amount}, {self.timestamp})"

class BankAccount:
    
    def __init__(self, name, balance=0, account_number=None):
        self.account_number = account_number if account_number else str(uuid.uuid4())[:8].upper()
        self.name = name
        self.balance = float(balance)
        self.transactions = []  # List of Transaction objects
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = Transaction("deposit", amount, "Deposit", self.balance)
            self.transactions.append(transaction)
            return "Deposit successful"
        return "Invalid amount"
        
    def withdraw(self, amount):
        if amount > self.balance:
            return "Low balance"
        elif amount <= 0:
            return "Invalid amount"
        else:
            self.balance -= amount
            transaction = Transaction("withdraw", amount, "Withdrawal", self.balance)
            self.transactions.append(transaction)
            return "Withdrawal successful"
    
    def transfer(self, amount, recipient_account_number, recipient_name):
        """Transfer money to another account"""
        if amount > self.balance:
            return "Low balance"
        elif amount <= 0:
            return "Invalid amount"
        else:
            self.balance -= amount
            transaction = Transaction("transfer_out", amount, f"Transfer to {recipient_name} ({recipient_account_number})", self.balance)
            self.transactions.append(transaction)
            return "Transfer successful"
    
    def receive_transfer(self, amount, sender_account_number, sender_name):
        """Receive a transfer from another account"""
        self.balance += amount
        transaction = Transaction("transfer_in", amount, f"Transfer from {sender_name} ({sender_account_number})", self.balance)
        self.transactions.append(transaction)
        
    def get_balance(self):
        return self.balance
    
    def get_transactions(self):
        """Return all transactions for this account"""
        return sorted(self.transactions, key=lambda x: x.timestamp, reverse=True)
    
    def display(self):
        print(f"Account: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")