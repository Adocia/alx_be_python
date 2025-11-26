import sys
from bank_account import BankAccount

def main():
    # Create a BankAccount instance with optional initial balance
    initial_balance = 0
    if len(sys.argv) > 1:
        try:
            initial_balance = float(sys.argv[1])
        except ValueError:
            print("Invalid initial balance. Defaulting to $0.")
    
    account = BankAccount(initial_balance)

    # Simple command loop
    while True:
        print("\nOptions: deposit, withdraw, balance, exit")
        command = input("Enter command: ").strip().lower()

        if command == "deposit":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif command == "withdraw":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif command == "balance":
            account.display_balance()
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
