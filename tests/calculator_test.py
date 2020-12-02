import unittest
from modules.calculator import add, divide, multiply, subtract


class TestCalculator(unittest.TestCase):
    def test_calculator(self):

        self.assertEqual(5, add(2, 3))
        self.assertEqual(5,subtract(8, 3))
        self.assertEqual(8,multiply(2, 4))
        self.assertEqual(4,divide(8,2))
