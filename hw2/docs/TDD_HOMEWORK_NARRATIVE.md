# Test-Driven Development (TDD) Homework Narrative
## My Journey Enhancing the Calculator Class

**Student Name:** [Your Name]  
**Date:** October 16, 2025  
**Assignment:** Homework 3 - TDD Implementation

---

## Introduction

I enhanced a Calculator class using Test-Driven Development. Starting with only `add()`, I added subtract, multiply, and divide operations following the Red-Green-Refactor cycle. TDD isn't just about testing—it's a design methodology where tests drive implementation decisions.

---

## Getting Started

The Calculator started with one method: `add(a, b)`. First, I verified the existing test worked.

I fixed an import issue (`calculator` → `Calc`), ran the test, and got my first green checkmark.

**Initial Status:** ✅ 1 test passing

---

## TDD Cycle 1: Adding Subtraction

### RED Phase - Failing Test First

Following TDD, I wrote the test *before* the code:

```python
def test_subtract(self):
    calc = Calculator()
    result = calc.subtract(5, 3)
    self.assertEqual(result, 2)  # Expect 5 - 3 = 2
```

❌ Expected failure:

```
AttributeError: 'Calculator' object has no attribute 'subtract'
```

The test defined the requirement: 5 - 3 = 2.

---

### GREEN Phase - Implementation

Simplest code to pass:

```python
def subtract(self, a, b):
    return a - b
```

Test results:

```
CalcTest.py::TestCalculator::test_add PASSED [ 50%]
CalcTest.py::TestCalculator::test_subtract PASSED [100%]
============ 2 passed in 0.02s =============
```

✅ Both tests pass.

---

### REFACTOR Phase

Code is clean and consistent with `add()`. No refactoring needed.

---

## TDD Cycle 2: Adding Multiplication

### RED Phase - Failing Test

Test first:

```python
def test_multiply(self):
    calc = Calculator()
    result = calc.multiply(4, 3)
    self.assertEqual(result, 12)  # Expect 4 * 3 = 12
```

❌ Expected `AttributeError`. Writing tests first forces API design before implementation.

---

### GREEN Phase - Implementation

```python
def multiply(self, a, b):
    return a * b
```

```
CalcTest.py::TestCalculator::test_add PASSED [ 33%]
CalcTest.py::TestCalculator::test_multiply PASSED [ 66%]
CalcTest.py::TestCalculator::test_subtract PASSED [100%]
============ 3 passed in 0.02s =============
```

✅ 3 operations complete.

---

### REFACTOR Phase

No changes needed.

---

## TDD Cycle 3: Adding Division

### Design Decision: Integer or Float?

The assignment required encoding design decisions in tests. Should division return int or float?

- Integer division (`7 // 2 = 3`) loses precision
- Float division (`7 / 2 = 3.5`) is accurate
- Real calculators use floats

**Decision:** Float division. Encoded in tests first.

---

### RED Phase - Three Tests

Division needed comprehensive coverage:

**Test 1: Basic Division** - `test_divide()`
```python
def test_divide(self):
    calc = Calculator()
    result = calc.divide(10, 2)
    self.assertEqual(result, 5.0)  # Expect 10 / 2 = 5.0 (float)
```

**Test 2: Non-Exact Division** - `test_divide_non_exact()`
```python
def test_divide_non_exact(self):
    calc = Calculator()
    result = calc.divide(7, 2)
    self.assertAlmostEqual(result, 3.5)  # Expect 7 / 2 = 3.5
```

**Test 3: Division by Zero** - `test_divide_by_zero()`
```python
def test_divide_by_zero(self):
    calc = Calculator()
    with self.assertRaises(ValueError):
        calc.divide(10, 0)  # Expect ValueError when dividing by zero
```

❌ **Test Results: ALL 3 FAILED**
```
FAILED CalcTest.py::TestCalculator::test_divide - AttributeError
FAILED CalcTest.py::TestCalculator::test_divide_by_zero - AttributeError
FAILED CalcTest.py::TestCalculator::test_divide_non_exact - AttributeError
======= 3 failed, 3 passed in 0.13s ========
```

