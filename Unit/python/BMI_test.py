import unittest
from BMI import wynik_BMI


class UnitTests(unittest.TestCase):
    def test_should_return_valid_output(self):
        self.assertEqual(wynik_BMI(1.5, 30), 'niedowaga')
        self.assertEqual(wynik_BMI(1.5, 100), 'otyłość kliniczna')
        self.assertEqual(wynik_BMI(1.5, 50), 'norma')
        self.assertEqual(wynik_BMI(1.5, 70), 'otyłość')

    def test_should_fail_on_empty_input(self):

        expected_non_empty_input="wprowadź obie wartości liczbowe"

        with self.assertRaisesRegex(ValueError, expected_non_empty_input):
            wynik_BMI(None, None)
        with self.assertRaisesRegex(ValueError, expected_non_empty_input):
            wynik_BMI(1.5, None)
        with self.assertRaisesRegex(ValueError, expected_non_empty_input):
            wynik_BMI(None, 20)
        
    def test_should_fail_on_string_input(self):

        expected_valid_input="błędne wartości"

        with self.assertRaisesRegex(ValueError, expected_valid_input):
            wynik_BMI('@#$', '@@#$')
        with self.assertRaisesRegex(ValueError, expected_valid_input):
            wynik_BMI(1.5, '@@#')
        with self.assertRaisesRegex(ValueError, expected_valid_input):
            wynik_BMI('@#$', 200)

    def test_should_fail_on_zero_input(self):

        with self.assertRaisesRegex(ValueError, "podaj wartość większą niż 0"):
            wynik_BMI(0, 0)