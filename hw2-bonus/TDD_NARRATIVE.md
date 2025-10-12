# TDD Narrative: Sudoku in Python

**Course**: Software Testing | **Assignment**: HW2 Bonus  
**Stack**: Python + pytest | **Author**: [Your Name]

---

## TL;DR

Built a Sudoku app using strict TDD (Red-Green-Refactor). Implemented:
- ✅ Validation engine
- ✅ Backtracking solver  
- ✅ Puzzle generator
- ✅ **Bonus**: Error handling

**Stats**: 9 tests, 100% pass rate, ~400 LOC

---

## Part 1: Core Features

### 🔴 Feature 1: Validation Engine

**Goal**: Check if placing a number breaks Sudoku rules

**Test** (`test_is_valid`):
```python
board = SudokuBoard(initial_grid)
assert board.is_valid(0, 2, 4) is True   # ✓ valid
assert board.is_valid(0, 2, 5) is False  # ✗ row conflict  
assert board.is_valid(0, 2, 8) is False  # ✗ col conflict
assert board.is_valid(1, 1, 9) is False  # ✗ box conflict
```

Tests all 3 Sudoku rules. Test fails → **RED** ✓

**🟢 Implementation**:
```python
def is_valid(self, row, col, num):
    # Check row, column, 3x3 box
    # Return False if conflict, True otherwise
```

Used `deepcopy` for grid, integer division for box calculation. Tests pass → **GREEN** ✓

**🔵 Refactor**: Code already clean, no changes needed.

### 🔴 Feature 2: Backtracking Solver

**Goal**: Solve any valid Sudoku puzzle

**Test** (`test_solve`):
```python
puzzle = SudokuBoard(incomplete_grid)
assert puzzle.solve() is True
assert puzzle.grid == expected_solution
```

Test with known puzzle/solution. Test fails → **RED** ✓

**🟢 Implementation**:
```python
def solve(self, randomize=False):
    empty = self.find_empty()
    if not empty: return True  # Done!
    
    row, col = empty
    for num in (shuffled if randomize else [1..9]):
        if self.is_valid(row, col, num):
            self.grid[row][col] = num
            if self.solve(randomize): return True
            self.grid[row][col] = 0  # Backtrack
    return False
```

Classic recursive backtracking. Added `randomize` flag for generator later. Tests pass → **GREEN** ✓

**🔵 Refactor**: Clean recursive solution, no changes.

### 🔴 Feature 3: Puzzle Generator

**Goal**: Create random puzzles with variable difficulty

**Test** (`test_generate`):
```python
puzzle, solution = generate(difficulty=45)
assert sum(row.count(0) for row in puzzle.grid) == 45
assert SudokuBoard(puzzle.grid).solve() is True  # Solvable
assert is_complete_and_valid(solution)  # Valid solution
```

Tests empty cell count, solvability, and solution validity. Tests fail → **RED** ✓

**🟢 Implementation**:
```python
def generate(difficulty):
    # Generate random complete solution
    solution = SudokuBoard([[0]*9 for _ in range(9)])
    solution.solve(randomize=True)  # Use randomized solver
    
    # Remove cells to create puzzle
    puzzle = SudokuBoard(solution.grid)
    removed = 0
    while removed < difficulty:
        row, col = random.randint(0,8), random.randint(0,8)
        if puzzle.grid[row][col] != 0:
            puzzle.grid[row][col] = 0
            removed += 1
    
    return puzzle, solution
```

Leveraged existing solver with randomization. Tests pass → **GREEN** ✓

**🔵 Refactor**: Fixed test - initially checked exact solution match, but puzzles can have multiple solutions. Refactored to validate *properties* instead.

---

## Part 2: Bonus Feature (2.3)

### 🔴 Error Handling & Validation

**Goal**: Don't crash on bad input, give helpful errors

**Tests** (5 new tests):
1. `test_validate_puzzle_with_invalid_numbers` - Reject num > 9 or < 0
2. `test_validate_puzzle_with_duplicate_givens` - Catch initial duplicates
3. `test_validate_puzzle_wrong_dimensions` - Reject non-9x9 grids
4. `test_solve_unsolvable_puzzle` - Return False, don't hang
5. `test_valid_puzzle_passes_validation` - Accept good puzzles

All fail → **RED** ✓

**🟢 Implementation**:
```python
def validate_puzzle(grid):
    # Check dimensions (9x9)
    # Check numbers (0-9 only)
    # Check no duplicate givens
    return (is_valid, error_message)
```

Returns tuple: `(True, "")` if valid, `(False, "specific error")` if not.

Tests pass → **GREEN** ✓

**🔵 Refactor**: Code clean, descriptive errors. Good to go.

---

## Final Stats

```bash
9 passed in 2.45s  # 4 core + 5 bonus tests
```

## Key Takeaways

**What Worked**:
- ✅ Test-first kept design clean
- ✅ Small cycles = steady progress
- ✅ Tests = living documentation
- ✅ Refactoring without fear

**Challenges**:
- Testing random generation → test invariants, not exact output
- Multiple solutions exist → validate properties, not exact matches
- Balance: concrete tests, but don't test implementation details

**Result**: 9/9 tests passing, clean codebase, bonus feature included.


---

# Appendix: AI & Team Collaboration Log

## Team Composition
**Solo work** - no team members. Individual assignment.

---

## AI Usage Summary

**Tool**: Claude (Anthropic)  
**Date**: Oct 12, 2025  
**Duration**: ~3 hours  
**Role**: Pair programming partner for TDD

### Development Flow

| Phase | Time | What Happened |
|-------|------|---------------|
| **1. Requirements** | 15min | AI read assignment docs, understood Part 1 (core) + Part 2 (bonus) |
| **2. Task 1.1** | 20min | RED: Wrote `test_is_valid` → GREEN: Implemented validation → REFACTOR: Clean |
| **3. Task 1.2** | 25min | RED: Wrote `test_solve` → GREEN: Backtracking algorithm → REFACTOR: Clean |
| **4. Task 1.3** | 30min | RED: Wrote `test_generate` → GREEN: Random generator → REFACTOR: Fixed test logic |
| **5. Docs v1** | 20min | Generated README, narrative, demo |
| **6. Bonus Check** | 5min | Evaluated bonuses, picked 2.3 (error handling) as most practical |
| **7. Bonus 2.3** | 45min | RED: 5 error tests → GREEN: `validate_puzzle()` → REFACTOR: Good errors |
| **8. Docs v2** | 15min | Updated all docs with bonus |
| **9. Verify** | 10min | Ran pytest (9/9 ✓), ran demo (4/4 ✓) |

### Division of Labor

**AI did**:
- Wrote all test code (TDD style)
- Implemented all production code
- Generated docs & demo
- Followed strict Red-Green-Refactor

**Student did**:
- Directed overall approach
- Chose to implement Bonus 2.3
- Reviewed & approved all code
- Made final decisions

### Learnings

- ✅ TDD discipline pays off
- ✅ Small cycles >> big bang approach
- ✅ Tests = executable specs
- ✅ Error handling matters
- ✅ Evaluate feature ROI (did 2.3, skipped complex ones)

### Challenges & Solutions

| Problem | Solution |
|---------|----------|
| How to test random output? | Test invariants (empty cells, solvability) |
| Multiple valid solutions exist | Validate properties, not exact matches |
| Initial test too strict | Refactored to check what actually matters |

---

## Transparency Statement

Per course policy: All code written with AI pair programming. Student controlled direction, reviewed everything, made all final decisions. TDD strictly followed throughout.

**Student**: [Your Name] | **Date**: Oct 12, 2025 | **Course**: Software Testing
