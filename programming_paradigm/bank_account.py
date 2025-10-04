class BankAccount:
    """A class to represent a bank account with basic banking operations."""
    
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount object.
        
        Args:
            initial_balance (float): The starting balance of the account. Defaults to 0.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): The amount to withdraw.
        
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds.
        """
        if amount > self.account_balance:
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.account_balance -= amount
            return True
    
    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")