#!/usr/bin/env python3
class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance inquiries.

    Attributes:
    balance (float): The current balance in the checkbook, initialized to 0.0.
    """

    def __init__(self):
        """
        Initializes the checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook.

        Parameters:
        amount (float): The amount to be deposited.

        Returns:
        None: Updates the balance and prints the transaction details.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook, if sufficient funds are available.

        Parameters:
        amount (float): The amount to be withdrawn.

        Returns:
        None: Updates the balance if the withdrawal is successful, otherwise prints an error message.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.

        Parameters:
        None

        Returns:
        None: Prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook class.
    Prompts the user to perform actions like deposit, withdraw, check balance, or exit.

    Parameters:
    None

    Returns:
    None: Continuously interacts with the user until 'exit' is chosen.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
