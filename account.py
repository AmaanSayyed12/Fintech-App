import uuid

class Account:
    def __init__(self, name, balance):
        self.id = str(uuid.uuid4())
        self.name = name
        self.balance = balance

class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance):
        account = Account(name, balance)
        self.accounts[account.id] = account
        print(f"Account created! Account ID: {account.id}, Balance: ${balance}")

    def get_account(self, account_id):
        return self.accounts.get(account_id)
