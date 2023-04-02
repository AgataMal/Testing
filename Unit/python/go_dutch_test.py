import unittest
import go_dutch
class UnitTests(unittest.TestCase):

    def test_amount_per_person(self):
        self.assertEqual(go_dutch.amount_per_person(5, 1000), 220)
