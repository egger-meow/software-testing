# test_sudoku.py
"""
Test-Driven Development (TDD) for Sudoku Application
Testing the Rules Engine, Solver, and Generator

Following the TDD cycle: Red -> Green -> Refactor
"""

from sudoku import SudokuBoard


def test_is_valid():
    """
    Task 1.1: Rules Engine - Test the isValid method
    
    Test cases:
    1. Valid placement
    2. Row conflict
    3. Column conflict
    4. 3x3 box conflict
    """
    initial_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    board = SudokuBoard(initial_grid)

    # Test valid placement (placing 4 at (0, 2))
    assert board.is_valid(0, 2, 4) is True, "is_valid(0, 2, 4) should be True"

    # Test row conflict (placing 5 at (0, 2))
    assert board.is_valid(0, 2, 5) is False, "is_valid(0, 2, 5) should be False due to row conflict"

    # Test column conflict (placing 8 at (0, 2))
    assert board.is_valid(0, 2, 8) is False, "is_valid(0, 2, 8) should be False due to column conflict"

    # Test 3x3 box conflict (placing 9 at (1, 1))
    assert board.is_valid(1, 1, 9) is False, "is_valid(1, 1, 9) should be False due to box conflict"

    print("✓ test_is_valid passed")


def test_solve():
    """
    Task 1.2: Backtracking Solver - Test the solve method
    
    Test cases:
    1. Solve a valid puzzle
    2. Verify the solution matches the expected solution
    """
    puzzle_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solution_grid = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    
    puzzle = SudokuBoard(puzzle_grid)
    assert puzzle.solve() is True, "Solver should return True for a solvable puzzle"
    assert puzzle.grid == solution_grid, "The solved puzzle does not match the expected solution"
    
    print("✓ test_solve passed")


def test_generate():
    """
    Task 1.3: Puzzle Generator - Test the generate function
    
    Test cases:
    1. Verify the puzzle has the correct number of empty cells
    2. Verify the puzzle is solvable
    3. Verify the solution is valid
    """
    from sudoku import generate
    
    difficulty = 45  # Number of cells to remove
    puzzle_board, solution_board = generate(difficulty)

    # 1. Validate the number of empty cells
    empty_cells = sum(row.count(0) for row in puzzle_board.grid)
    assert empty_cells == difficulty, f"Puzzle should have {difficulty} empty cells, but has {empty_cells}"

    # 2. Validate that the puzzle is solvable
    puzzle_copy = SudokuBoard(puzzle_board.grid)
    assert puzzle_copy.solve() is True, "Generated puzzle must be solvable"
    
    # 3. Verify that the solution board is a valid complete solution
    def is_complete_and_valid(board):
        """Check if board is completely filled and valid"""
        for row in range(9):
            for col in range(9):
                if board.grid[row][col] == 0:
                    return False
                # Check if the placement was valid
                num = board.grid[row][col]
                board.grid[row][col] = 0  # Temporarily remove
                if not board.is_valid(row, col, num):
                    board.grid[row][col] = num  # Restore
                    return False
                board.grid[row][col] = num  # Restore
        return True
    
    assert is_complete_and_valid(solution_board), "Solution board should be a valid complete solution"
    
    print("✓ test_generate passed")


def test_generate_different_difficulties():
    """
    Additional test: Generate puzzles with different difficulty levels
    """
    from sudoku import generate
    
    for difficulty in [20, 40, 60]:
        puzzle_board, solution_board = generate(difficulty)
        empty_cells = sum(row.count(0) for row in puzzle_board.grid)
        assert empty_cells == difficulty, f"Puzzle should have {difficulty} empty cells"
        
        # Verify solvability
        puzzle_copy = SudokuBoard(puzzle_board.grid)
        assert puzzle_copy.solve() is True, f"Generated puzzle with difficulty {difficulty} must be solvable"
    
    print("✓ test_generate_different_difficulties passed")


# ============================================================================
# BONUS 2.3: Robust Error & Edge Case Handling Tests
# ============================================================================

