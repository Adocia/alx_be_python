import sys
from bank_account import BankAccount

def main():
    # Optional initial balance
    initial_balance = 0
    args = sys.argv[1:]

    if len(args) > 0:
        try:
            # If the first argument is a number, treat it as initial balance
            initial_balance = float(args[0])
            args = args[1:]
        except ValueError:
            pass  # first argument is a command, not a number

    account = BankAccount(initial_balance)

    # Process commands in order
    i = 0
    while i < len(args):
        cmd = args[i].lower()

        if cmd == "deposit":
            try:
                amount = float(args[i + 1])
                account.deposit(amount)
                i += 2
            except (IndexError, ValueError):
                print("Invalid deposit amount.")
                i += 2
        elif cmd == "withdraw":
            try:
                amount = float(args[i + 1])
                account.withdraw(amount)
                i += 2
            except (IndexError, ValueError):
                print("Invalid withdraw amount.")
                i += 2
        elif cmd == "balance":
            account.display_balance()
            i += 1
        else:
            print(f"Unknown command: {cmd}")
            i += 1

if __name__ == "__main__":
    main()
