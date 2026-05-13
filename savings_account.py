from Account import Account

class Savings(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02, withdrawal_limit=100):
       super().__init__(owner, balance)
       self.interest_rate = interest_rate
       self.withdrawal_limit = withdrawal_limit


    def apply_interest(self):
       interest = self.get_balance() * self.interest_rate
       self.deposit(interest)
       print(f"Interest of ${interest} applied. New balance is ${self.get_balance()}")


    def withdraw(self, amount):
        if amount < self.withdrawal_limit:
            if 0 < amount <= self.get_balance():
                print(f"Withdrew ${amount}. Remaining balance is ${self.get_balance()} )")
                self.set_balance(float(amount))
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal limit reached")

#*Really wanted to allow all parameters to be customised by inputs but the class objects don't allow me pass in floats.
# initial_deposit = input("Enter the initial deposit amount: ")
# print("___Savings Account___")
# savings = Savings("Ben", initial_deposit) #This is a constructor, creates object doesn't allow me pass in a float for some reason
# initial_deposit = (float(initial_deposit))
# print(f"Initial balance: ${savings.get_balance()}")
# deposit_amount = (float(input("Enter initial deposit: ")))
# deposit_amount = (float(deposit_amount))
# savings.deposit(deposit_amount)
# withdrawal_amount = (float(input("Enter withdrawal amount: ")))
# withdrawal_amount = (float(withdrawal_amount))
# savings.withdraw(withdrawal_amount)
# savings.apply_interest()

print("___Savings Account___")
savings = Savings("Ben", 500)
savings.deposit(250)
savings.withdraw(100)
savings.apply_interest()