# Code Submission - TDD Calculator Enhancement
## Homework 3 - Test-Driven Development

**Date:** October 16, 2025  
**Assignment:** Add subtract, multiply, and divide operations to Calculator using TDD

---

## Final Calculator Implementation

### File: `Calc.py`

```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
```

**Lines of Code:** 14  
**Methods:** 4 (add, subtract, multiply, divide)  
**Features:**
- All four basic arithmetic operations
- Error handling for division by zero
- Returns float for division (precise results)
- Clean, minimal implementation

---

## Complete Test Suite

### File: `CalcTest.py`

```python
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
```

**Test Count:** 6 tests  
**Coverage:**
- Basic arithmetic operations (add, subtract, multiply, divide)
- Edge case: non-exact division
- Error case: division by zero

---

## Test Execution Results

### Command
```bash
python -m unittest CalcTest.py -v
```

### Output
```
test_add (CalcTest.TestCalculator) ... ok
test_divide (CalcTest.TestCalculator) ... ok
test_divide_by_zero (CalcTest.TestCalculator) ... ok
test_divide_non_exact (CalcTest.TestCalculator) ... ok
test_multiply (CalcTest.TestCalculator) ... ok
test_subtract (CalcTest.TestCalculator) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

### Alternative Output (pytest)
```bash
python -m pytest CalcTest.py -v
```

```
CalcTest.py::TestCalculator::test_add PASSED [ 16%]
CalcTest.py::TestCalculator::test_divide PASSED [ 33%]
CalcTest.py::TestCalculator::test_divide_by_zero PASSED [ 50%]
CalcTest.py::TestCalculator::test_divide_non_exact PASSED [ 66%]
CalcTest.py::TestCalculator::test_multiply PASSED [ 83%]
CalcTest.py::TestCalculator::test_subtract PASSED [100%]

============ 6 passed in 0.02s =============
```

---

## Test Results Summary

| Test Name | Purpose | Expected Result | Actual Result | Status |
|-----------|---------|-----------------|---------------|--------|
| `test_add` | Addition operation | 2 + 3 = 5 | 5 | ✅ PASS |
| `test_subtract` | Subtraction operation | 5 - 3 = 2 | 2 | ✅ PASS |
| `test_multiply` | Multiplication operation | 4 × 3 = 12 | 12 | ✅ PASS |
| `test_divide` | Basic division | 10 ÷ 2 = 5.0 | 5.0 | ✅ PASS |
| `test_divide_non_exact` | Non-exact division | 7 ÷ 2 = 3.5 | 3.5 | ✅ PASS |
| `test_divide_by_zero` | Error handling | ValueError raised | ValueError | ✅ PASS |

**Overall Result:** ✅ **ALL TESTS PASS (6/6)**

---

## Design Decisions

### 1. Division Returns Float
**Decision:** Use Python's true division operator `/` which returns float.

**Rationale:**
- More mathematically accurate than integer division
- Handles non-exact divisions correctly (7 ÷ 2 = 3.5, not 3)
- Matches behavior of real-world calculators
- Encoded in tests before implementation

### 2. Division by Zero Handling
**Decision:** Raise `ValueError` with descriptive message.

**Rationale:**
- Clearer than allowing Python's default `ZeroDivisionError`
- Provides custom error message: "Cannot divide by zero"
- Allows calling code to catch and handle specifically
- Tested with `assertRaises()` to verify behavior

### 3. Test Fixture with setUp()
**Decision:** Use `setUp()` method to create Calculator instance.

**Rationale:**
- Eliminates code duplication across tests
- Follows unittest best practices
- Each test still gets a fresh instance
- Easier to maintain and modify

---

## TDD Process Verification

### Evidence of TDD Methodology

#### Cycle 1: Subtract
1. ❌ **RED:** Wrote `test_subtract()` → AttributeError
2. ✅ **GREEN:** Implemented `subtract()` → Test passes
3. ♻️ **REFACTOR:** No changes needed

#### Cycle 2: Multiply
1. ❌ **RED:** Wrote `test_multiply()` → AttributeError
2. ✅ **GREEN:** Implemented `multiply()` → Test passes
3. ♻️ **REFACTOR:** No changes needed

#### Cycle 3: Divide
1. ❌ **RED:** Wrote 3 divide tests → All AttributeError
2. ✅ **GREEN:** Implemented `divide()` → All tests pass
3. ♻️ **REFACTOR:** Added `setUp()` method → All tests still pass

---

## File Structure

```
hw2/
├── Calc.py                          # Calculator implementation
├── CalcTest.py                      # Complete test suite
└── docs/
    ├── TDD_HOMEWORK_NARRATIVE.md    # Detailed TDD process narrative
    └── CODE_SUBMISSION.md           # This file - code printout
```

---

## How to Run Tests

### Prerequisites
```bash
# Python 3.x required
python --version

# Optional: Install pytest for enhanced output
pip install pytest
```

### Run with unittest (built-in)
```bash
# Verbose output
python -m unittest CalcTest.py -v

# Simple output
python CalcTest.py
```

### Run with pytest (if installed)
```bash
# Verbose output
python -m pytest CalcTest.py -v

# With coverage report
python -m pytest CalcTest.py --cov=Calc
```

### Expected Output
All 6 tests should pass with OK status.

---

## Submission Checklist

- ✅ All tests pass (6/6)
- ✅ Final version of Calc.py included
- ✅ All test code in CalcTest.py included
- ✅ Test execution output documented
- ✅ TDD narrative describing process
- ✅ Design decisions documented (float division, error handling)
- ✅ Refactoring documented (setUp method)

---

## Additional Notes

### Code Quality
- No code duplication
- Clear, descriptive variable names
- Proper error handling
- Comprehensive test coverage
- Follows Python conventions (PEP 8)

### Test Quality
- Each test focuses on single behavior
- Tests are independent and isolated
- Clear assertions with comments
- Edge cases covered (division by zero, non-exact division)
- Uses appropriate assertion methods

### TDD Benefits Demonstrated
- Tests documented requirements before implementation
- Incremental development prevented integration issues
- Refactoring was safe due to test coverage
- Design decisions encoded in tests
- High confidence in code correctness

---

**End of Code Submission Document**
