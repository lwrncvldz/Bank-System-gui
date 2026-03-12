#!/usr/bin/env python
"""Quick test to verify desktop GUI loads without errors"""
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
sys.path.insert(0, script_dir)

print("Testing desktop GUI imports...")
try:
    from gui import BankGUI, get_or_create_admin_password
    print("✓ Desktop GUI imports successful")
    
    # Test admin password
    password = get_or_create_admin_password()
    print(f"✓ Admin password: {password}")
    
    print("\n✅ Desktop GUI is ready to run!")
    print("Run: python main.py")
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
