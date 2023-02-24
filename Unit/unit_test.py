import unittest
import math_operation


class UnitTests(unittest.TestCase):

    def test_sum_result(self):
        sum_result = math_operation.sum_result([2, 3, 4, 5])
        self.assertEqual(sum_result, 14)

    def test_czy_liczba_pierwsza(self):
        result = math_operation.czy_liczba_pierwsza(5)
        self.assertTrue(result)
        result = math_operation.czy_liczba_pierwsza(4)
        self.assertFalse(result)
        result = math_operation.czy_liczba_pierwsza(7)
        self.assertTrue(result)
        result = math_operation.czy_liczba_pierwsza(1)
        self.assertFalse(result)
