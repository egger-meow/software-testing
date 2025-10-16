# Test-Driven Development (TDD) Narrative for Calculator

## Student: [Your Name]
## Date: October 10, 2025
## Assignment: Homework 2 - CalcTDD

---

## Overview

This document describes the Test-Driven Development process used to extend the Calculator class with three new operations: **subtract**, **multiply**, and **divide**. The implementation follows the TDD red-green-refactor cycle:

1. **RED**: Write a failing test
2. **GREEN**: Write minimal code to make the test pass
3. **REFACTOR**: Improve the code while keeping tests green

---

## Initial State

The Calculator class initially implemented only one function:
- `add(a, b)` - returns the sum of two integers

The goal was to add three new operations using TDD principles.

---

## TDD Cycle 1: Subtract Operation

### Step 1: Write a Failing Test (RED)

**Test Created:**
```python
def test_subtract(self):
    calc = Calculator()
    result = calc.subtract(5, 3)
    self.assertEqual(result, 2)  # Expect 5 - 3 = 2
```

**Java equivalent:**
```java
@Test public void testSubtract()
{
    assertTrue ("Calc subtract incorrect", 2 == Calc.subtract (5, 3));
}
```

**JavaScript equivalent:**
```javascript
test("test_subtract", () => {
    assertEqual(Calc.subtract(5, 3), 2, "Subtraction failed");
});
```

**Rationale:** This test defines the requirement that the Calculator should be able to subtract one integer from another. Running this test produces an error because the `subtract` method doesn't exist yet.

**Test Result:** ❌ FAILED (Method not found)

### Step 2: Implement Minimum Code (GREEN)

**Code Added:**
```python
def subtract(self, a, b):
    """Subtract b from a"""
    return a - b
```

**Changes Made:**
- Added `subtract` method to Calculator class
- Takes two parameters: `a` (minuend) and `b` (subtrahend)
- Returns the difference `a - b`

**Test Result:** ✅ PASSED

### Step 3: Refactor

**Refactoring:** No refactoring needed. The implementation is already simple and follows the single responsibility principle.

---

## TDD Cycle 2: Multiply Operation

### Step 1: Write a Failing Test (RED)

**Test Created:**
```python
def test_multiply(self):
    calc = Calculator()
    result = calc.multiply(4, 3)
    self.assertEqual(result, 12)  # Expect 4 * 3 = 12
```

**Java equivalent:**
```java
@Test public void testMultiply()
{
    assertTrue ("Calc multiply incorrect", 12 == Calc.multiply (4, 3));
}
```

**JavaScript equivalent:**
```javascript
test("test_multiply", () => {
    assertEqual(Calc.multiply(4, 3), 12, "Multiplication failed");
});
```

**Rationale:** This test defines the requirement for multiplication functionality. The test expects the product of two integers.

**Test Result:** ❌ FAILED (Method not found)

### Step 2: Implement Minimum Code (GREEN)

**Code Added:**
```python
def multiply(self, a, b):
    """Multiply two numbers"""
    return a * b
```

**Changes Made:**
- Added `multiply` method to Calculator class
- Takes two parameters: `a` and `b` (factors)
- Returns the product `a * b`

**Test Result:** ✅ PASSED

### Step 3: Refactor

**Refactoring:** No refactoring needed. The implementation is straightforward and efficient.

---

## TDD Cycle 3: Divide Operation

### Step 1: Write a Failing Test (RED)

**Design Decision:** Before writing the test, we made a critical decision: **Should division return an integer or a floating-point number?**

**Decision:** Division should return a **floating-point number** (float/double) to preserve precision. For example, 10 ÷ 3 should return 3.333... not 3.

**Test Created:**
```python
def test_divide(self):
    calc = Calculator()
    result = calc.divide(10, 2)
    self.assertEqual(result, 5.0)  # Expect 10 / 2 = 5.0
```

**Java equivalent:**
```java
@Test public void testDivide()
{
    assertEquals ("Calc divide incorrect", 5.0, Calc.divide (10, 2), 0.001);
}
```

**JavaScript equivalent:**
```javascript
test("test_divide", () => {
    assertEqual(Calc.divide(10, 2), 5.0, "Division failed");
});
```

**Rationale:** This test defines the requirement that division should return a floating-point result.

**Test Result:** ❌ FAILED (Method not found)

### Step 2: Implement Minimum Code (GREEN)

