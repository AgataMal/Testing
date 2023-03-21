import unittest
from BMI import wynik_BMI


class UnitTests(unittest.TestCase):
    def test_wynik_BMI(self):
        self.assertEqual(wynik_BMI(1.5, 30), 'niedowaga')
        self.assertEqual(wynik_BMI(1.5, 100), 'otyłość kliniczna')
        self.assertEqual(wynik_BMI(1.5, 50), 'norma')
        self.assertEqual(wynik_BMI(1.5, 70), 'otyłość')

        expected_non_empty_input="wprowadź obie wartości liczbowe"

        with self.assertRaisesRegex(ValueError, "podaj wartość większą niż 0"):
            wynik_BMI(0, 0)
        with self.assertRaisesRegex(ValueError, expected_non_empty_input):
            wynik_BMI(None, None)
        with self.assertRaisesRegex(ValueError, expected_non_empty_input):
            wynik_BMI(1.5, None)
        with self.assertRaisesRegex(ValueError, expected_non_empty_input):
            wynik_BMI(None, 20)
        
        expected_valid_input="błędne wartości"

        with self.assertRaisesRegex(ValueError, expected_valid_input):
            wynik_BMI('@#$', '@@#$')
        with self.assertRaisesRegex(ValueError, expected_valid_input):
            wynik_BMI(1.5, '@@#')
        with self.assertRaisesRegex(ValueError, expected_valid_input):
            wynik_BMI('@#$', 200)
