from models.account import Account
from models.users import Users
## Creating account
class Bank:
    def __init__(self):
        self.users=[]
    ## Get user
    def get_user(self,username):
        for user in self.users:
            if user.username==username:
                return user

   ## Register user    
    def register_user(self,name, username,password):
        if self.get_user(username):
            print("Username already exists.")
            return None
        new_user =Users(name,username,password)
        self.users.append(new_user)
        print(f"You are registered successfully Name: {name} Username: {username} Account No: {new_user.account.account_no}")
        return new_user
    ##Login
    def login_user(self,username,password):
        user=self.get_user(username)
        if user and user.password ==password:
            print(f"Login successful. Welcome, {user.name}")
            return user
        print("Login failed. Invalid username or password.")
        return None
    def user_profile(self,user):
        print("=== User Profile ===")
        print(f"Name: {user.name}")
        print(f"Username: {user.username}")
        print(f"Account Number: {user.account.account_no}")
        
        print("====================")      
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