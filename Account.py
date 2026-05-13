class Account:
    def __init__(self, owner, balance = 0): #constructor, creates classes and class objects
        self.owner = owner
        self.__balance = balance #Encapsulation: Making Balance Private


    def deposit(self, amount):
        """Base withdraw method to be overridden(Polymorphism)"""
        # print(f"deposited ${amount}.")
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of ${amount} successful. New balance is ${self.__balance} ")
        else:
            print(f"Deposit amount must be greater than 0")


    def withdraw(self, amount):
        """Base withdraw method to be overridden(Polymorphism)"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance is ${self.__balance} ")
        else:
            print(f"Insufficient Funds")


    def get_balance(self):
        return self.__balance

    def set_balance(self, deduction):
        self.__balance -= deduction
        return self.__balance



