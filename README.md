# Professional Bank System - Mobile App

A complete mobile banking application with admin dashboard, built with Python and Kivy framework.

## Features

### User Features
✅ **Create Account** - Generate unique account numbers automatically  
✅ **Deposit Money** - Add funds to your account  
✅ **Withdraw Money** - Withdraw funds (with balance check)  
✅ **Check Balance** - View your current account balance  
✅ **Transfer Money** - Send money to other accounts  
✅ **Transaction History** - View all transactions with timestamps  
✅ **Search Accounts** - Search by account number or name  
✅ **Account Settings** - View system statistics and security info  

### Admin Features
✅ **Admin Dashboard** - View all accounts in a table format  
✅ **Password Protected** - Secure login with auto-generated password  
✅ **Account Overview** - See total accounts and total balance  
✅ **Real-time Updates** - Refresh to see latest data  

## Installation

### Requirements
- Python 3.8+
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

**Desktop Version (Tkinter):**
```bash
python main.py
```

**Mobile Version (Kivy):**
```bash
python mobile_app.py
```

## Usage Guide

### Creating an Account
1. Click "➕ Create Account" from the menu
2. Enter your full name
3. Click "✓ Create"
4. Your unique account number will be generated

### Making a Deposit
1. Click "💰 Deposit Money"
2. Enter your account number
3. Enter the amount to deposit
4. Click "✓ Deposit"

### Withdrawing Money
1. Click "💸 Withdraw Money"
2. Enter your account number
3. Enter the amount to withdraw
4. Click "✓ Withdraw"

### Checking Balance
1. Click "📊 Check Balance"
2. Enter your account number
3. Click "🔍 Check"

### Transferring Money
1. Click "💲 Transfer Money"
2. Enter your account number (from)
3. Enter recipient's account number (to)
4. Enter the amount
5. Click "✓ Transfer"

### Viewing Transaction History
1. Click "📜 Transaction History"
2. Enter your account number
3. Click "📜 Load History"
4. View all your transactions with dates and balance updates

### Searching for Accounts
1. Click "🔍 Search Account"
2. Enter account number or name to search
3. Click "🔍 Search"
4. View matching accounts with balances

### Accessing Admin Dashboard
1. Click "👨‍💼 Admin Dashboard"
2. Enter the admin password (shown when you first run the app)
3. View all accounts and total system balance
4. Click "🔄 Refresh" to update data

## Admin Password

When you first run the application, an admin password will be:
1. Displayed in the console
2. Saved to `admin_password.txt`

**Keep this password safe!** Don't share it with unauthorized users.

## Data Storage

- **Desktop Version**: Uses `bank_db.json` to store all accounts and transactions
- **Mobile Version**: Uses the same data storage as desktop

All data is saved automatically after each transaction.

## File Structure

```
Simple Bank System/
├── models.py           # Bank account and transaction models
├── bank.py            # Bank operations logic
├── storage.py         # Data persistence (JSON)
├── gui.py             # Desktop GUI (Tkinter)
├── mobile_app.py      # Mobile GUI (Kivy)
├── main.py            # Desktop app entry point
├── admin_password.txt # Admin password (auto-generated)
└── bank_db.json       # Account and transaction data
```

## Building for Mobile (Android/iOS)

### For Android:

1. Install Buildozer:
```bash
pip install buildozer cython
```

2. Configure buildozer.spec (create if it doesn't exist):
```bash
buildozer android debug
```

3. Build APK:
```bash
buildozer android debug
```

The APK will be in the `bin/` folder.

### For iOS:
Requires macOS with Xcode. Use similar buildozer commands with `ios` instead of `android`.

## Security Features

🔐 **Password Protected Admin Panel**  
🔐 **Secure Account Storage**  
🔐 **Transaction Logging**  
🔐 **Unique Account Numbers**  

## Technologies Used

- **Python 3.8+** - Core language
- **Kivy 2.2.1** - Mobile cross-platform framework
- **Tkinter** - Desktop GUI
- **JSON** - Data storage format
- **UUID** - Unique account number generation

## Requirements Compatibility

### Kivy Framework
- Works on: Android, iOS, Windows, macOS, Linux
- Responsive touch interface for mobile
- Professional UI with customizable themes

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'kivy'"
**Solution**: Run `pip install -r requirements.txt`

### Issue: "Can't find admin_password.txt"
**Solution**: The file is created automatically on first run. Check the Same directory as the app.

### Issue: "Account not found" error
**Solution**: Make sure you're entering the correct account number. Use the search feature to find your account.

### Issue: Transaction not saving
**Solution**: Make sure you have write permissions to the directory. Check that `bank_db.json` exists.

## Future Enhancements

- 📱 Biometric login (fingerprint/face recognition)
- 📊 Advanced analytics and reports
- 💳 Card management
- 🔔 Push notifications for transactions
- 📈 Investment portfolio tracking
- 🌐 Multi-currency support

## License

Free to use and modify for educational purposes.

## Version

Version 1.0 - March 2026

---

**Created with ❤️ for Mobile Banking**
