# Sudoku Application - Test-Driven Development (TDD)

**Student**: 侯均頲 (109700046) | **Course**: Software Testing | **NYCU**

## Project Overview

A complete Sudoku application built using **strict TDD** (Red-Green-Refactor) methodology in Python.

### Core Features
1. **Rules Engine** - Validates Sudoku moves
2. **Backtracking Solver** - Solves any valid Sudoku puzzle
3. **Puzzle Generator** - Creates random puzzles with varying difficulty

### Bonus Features ⭐
- ✅ **Bonus 2.3**: Robust error handling with descriptive messages
- ✅ **Bonus 2.1**: Uniqueness guarantee (generates puzzles with exactly one solution)
- ✅ **Bonus 2.2**: Difficulty rating engine (rates puzzles as Easy/Medium/Hard)

**Stats**: 17 tests | 100% pass rate | ~530 LOC

## Quick Start

```bash
# Install dependencies
pip install pytest

# Run all tests
pytest test_sudoku.py -v

# Run demo
python demo.py
```

Expected output: **17 passed in 0.23s** ✅

## Files Structure

```
hw2-bonus/
├── sudoku.py                  # Main application logic (~530 LOC)
├── test_sudoku.py             # Comprehensive test suite (17 tests)
├── demo.py                    # Demonstration script
├── README.md                  # This file
├── TDD_NARRATIVE.md           # Complete TDD narrative report
├── SUBMISSION_INSTRUCTIONS.md # Submission checklist
├── requirements.txt           # Python dependencies
├── screenshots/               # Test screenshots (for submission)
│   └── all_tests_passing.png # Required: 17 tests passing
└── docs/                      # Reference documentation
    ├── TDD for sudoku.md
    └── ...
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pytest (for running tests)

### Install Dependencies
```bash
pip install pytest
```

## Running the Application

### Run Tests
```bash
# Run all tests
pytest test_sudoku.py -v

# Run with detailed output
pytest test_sudoku.py -vv
```

### Run Demo
```bash
python demo.py
```

## TDD Process Documentation

This project follows the **Red → Green → Refactor** cycle for each feature.

### Phase 1: Task 1.1 - Rules Engine (isValid)

#### 🔴 Red: Write Failing Tests
**File**: `test_sudoku.py` - `test_is_valid()`

**Test Cases Created**:
1. Valid placement - placing 4 at position (0, 2)
2. Row conflict - placing 5 at position (0, 2) when 5 exists in row
3. Column conflict - placing 8 at position (0, 2) when 8 exists in column
4. 3×3 box conflict - placing 9 at position (1, 1) when 9 exists in box

**Why These Tests?**
These tests cover all three core Sudoku rules:
- Each row must contain unique digits (1-9)
- Each column must contain unique digits (1-9)
- Each 3×3 box must contain unique digits (1-9)

#### 🟢 Green: Implement to Pass Tests
**File**: `sudoku.py` - `SudokuBoard.is_valid()`

**Implementation Strategy**:
```python
def is_valid(self, row, col, num):
    # Check row: iterate through all columns in the row
    # Check column: iterate through all rows in the column
    # Check 3×3 box: calculate box start position and iterate
    return True if all checks pass
```

**Key Design Decisions**:
- Used `deepcopy` for grid initialization to prevent mutation of original data
- Separated the three validation checks for clarity
- Used integer division (`//`) to calculate 3×3 box starting positions

#### 🔵 Refactor: Clean Up
The initial implementation was already clean and idiomatic:
- Clear separation of concerns (3 distinct checks)
- Readable variable names
- No duplication
- **No refactoring needed at this stage**

---

### Phase 2: Task 1.2 - Backtracking Solver (solve)

#### 🔴 Red: Write Failing Tests
**File**: `test_sudoku.py` - `test_solve()`

**Test Case Created**:
- Provide an incomplete puzzle with a known solution
- Assert that `solve()` returns `True`
- Assert that the solved board matches the expected solution

**Why This Test?**
This test ensures:
1. The solver can find a solution
2. The solution is correct (not just any valid board)
3. The solver modifies the board in-place

#### 🟢 Green: Implement Backtracking Algorithm
**File**: `sudoku.py` - `SudokuBoard.solve()` and `find_empty()`

**Implementation Strategy**:
```python
def solve(self, randomize=False):
    1. Find an empty cell (using find_empty helper)
    2. If no empty cell exists, puzzle is solved → return True
    3. Try numbers 1-9 in the empty cell
    4. For each number, check if it's valid
    5. If valid, place the number and recursively solve
    6. If recursion succeeds, return True
    7. If recursion fails, backtrack (set cell to 0) and try next number
    8. If all numbers fail, return False
```

**Key Design Decisions**:
- Added `randomize` parameter for future puzzle generation
- Used helper method `find_empty()` for single responsibility
- Classic recursive backtracking with state restoration

