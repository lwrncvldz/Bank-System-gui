from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from bank import Bank

# Set window size for mobile (smaller for testing)
Window.size = (400, 800)

class BankMobileApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bank = Bank()
        self.current_account = None
        self.admin_password = self.get_admin_password()
    
    def get_admin_password(self):
        """Get admin password from file"""
        try:
            with open("admin_password.txt", 'r') as f:
                return f.read().strip()
        except:
            return "admin123"
    
    def build(self):
        self.title = "Professional Bank System"
        self.screen_manager = ScreenManager(transition=FadeTransition())
        
        # Add screens
        self.screen_manager.add_widget(MenuScreen(name='menu', app=self))
        self.screen_manager.add_widget(CreateAccountScreen(name='create', app=self))
        self.screen_manager.add_widget(DepositScreen(name='deposit', app=self))
        self.screen_manager.add_widget(WithdrawScreen(name='withdraw', app=self))
        self.screen_manager.add_widget(CheckBalanceScreen(name='balance', app=self))
        self.screen_manager.add_widget(TransferMoneyScreen(name='transfer', app=self))
        self.screen_manager.add_widget(TransactionHistoryScreen(name='history', app=self))
        self.screen_manager.add_widget(SearchAccountScreen(name='search', app=self))
        self.screen_manager.add_widget(AccountSettingsScreen(name='settings', app=self))
        self.screen_manager.add_widget(AdminLoginScreen(name='admin_login', app=self))
        self.screen_manager.add_widget(AdminDashboardScreen(name='admin', app=self))
        
        return self.screen_manager

class MenuScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Header
        header = BoxLayout(size_hint_y=0.15, orientation='vertical')
        header.add_widget(Label(text="🏦 PROFESSIONAL BANK", font_size='24sp', bold=True, color=(0.12, 0.37, 0.58, 1)))
        header.add_widget(Label(text="Mobile Banking System", font_size='14sp', color=(0.44, 0.62, 0.8, 1)))
        layout.add_widget(header)
        
        # Menu buttons
        button_configs = [
            ("➕ Create Account", "create"),
            ("💰 Deposit Money", "deposit"),
            ("💸 Withdraw Money", "withdraw"),
            ("📊 Check Balance", "balance"),
            ("💲 Transfer Money", "transfer"),
            ("📜 Transaction History", "history"),
            ("🔍 Search Account", "search"),
            ("⚙️ Account Settings", "settings"),
            ("👨‍💼 Admin Dashboard", "admin_login"),
        ]
        
        # Create scrollable button area
        scroll = ScrollView(size_hint=(1, 0.85))
        button_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        button_layout.bind(minimum_height=button_layout.setter('height'))
        
        for text, screen in button_configs:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=60,
                background_color=(0.12, 0.37, 0.58, 1),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=lambda x, s=screen: self.go_to_screen(s))
            button_layout.add_widget(btn)
        
        scroll.add_widget(button_layout)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
    
    def go_to_screen(self, screen_name):
        self.manager.current = screen_name

class CreateAccountScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Header
        layout.add_widget(Label(text="Create New Account", size_hint_y=0.1, font_size='20sp', bold=True))
        
        # Form
        form_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.6)
        
        layout.add_widget(Label(text="Full Name", size_hint_y=None, height=30))
        self.name_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.name_input)
        
        self.message = Label(text="", size_hint_y=None, height=40)
        form_layout.add_widget(self.message)
        
        layout.add_widget(form_layout)
        
        # Buttons
        btn_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.2)
        btn_create = Button(text="✓ Create", background_color=(0.15, 0.68, 0.38, 1))
        btn_create.bind(on_press=self.create_account)
        btn_layout.add_widget(btn_create)
        
        btn_back = Button(text="← Back", background_color=(0.75, 0.75, 0.75, 1))
        btn_back.bind(on_press=lambda x: self.go_back())
        btn_layout.add_widget(btn_back)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def create_account(self, instance):
        name = self.name_input.text.strip()
        if name:
            acc_no = self.app.bank.create_account(name)
            self.message.text = f"✓ Account Created!\nNo: {acc_no}"
            self.message.color = (0.15, 0.68, 0.38, 1)
            self.name_input.text = ""
        else:
            self.message.text = "✗ Please enter your name"
            self.message.color = (0.90, 0.30, 0.24, 1)
    
    def go_back(self):
        self.manager.current = 'menu'

class DepositScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Deposit Money", size_hint_y=0.1, font_size='20sp', bold=True))
        
        form_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.6)
        
        layout.add_widget(Label(text="Account Number", size_hint_y=None, height=30))
        self.acc_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.acc_input)
        
        layout.add_widget(Label(text="Amount ($)", size_hint_y=None, height=30))
        self.amount_input = TextInput(multiline=False, size_hint_y=None, height=40, input_filter='float')
        form_layout.add_widget(self.amount_input)
        
        self.message = Label(text="", size_hint_y=None, height=40)
        form_layout.add_widget(self.message)
        
        layout.add_widget(form_layout)
        
        btn_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.2)
        btn_deposit = Button(text="✓ Deposit", background_color=(0.15, 0.68, 0.38, 1))
        btn_deposit.bind(on_press=self.deposit)
        btn_layout.add_widget(btn_deposit)
        
        btn_back = Button(text="← Back", background_color=(0.75, 0.75, 0.75, 1))
        btn_back.bind(on_press=lambda x: self.go_back())
        btn_layout.add_widget(btn_back)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def deposit(self, instance):
        acc = self.acc_input.text.strip()
        try:
            amount = float(self.amount_input.text)
            result = self.app.bank.deposit(acc, amount)
            if "successful" in result.lower():
                self.message.text = f"✓ {result}"
                self.message.color = (0.15, 0.68, 0.38, 1)
                self.acc_input.text = ""
                self.amount_input.text = ""
            else:
                self.message.text = f"✗ {result}"
                self.message.color = (0.90, 0.30, 0.24, 1)
        except ValueError:
            self.message.text = "✗ Invalid amount"
            self.message.color = (0.90, 0.30, 0.24, 1)
    
    def go_back(self):
        self.manager.current = 'menu'

class WithdrawScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Withdraw Money", size_hint_y=0.1, font_size='20sp', bold=True))
        
        form_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.6)
        
        layout.add_widget(Label(text="Account Number", size_hint_y=None, height=30))
        self.acc_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.acc_input)
        
        layout.add_widget(Label(text="Amount ($)", size_hint_y=None, height=30))
        self.amount_input = TextInput(multiline=False, size_hint_y=None, height=40, input_filter='float')
        form_layout.add_widget(self.amount_input)
        
        self.message = Label(text="", size_hint_y=None, height=40)
        form_layout.add_widget(self.message)
        
        layout.add_widget(form_layout)
        
        btn_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.2)
        btn_withdraw = Button(text="✓ Withdraw", background_color=(0.15, 0.68, 0.38, 1))
        btn_withdraw.bind(on_press=self.withdraw)
        btn_layout.add_widget(btn_withdraw)
        
        btn_back = Button(text="← Back", background_color=(0.75, 0.75, 0.75, 1))
        btn_back.bind(on_press=lambda x: self.go_back())
        btn_layout.add_widget(btn_back)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def withdraw(self, instance):
        acc = self.acc_input.text.strip()
        try:
            amount = float(self.amount_input.text)
            result = self.app.bank.withdraw(acc, amount)
            if "successful" in result.lower():
                self.message.text = f"✓ {result}"
                self.message.color = (0.15, 0.68, 0.38, 1)
                self.acc_input.text = ""
                self.amount_input.text = ""
            else:
                self.message.text = f"✗ {result}"
                self.message.color = (0.90, 0.30, 0.24, 1)
        except ValueError:
            self.message.text = "✗ Invalid amount"
            self.message.color = (0.90, 0.30, 0.24, 1)
    
    def go_back(self):
        self.manager.current = 'menu'

class CheckBalanceScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Check Balance", size_hint_y=0.1, font_size='20sp', bold=True))
        
        form_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.6)
        
        layout.add_widget(Label(text="Account Number", size_hint_y=None, height=30))
        self.acc_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.acc_input)
        
        self.balance_display = Label(text="", size_hint_y=None, height=60, font_size='18sp', bold=True)
        form_layout.add_widget(self.balance_display)
        
        self.message = Label(text="", size_hint_y=None, height=40)
        form_layout.add_widget(self.message)
        
        layout.add_widget(form_layout)
        
        btn_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.2)
        btn_check = Button(text="🔍 Check", background_color=(0.15, 0.68, 0.38, 1))
        btn_check.bind(on_press=self.check_balance)
        btn_layout.add_widget(btn_check)
        
        btn_back = Button(text="← Back", background_color=(0.75, 0.75, 0.75, 1))
        btn_back.bind(on_press=lambda x: self.go_back())
        btn_layout.add_widget(btn_back)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def check_balance(self, instance):
        acc = self.acc_input.text.strip()
        balance = self.app.bank.check_balance(acc)
        if balance is not None:
            self.balance_display.text = f"Balance: ${balance:.2f}"
            self.balance_display.color = (0.15, 0.68, 0.38, 1)
            self.message.text = f"✓ Account: {acc}"
            self.message.color = (0.15, 0.68, 0.38, 1)
        else:
            self.message.text = "✗ Account not found"
            self.message.color = (0.90, 0.30, 0.24, 1)
            self.balance_display.text = ""
        self.acc_input.text = ""
    
    def go_back(self):
        self.manager.current = 'menu'

class TransferMoneyScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Transfer Money", size_hint_y=0.08, font_size='20sp', bold=True))
        
        form_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.6)
        
        layout.add_widget(Label(text="From Account", size_hint_y=None, height=30))
        self.from_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.from_input)
        
        layout.add_widget(Label(text="To Account", size_hint_y=None, height=30))
        self.to_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.to_input)
        
        layout.add_widget(Label(text="Amount ($)", size_hint_y=None, height=30))
        self.amount_input = TextInput(multiline=False, size_hint_y=None, height=40, input_filter='float')
        form_layout.add_widget(self.amount_input)
        
        self.message = Label(text="", size_hint_y=None, height=50)
        form_layout.add_widget(self.message)
        
        layout.add_widget(form_layout)
        
        btn_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.2)
        btn_transfer = Button(text="✓ Transfer", background_color=(0.15, 0.68, 0.38, 1))
        btn_transfer.bind(on_press=self.transfer)
        btn_layout.add_widget(btn_transfer)
        
        btn_back = Button(text="← Back", background_color=(0.75, 0.75, 0.75, 1))
        btn_back.bind(on_press=lambda x: self.go_back())
        btn_layout.add_widget(btn_back)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def transfer(self, instance):
        from_acc = self.from_input.text.strip()
        to_acc = self.to_input.text.strip()
        try:
            amount = float(self.amount_input.text)
            result = self.app.bank.transfer(from_acc, to_acc, amount)
            if "successful" in result.lower():
                self.message.text = f"✓ {result}"
                self.message.color = (0.15, 0.68, 0.38, 1)
                self.from_input.text = ""
                self.to_input.text = ""
                self.amount_input.text = ""
            else:
                self.message.text = f"✗ {result}"
                self.message.color = (0.90, 0.30, 0.24, 1)
        except ValueError:
            self.message.text = "✗ Invalid amount"
            self.message.color = (0.90, 0.30, 0.24, 1)
    
    def go_back(self):
        self.manager.current = 'menu'

class TransactionHistoryScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Transaction History", size_hint_y=0.1, font_size='20sp', bold=True))
        
        layout.add_widget(Label(text="Account Number", size_hint_y=None, height=30))
        self.acc_input = TextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.acc_input)
        
        # Scrollable transaction list
        self.scroll = ScrollView(size_hint=(1, 0.6))
        self.trans_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.trans_layout.bind(minimum_height=self.trans_layout.setter('height'))
        self.scroll.add_widget(self.trans_layout)
        layout.add_widget(self.scroll)
        
        # Buttons
        btn_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.15)
        btn_load = Button(text="📜 Load History", background_color=(0.15, 0.68, 0.38, 1))
        btn_load.bind(on_press=self.load_history)
        btn_layout.add_widget(btn_load)
        
        btn_back = Button(text="← Back", background_color=(0.75, 0.75, 0.75, 1))
        btn_back.bind(on_press=lambda x: self.go_back())
        btn_layout.add_widget(btn_back)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def load_history(self, instance):
        acc = self.acc_input.text.strip()
        self.trans_layout.clear_widgets()
        
        transactions = self.app.bank.get_transactions(acc)
        if transactions:
            for trans in transactions:
                trans_text = f"[{trans.timestamp}]\n{trans.type.upper()}: ${trans.amount:.2f}\n{trans.description}\nBalance: ${trans.balance_after:.2f}"
                trans_label = Label(text=trans_text, size_hint_y=None, height=80)
                self.trans_layout.add_widget(trans_label)
        else:
            self.trans_layout.add_widget(Label(text="No transactions found", size_hint_y=None, height=50))
    
    def go_back(self):
        self.manager.current = 'menu'

class SearchAccountScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Search Account", size_hint_y=0.1, font_size='20sp', bold=True))
        
        layout.add_widget(Label(text="Search (Name or Account #)", size_hint_y=None, height=30))
        self.search_input = TextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.search_input)
        
        # Scrollable results
        self.scroll = ScrollView(size_hint=(1, 0.6))
        self.results_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.results_layout.bind(minimum_height=self.results_layout.setter('height'))
        self.scroll.add_widget(self.results_layout)
        layout.add_widget(self.scroll)
        
        # Buttons
        btn_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.15)
        btn_search = Button(text="🔍 Search", background_color=(0.15, 0.68, 0.38, 1))
        btn_search.bind(on_press=self.search)
        btn_layout.add_widget(btn_search)
        
        btn_back = Button(text="← Back", background_color=(0.75, 0.75, 0.75, 1))
        btn_back.bind(on_press=lambda x: self.go_back())
        btn_layout.add_widget(btn_back)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def search(self, instance):
        search_term = self.search_input.text.strip()
        self.results_layout.clear_widgets()
        
        results = self.app.bank.search_account(search_term)
        if results:
            for acc_no, account in results:
                result_text = f"Account: {acc_no}\nName: {account.name}\nBalance: ${account.balance:.2f}"
                result_label = Label(text=result_text, size_hint_y=None, height=80)
                self.results_layout.add_widget(result_label)
        else:
            self.results_layout.add_widget(Label(text="No accounts found", size_hint_y=None, height=50))
    
    def go_back(self):
        self.manager.current = 'menu'

class AccountSettingsScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        layout.add_widget(Label(text="Account Settings", size_hint_y=0.15, font_size='20sp', bold=True))
        
        info_layout = GridLayout(cols=1, spacing=20, size_hint_y=0.6)
        
        total_accounts = self.app.bank.get_account_count()
        total_balance = self.app.bank.get_total_balance()
        
        info_layout.add_widget(Label(
            text=f"📊 System Statistics\n\nTotal Accounts: {total_accounts}\nTotal Balance: ${total_balance:.2f}",
            size_hint_y=None,
            height=100
        ))
        
        info_layout.add_widget(Label(
            text="🔐 Security\n\nPassword Protected Admin Panel\nSecure Account Storage\nTransaction Logging",
            size_hint_y=None,
            height=100
        ))
        
        layout.add_widget(info_layout)
        
        btn_back = Button(text="← Back to Menu", size_hint_y=0.15, background_color=(0.75, 0.75, 0.75, 1))
        btn_back.bind(on_press=lambda x: self.go_back())
        layout.add_widget(btn_back)
        
        self.add_widget(layout)
    
    def go_back(self):
        self.manager.current = 'menu'

class AdminLoginScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        layout.add_widget(Label(text="Admin Portal", size_hint_y=0.15, font_size='20sp', bold=True))
        layout.add_widget(Label(text="Authentication Required", size_hint_y=0.1, font_size='14sp'))
        
        form_layout = GridLayout(cols=1, spacing=15, size_hint_y=0.6)
        
        layout.add_widget(Label(text="Admin Password", size_hint_y=None, height=30))
        self.password_input = TextInput(multiline=False, password=True, size_hint_y=None, height=40)
        form_layout.add_widget(self.password_input)
        
        self.message = Label(text="", size_hint_y=None, height=40)
        form_layout.add_widget(self.message)
        
        layout.add_widget(form_layout)
        
        btn_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.15)
        btn_login = Button(text="🔓 Login", background_color=(0.15, 0.68, 0.38, 1))
        btn_login.bind(on_press=self.verify_password)
        btn_layout.add_widget(btn_login)
        
        btn_back = Button(text="← Back", background_color=(0.75, 0.75, 0.75, 1))
        btn_back.bind(on_press=lambda x: self.go_back())
        btn_layout.add_widget(btn_back)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def verify_password(self, instance):
        password = self.password_input.text
        if password == self.app.admin_password:
            self.password_input.text = ""
            self.manager.current = 'admin'
        else:
            self.message.text = "✗ Incorrect password"
            self.message.color = (0.90, 0.30, 0.24, 1)
            self.password_input.text = ""
    
    def go_back(self):
        self.manager.current = 'menu'

class AdminDashboardScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="Admin Dashboard", size_hint_y=0.1, font_size='20sp', bold=True))
        
        # Scrollable accounts list
        self.scroll = ScrollView(size_hint=(1, 0.7))
        self.accounts_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.accounts_layout.bind(minimum_height=self.accounts_layout.setter('height'))
        self.scroll.add_widget(self.accounts_layout)
        layout.add_widget(self.scroll)
        
        # Buttons
        btn_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.15)
        btn_refresh = Button(text="🔄 Refresh", background_color=(0.15, 0.68, 0.38, 1))
        btn_refresh.bind(on_press=self.load_accounts)
        btn_layout.add_widget(btn_refresh)
        
        btn_back = Button(text="← Back", background_color=(0.75, 0.75, 0.75, 1))
        btn_back.bind(on_press=lambda x: self.go_back())
        btn_layout.add_widget(btn_back)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
        
        # Load accounts on screen display
        self.bind(on_enter=lambda *args: self.load_accounts(None))
    
    def load_accounts(self, instance):
        self.accounts_layout.clear_widgets()
        
        accounts = self.app.bank.get_all_accounts()
        total_balance = self.app.bank.get_total_balance()
        
        # Add summary
        summary_text = f"Total Accounts: {len(accounts)}\nTotal Balance: ${total_balance:.2f}"
        self.accounts_layout.add_widget(Label(text=summary_text, size_hint_y=None, height=60, bold=True))
        
        # Add accounts
        for acc_no, account in accounts.items():
            account_text = f"{account.name}\nAccount: {acc_no}\nBalance: ${account.balance:.2f}"
            account_label = Label(text=account_text, size_hint_y=None, height=90)
            self.accounts_layout.add_widget(account_label)
    
    def go_back(self):
        self.manager.current = 'menu'

if __name__ == '__main__':
    BankMobileApp().run()
