import unittest
import wyplata

class UnitTests(unittest.TestCase):

    def test_wyplac(self):
        self.assertEqual(wyplata.wyplac(50, 2345), 50)
        with self.assertRaisesRegex(ValueError, "błędna kwota"):
            wyplata.wyplac (2000, 2345)
        with self.assertRaisesRegex(ValueError, "błędny pin"):
            wyplata.wyplac (50, 1345)
        with self.assertRaisesRegex(ValueError, "błędna kwota"):
            wyplata.wyplac (-50, 2345)         
        