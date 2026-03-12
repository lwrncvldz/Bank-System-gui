# Mobile App Quick Start Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager

## Installation (5 minutes)

### 1. Install Required Packages
```bash
pip install -r requirements.txt
```

This installs:
- `kivy` - Mobile app framework
- `buildozer` - Android/iOS build tool (optional)
- `cython` - Performance optimization

### 2. Run the Mobile App
```bash
python mobile_app.py
```

A window will open showing the mobile banking app interface.

## Key Features Explained

### 1. Create Account 🏠
- Enter your full name
- System generates unique account number automatically
- Account is created instantly with $0 balance

### 2. Deposit Money 💰
- Enter your account number and amount
- Money is added to your account balance
- Transaction is recorded in history

### 3. Withdraw Money 💸
- Enter your account number and amount
- System checks if you have enough balance
- Transaction is denied if balance is insufficient

### 4. Check Balance 📊
- Enter your account number
- See your current balance immediately
- Shows account holder name

### 5. Transfer Money 💲
- Enter sender's account number
- Enter recipient's account number
- Enter transfer amount
- Both accounts are updated automatically

### 6. Transaction History 📜
- View all transactions for an account
- See transaction type (deposit, withdraw, transfer)
- Shows balance after each transaction
- Timestamp included for reference

### 7. Search Account 🔍
- Search by account number or name
- See matching accounts with balances
- Useful for finding recipient accounts for transfers

### 8. Admin Dashboard 👨‍💼
- View all accounts in the system
- See total number of accounts
- View total system balance
- Password protected (auto-generated)

## First Time Setup

When you run the app, the admin password will be automatically generated:
1. Password is displayed in console (copy and save it!)
2. Password is saved in `admin_password.txt` file
3. Use this password to access admin dashboard

**Important**: Keep the admin password safe!

## Data Files

After running the app, these files will be created:

```
Simple Bank System/
├── bank_db.json           # All account data and transactions
├── admin_password.txt     # Admin login password
└── mobile_app.py         # The app itself
```

## Testing the App

### Quick Test Scenario:
1. Create Account → Enter "John Doe" → Get account number (e.g., A1B2C3D4)
2. Create Account → Enter "Jane Smith" → Get account number (e.g., E5F6G7H8)
3. Deposit to John → A1B2C3D4 → $1000
4. Withdraw from John → A1B2C3D4 → $200
5. Transfer → From: A1B2C3D4 → To: E5F6G7H8 → $300
6. Check History → A1B2C3D4 → See all transactions
7. Check Admin Dashboard → Password: (from admin_password.txt)

## Mobile App Interface

The app has a phone-like interface:
- **Width**: 400px (mobile width)
- **Height**: 800px (mobile height)
- **Touch-friendly**: Large buttons and text
- **Professional colors**: Blue theme with green accents

## Building for Android Device

After testing on desktop:

```bash
# Install buildozer dependencies (requires Java and Android SDK)
buildozer android debug

# This creates an APK file in bin/
# Transfer the APK to your Android device and install
```

## Building for iPhone/iPad

Requires macOS with Xcode:

```bash
buildozer ios debug
```

## Common Questions

**Q: Can I use the same data on desktop and mobile?**
A: Yes! Both versions use the same `bank_db.json` file.

**Q: How do I reset all data?**
A: Delete `bank_db.json`. New file will be created on next run.

**Q: What if I forgot the admin password?**
A: Delete `admin_password.txt` and restart the app. A new password will be generated.

**Q: Can I change the admin password?**
A: Currently, you need to manually edit `admin_password.txt` and restart.

**Q: How many accounts can the system handle?**
A: Theoretically unlimited! Limited only by your storage.

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'kivy'"
```bash
pip install kivy==2.2.1
```

### Issue: App doesn't start
- Make sure you're in the correct directory
- Check that `bank.py`, `storage.py`, and `models.py` are present
- Try: `python -m pip install --upgrade kivy`

### Issue: Data not saving
- Check that you have write permissions in the folder
- Make sure disk is not full
- Check for error messages in console

### Issue: Admin password not showing
- Check `admin_password.txt` file
- If missing, delete it and restart app
- New password will be generated

## Performance Tips

- Close unnecessary apps for better performance
- For large datasets (1000+ accounts), refresh may take a few seconds
- Mobile devices generally perform better than testing on desktop window

## Next Steps

1. Test all features on desktop
2. Create test accounts and transactions
3. Review data in `bank_db.json`
4. When ready, build for Android/iOS

---

**Happy Banking! 🏦💳**
