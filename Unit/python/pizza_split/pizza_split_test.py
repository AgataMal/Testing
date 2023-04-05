import unittest
import pizza_split

class UnitTests(unittest.TestCase):
    def test_pizza_split(self):
        self.assertEqual(pizza_split.pizza_split(4,4), 1)