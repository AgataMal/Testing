class Bank:
    def __init__(self, money=0) -> None:
        self.__balance = money

    def add_money(self, money):
        if money > 0:
            self.__balance += money
            return self.__balance
        else:
            raise ValueError("podaj kwotę większą od 0")

    def withdraw_money(self, money):
        if not money % 1 == 0:
            raise ValueError("tylko liczba całkowita")
        if self.__balance - money > 0:
            self.__balance -= money
            return self.__balance
        else:
            raise ValueError("kwota przeracza stan konta")

    def get_balance(self):
        return self.__balance
