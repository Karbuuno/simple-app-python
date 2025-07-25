from services.bank_service import Bank

def main():
    bank = Bank()
    logged_in_user = None

    while True:
        try:
            print("\n=== BANKING APP ===")
            if logged_in_user:
                print(f"Logged in as: {logged_in_user.username}")
            print("1. Register")
            print("2. Login")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. View Transactions")
            print("6. Account Details")
            print("7. Logout")
            print("8. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter full name: ")
                username = input("Choose a username: ")
                password = input("Choose a password: ")
                user = bank.register_user(name, username, password)
                if user:
                    logged_in_user = user

            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                logged_in_user = bank.login_user(username, password)

            elif choice in ["3", "4", "5", "6"]:
                if not logged_in_user:
                    print("Please login first.")
                    continue

                account = logged_in_user.account

                if choice == "3":
                    try:
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    except ValueError:
                        print("❌ Invalid amount. Please enter a number.")

                elif choice == "4":
                    try:
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    except ValueError:
                        print("❌ Invalid amount. Please enter a number.")

                elif choice == "5":
                    account.show_transactions()

                elif choice == "6":
                    bank.user_profile(logged_in_user)

            elif choice == "7":
                logged_in_user = None
                print("✅ Logged out.")

            elif choice == "8":
                print("👋 Thanks for using the banking app!")
                break

            else:
                print("❌ Invalid option. Please choose from 1–8.")
        
        except Exception as e:
            print(f"❌ An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