❌ Three failing tests = clear specification.

---

### GREEN Phase - Implementation with Error Handling

```python
def divide(self, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Implementation:
1. Checks for division by zero
2. Raises `ValueError` (clearer than `ZeroDivisionError`)
3. Uses `/` operator for float results

**Test Result:** ✅ ALL PASSED
```
CalcTest.py::TestCalculator::test_add PASSED [ 16%]
CalcTest.py::TestCalculator::test_divide PASSED [ 33%]
CalcTest.py::TestCalculator::test_divide_by_zero PASSED [ 50%]
CalcTest.py::TestCalculator::test_divide_non_exact PASSED [ 66%]
CalcTest.py::TestCalculator::test_multiply PASSED [ 83%]
CalcTest.py::TestCalculator::test_subtract PASSED [100%]
============ 6 passed in 0.02s =============
```

Six tests pass. Tests guided implementation of happy paths and edge cases.

---

### REFACTOR Phase - Eliminating Duplication

Every test started with `calc = Calculator()`. This violates DRY.

Solution: Use `setUp()` method:

**Before Refactoring:**
```python
def test_add(self):
    calc = Calculator()
    result = calc.add(2, 3)
    ...

def test_subtract(self):
    calc = Calculator()
    result = calc.subtract(5, 3)
    ...
```

**After Refactoring:**
```python
def setUp(self):
    """Set up test fixture - create Calculator instance before each test"""
    self.calc = Calculator()

def test_add(self):
    result = self.calc.add(2, 3)
    ...

def test_subtract(self):
    result = self.calc.subtract(5, 3)
    ...
