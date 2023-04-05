import unittest
import sorting

class UnitTests(unittest.TestCase):
    def test_sorting(self):
        self.assertEqual(sorting.bubble_sort([3,4,5,2,1]), 7)