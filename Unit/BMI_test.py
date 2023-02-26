import unittest
import BMI

class UnitTests(unittest.TestCase):
    def test_wynik_BMI(self):
        self.assertEqual(BMI.czy_gruby(1.5, 30),'niedowaga')
        self.assertEqual(BMI.czy_gruby(1.5, 100),'otyłość kliniczna')
        self.assertEqual(BMI.czy_gruby(1.5, 50),'norma')
        self.assertEqual(BMI.czy_gruby(1.5, 70),'otyłość')

