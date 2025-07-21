
## simple bank account
import random

class Account:
    def __init__(self, account_id, name):
        self.account_id=self.generate_account_number()
        self.name=name
        self.balance=0.0
        self.transactions=[]
    def generate_account_number(self):
        return random.randint(10000000,99999999)
    def deposit(self,amount):
        if amount <= 0:
            print("invalid deposit amount")
            return
        self.balance +=amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <0:
            print("insufficient balance")
            return
        self.balance-=amount
        self.transactions.append(f"Withdraw:{amount}")

    def display_account_info(self):
        print("Account information")
        print(f"Name: {self.name} Account ID: {self.account_id} Balance: {self.balance}")
        if self.transactions:
            self.show_transactions()  
        else:
            print("No transactions yet.")
        print("================================")
           

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)
        
        