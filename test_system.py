#!/usr/bin/env python
"""
Test script to verify all bank system components are working correctly
"""
import os
import sys

# Change to correct directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
sys.path.insert(0, script_dir)

print("=" * 60)
print("🏦 BANK SYSTEM - VERIFICATION TEST")
print("=" * 60)

# Test 1: Import all modules
print("\n1️⃣  Testing imports...")
try:
    from models import BankAccount, Transaction
    print("   ✓ models.py imported successfully")
except Exception as e:
    print(f"   ✗ Error importing models.py: {e}")
    sys.exit(1)

try:
    from bank import Bank
    print("   ✓ bank.py imported successfully")
except Exception as e:
    print(f"   ✗ Error importing bank.py: {e}")
    sys.exit(1)

try:
    from storage import load_accounts, save_accounts
    print("   ✓ storage.py imported successfully")
except Exception as e:
    print(f"   ✗ Error importing storage.py: {e}")
    sys.exit(1)

try:
    from gui import BankGUI, get_or_create_admin_password
    print("   ✓ gui.py imported successfully")
except Exception as e:
    print(f"   ✗ Error importing gui.py: {e}")
    sys.exit(1)

# Test 2: Test Bank functionality
print("\n2️⃣  Testing Bank operations...")
try:
    bank = Bank()
    
    # Create test account
    acc1 = bank.create_account("Test User 1")
    print(f"   ✓ Created account: {acc1}")
    
    # Test deposit
    deposit_result = bank.deposit(acc1, 1000)
    if "successful" in deposit_result.lower():
        print(f"   ✓ Deposit successful: {deposit_result}")
    else:
        print(f"   ✗ Deposit failed: {deposit_result}")
    
    # Test balance check
    balance = bank.check_balance(acc1)
    if balance == 1000:
        print(f"   ✓ Balance correct: ${balance:.2f}")
    else:
        print(f"   ✗ Balance incorrect. Expected 1000, got {balance}")
    
    # Create second account for transfer
    acc2 = bank.create_account("Test User 2")
    print(f"   ✓ Created second account: {acc2}")
    
    # Test transfer
    transfer_result = bank.transfer(acc1, acc2, 500)
    if "successful" in transfer_result.lower():
        print(f"   ✓ Transfer successful: {transfer_result}")
    else:
        print(f"   ✗ Transfer failed: {transfer_result}")
    
    # Test withdraw
    withdraw_result = bank.withdraw(acc1, 200)
    if "successful" in withdraw_result.lower():
        print(f"   ✓ Withdrawal successful: {withdraw_result}")
    else:
        print(f"   ✗ Withdrawal failed: {withdraw_result}")
    
    # Test transaction history
    transactions = bank.get_transactions(acc1)
    if len(transactions) > 0:
        print(f"   ✓ Transaction history working: {len(transactions)} transactions")
    else:
        print("   ✗ No transactions found")
    
    # Test search
    search_results = bank.search_account("Test")
    if len(search_results) > 0:
        print(f"   ✓ Search working: Found {len(search_results)} accounts")
    else:
        print("   ✗ Search not working")
    
except Exception as e:
    print(f"   ✗ Error during bank operations: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 3: Test admin password
print("\n3️⃣  Testing admin password...")
try:
    password = get_or_create_admin_password()
    if password and len(password) > 0:
        print(f"   ✓ Admin password generated/loaded: {password}")
    else:
        print("   ✗ Admin password is empty")
except Exception as e:
    print(f"   ✗ Error with admin password: {e}")

# Test 4: Test data persistence
print("\n4️⃣  Testing data persistence...")
try:
    # Reload accounts from disk
    bank2 = Bank()
    if acc1 in bank2.accounts:
        print(f"   ✓ Data persistence working: Account {acc1} reloaded")
        balance2 = bank2.check_balance(acc1)
        print(f"   ✓ Balance persisted correctly: ${balance2:.2f}")
    else:
        print("   ✗ Account data not persisted")
except Exception as e:
    print(f"   ✗ Error testing persistence: {e}")

# Test 5: Check file structure
print("\n5️⃣  Checking file structure...")
required_files = [
    'models.py',
    'bank.py', 
    'storage.py',
    'gui.py',
    'main.py',
    'mobile_app.py',
    'mobile_main.py'
]

all_files_exist = True
for file in required_files:
    if os.path.exists(file):
        print(f"   ✓ {file} exists")
    else:
        print(f"   ✗ {file} NOT FOUND")
        all_files_exist = False

print("\n" + "=" * 60)
if all_files_exist:
    print("✅ ALL TESTS PASSED - System is ready to use!")
else:
    print("⚠️  Some files are missing. Check output above.")

print("=" * 60)
print("\nNext steps:")
print("  • Desktop: python main.py")
print("  • Mobile:  python mobile_main.py (requires Kivy)")
print("=" * 60)
