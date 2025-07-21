from models.account import Account
from services.transaction_service import show_history


acc1 =Account(1,"xussein")

acc1.deposit(2000)
acc1.withdraw(100)
acc1.display_account_info()
