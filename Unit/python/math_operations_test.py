import unittest
import math_operation
from parameterized import parameterized


class UnitTests(unittest.TestCase):

    def test_sum_result(self):
        sum_result = math_operation.sum_result([2, 3, 4, 5])
        self.assertEqual(sum_result, 14)

    @parameterized.expand([(5, True), (4, False), (7, True), (1, False)])
    def test_czy_liczba_pierwsza(self, input, expected):
        result = math_operation.czy_liczba_pierwsza(input)
        self.assertEqual(result, expected)

    def test_reverse_list(self):
        lista = math_operation.reverse_list([2, 3, 4])
        self.assertEqual(lista, [4, 3, 2])

    def test_reverse_list2(self):
        lista = math_operation.reverse_list2([2, 3, 4, 1, 5])
        self.assertEqual(lista, [5, 1, 4, 3, 2])
        with self.assertRaisesRegex(ValueError,"brak środkowego elementu"):
            math_operation.reverse_list2([1,2,3,6])

    def test_duplikaty(self):
        self.assertEqual(math_operation.duplikaty(
            [20, 30, 40], [20, 40, 50]), [20, 40])

    @parameterized.expand([
        ([], None), ([5, 6, 7, 8], 6.5), ([5, 6, 7, -8], 2.5)])
    def test_srednia(self, input, expected):
        self.assertEqual(math_operation.srednia(input), expected)

    def test_triangle_field(self):
        self.assertEqual(math_operation.triangle_field(10, 15), 75)

    @parameterized.expand([
        (1, -2, 1, [1]),
        (2, 5, -3, [-3, 0.5])
    ])
    def test_quadratic_function(self, a, b, c, expected):
        self.assertIsNone(math_operation.quadratic_function(2, 2, 2))
        self.assertListEqual(
            math_operation.quadratic_function(a,b,c), expected)

    def test_odd_even_counts(self):
        lista=[2,3,4,5,6,7]
        expected= [3,3]
        self.assertEqual(math_operation.odd_even_counts(lista), expected)

    def test_even_counts(self):
        lista=[2,3,4,5,6,7]
        expected= [3,3]
        self.assertEqual(math_operation.even_counts(lista), expected)