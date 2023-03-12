import unittest
import lampka

class UnitTests(unittest.TestCase):

    def test_lampka(self):
        lampeczka=lampka.Lampka()
        self.assertFalse(lampeczka.czy_wlaczona)
        lampeczka.pstryk()
        self.assertTrue(lampeczka.czy_wlaczona)
        lampeczka.pstryk()
        self.assertFalse(lampeczka.czy_wlaczona)