# Task 5: Encapsulation and Abstraction

from abc import ABC, abstractmethod

# Abstract parent class
class Account(ABC):

    @abstractmethod
    def account_type(self):
        pass


# Child class
class SavingsAccount(Account):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # Implementing abstract method
    def account_type(self):
        print("Account Type: Savings Account")

    # Method to deposit money
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Deposited Amount:", amount)

    # Method to access private balance
    def get_balance(self):
        return self.__balance

    # Display account details
    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


# Creating object
account1 = SavingsAccount("Pravalika", 5000)

print("BANK ACCOUNT DETAILS")
print("====================")

account1.account_type()
account1.display()

# Depositing money
account1.deposit(2000)

# Displaying updated balance
print("Updated Balance:", account1.get_balance())