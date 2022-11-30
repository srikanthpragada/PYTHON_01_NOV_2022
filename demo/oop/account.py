class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Balance is {self.balance} but withdraw amount is {self.amount}"


class Account:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid transaction amount!")

        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientBalanceError(self.balance, amount)

        self.balance -= amount

    def getbalance(self):
        return self.balance


a1 = Account(101, "Andy")
a1.deposit(10000)
a1.deposit(5000)
try:
    a1.withdraw(100000)
except Exception as ex:
    print(ex)

print(a1.getbalance())
