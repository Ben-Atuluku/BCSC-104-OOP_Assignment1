from Account import Account
class Current(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
       super().__init__(owner, balance)
       self.overdraft_limit = overdraft_limit
