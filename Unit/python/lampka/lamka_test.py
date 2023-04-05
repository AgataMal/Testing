import unittest
import lampka

class UnitTests(unittest.TestCase):

    def test_lampka(self):
        lampeczka=lampka.Lampka()
        self.assertTrue(lampeczka.pstryk())
        self.assertFalse(lampeczka.pstryk())
        self.assertTrue(lampeczka.pstryk())