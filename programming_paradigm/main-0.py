import sys
from bank_account import BankAccount

def main():
    # Optional initial balance from command line
    initial_balance = 0
    if len(sys.argv) > 1:
        try:
            initial_balance = float(sys.argv[1])
        except ValueError:
            print("Invalid initial balance. Defaulting to $0.")

    account = BankAccount(initial_balance)

    # Read commands in a simple loop
    while True:
        command = input().strip().lower()  # input only, no prompt

        if command == "deposit":
            try:
                amount = float(input())
                account.deposit(amount)  # deposit prints exactly once
            except ValueError:
                print("Invalid amount.")
        elif command == "withdraw":
            try:
                amount = float(input())
                account.withdraw(amount)  # withdraw prints exactly once
            except ValueError:
                print("Invalid amount.")
        elif command == "balance":
            account.display_balance()  # prints exactly once
        elif command == "exit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