#### 🔵 Refactor: Clean Up
The implementation is a standard, elegant backtracking solution:
- Clear base case and recursive case
- Helper function for finding empty cells
- **No refactoring needed**

---

### Phase 3: Task 1.3 - Puzzle Generator (generate)

#### 🔴 Red: Write Failing Tests
**File**: `test_sudoku.py` - `test_generate()` and `test_generate_different_difficulties()`

**Test Cases Created**:
1. Verify the puzzle has the correct number of empty cells
2. Verify the puzzle is solvable
3. Verify the solution board is a valid complete solution
4. Test multiple difficulty levels (20, 40, 60 cells removed)

**Why These Tests?**
- **Empty cells test**: Ensures generator respects difficulty parameter
- **Solvability test**: Ensures generated puzzles can be solved
- **Solution validity test**: Ensures the provided solution is correct
- **Multiple difficulties**: Ensures generator works across a range

#### 🟢 Green: Implement Generator
**File**: `sudoku.py` - `generate()`

**Implementation Strategy**:
```python
def generate(difficulty):
    1. Create an empty 9×9 grid (all zeros)
    2. Solve it with randomize=True to get a random complete solution
    3. Create a copy of the solution as the puzzle
    4. Remove 'difficulty' number of cells randomly
    5. Return both puzzle and solution boards
```

**Key Design Decisions**:
- Leveraged existing `solve()` method with randomization
- Used `deepcopy` to create independent puzzle from solution
- Random cell removal ensures different puzzles each run
- Efficient: keeps trying random positions until enough cells removed

#### 🔵 Refactor: Improve Test Logic
**Refactoring Applied**: Modified test assertion logic

**Original Problem**: The test was checking if `puzzle_copy.grid == solution_board.grid`, but since the puzzle was created by removing cells from one solution, solving it again with a non-deterministic backtracking algorithm might produce a different (but still valid) solution.

**Refactored Solution**: Changed test to verify:
1. The puzzle is solvable (✓)
2. The solution board itself is valid and complete (✓)

This is more robust and tests the actual requirement.

---

## Test Results

All 17 tests pass successfully:

```bash
pytest test_sudoku.py -v
```

```
test_sudoku.py::test_is_valid PASSED                              [  5%]
test_sudoku.py::test_solve PASSED                                 [ 11%]
test_sudoku.py::test_generate PASSED                              [ 17%]
test_sudoku.py::test_generate_different_difficulties PASSED       [ 23%]
test_sudoku.py::test_validate_puzzle_with_invalid_numbers PASSED  [ 29%]
test_sudoku.py::test_validate_puzzle_with_duplicate_givens PASSED [ 35%]
test_sudoku.py::test_validate_puzzle_wrong_dimensions PASSED      [ 41%]
test_sudoku.py::test_solve_unsolvable_puzzle PASSED               [ 47%]
test_sudoku.py::test_valid_puzzle_passes_validation PASSED        [ 52%]
test_sudoku.py::test_count_solutions_single PASSED                [ 58%]
test_sudoku.py::test_count_solutions_multiple PASSED              [ 64%]
test_sudoku.py::test_count_solutions_none PASSED                  [ 70%]
test_sudoku.py::test_generate_unique_solution PASSED              [ 76%]
test_sudoku.py::test_rate_easy_puzzle PASSED                      [ 82%]
test_sudoku.py::test_rate_medium_puzzle PASSED                    [ 88%]
test_sudoku.py::test_rate_hard_puzzle PASSED                      [ 94%]
test_sudoku.py::test_human_solver_techniques PASSED               [100%]

======================== 17 passed in 0.23s =========================
```

**Breakdown**:
- 4 core tests (validation, solver, generator)
- 5 Bonus 2.3 tests (error handling)
- 4 Bonus 2.1 tests (uniqueness guarantee)
- 4 Bonus 2.2 tests (difficulty rating)

## Key TDD Principles Applied

### 1. **Test First**
Every feature was developed by:
- Writing the test first (Red)
- Watching it fail
- Then implementing the minimum code to pass (Green)

### 2. **Small Steps**
Each TDD cycle focused on a single, small feature:
- Task 1.1: Only validation
- Task 1.2: Only solving
- Task 1.3: Only generation

### 3. **Refactor with Confidence**
Tests act as a safety net, allowing refactoring without fear of breaking functionality.

### 4. **Executable Specification**
The test suite serves as living documentation of what the code should do.

### 5. **Design Through Testing**
Writing tests first influenced good design decisions:
- Clear method signatures
- Single responsibility (e.g., `find_empty()` helper)
- Proper abstraction (SudokuBoard class)

## Design Highlights

### Clean Architecture
- **SudokuBoard Class**: Encapsulates board state and operations
- **Separation of Concerns**: Each method has a single, clear purpose
- **Immutability Protection**: Uses `deepcopy` to prevent unintended mutations

### Algorithmic Efficiency
- **Backtracking Solver**: O(9^(empty cells)) worst case, but efficient pruning
- **Validation**: O(1) for each check (always checks 9+9+9 = 27 cells max)
- **Generation**: O(n) where n is the difficulty level

