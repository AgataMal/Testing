class Bank:
    def __init__(self, money=0) -> None:
        self.amount = money

    def add_money(self, money):
        self.amount += money
        return self.amount

    def withdraw_money(self, money):
        self.amount -= money
        return self.amount
