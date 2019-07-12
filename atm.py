import time

current_time = time.strftime(r"%d.%m.%Y %H:%M:%S", time.localtime())


class atm:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.transactions = dict()
        self.transactions["Deposits"] = {}
        self.transactions["Withdrawals"] = {}

    def deposit(self, amt):
        if amt <= 1000 and amt >= 0:
            self.balance += amt
            self.transactions["Deposits"].update({current_time: (+amt)})
        else:
            raise ValueError("Invalid Amount.")

    def withdrawal(self, amt):
        if amt > 500 or amt < 0:
            raise ValueError("Invalid Amount")
        elif amt <= 500 and amt > 0 and amt <= self.balance:
            self.balance -= amt
            self.transactions["Withdrawals"].update({current_time: (-amt)})
        elif amt > self.balance:
            return "Insufficient Funds"

    def check_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

    def get_deposits(self):
        for k, v in self.transactions["Deposits"].items():
            return "Deposit", k, v

    def get_withdrawals(self):
        for k, v in self.transactions["Withdrawals"].items():
            return "Withdrawal", k, v

    def get_name(self):
        return self.name

    def get_pin(self):
        return self.pin

    def init(self):
        self.usr = str(input("What's your name? "))
        self.usr_pin = int(input("What's your pin number? "))
        # if self.usr


jameson = atm("Jameson", "1234")
jameson.deposit(500)
print(jameson.check_balance())
jameson.withdrawal(500)
print(jameson.check_balance())
jameson.withdrawal(400)
print(jameson.check_balance())
jameson.withdrawal(450)
print(jameson.check_balance())
jameson.withdrawal(400)
print(jameson.check_balance())
print(jameson.get_transactions())
print(jameson.get_deposits())
print(jameson.get_withdrawals())