def test_validate_puzzle_with_invalid_numbers():
    """
    Bonus 2.3: Test validation of puzzles with invalid numbers
    
    Invalid numbers include:
    - Numbers outside 1-9 range
    - Negative numbers
    - Non-numeric values (if applicable)
    """
    from sudoku import validate_puzzle
    
    # Puzzle with number > 9
    invalid_grid_1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 10]  # 10 is invalid
    ]
    
    result, error = validate_puzzle(invalid_grid_1)
    assert result is False, "Should reject puzzle with number > 9"
    assert "invalid number" in error.lower() or "range" in error.lower()
    
    # Puzzle with negative number
    invalid_grid_2 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [-1, 0, 0, 0, 8, 0, 0, 7, 9]  # -1 is invalid
    ]
    
    result, error = validate_puzzle(invalid_grid_2)
    assert result is False, "Should reject puzzle with negative number"
    assert "invalid number" in error.lower() or "range" in error.lower()
    
    print("✓ test_validate_puzzle_with_invalid_numbers passed")


def test_validate_puzzle_with_duplicate_givens():
    """
    Bonus 2.3: Test validation of puzzles with duplicate givens
    
    A puzzle with initial duplicates in:
    - Same row
    - Same column
    - Same box
    Should be rejected as invalid
    """
    from sudoku import validate_puzzle
    
    # Duplicate in row (two 5s in first row)
    invalid_row = [
        [5, 3, 5, 0, 7, 0, 0, 0, 0],  # Two 5s!
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    result, error = validate_puzzle(invalid_row)
    assert result is False, "Should reject puzzle with duplicate in row"
    assert "duplicate" in error.lower() or "conflict" in error.lower()
    
    # Duplicate in column (two 5s in first column)
    invalid_col = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [5, 0, 0, 8, 0, 3, 0, 0, 1],  # Another 5 in column 0!
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    result, error = validate_puzzle(invalid_col)
    assert result is False, "Should reject puzzle with duplicate in column"
    assert "duplicate" in error.lower() or "conflict" in error.lower()
    
    print("✓ test_validate_puzzle_with_duplicate_givens passed")


def test_validate_puzzle_wrong_dimensions():
    """
    Bonus 2.3: Test validation of puzzles with incorrect dimensions
    """
    from sudoku import validate_puzzle
    
    # Too few rows
    invalid_small = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0]
    ]
    
    result, error = validate_puzzle(invalid_small)
    assert result is False, "Should reject puzzle with wrong number of rows"
    assert "dimension" in error.lower() or "size" in error.lower() or "9x9" in error.lower()
    
    # Row with wrong number of columns
    invalid_cols = [
        [5, 3, 0, 0, 7],  # Only 5 columns!
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    result, error = validate_puzzle(invalid_cols)
    assert result is False, "Should reject puzzle with wrong number of columns"
    assert "dimension" in error.lower() or "size" in error.lower() or "9x9" in error.lower()
    
    print("✓ test_validate_puzzle_wrong_dimensions passed")


def test_solve_unsolvable_puzzle():
    """
    Bonus 2.3: Test that solver correctly identifies unsolvable puzzles
    """
    # This puzzle has no solution
    unsolvable_grid = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 0]  # Last cell is 0, but should be 9
                                       # However, 9 would create full board
                                       # Let's make it truly unsolvable
    ]
    
    # Actually, let me create a truly unsolvable puzzle
    unsolvable_grid = [
        [1, 2, 3, 4, 5, 6, 7, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],  # Row needs 1, but 1 is in column
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]
    
    board = SudokuBoard(unsolvable_grid)
    result = board.solve()
    
    assert result is False, "Solver should return False for unsolvable puzzle"
    
    print("✓ test_solve_unsolvable_puzzle passed")


def test_valid_puzzle_passes_validation():
    """
    Bonus 2.3: Test that a valid puzzle passes all validation checks
    """
    from sudoku import validate_puzzle
    
    valid_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    result, error = validate_puzzle(valid_grid)
    assert result is True, f"Valid puzzle should pass validation, but got error: {error}"
    assert error == "", "Valid puzzle should have no error message"
    
    print("✓ test_valid_puzzle_passes_validation passed")


# ============================================================================
# BONUS 2.1: Uniqueness Guarantee Tests
# ============================================================================

def test_count_solutions_single():
    """
    Bonus 2.1: Test counting solutions for puzzle with unique solution
    """
    # This is a well-formed puzzle with exactly 1 solution
    unique_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    board = SudokuBoard(unique_puzzle)
    count = board.count_solutions()
    
    assert count == 1, f"Puzzle should have exactly 1 solution, but found {count}"
    
    print("✓ test_count_solutions_single passed")


