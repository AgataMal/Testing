class Bank:
    def __init__(self, money=0) -> None:
        self.__balance = money

    def add_money(self, money):
        self.__balance += money
        return self.__balance

    def withdraw_money(self, money):
        self.__balance -= money
        return self.__balance

    def get_balance(self):
        return self.__balance
