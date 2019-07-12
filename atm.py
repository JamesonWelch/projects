import datetime


class atm:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.transactions = dict()
        self.transactions["Deposits"] = {}
        self.transactions["Withdrawals"] = {}
        if len(str(self.pin)) != 4:
            raise ValueError("Pin Number Too Long. Must be 4 digits.")

    def deposit(self, amt):
        """ Deposits money into account up to $1000 """
        current_time = str(datetime.datetime.now())
        if amt <= 1000 and amt > 0:
            self.balance += amt
            self.transactions["Deposits"].update({current_time: (+amt)})
        else:
            raise ValueError("Invalid Amount.")

    def withdrawal(self, amt):
        """ Withdrawals money from account up to $500 """
        current_time = str(datetime.datetime.now())
        if amt > 500 or amt < 0:
            raise ValueError("Invalid Amount")
        elif amt <= 500 and amt > 0 and amt <= self.balance:
            self.balance -= amt
            self.transactions["Withdrawals"].update({current_time: (-amt)})
        elif amt > self.balance:
            print("Insufficient Funds")

    def check_balance(self):
        return self.balance

    def get_transactions(self):
        for k, v in self.transactions.items():
            print(k, v)

    def get_deposits(self):
        for k, v in self.transactions["Deposits"].items():
            print("Deposit", k, v)

    def get_withdrawals(self):
        for k, v in self.transactions["Withdrawals"].items():
            print("Withdrawal", k, v)

    def get_name(self):
        print(self.name)

    def get_pin(self):
        print(self.pin)


jameson = atm("Jameson", "1234")
jameson.deposit(1000)
print(jameson.check_balance())
jameson.withdrawal(500)
print(jameson.check_balance())
jameson.deposit(400)
print(jameson.check_balance())
jameson.withdrawal(450)
print(jameson.check_balance())
jameson.withdrawal(400)
print(jameson.check_balance())
print(jameson.get_transactions())
print(jameson.get_deposits())
print(jameson.get_withdrawals())

trish = atm("Trish", "2345")
trish.deposit(1000)

print(trish.check_balance())
print(trish.balance)
