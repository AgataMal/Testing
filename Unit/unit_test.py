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

    def test_reverse_list(self):
        lista = math_operation.reverse_list([2, 3, 4])
        self.assertEqual(lista, [4, 3, 2])

    def test_reverse_list2(self):
        lista = math_operation.reverse_list2([2, 3, 4, 1, 5])
        self.assertEqual(lista, [5, 1, 4, 3, 2])

    def test_duplikaty(self):
        self.assertEqual(math_operation.duplikaty(
            [20, 30, 40], [20, 40, 50]), [20, 40])

    def test_srednia(self):
        self.assertEqual(math_operation.srednia([]), None)
        self.assertEqual(math_operation.srednia([5, 6, 7, 8]), 6.5)
        self.assertEqual(math_operation.srednia([5, 6, 7, -8]), 2.5)
