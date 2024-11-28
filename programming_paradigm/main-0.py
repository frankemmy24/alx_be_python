# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Ensure correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: python main-0.py <operation> <amount>")
        print("Operations: deposit, withdraw, display")
        return

    # Parse command-line arguments
    operation = sys.argv[1].lower()
    amount = float(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else None

    # Initialize BankAccount with an optional initial balance
    account = BankAccount()

    # Perform the requested operation
    if operation == "deposit":
        if amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")
    elif operation == "withdraw":
        if amount is not None:
            success = account.withdraw(amount)
            if success:
                print(f"Withdrew: ${amount:.2f}")
        else:
            print("Invalid withdrawal amount.")
    elif operation == "display":
        account.display_balance()
    else:
        print("Invalid operation. Please choose deposit, withdraw, or display.")

if __name__ == "__main__":
    main()