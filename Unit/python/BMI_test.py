import unittest
import BMI


class UnitTests(unittest.TestCase):
    def test_wynik_BMI(self):
        self.assertEqual(BMI.czy_gruby(1.5, 30), 'niedowaga')
        self.assertEqual(BMI.czy_gruby(1.5, 100), 'otyłość kliniczna')
        self.assertEqual(BMI.czy_gruby(1.5, 50), 'norma')
        self.assertEqual(BMI.czy_gruby(1.5, 70), 'otyłość')

        self.assertEqual(BMI.czy_gruby(0, 0), "błąd")
        self.assertEqual(BMI.czy_gruby(1.5, None), "błąd")
        self.assertEqual(BMI.czy_gruby(None, None), "błąd")
        self.assertEqual(BMI.czy_gruby(None, 20), "błąd")

        self.assertEqual(BMI.czy_gruby('@#$', '@@#$'), "błąd")
        self.assertEqual(BMI.czy_gruby(1.5, '@@#'), "błąd")
        self.assertEqual(BMI.czy_gruby('@#$', 200), "błąd")
