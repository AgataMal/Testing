import unittest
import exercises

class UnitTests(unittest.TestCase):

    def test_is_adult(self):
        adult=exercises.is_adult(20)
        self.assertTrue(adult)

    def test_not_is_adult(self):
        self.assertFalse(exercises.is_adult(15))

    def test_triangle_field(self):
        self.assertEqual(exercises.triangle_field (10,15),75)

    