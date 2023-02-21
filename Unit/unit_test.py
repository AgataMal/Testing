import unittest
import wynik

class UnitTests(unittest.TestCase):
    
    def test_wynik(self):
        sum_wynik=wynik.wynik([2,3,4,5])
        self.assertEqual (sum_wynik,14)


