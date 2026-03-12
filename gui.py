import tkinter as tk
from tkinter import ttk, messagebox
from bank import Bank
import secrets
import string

# --- Admin Password Management ---
ADMIN_PASSWORD_FILE = "admin_password.txt"

def generate_admin_password():
    """Generate a secure random password"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(characters) for _ in range(12))

def get_or_create_admin_password():
    """Get existing password or create a new one"""
    try:
        with open(ADMIN_PASSWORD_FILE, 'r') as f:
            password = f.read().strip()
            if password:
                return password
    except FileNotFoundError:
        pass
    
    # Generate new password
    password = generate_admin_password()
    with open(ADMIN_PASSWORD_FILE, 'w') as f:
        f.write(password)
    
    return password

# --- Custom Style Configuration ---
def configure_styles():
    style = ttk.Style()
    
    # Define color palette
    PRIMARY_COLOR = "#1E5F96"      # Professional blue
    SECONDARY_COLOR = "#2D7CAE"    # Lighter blue
    ACCENT_COLOR = "#27AE60"       # Green for success
    DANGER_COLOR = "#E74C3C"        # Red for errors
    BG_COLOR = "#F5F7FA"           # Light gray background
    TEXT_COLOR = "#2C3E50"         # Dark gray text
    
    style.theme_use('clam')
    
    # Configure label styles
    style.configure('Title.TLabel', font=("Segoe UI", 20, "bold"), foreground=PRIMARY_COLOR)
    style.configure('Heading.TLabel', font=("Segoe UI", 14, "bold"), foreground=PRIMARY_COLOR)
    style.configure('Normal.TLabel', font=("Segoe UI", 10), foreground=TEXT_COLOR)
    style.configure('Success.TLabel', font=("Segoe UI", 10), foreground=ACCENT_COLOR)
    style.configure('Error.TLabel', font=("Segoe UI", 10), foreground=DANGER_COLOR)
    
    # Configure button styles
    style.configure('TButton', font=("Segoe UI", 10))
    style.map('TButton',
        foreground=[('active', '#FFFFFF')],
        background=[('active', SECONDARY_COLOR)])
    
    style.configure('Primary.TButton', font=("Segoe UI", 11, "bold"))
    style.map('Primary.TButton',
        background=[('active', SECONDARY_COLOR)])
    
    style.configure('Secondary.TButton', font=("Segoe UI", 10))
    
    # Configure entry styles
    style.configure('TEntry', font=("Segoe UI", 10), padding=5)
    
    # Frame styles
    style.configure('Main.TFrame', background=BG_COLOR)
    style.configure('Header.TFrame', background=PRIMARY_COLOR)
    style.configure('Card.TFrame', background="white", relief="flat")
    
    return style, PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, DANGER_COLOR, BG_COLOR, TEXT_COLOR


# --- Base Frame for common padding and responsive layout ---
class BaseFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.controller = controller
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Create header
        self.create_header()
    
    def create_header(self):
        header_frame = ttk.Frame(self, style='Header.TFrame', height=60)
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        header_frame.grid_columnconfigure(0, weight=1)
        
        title = ttk.Label(header_frame, text="🏦 PROFESSIONAL BANK SYSTEM", font=("Segoe UI", 16, "bold"), foreground="white", background="#1E5F96")
        title.grid(row=0, column=0, sticky="w", padx=20, pady=15)


# --- Main GUI ---
class BankGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bank = Bank()
        
        # Get or create admin password
        self.admin_password = get_or_create_admin_password()
        
        # Configure styles
        self.style, self.PRIMARY_COLOR, self.SECONDARY_COLOR, self.ACCENT_COLOR, self.DANGER_COLOR, self.BG_COLOR, self.TEXT_COLOR = configure_styles()
        
        self.title("Professional Bank System")
        self.geometry("800x700")
        self.minsize(700, 650)
        self.configure(bg="#F5F7FA")

        # Configure root grid for responsiveness
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Container to hold all frames
        container = ttk.Frame(self, style='Main.TFrame')
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize frames
        self.frames = {}
        for F in (MenuFrame, CreateAccountFrame, DepositFrame, WithdrawFrame, CheckBalanceFrame, AdminLoginFrame, AdminFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MenuFrame)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


# --- Menu Frame ---
class MenuFrame(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Content frame
        content_frame = ttk.Frame(self, style='Main.TFrame')
        content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Welcome message
        welcome_label = ttk.Label(content_frame, text="Welcome to Your Banking Hub", style='Heading.TLabel')
        welcome_label.grid(row=0, column=0, sticky="w", pady=(20, 10))
        
        subtitle = ttk.Label(content_frame, text="Select an operation below to get started", style='Normal.TLabel')
        subtitle.grid(row=1, column=0, sticky="w", pady=(0, 30))

        # Menu buttons in a nice grid
        buttons = [
            ("➕ Create Account", CreateAccountFrame),
            ("💰 Deposit Money", DepositFrame),
            ("💸 Withdraw Money", WithdrawFrame),
            ("📊 Check Balance", CheckBalanceFrame),
            ("👨‍💼 Admin Dashboard", AdminLoginFrame)
        ]

        for i, (text, frame) in enumerate(buttons):
            btn = ttk.Button(content_frame, text=text, command=lambda f=frame: controller.show_frame(f), style='Primary.TButton')
            btn.grid(row=i+2, column=0, sticky="ew", pady=12)

        self.grid_columnconfigure(0, weight=1)


# --- Create Account Frame ---
class CreateAccountFrame(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Content frame with padding
        content_frame = ttk.Frame(self, style='Main.TFrame')
        content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=30)
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title = ttk.Label(content_frame, text="Create New Account", style='Heading.TLabel')
        title.grid(row=0, column=0, sticky="w", pady=(0, 20))
        
        # Form container (card-like)
        form_frame = ttk.Frame(content_frame, style='Card.TFrame')
        form_frame.grid(row=1, column=0, sticky="ew", padx=0, pady=10)
        form_frame.grid_columnconfigure(1, weight=1)
        
        # Name input
        ttk.Label(form_frame, text="Full Name", style='Normal.TLabel').grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))
        self.entry_name = ttk.Entry(form_frame, width=30)
        self.entry_name.grid(row=1, column=0, columnspan=2, sticky="ew", padx=15, pady=(0, 15))
        self.entry_name.focus()
        
        # Result messages
        self.result_label = ttk.Label(content_frame, text="", style='Success.TLabel')
        self.result_label.grid(row=2, column=0, sticky="w", pady=10)

        self.account_number_label = ttk.Label(content_frame, text="", font=("Segoe UI", 11, "bold"), foreground="#1E5F96")
        self.account_number_label.grid(row=3, column=0, sticky="w", pady=(5, 20))

        # Button frame
        button_frame = ttk.Frame(content_frame, style='Main.TFrame')
        button_frame.grid(row=4, column=0, sticky="ew", pady=10)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # Buttons
        ttk.Button(button_frame, text="✓ Create Account", command=self.create_account, style='Primary.TButton').grid(row=0, column=0, sticky="ew", padx=(0, 5))
        ttk.Button(button_frame, text="← Back to Menu", command=lambda: controller.show_frame(MenuFrame), style='Secondary.TButton').grid(row=0, column=1, sticky="ew", padx=(5, 0))

    def create_account(self):
        name = self.entry_name.get().strip()
        if name:
            acc_no = self.controller.bank.create_account(name)
            self.result_label.config(text="✓ Account created successfully!", style='Success.TLabel')
            self.account_number_label.config(text=f"Account Number: {acc_no}")
            self.entry_name.delete(0, tk.END)
            self.entry_name.focus()
        else:
            self.result_label.config(text="✗ Please enter your full name", style='Error.TLabel')
            self.account_number_label.config(text="")


# --- Deposit Frame ---
class DepositFrame(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Content frame with padding
        content_frame = ttk.Frame(self, style='Main.TFrame')
        content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=30)
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title = ttk.Label(content_frame, text="Deposit Money", style='Heading.TLabel')
        title.grid(row=0, column=0, sticky="w", pady=(0, 20))
        
        # Form container (card-like)
        form_frame = ttk.Frame(content_frame, style='Card.TFrame')
        form_frame.grid(row=1, column=0, sticky="ew", padx=0, pady=10)
        form_frame.grid_columnconfigure(1, weight=1)
        
        # Account number input
        ttk.Label(form_frame, text="Account Number", style='Normal.TLabel').grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))
        self.entry_acc = ttk.Entry(form_frame, width=30)
        self.entry_acc.grid(row=1, column=0, columnspan=2, sticky="ew", padx=15, pady=(0, 15))
        self.entry_acc.focus()
        
        # Amount input
        ttk.Label(form_frame, text="Amount ($)", style='Normal.TLabel').grid(row=2, column=0, sticky="w", padx=15, pady=(15, 5))
        self.entry_amount = ttk.Entry(form_frame, width=30)
        self.entry_amount.grid(row=3, column=0, columnspan=2, sticky="ew", padx=15, pady=(0, 15))
        
        # Result message
        self.result_label = ttk.Label(content_frame, text="", style='Success.TLabel')
        self.result_label.grid(row=2, column=0, sticky="w", pady=10)

        # Button frame
        button_frame = ttk.Frame(content_frame, style='Main.TFrame')
        button_frame.grid(row=3, column=0, sticky="ew", pady=10)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # Buttons
        ttk.Button(button_frame, text="✓ Deposit", command=self.deposit, style='Primary.TButton').grid(row=0, column=0, sticky="ew", padx=(0, 5))
        ttk.Button(button_frame, text="← Back to Menu", command=lambda: controller.show_frame(MenuFrame), style='Secondary.TButton').grid(row=0, column=1, sticky="ew", padx=(5, 0))

    def deposit(self):
        acc = self.entry_acc.get().strip()
        try:
            amount = float(self.entry_amount.get())
            if amount <= 0:
                self.result_label.config(text="✗ Amount must be greater than 0", style='Error.TLabel')
                return
        except ValueError:
            self.result_label.config(text="✗ Please enter a valid amount", style='Error.TLabel')
            return
        self.controller.bank.deposit(acc, amount)
        self.result_label.config(text=f"✓ Successfully deposited ${amount:.2f}", style='Success.TLabel')
        self.entry_acc.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)
        self.entry_acc.focus()


# --- Withdraw Frame ---
class WithdrawFrame(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Content frame with padding
        content_frame = ttk.Frame(self, style='Main.TFrame')
        content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=30)
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title = ttk.Label(content_frame, text="Withdraw Money", style='Heading.TLabel')
        title.grid(row=0, column=0, sticky="w", pady=(0, 20))
        
        # Form container (card-like)
        form_frame = ttk.Frame(content_frame, style='Card.TFrame')
        form_frame.grid(row=1, column=0, sticky="ew", padx=0, pady=10)
        form_frame.grid_columnconfigure(1, weight=1)
        
        # Account number input
        ttk.Label(form_frame, text="Account Number", style='Normal.TLabel').grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))
        self.entry_acc = ttk.Entry(form_frame, width=30)
        self.entry_acc.grid(row=1, column=0, columnspan=2, sticky="ew", padx=15, pady=(0, 15))
        self.entry_acc.focus()
        
        # Amount input
        ttk.Label(form_frame, text="Amount ($)", style='Normal.TLabel').grid(row=2, column=0, sticky="w", padx=15, pady=(15, 5))
        self.entry_amount = ttk.Entry(form_frame, width=30)
        self.entry_amount.grid(row=3, column=0, columnspan=2, sticky="ew", padx=15, pady=(0, 15))
        
        # Result message
        self.result_label = ttk.Label(content_frame, text="", style='Success.TLabel')
        self.result_label.grid(row=2, column=0, sticky="w", pady=10)

        # Button frame
        button_frame = ttk.Frame(content_frame, style='Main.TFrame')
        button_frame.grid(row=3, column=0, sticky="ew", pady=10)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # Buttons
        ttk.Button(button_frame, text="✓ Withdraw", command=self.withdraw, style='Primary.TButton').grid(row=0, column=0, sticky="ew", padx=(0, 5))
        ttk.Button(button_frame, text="← Back to Menu", command=lambda: controller.show_frame(MenuFrame), style='Secondary.TButton').grid(row=0, column=1, sticky="ew", padx=(5, 0))

    def withdraw(self):
        acc = self.entry_acc.get().strip()
        try:
            amount = float(self.entry_amount.get())
            if amount <= 0:
                self.result_label.config(text="✗ Amount must be greater than 0", style='Error.TLabel')
                return
        except ValueError:
            self.result_label.config(text="✗ Please enter a valid amount", style='Error.TLabel')
            return
        self.controller.bank.withdraw(acc, amount)
        self.result_label.config(text=f"✓ Successfully withdrawn ${amount:.2f}", style='Success.TLabel')
        self.entry_acc.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)
        self.entry_acc.focus()


# --- Check Balance Frame ---
class CheckBalanceFrame(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Content frame with padding
        content_frame = ttk.Frame(self, style='Main.TFrame')
        content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=30)
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title = ttk.Label(content_frame, text="Check Account Balance", style='Heading.TLabel')
        title.grid(row=0, column=0, sticky="w", pady=(0, 20))
        
        # Form container (card-like)
        form_frame = ttk.Frame(content_frame, style='Card.TFrame')
        form_frame.grid(row=1, column=0, sticky="ew", padx=0, pady=10)
        form_frame.grid_columnconfigure(1, weight=1)
        
        # Account number input
        ttk.Label(form_frame, text="Account Number", style='Normal.TLabel').grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))
        self.entry_acc = ttk.Entry(form_frame, width=30)
        self.entry_acc.grid(row=1, column=0, columnspan=2, sticky="ew", padx=15, pady=(0, 15))
        self.entry_acc.focus()
        
        # Result message
        self.result_label = ttk.Label(content_frame, text="", style='Success.TLabel')
        self.result_label.grid(row=2, column=0, sticky="ew", pady=15)
        
        # Balance display
        self.balance_display = ttk.Label(content_frame, text="", font=("Segoe UI", 16, "bold"), foreground="#27AE60")
        self.balance_display.grid(row=3, column=0, sticky="w", pady=(10, 20))

        # Button frame
        button_frame = ttk.Frame(content_frame, style='Main.TFrame')
        button_frame.grid(row=4, column=0, sticky="ew", pady=10)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # Buttons
        ttk.Button(button_frame, text="🔍 Check Balance", command=self.check_balance, style='Primary.TButton').grid(row=0, column=0, sticky="ew", padx=(0, 5))
        ttk.Button(button_frame, text="← Back to Menu", command=lambda: controller.show_frame(MenuFrame), style='Secondary.TButton').grid(row=0, column=1, sticky="ew", padx=(5, 0))

    def check_balance(self):
        acc = self.entry_acc.get().strip()
        if acc:
            account = self.controller.bank.accounts.get(acc)
            if account:
                self.result_label.config(text=f"✓ Account found: {account.name}", style='Success.TLabel')
                self.balance_display.config(text=f"Balance: ${account.balance:.2f}")
            else:
                self.result_label.config(text="✗ Account number not found", style='Error.TLabel')
                self.balance_display.config(text="")
        else:
            self.result_label.config(text="✗ Please enter an account number", style='Error.TLabel')
            self.balance_display.config(text="")
        self.entry_acc.delete(0, tk.END)
        self.entry_acc.focus()


# --- Admin Login Frame ---
class AdminLoginFrame(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Content frame with padding
        content_frame = ttk.Frame(self, style='Main.TFrame')
        content_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=30)
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title = ttk.Label(content_frame, text="Admin Portal - Authentication Required", style='Heading.TLabel')
        title.grid(row=0, column=0, sticky="w", pady=(0, 30))
        
        # Form container (card-like)
        form_frame = ttk.Frame(content_frame, style='Card.TFrame')
        form_frame.grid(row=1, column=0, sticky="ew", padx=0, pady=10)
        form_frame.grid_columnconfigure(1, weight=1)
        
        # Password label
        ttk.Label(form_frame, text="Admin Password", style='Normal.TLabel').grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))
        
        # Password entry
        self.entry_password = ttk.Entry(form_frame, show="•", width=30)
        self.entry_password.grid(row=1, column=0, columnspan=2, sticky="ew", padx=15, pady=(0, 15))
        self.entry_password.focus()
        
        # Bind Enter key
        self.entry_password.bind('<Return>', lambda e: self.verify_password())
        
        # Result message
        self.result_label = ttk.Label(content_frame, text="", style='Error.TLabel')
        self.result_label.grid(row=2, column=0, sticky="w", pady=10)

        # Button frame
        button_frame = ttk.Frame(content_frame, style='Main.TFrame')
        button_frame.grid(row=3, column=0, sticky="ew", pady=10)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # Buttons
        ttk.Button(button_frame, text="🔓 Login", command=self.verify_password, style='Primary.TButton').grid(row=0, column=0, sticky="ew", padx=(0, 5))
        ttk.Button(button_frame, text="← Back to Menu", command=lambda: controller.show_frame(MenuFrame), style='Secondary.TButton').grid(row=0, column=1, sticky="ew", padx=(5, 0))

    def verify_password(self):
        """Verify the admin password"""
        password = self.entry_password.get()
        
        if password == self.controller.admin_password:
            self.result_label.config(text="", style='Error.TLabel')
            self.entry_password.delete(0, tk.END)
            self.controller.show_frame(AdminFrame)
        else:
            self.result_label.config(text="✗ Incorrect password. Please try again.", style='Error.TLabel')
            self.entry_password.delete(0, tk.END)
            self.entry_password.focus()


# --- Admin Frame ---
class AdminFrame(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Content frame with padding
        content_frame = ttk.Frame(self, style='Main.TFrame')
        content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)
        
        # Title and info
        title_frame = ttk.Frame(content_frame, style='Main.TFrame')
        title_frame.grid(row=0, column=0, sticky="ew", pady=(0, 15))
        ttk.Label(title_frame, text="Admin Dashboard - All Accounts", style='Heading.TLabel').pack(side="left")
        
        self.account_count_label = ttk.Label(title_frame, text="", style='Normal.TLabel')
        self.account_count_label.pack(side="right")
        
        # Create Treeview for displaying accounts
        tree_frame = ttk.Frame(content_frame, style='Card.TFrame')
        tree_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=10)
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Create scrollbars
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        vsb.grid(row=0, column=1, sticky="ns", padx=(0, 5))
        
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        hsb.grid(row=1, column=0, sticky="ew", pady=(0, 5))
        
        # Create Treeview
        self.tree = ttk.Treeview(
            tree_frame,
            columns=("Account Number", "Name", "Balance"),
            height=15,
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set
        )
        
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        # Define column headings and widths
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Account Number", anchor="center", width=150)
        self.tree.column("Name", anchor="w", width=200)
        self.tree.column("Balance", anchor="e", width=120)
        
        self.tree.heading("#0", text="", anchor="w")
        self.tree.heading("Account Number", text="Account Number", anchor="center")
        self.tree.heading("Name", text="Name", anchor="w")
        self.tree.heading("Balance", text="Balance", anchor="e")
        
        # Configure tag colors for alternating rows
        self.tree.tag_configure('oddrow', background='#F5F7FA')
        self.tree.tag_configure('evenrow', background='white')
        
        self.tree.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Button frame
        button_frame = ttk.Frame(content_frame, style='Main.TFrame')
        button_frame.grid(row=2, column=0, sticky="ew", pady=15)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # Buttons
        ttk.Button(button_frame, text="🔄 Refresh Data", command=self.load_accounts_data, style='Primary.TButton').grid(row=0, column=0, sticky="ew", padx=(0, 5))
        ttk.Button(button_frame, text="← Back to Menu", command=lambda: controller.show_frame(MenuFrame), style='Secondary.TButton').grid(row=0, column=1, sticky="ew", padx=(5, 0))
        
        # Load data on initialization
        self.load_accounts_data()
    
    def load_accounts_data(self):
        """Load and display all accounts in the treeview"""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get accounts from bank
        accounts = self.controller.bank.accounts
        
        # Update account count
        self.account_count_label.config(text=f"Total Accounts: {len(accounts)}")
        
        # Add accounts to tree with alternating colors
        total_balance = 0
        for i, (acc_no, account) in enumerate(accounts.items()):
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            values = (acc_no, account.name, f"${account.balance:.2f}")
            self.tree.insert("", "end", values=values, tags=(tag,))
            total_balance += account.balance
        
        # Update the title with total balance info
        if len(accounts) > 0:
            self.account_count_label.config(text=f"Total Accounts: {len(accounts)} | Total Balance: ${total_balance:.2f}")