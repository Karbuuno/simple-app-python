from services.bank_service import Bank

bank = Bank()

while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Transactions\n5. Account Details\n6. Exit")
    choice = input("Enter your choice (1-6): ")

    try:
        if choice == "1":
            name = input("Enter your name: ")
            bank.create_account(name)

        elif choice in ["2", "3", "4", "5"]:
            acc_no = int(input("Enter your account number: "))
            found_account = bank.find_account(acc_no)

            if not found_account:
                print(f"Account with account number {acc_no} not found.")
                continue

            if choice == "2":
                amount = float(input("Enter the amount to deposit: "))
                found_account.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: "))
                found_account.withdraw(amount)

            elif choice == "4":
                found_account.show_transactions()

            elif choice == "5":
                found_account.display_account_info()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select between 1 and 6.")

    except ValueError:
        print("Invalid input. Please enter correct data.")