**Code Added:**
```python
def divide(self, a, b):
    """Divide a by b, returns float"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

**Java equivalent:**
```java
static public double divide (int a, int b)
{
    if (b == 0) {
        throw new IllegalArgumentException("Cannot divide by zero");
    }
    return (double) a / b;
}
```

**Changes Made:**
- Added `divide` method to Calculator class
- Takes two parameters: `a` (dividend) and `b` (divisor)
- Returns floating-point result `a / b`
- **Important:** Added validation to prevent division by zero

**Test Result:** ✅ PASSED

### Step 3: Refactor

**Refactoring Consideration:** We added error handling for division by zero, which is good defensive programming. However, this added logic should be tested!

---

## TDD Cycle 4: Edge Case - Division by Zero

### Step 1: Write a Failing Test (RED)

**Test Created:**
```python
def test_divide_by_zero(self):
    calc = Calculator()
    with self.assertRaises(ValueError):
        calc.divide(10, 0)
```

**Java equivalent:**
```java
@Test(expected = IllegalArgumentException.class)
public void testDivideByZero()
{
    Calc.divide (10, 0);
}
```

**JavaScript equivalent:**
```javascript
test("test_divide_by_zero", () => {
    assertThrows(() => Calc.divide(10, 0), "Divide by zero should throw error");
});
```

**Rationale:** Division by zero is undefined and should raise an exception rather than return an incorrect value or crash unexpectedly.

**Test Result:** ✅ PASSED (Exception handling already implemented)

### Step 2: Implementation

**No changes needed** - The exception handling was already added in the previous step.

### Step 3: Refactor

**Refactoring:** No refactoring needed.

---

## Final Implementation Summary

### Python (Calc.py)
```python
class Calculator:
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b, returns float"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
```

### Test Coverage
- ✅ Addition of positive integers
- ✅ Subtraction of positive integers
- ✅ Multiplication of positive integers
- ✅ Division with floating-point precision
- ✅ Division by zero error handling

---

## Key TDD Principles Demonstrated

1. **Test First:** Every feature was defined by a test before implementation
2. **Red-Green-Refactor:** Followed the TDD cycle strictly
3. **Minimal Implementation:** Only wrote code necessary to pass tests
4. **Incremental Development:** Added one feature at a time
5. **Requirements as Tests:** Design decisions (like returning float for division) were encoded in tests
6. **Edge Case Testing:** Considered and tested error conditions (division by zero)

---

## Design Decisions

### 1. Division Return Type
**Decision:** Return floating-point numbers (float/double) instead of integers.

**Rationale:**
- Preserves precision (e.g., 7 ÷ 2 = 3.5, not 3)
- More mathematically correct
- Follows Python's default division behavior (Python 3)

### 2. Error Handling for Division by Zero
**Decision:** Throw an exception rather than return a special value or crash.

**Rationale:**
- Division by zero is an error condition, not a valid operation
- Exceptions allow calling code to handle the error appropriately
- Prevents silent failures and undefined behavior

### 3. Static Methods (Java/JavaScript)
**Decision:** Used static methods in Java and JavaScript implementations.

**Rationale:**
- Calculator operations are stateless (no instance variables needed)
- Static methods are more efficient (no object instantiation required)
- Consistent with the original `add` implementation

---

## Multi-Language Implementation

All functionality was implemented in three languages:

1. **Python** (Calc.py, CalcTest.py)
   - Used unittest framework
   - Python 3 division operator (/) returns float by default
   - Raises ValueError for division by zero

2. **Java** (Calc.java, CalcTest.java)
   - Used JUnit 4 framework
   - Explicit cast to double for division
   - Throws IllegalArgumentException for division by zero

3. **JavaScript** (Calc.js, CalcTest.js)
   - Custom test framework (simple but effective)
   - JavaScript division naturally returns float
   - Throws Error for division by zero

---

## Testing Results

All tests pass successfully in all three implementations. See the accompanying screenshot for proof of test execution.

### Python Test Output
```
test_add (__main__.TestCalculator) ... ok
test_divide (__main__.TestCalculator) ... ok
test_divide_by_zero (__main__.TestCalculator) ... ok
test_multiply (__main__.TestCalculator) ... ok
test_subtract (__main__.TestCalculator) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

---

## Conclusion

This assignment successfully demonstrated Test-Driven Development by:
1. Writing failing tests first for each new feature
2. Implementing minimal code to make tests pass
3. Refactoring when necessary
4. Encoding design decisions in automated tests
5. Testing edge cases and error conditions
6. Achieving 100% test coverage for all implemented operations

The final Calculator class now supports four basic arithmetic operations with proper error handling, and all functionality is backed by comprehensive automated tests.

---

## Files Submitted

1. **Calc.py** - Python implementation of Calculator class
2. **CalcTest.py** - Python unit tests
3. **Calc.java** - Java implementation of Calc class
4. **CalcTest.java** - Java JUnit tests
5. **Calc.js** - JavaScript implementation of Calc class
6. **CalcTest.js** - JavaScript tests
7. **TDD_NARRATIVE.md** - This document
8. **test_results_screenshot.png** - Screenshot showing all tests pass
