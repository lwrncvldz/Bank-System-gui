from models import BankAccount, Transaction
import json
import os

FILENAME = "bank_db.json"

def load_accounts():
    """Load accounts from JSON file"""
    accounts = {}
    
    try:
        if os.path.exists(FILENAME):
            with open(FILENAME, 'r') as file:
                data = json.load(file)
                
                for acc_no, account_data in data.items():
                    account = BankAccount(
                        account_data["name"],
                        float(account_data["balance"]),
                        acc_no
                    )
                    
                    # Load transactions
                    for trans_data in account_data.get("transactions", []):
                        transaction = Transaction(
                            trans_data["type"],
                            trans_data["amount"],
                            trans_data.get("description", ""),
                            trans_data.get("balance_after", 0),
                            trans_data.get("timestamp")
                        )
                        account.transactions.append(transaction)
                    
                    accounts[acc_no] = account
    
    except Exception as e:
        print(f"Error loading accounts: {e}")
    
    return accounts

def save_accounts(accounts):
    """Save accounts to JSON file"""
    data = {}
    
    for acc_no, account in accounts.items():
        data[acc_no] = {
            "name": account.name,
            "balance": account.balance,
            "transactions": [
                {
                    "id": trans.id,
                    "type": trans.type,
                    "amount": trans.amount,
                    "description": trans.description,
                    "balance_after": trans.balance_after,
                    "timestamp": trans.timestamp
                }
                for trans in account.transactions
            ]
        }
    
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=2)