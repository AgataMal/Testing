import unittest
from bank import *


class UnitTests(unittest.TestCase):
    def test_create_bank(self):
        bankPKO = Bank()
        self.assertIsInstance(bankPKO, Bank)
        self.assertEqual(bankPKO.get_balance(), 0)

    def test_add_money(self):
        bankPKO = Bank()
        self.assertEqual(bankPKO.add_money(100), 100)

    def test_withdraw_money(self):
        bankPKO = Bank(200)
        self.assertEqual(bankPKO.withdraw_money(100), 100)
