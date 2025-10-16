import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixture - create Calculator instance before each test"""
        self.calc = Calculator()
    
    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5
    
    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)  # Expect 5 - 3 = 2
    
    def test_multiply(self):
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12)  # Expect 4 * 3 = 12
    
    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)  # Expect 10 / 2 = 5.0 (float)
    
    def test_divide_non_exact(self):
        result = self.calc.divide(7, 2)
        self.assertAlmostEqual(result, 3.5)  # Expect 7 / 2 = 3.5
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)  # Expect ValueError when dividing by zero

if __name__ == "__main__":
    unittest.main()