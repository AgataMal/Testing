import unittest
import math_operation

class UnitTests(unittest.TestCase):
    
    def test_sum_result(self):
        sum_result=math_operation.sum_result([2,3,4,5])
        self.assertEqual(sum_result,14)