```

**Benefits:**
- No repeated code across 6 tests
- Unittest best practice
- Each test gets fresh instance
- Easier to maintain

**Verification:**

```
Ran 6 tests in 0.001s
OK
```

✅ All tests still pass. TDD enables confident refactoring.

---

## Final Implementation

### Calculator Class (Calc.py)
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

### Test Suite (CalcTest.py)
```python
import unittest
from Calc import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixture - create Calculator instance before each test"""
        self.calc = Calculator()
    
    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)
    
    def test_multiply(self):
        result = self.calc.multiply(4, 3)
        self.assertEqual(result, 12)
    
    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_non_exact(self):
        result = self.calc.divide(7, 2)
        self.assertAlmostEqual(result, 3.5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
```

---

## Test Coverage Summary

| Operation | Test Cases | Status |
|-----------|-----------|--------|
| Addition | 1 test | ✅ PASS |
| Subtraction | 1 test | ✅ PASS |
| Multiplication | 1 test | ✅ PASS |
| Division | 3 tests (basic, non-exact, zero) | ✅ PASS |
| **TOTAL** | **6 tests** | **✅ ALL PASS** |

---

## Final Test Results

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

---

## TDD Principles Followed

### 1. Red-Green-Refactor Cycle
✅ Followed strictly:
- RED: Failing test first
- GREEN: Minimal code to pass
- REFACTOR: Improve quality

### 2. Test-First Development
✅ No code without failing test:
- Tests written before implementation
- Tests define requirements

### 3. Minimal Implementation
✅ No over-engineering:
- Only code needed to pass tests
- No speculative features

### 4. Continuous Testing
✅ Tests after every change:
- Before: Verify failure
- After implementation: Verify pass
- After refactoring: Verify pass

### 5. Design Through Tests
✅ Tests encode decisions:
- Division returns float
- Division by zero raises ValueError
- Clear assertions define behavior

---

## What I Learned

### Tests Are Living Documentation
Tests serve as executable specifications. Reading `CalcTest.py` shows what Calculator does without reading implementation.

### TDD Enables Confident Refactoring
Comprehensive test coverage made refactoring risk-free. Instant feedback if something breaks.

### Design Decisions in Tests
Writing tests first forces API design upfront. Error handling was designed in, not bolted on.

### Small Steps Prevent Problems
One operation at a time with full coverage. No multiple broken things to debug.

---

## Reflection

TDD transformed my understanding. I started thinking it was "just testing." I finished knowing it's a design methodology.

Final result:
- ✅ 6 tests passing
- ✅ Edge cases handled (division by zero, non-exact division)
- ✅ Design decisions in tests (float division)
- ✅ Clean, maintainable code
- ✅ Confident refactoring

**Key insight:** Tests drive design, not just verify it.

**Status:** Assignment complete.

---

## Appendix: Command History

```bash
# Initial test run (verify existing tests)
python -m pytest CalcTest.py -v

# After adding subtract test (RED phase)
python -m pytest CalcTest.py -v  # 1 failed, 1 passed

# After implementing subtract (GREEN phase)
python -m pytest CalcTest.py -v  # 2 passed

# After adding multiply test (RED phase)
python -m pytest CalcTest.py -v  # 1 failed, 2 passed

# After implementing multiply (GREEN phase)
python -m pytest CalcTest.py -v  # 3 passed

# After adding divide tests (RED phase)
python -m pytest CalcTest.py -v  # 3 failed, 3 passed

# After implementing divide (GREEN phase)
python -m pytest CalcTest.py -v  # 6 passed

# After refactoring tests (REFACTOR phase)
python -m pytest CalcTest.py -v  # 6 passed

# Final test run with unittest
python -m unittest CalcTest.py -v  # OK - 6 tests
```

---

## Appendix: AI & Collaboration Log

### AI Interaction Records

**Tool Used:** Windsurf Cascade (Claude AI)  
**Date:** October 16, 2025  
**Purpose:** Code generation, TDD guidance, documentation assistance

#### Key Interactions:

**1. Initial Setup & TDD Guidance**
- **Request:** Asked AI to help complete homework following strict TDD methodology
- **AI Role:** Guided through Red-Green-Refactor cycles, ensured failing tests written before implementation
- **Outcome:** Successfully followed TDD discipline for all three operations

**2. Design Decision Support**
- **Request:** Division implementation—integer vs. float decision
- **AI Role:** Helped analyze trade-offs, suggested writing tests to encode decision (per assignment requirements)
- **Outcome:** Chose float division, encoded in tests before implementation

**3. Error Handling**
- **Request:** How to handle division by zero
- **AI Role:** Suggested `ValueError` with descriptive message, created test with `assertRaises()`
- **Outcome:** Comprehensive error handling tested before implementation

**4. Test Refactoring**
- **Request:** AI noticed code duplication in tests
- **AI Role:** Suggested `setUp()` method following unittest best practices
- **Outcome:** Cleaner tests, verified with full test run

**5. Documentation**
- **Request:** Create TDD narrative
- **AI Role:** Structured narrative, documented Red-Green-Refactor cycles
- **Outcome:** Complete documentation with results and rationale

#### AI Usage Transparency

**Code Implementation:** AI generated code following TDD methodology (test-first approach)  
**Test Design:** Tests written per TDD discipline with AI assistance for syntax  
**Documentation:** AI helped structure narrative; content reflects actual implementation process  
**Learning Value:** AI served as pair programmer, teaching TDD methodology through hands-on practice

### Team Collaboration

**Team Size:** Individual assignment  
**Solo Work:** All implementation, testing, and documentation completed independently with AI assistance

### Commands Executed

```bash
# Test runs throughout TDD cycles
python -m pytest CalcTest.py -v          # Multiple runs after each implementation
python -m unittest CalcTest.py -v        # Final verification
```

### Reflection on AI-Assisted Learning

AI as a pair programmer enhanced learning. Rather than just answers, AI guided me through TDD methodology—failing tests first, minimal code, thoughtful refactoring. Hands-on practice beats lectures.

---

**End of TDD Narrative**
