class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance = self.balance + self.balance*self.interest_rate

def test(input, expected, msg):
    if input == expected:
        print(msg, "passed")
    else:
        print(msg, "failed")

account = BankAccount("234234", 100)

account.deposit(100)
test(account.get_balance(), 200, "1")

account.withdraw(50)
test(account.get_balance(), 150, "2")

savings_account = SavingsAccount("234234", 1000, 0.1)

savings_account.withdraw(100)
test(savings_account.get_balance(), 900, "3")

savings_account.deposit(140)
test(savings_account.get_balance(), 1040, "4")

savings_account.add_interest()
test(savings_account.get_balance(), 1144, "5")
