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
├── README.md                           # This file
├── src/                                # Source code
│   ├── python/
│   │   └── Calc.py                     # Python implementation
│   ├── javascript/
│   │   └── Calc.js                     # JavaScript implementation
│   └── java/
│       └── Calc.java                   # Java implementation
├── tests/                              # Test files
│   ├── python/
│   │   └── CalcTest.py                 # Python unit tests
│   ├── javascript/
│   │   └── CalcTest.js                 # JavaScript tests
│   └── java/
│       └── CalcTest.java               # Java JUnit tests
├── docs/                               # Documentation
│   ├── TDD_NARRATIVE.md                # Detailed TDD narrative
│   ├── CalcTDD.pdf                     # Assignment specification
│   ├── CODE_PRINTOUT.md                # Code printout
│   ├── SUBMISSION_SUMMARY.md           # Submission summary
│   ├── HOW_TO_SUBMIT.md                # Submission guide
│   └── image.png                       # Screenshot
└── scripts/                            # Utility scripts
    └── run_all_tests.ps1               # PowerShell script to run all tests
```

## Running Tests

### Run All Tests (Recommended)
```bash
# Using PowerShell script (from project root)
.\scripts\run_all_tests.ps1
```

### Python Tests
```bash
# From project root
cd tests/python
python -m unittest CalcTest.py -v
cd ../..

# Or run directly
python tests/python/CalcTest.py
```

### Java Tests
```bash
# Compile (requires JUnit 4 in classpath) - from project root
javac -cp .;junit-4.13.2.jar src/java/Calc.java tests/java/CalcTest.java

# Run tests
java -cp .;junit-4.13.2.jar;hamcrest-core-1.3.jar org.junit.runner.JUnitCore tests.java.CalcTest
```

### JavaScript Tests
```bash
# From project root
cd tests/javascript
node CalcTest.js
cd ../..

# Or run directly
node tests/javascript/CalcTest.js
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

1. Source code in `src/` directory (organized by language)
2. Test code in `tests/` directory (organized by language)
3. Documentation in `docs/` directory
4. Utility scripts in `scripts/` directory
5. This README at project root

## Author
[Your Name]

## Date
October 10, 2025

## Assignment
Software Testing - Homework 2: Test-Driven Development
