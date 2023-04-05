import unittest
from BMI import wynik_BMI
from parameterized import parameterized


class UnitTests(unittest.TestCase):
    @parameterized.expand([
        (1.5, 30, 'niedowaga'),
        (1.5, 100, 'otyłość kliniczna'),
        (1.5, 50, 'norma'),
        (1.5, 70, 'otyłość')
    ])
    def test_should_return_valid_output(self, height, weight, expected):
        self.assertEqual(wynik_BMI(height, weight), expected)

    @parameterized.expand([
        (None, None), (1.5, None), (None, 20)
    ])
    def test_should_fail_on_empty_input(self, height, weight):
        with self.assertRaisesRegex(ValueError, "wprowadź obie wartości liczbowe"):
            wynik_BMI(height, weight)

    @parameterized.expand([
        ('@#$', '@@#$'), (1.5, '@@#'), ('@#$', 200)
    ])
    def test_should_fail_on_string_input(self, height, weight):

        with self.assertRaisesRegex(ValueError, "błędne wartości"):
            wynik_BMI(height, weight)

    def test_should_fail_on_zero_input(self):

        with self.assertRaisesRegex(ValueError, "podaj wartość większą niż 0"):
            wynik_BMI(0, 0)
