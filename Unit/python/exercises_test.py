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

    def test_is_Weird(self):
        exercises.is_Weird(24)

    def test_is_leap(self):
        self.assertTrue(exercises.is_leap(2000))
        self.assertTrue(exercises.is_leap(2400))
        self.assertFalse(exercises.is_leap(1900))
        self.assertFalse(exercises.is_leap(1800))
        self.assertFalse(exercises.is_leap(2100))
        self.assertFalse(exercises.is_leap(2200))
        self.assertFalse(exercises.is_leap(2300))
        self.assertFalse(exercises.is_leap(2500))
    
    def test_capitalize(self):
       
        self.assertEqual( exercises.capitalize("ola nowak"),"Ola Nowak")
        self.assertEqual( exercises.capitalize("1ola 2nowak"),"1ola 2nowak")
        