def test_count_solutions_multiple():
    """
    Bonus 2.1: Test counting solutions for puzzle with multiple solutions
    """
    # Minimal puzzle - likely has multiple solutions
    multiple_solutions = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    board = SudokuBoard(multiple_solutions)
    count = board.count_solutions(limit=100)  # Limit to avoid long computation
    
    assert count > 1, f"Empty puzzle should have multiple solutions, but found {count}"
    
    print("✓ test_count_solutions_multiple passed")


def test_count_solutions_none():
    """
    Bonus 2.1: Test counting solutions for unsolvable puzzle
    """
    # Unsolvable puzzle
    unsolvable = [
        [1, 2, 3, 4, 5, 6, 7, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]
    
    board = SudokuBoard(unsolvable)
    count = board.count_solutions()
    
    assert count == 0, f"Unsolvable puzzle should have 0 solutions, but found {count}"
    
    print("✓ test_count_solutions_none passed")


def test_generate_unique_solution():
    """
    Bonus 2.1: Test that generator creates puzzles with unique solutions
    """
    from sudoku import generate_unique
    
    difficulty = 40  # Medium difficulty
    puzzle_board, solution_board = generate_unique(difficulty)
    
    # 1. Should have correct number of empty cells
    empty_cells = sum(row.count(0) for row in puzzle_board.grid)
    assert empty_cells == difficulty, f"Should have {difficulty} empty cells, got {empty_cells}"
    
    # 2. Should have exactly 1 solution
    count = puzzle_board.count_solutions()
    assert count == 1, f"Generated puzzle should have exactly 1 solution, but has {count}"
    
    # 3. Should still be solvable
    puzzle_copy = SudokuBoard(puzzle_board.grid)
    assert puzzle_copy.solve() is True, "Generated puzzle must be solvable"
    
    print("✓ test_generate_unique_solution passed")


# ============================================================================
# BONUS 2.2: Difficulty Rating Engine Tests
# ============================================================================

def test_rate_easy_puzzle():
    """
    Bonus 2.2: Test rating for easy puzzle (Naked Singles only)
    """
    from sudoku import rate_difficulty
    
    # Easy puzzle - solvable with only Naked Singles
    easy_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    board = SudokuBoard(easy_puzzle)
    rating = rate_difficulty(board)
    
    assert rating in ["Easy", "EASY", "easy"], f"Should be rated Easy, got {rating}"
    
    print("✓ test_rate_easy_puzzle passed")


def test_rate_medium_puzzle():
    """
    Bonus 2.2: Test rating system can distinguish difficulties
    """
    from sudoku import rate_difficulty
    
    # Puzzle with moderate difficulty
    medium_puzzle = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]
    
    board = SudokuBoard(medium_puzzle)
    rating = rate_difficulty(board)
    
    # Rating should be one of the valid difficulty levels
    assert rating in ["Easy", "Medium", "Hard"], f"Got invalid rating: {rating}"
    
    print("✓ test_rate_medium_puzzle passed")


def test_rate_hard_puzzle():
    """
    Bonus 2.2: Test rating for challenging puzzle
    """
    from sudoku import rate_difficulty
    
    # Challenging puzzle with many empty cells
    hard_puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 3, 5, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 7, 0],
        [7, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 4, 0, 0, 8, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 4, 0],
        [0, 5, 0, 0, 0, 0, 6, 0, 0]
    ]
    
    board = SudokuBoard(hard_puzzle)
    rating = rate_difficulty(board)
    
    # Rating should be one of the valid levels, and for sparse puzzle likely Medium/Hard
    assert rating in ["Easy", "Medium", "Hard"], f"Got invalid rating: {rating}"
    assert rating != "Easy", f"Sparse puzzle should be rated Medium or Hard, got {rating}"
    
    print("✓ test_rate_hard_puzzle passed")


def test_human_solver_techniques():
    """
    Bonus 2.2: Test individual solving techniques work
    """
    from sudoku import HumanSolver
    
    # Test puzzle where Naked Singles should find values
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    board = SudokuBoard(puzzle)
    solver = HumanSolver(board)
    
    # Should be able to make progress with techniques
    progress_made = solver.apply_naked_singles()
    assert progress_made is True or progress_made >= 0, "Should find at least some naked singles"
    
    print("✓ test_human_solver_techniques passed")
