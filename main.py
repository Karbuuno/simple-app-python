from models.account import Account
from services.transaction_service import show_history


acc1 =Account()
while True:
    choice =input("\n1. Deposit\n2. withdraw\n3. Transactions\n4. Account Details")
    try:
        if choice=="1":
            price= float(input("Enter the amount you will like to deposit"))
            acc1.deposit(price)
        elif choice=="2":
            price= float(input("Enter the amount you will like to withdraw"))
            acc1.withdraw(price)
        elif choice=="3":
            acc1.show_transactions()
        elif choice=="4":
            acc1.display_account_info()
        else:
            print("Invalid choice. Please select between 1 and 4.")    
    except ValueError:
         print("Invalid input. Please enter correct data.")

