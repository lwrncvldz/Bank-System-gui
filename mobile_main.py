import os
import sys

# Change to the correct directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Add current directory to path
sys.path.insert(0, script_dir)

from mobile_app import BankMobileApp

if __name__ == '__main__':
    BankMobileApp().run()
