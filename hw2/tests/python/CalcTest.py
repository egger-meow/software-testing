import unittest
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src' / 'python'))
from Calc import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5
    
    # TDD Step 1: Test for subtract (FAILING TEST)
    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)  # Expect 5 - 3 = 2
    
    # TDD Step 2: Test for multiply (FAILING TEST)
    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 3)
        self.assertEqual(result, 12)  # Expect 4 * 3 = 12
    
    # TDD Step 3: Test for divide (FAILING TEST)
    # Decision: divide should return float for precision
    def test_divide(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5.0)  # Expect 10 / 2 = 5.0
    
    # TDD Step 4: Test for divide by zero (edge case)
    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()