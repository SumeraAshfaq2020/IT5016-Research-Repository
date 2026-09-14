# Simple Banking System
# This program demonstrates basic Object-Oriented Programming (OOP)


# Account class stores account information
class Account:

    # __init__ sets the starting account details
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # Method to add money to the account
    def deposit(self, amount):
        self.balance = self.balance + amount

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful.")
        else:
            print("Not enough balance.")

    # Method to display the current balance
    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


# Customer class stores customer information
class Customer:

    def __init__(self, name, account):
        self.name = name
        self.account = account

    # Method to display customer information
    def display_customer(self):
        print("Customer Name:", self.name)
        self.account.display_balance()


# Creating an Account object
my_account = Account("ACC1001", 500)

# Creating a Customer object
customer = Customer("Sumera", my_account)

# Displaying starting information
customer.display_customer()

# Depositing money
my_account.deposit(200)

# Withdrawing money
my_account.withdraw(100)

# Displaying updated balance
print("\nAfter transactions:")
my_account.display_balance()
