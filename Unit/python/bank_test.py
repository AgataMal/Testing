import unittest
import bank


class UnitTests(unittest.TestCase):
    def test_create_bank(self):
        bankPKO = bank.Bank()
        self.assertIsInstance(bankPKO, bank.Bank)
        self.assertEqual(bankPKO.amount, 0)

    def test_add_money(self):
        bankPKO = bank.Bank()
        self.assertEqual(bankPKO.add_money(100), 100 )

    def test_withdraw_money(self):
        bankPKO = bank.Bank(200)
        self.assertEqual(bankPKO.withdraw_money(100), 100 )