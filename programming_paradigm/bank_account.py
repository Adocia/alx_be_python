# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self.__account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient."""
        if amount > self.__account_balance:
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
     """Print the current account balance with 2 decimal places."""
    print(f"Current Balance: ${self.__account_balance:.2f}")

    
