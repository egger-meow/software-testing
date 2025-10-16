# Calculator TDD - Homework 3

> **Test-Driven Development Implementation**  
> Software Testing Course | October 16, 2025

## 📋 Overview

A Calculator class enhanced using Test-Driven Development methodology. Starting with basic addition, I added subtract, multiply, and divide operations following strict Red-Green-Refactor cycles.

**Language:** Python  
**Test Framework:** unittest  
**Total Tests:** 6 (all passing ✅)

---

## 📁 Project Structure

```
hw2/
├── Calc.py                 # Calculator implementation
├── CalcTest.py             # Test suite (6 tests)
├── Calc.java               # Java version (reference)
├── Calc.js                 # JavaScript version (reference)
├── CalcTest.java           # Java tests (reference)
├── CalcTest.js             # JavaScript tests (reference)
├── docs/
│   ├── TDD_HOMEWORK_NARRATIVE.md    # Complete TDD process narrative
│   ├── CODE_SUBMISSION.md           # Code printouts & test results
│   ├── HOMEWORK_SUMMARY.md          # Quick overview
│   ├── hw3.md                       # Assignment instructions
│   ├── teachers_words.txt           # AI interaction requirements
│   └── image.png                    # Assignment screenshot
└── README.md               # This file
```

---

## 🚀 Quick Start

### Run Tests

```bash
# Using unittest (recommended)
python -m unittest CalcTest.py -v

# Using pytest
python -m pytest CalcTest.py -v

# Direct execution
python CalcTest.py
```

### Expected Output

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

## 🔧 Operations Implemented

| Operation | Signature | Returns | Notes |
|-----------|-----------|---------|-------|
| **Add** | `add(a, b)` | Number | Sum of a and b |
| **Subtract** | `subtract(a, b)` | Number | Difference (a - b) |
| **Multiply** | `multiply(a, b)` | Number | Product of a and b |
| **Divide** | `divide(a, b)` | Float | Quotient (a / b) |

### Design Decisions

1. **Float Division** - Returns float for precision (7 ÷ 2 = 3.5, not 3)
2. **Error Handling** - Raises `ValueError` on division by zero
3. **Test-First** - All design decisions encoded in tests before implementation

---

## 📝 TDD Process Summary

### Cycle 1: Subtract
```
❌ RED → Write test_subtract() → Expected failure
✅ GREEN → Implement subtract() → Test passes
♻️ REFACTOR → Code clean, no changes needed
```

### Cycle 2: Multiply
```
❌ RED → Write test_multiply() → Expected failure
✅ GREEN → Implement multiply() → Test passes
♻️ REFACTOR → Code clean, no changes needed
```

### Cycle 3: Divide
```
❌ RED → Write 3 divide tests → All fail
✅ GREEN → Implement divide() with error handling → All pass
♻️ REFACTOR → Add setUp() method → Tests still pass
```

**Full narrative:** See [`docs/TDD_HOMEWORK_NARRATIVE.md`](docs/TDD_HOMEWORK_NARRATIVE.md)

---

## ✅ Test Coverage

| Test | Purpose | Status |
|------|---------|--------|
| `test_add` | Basic addition (2 + 3 = 5) | ✅ PASS |
| `test_subtract` | Basic subtraction (5 - 3 = 2) | ✅ PASS |
| `test_multiply` | Basic multiplication (4 × 3 = 12) | ✅ PASS |
| `test_divide` | Exact division (10 ÷ 2 = 5.0) | ✅ PASS |
| `test_divide_non_exact` | Non-exact division (7 ÷ 2 = 3.5) | ✅ PASS |
| `test_divide_by_zero` | Error handling (raises ValueError) | ✅ PASS |

**Coverage:** 100% of Calculator methods tested

---

## 📚 Documentation

- **[TDD_HOMEWORK_NARRATIVE.md](docs/TDD_HOMEWORK_NARRATIVE.md)** - First-person narrative documenting entire TDD process with Red-Green-Refactor cycles
- **[CODE_SUBMISSION.md](docs/CODE_SUBMISSION.md)** - Complete code printouts and test execution results
- **[HOMEWORK_SUMMARY.md](docs/HOMEWORK_SUMMARY.md)** - Quick overview and success metrics
- **AI Interaction Log** - Included in narrative appendix per course requirements

---

## 🎯 Key Learnings

1. **Tests Drive Design** - Writing tests first forces thoughtful API design
2. **Refactoring Confidence** - Comprehensive tests enable safe refactoring
3. **Small Steps Win** - Incremental development prevents complex debugging
4. **Tests as Documentation** - Test code serves as executable specification

---

## 🛠️ Technologies

- **Language:** Python 3.10+
- **Testing:** unittest (built-in)
- **Alternative:** pytest (optional)
- **TDD Methodology:** Red-Green-Refactor

---

## 📦 Submission Includes

- ✅ Final Calculator implementation (`Calc.py`)
- ✅ Complete test suite (`CalcTest.py`)
- ✅ TDD process narrative (first-person, student perspective)
- ✅ Code printouts with test results
- ✅ Design decision documentation
- ✅ AI interaction log (transparency per course policy)
- ✅ All tests passing screenshot evidence

---

## 👤 Author

**Student:** [Your Name]  
**Course:** Software Testing  
**Assignment:** Homework 3 - Test-Driven Development  
**Date:** October 16, 2025

---

## 📖 Assignment Requirements Met

- ✅ Add subtract, multiply, divide operations using TDD
- ✅ Follow Red-Green-Refactor cycle strictly
- ✅ Encode design decisions in tests (float division)
- ✅ Include comprehensive narrative of TDD process
- ✅ Document changes needed to pass each test
- ✅ Document refactoring decisions
- ✅ Submit code printouts
- ✅ Submit screenshot of all tests passing
- ✅ Include AI interaction log

**Status:** Complete and ready for submission 🎓
