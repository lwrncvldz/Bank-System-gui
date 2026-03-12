from models import BankAccount
from storage import load_accounts, save_accounts


class Bank:

    def __init__(self):
        self.accounts = load_accounts()

    def create_account(self, name):
        new_account = BankAccount(name)
        acc_no = new_account.account_number
        self.accounts[acc_no] = new_account
        save_accounts(self.accounts)
        print(f"Account created with number: {acc_no}")
        return acc_no

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            result = self.accounts[acc_no].deposit(amount)
            save_accounts(self.accounts)
            return result
        else:
            return "Account not found"

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts:
            result = self.accounts[acc_no].withdraw(amount)
            save_accounts(self.accounts)
            return result
        else:
            return "Account not found"

    def check_balance(self, acc_no):
        if acc_no in self.accounts:
            return self.accounts[acc_no].balance
        else:
            return None
    
    def transfer(self, from_acc_no, to_acc_no, amount):
        """Transfer money from one account to another"""
        if from_acc_no not in self.accounts:
            return "Sender account not found"
        if to_acc_no not in self.accounts:
            return "Recipient account not found"
        
        from_account = self.accounts[from_acc_no]
        to_account = self.accounts[to_acc_no]
        
        # Check if sender has sufficient balance
        if amount > from_account.balance:
            return "Insufficient balance"
        if amount <= 0:
            return "Invalid amount"
        
        # Perform transfer
        result = from_account.transfer(amount, to_account.account_number, to_account.name)
        if "successful" in result.lower():
            to_account.receive_transfer(amount, from_account.account_number, from_account.name)
            save_accounts(self.accounts)
            return f"Transfer successful: ${amount:.2f} sent to {to_account.name}"
        else:
            return result
    
    def get_transactions(self, acc_no):
        """Get transaction history for an account"""
        if acc_no in self.accounts:
            return self.accounts[acc_no].get_transactions()
        else:
            return []
    
    def search_account(self, search_term):
        """Search accounts by name or account number"""
        results = []
        search_term_lower = search_term.lower()
        
        for acc_no, account in self.accounts.items():
            if (search_term_lower in acc_no.lower() or 
                search_term_lower in account.name.lower()):
                results.append((acc_no, account))
        
        return results
    
    def get_all_accounts(self):
        """Return all accounts"""
        return self.accounts
    
    def get_total_balance(self):
        """Calculate total balance across all accounts"""
        return sum(account.balance for account in self.accounts.values())
    
    def get_account_count(self):
        """Get total number of accounts"""
        return len(self.accounts)