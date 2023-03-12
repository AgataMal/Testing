import unittest
import wyplata

class UnitTests(unittest.TestCase):

    def test_wyplac(self):
        self.assertEqual(wyplata.wyplac(50, 2345), 50)
        self.assertEqual(wyplata.wyplac(2000, 2345), None)
        self.assertEqual(wyplata.wyplac(50, 1345), None)
        self.assertEqual(wyplata.wyplac(-50, 2345), None)  