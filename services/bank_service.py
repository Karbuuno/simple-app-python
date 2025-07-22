from models.account import Account
## Creating account
class Bank:
    def __init__(self):
        self.accounts=[]
    def create_account(self, name):
        new_account=Account(name)
        self.accounts.append(new_account)
        print(f"Account created successfully. Acount No: {new_account.account_no}")
        return new_account 
    def find_account(self, account_no):
        for account in self.accounts:
            if account.account_no==account_no:
                return account
        print(f"Account with account number: {account_no} not found.") 
        return None  