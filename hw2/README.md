# Calculator TDD Homework

## Overview
This repository contains a Test-Driven Development implementation of a Calculator class with four basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division

## Files Structure

```
hw2/
├── Calc.py              # Python implementation
├── CalcTest.py          # Python unit tests
├── Calc.java            # Java implementation
├── CalcTest.java        # Java JUnit tests
├── Calc.js              # JavaScript implementation
├── CalcTest.js          # JavaScript tests
├── TDD_NARRATIVE.md     # Detailed TDD narrative
├── README.md            # This file
└── CalcTDD.pdf          # Assignment specification
```

## Running Tests

### Python Tests
```bash
# Run with unittest
python -m unittest CalcTest.py

# Or run directly
python CalcTest.py

# Verbose output
python CalcTest.py -v
```

### Java Tests
```bash
# Compile (requires JUnit 4 in classpath)
javac -cp .;junit-4.13.2.jar;hamcrest-core-1.3.jar Calc.java CalcTest.java

# Run tests
java -cp .;junit-4.13.2.jar;hamcrest-core-1.3.jar org.junit.runner.JUnitCore CalcTest
```

### JavaScript Tests
```bash
# Run with Node.js
node CalcTest.js
```

## Expected Test Output

### Python
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

### JavaScript
```
Running Calc tests...

✓ test_add
✓ test_subtract
✓ test_multiply
✓ test_divide
✓ test_divide_by_zero

All tests completed!
```

## Implementation Details

### Operations Implemented

1. **add(a, b)** - Returns the sum of two numbers
2. **subtract(a, b)** - Returns the difference (a - b)
3. **multiply(a, b)** - Returns the product of two numbers
4. **divide(a, b)** - Returns the quotient (a / b) as a floating-point number
   - Throws exception if b is zero

### Design Decisions

1. **Division returns floating-point** - To preserve precision (e.g., 7 ÷ 2 = 3.5)
2. **Division by zero throws exception** - Prevents undefined behavior
3. **Static methods** (Java/JavaScript) - Calculator operations are stateless

## TDD Process

Each feature was developed following the Red-Green-Refactor cycle:

1. **RED** - Write a failing test
2. **GREEN** - Write minimal code to pass
3. **REFACTOR** - Improve code quality

See `TDD_NARRATIVE.md` for detailed descriptions of each TDD cycle.

## Test Coverage

All implementations include tests for:
- ✅ Basic addition
- ✅ Basic subtraction
- ✅ Basic multiplication
- ✅ Basic division with floating-point result
- ✅ Division by zero error handling

## Submission Contents

1. Source code (Calc.py, Calc.java, Calc.js)
2. Test code (CalcTest.py, CalcTest.java, CalcTest.js)
3. TDD narrative document (TDD_NARRATIVE.md)
4. This README
5. Screenshot showing all tests pass

## Author
[Your Name]

## Date
October 10, 2025

## Assignment
Software Testing - Homework 2: Test-Driven Development
