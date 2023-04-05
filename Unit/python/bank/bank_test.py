import unittest
from bank import *
from parameterized import parameterized

class UnitTests(unittest.TestCase):
    def test_create_bank(self):
        bankPKO = Bank()
        self.assertIsInstance(bankPKO, Bank)
        self.assertEqual(bankPKO.get_balance(), 0)

    def test_add_money(self):
        bankPKO = Bank()
        self.assertEqual(bankPKO.add_money(100), 100)
        with self.assertRaisesRegex(ValueError, "podaj kwotę większą od 0"):
            bankPKO.add_money(0)

    def test_withdraw_money(self):
        bankPKO = Bank(200)
        self.assertEqual(bankPKO.withdraw_money(100), 100)

    @parameterized.expand([
        (100,300,"kwota przeracza stan konta"), (100, 0.01, "tylko liczba całkowita")
    ])
    def test_should_fail_withdraw_money(self, initial_amount, withdraw_amount, error_message):
        bankPKO= Bank(initial_amount)
        with self.assertRaisesRegex(ValueError, error_message):
            bankPKO.withdraw_money(withdraw_amount)