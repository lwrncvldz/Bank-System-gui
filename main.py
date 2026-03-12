from gui import BankGUI, get_or_create_admin_password
import os

def main():
    # Change to the correct directory with the bank files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Get and display admin password
    admin_password = get_or_create_admin_password()
    print("=" * 50)
    print("🏦 PROFESSIONAL BANK SYSTEM")
    print("=" * 50)
    print(f"\n⚠️  ADMIN PASSWORD: {admin_password}")
    print("\n📋 Keep this password safe!")
    print("(Saved in: admin_password.txt)\n")
    print("=" * 50 + "\n")
    
    app = BankGUI()
    app.mainloop()

if __name__ == "__main__":
    main()