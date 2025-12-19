class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(a, amt): # Testing if I can write anything else instead of self
        a.balance += amt

b1 = BankAccount('abhishek', 1000000)
print(b1.balance)
b1.deposit(1223202)
print(b1.balance)