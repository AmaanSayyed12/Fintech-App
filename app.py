from account import AccountManager
from transaction import TransactionManager
from fraud_detection import FraudDetection

# Initialize components
account_manager = AccountManager()
transaction_manager = TransactionManager()
fraud_detector = FraudDetection("data/transactions.csv")

def main():
    print("Welcome to the FinTech Application!")
    while True:
        print("\n1. Create Account")
        print("2. Perform Transaction")
        print("3. Detect Fraud")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter your name: ")
            balance = float(input("Enter initial deposit: "))
            account_manager.create_account(name, balance)
        elif choice == '2':
            account_id = input("Enter your account ID: ")
            amount = float(input("Enter transaction amount: "))
            transaction_manager.perform_transaction(account_id, amount)
        elif choice == '3':
            print("Running Fraud Detection...")
            fraud_detector.run()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
