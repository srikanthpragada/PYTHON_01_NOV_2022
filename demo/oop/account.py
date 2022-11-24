class Account:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getbalance(self):
        return self.balance


a1 = Account(101, "Andy")
a1.deposit(10000)
a1.deposit(5000)
print(a1.getbalance())