### Extensibility
The design demonstrates extensibility through implemented bonuses:
- ✅ Uniqueness checking via `count_solutions()` method (Bonus 2.1)
- ✅ Difficulty rating via human technique simulation (Bonus 2.2)
- ✅ Robust validation with descriptive errors (Bonus 2.3)
- Future: Different board sizes, more advanced techniques (X-Wing, Swordfish)

### Phase 4: Task 2.3 - Robust Error Handling (Bonus) ✅ COMPLETED

#### 🔴 Red: Write Failing Tests
**File**: `test_sudoku.py` - 5 new test functions for Bonus 2.3

**Test Cases Created**:
1. `test_validate_puzzle_with_invalid_numbers()` - Numbers outside 0-9 range
2. `test_validate_puzzle_with_duplicate_givens()` - Duplicates in rows/columns/boxes
3. `test_validate_puzzle_wrong_dimensions()` - Non-9x9 grids
4. `test_solve_unsolvable_puzzle()` - Unsolvable puzzle detection
5. `test_valid_puzzle_passes_validation()` - Valid puzzles accepted

**Why These Tests?**
These tests ensure robust error handling:
- Invalid input rejection (bad numbers, wrong size)
- Logical error detection (duplicate givens)
- Graceful failure (unsolvable puzzles return False, not crash)

#### 🟢 Green: Implement Validation Function
**File**: `sudoku.py` - `validate_puzzle(grid)`

**Implementation Strategy**:
```python
def validate_puzzle(grid):
    # Check 1: Correct dimensions (9x9)
    # Check 2: Valid numbers (0-9 only)
    # Check 3: No duplicate givens in rows, columns, boxes
    return (is_valid, error_message)
```

**Key Design Decisions**:
- Returns tuple: (bool, str) for both result and error message
- Comprehensive error messages for debugging
- Does not crash on invalid input
- Validates before any processing

#### 🔵 Refactor: Clean Up
The validation logic is clear and well-structured:
- Three distinct validation phases
- Descriptive error messages
- Early return on first error found
- **No refactoring needed**

---

## Bonus Features Summary

### Phase 5: Bonus 2.1 - Uniqueness Guarantee ✅

**Implementation**:
- `count_solutions()` - Counts all possible solutions (with optional limit for performance)
- `generate_unique()` - Generates puzzles with exactly one solution
- Uses iterative cell removal with uniqueness checking

**Key Technique**: After removing each cell, verify puzzle still has unique solution using `count_solutions(limit=2)`. If not unique, restore the cell.

### Phase 6: Bonus 2.2 - Difficulty Rating Engine ✅

**Implementation**:
- `HumanSolver` class - Simulates human solving techniques
- `rate_difficulty()` - Rates puzzles as Easy/Medium/Hard

**Techniques Implemented**:
- **Naked Singles**: Cell has only 1 possible value
- **Hidden Singles**: Value can only go in 1 cell in a unit
- **Naked Pairs**: Advanced technique detection

**Rating Logic**:
- Easy: Solvable with Naked Singles only
- Medium: Requires Hidden Singles
- Hard: Requires Naked Pairs or can't solve with basic techniques

## Learning Outcomes

Through this TDD exercise, we demonstrated:

1. ✅ **Red-Green-Refactor Cycle**: Applied rigorously for each feature (6 phases total)
2. ✅ **Test Design**: Created 17 comprehensive test cases covering happy paths and edge cases
3. ✅ **Incremental Development**: Built features one at a time with strict TDD discipline
4. ✅ **Code Quality**: Maintained clean, readable, maintainable code (~530 LOC)
5. ✅ **Documentation**: Tests serve as executable documentation
6. ✅ **Bonus Features**: Successfully implemented all 3 bonus features (2.1, 2.2, 2.3)

## Key Achievements

- 🎯 **100% Test Coverage**: All features have comprehensive test coverage
- 🚀 **All Bonuses Completed**: Uniqueness guarantee, difficulty rating, error handling
- 📐 **Clean Architecture**: SudokuBoard class + HumanSolver for technique simulation
- ⚡ **Performance Optimized**: Smart use of `limit` parameter in solution counting
- 📝 **Well Documented**: Complete TDD narrative in `TDD_NARRATIVE.md`

## References

- Assignment: `docs/TDD for sudoku.md`
- Implementation Guide: `docs/Sudoku Generator with TDD in Python.md`
- Developer Guide: `docs/The Ultimate Sudoku Developer's Guide.md`
- TDD Guide: `docs/A Comprehensive Guide to Test-Driven Development.md`
- Full TDD Narrative: `TDD_NARRATIVE.md`

---

## Author

**侯均頲** (109700046)  
Software Testing | NYCU  
Developed using strict TDD methodology with AI pair programming

## Repository

https://github.com/egger-meow/software-testing/tree/main/hw2-bonus

---

**License**: Educational use only
