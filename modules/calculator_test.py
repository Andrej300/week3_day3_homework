import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual("The answer is 10", add_numbers(5, 5))

    def test_subtract_numbers(self):
        self.assertEqual("The answer is 4", subtract_numbers(8, 4))

    def test_multiply_numbers(self):
        self.assertEqual("The answer is 9", multiply_numbers(3, 3))

    
    def test_divide_numbers(self):
        self.assertEqual("The answer is 2.0", divide_numbers(10, 5))

    

    

