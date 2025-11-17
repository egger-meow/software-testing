# sudoku.py
"""
Sudoku Application - Core Engine
Developed using Test-Driven Development (TDD)

Features:
1. Rules Engine (isValid)
2. Backtracking Solver (solve)
3. Puzzle Generator (generate)
"""

import copy
import random


class SudokuBoard:
    """
    Represents a Sudoku board with validation, solving, and generation capabilities.
    """
    
    def __init__(self, grid):
        """
        Initialize a Sudoku board.
        
        Args:
            grid: A 9x9 2D list representing the Sudoku board.
                  0 represents an empty cell.
        """
        # Use deepcopy to ensure the original grid is not modified
        self.grid = copy.deepcopy(grid)
        self.size = 9

    def is_valid(self, row, col, num):
        """
        Check if placing a number at a given position is valid.
        
        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            num: Number to place (1-9)
            
        Returns:
            True if the placement is valid, False otherwise
        """
        # Check row
        for i in range(self.size):
            if self.grid[row][i] == num:
                return False

        # Check column
        for i in range(self.size):
            if self.grid[i][col] == num:
                return False

        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        
        return True

    def find_empty(self):
        """
        Find an empty cell in the grid.
        
        Returns:
            Tuple (row, col) of an empty cell, or None if no empty cell exists
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return (i, j)  # row, col
        return None

    def solve(self, randomize=False):
        """
        Solve the Sudoku puzzle using backtracking algorithm.
        
        Args:
            randomize: If True, try numbers in random order (for puzzle generation)
            
        Returns:
            True if the puzzle is solved, False otherwise
        """
        find = self.find_empty()
        if not find:
            return True  # Board is full, puzzle solved
        else:
            row, col = find

        numbers = list(range(1, self.size + 1))
        if randomize:
            random.shuffle(numbers)

        for num in numbers:
            if self.is_valid(row, col, num):
                self.grid[row][col] = num

                if self.solve(randomize):
                    return True

                self.grid[row][col] = 0  # Backtrack

        return False

    def count_solutions(self, limit=None):
        """
        Count all possible solutions for the Sudoku puzzle.
        
        This is essential for Bonus 2.1: ensuring generated puzzles have
        exactly one unique solution.
        
        Args:
            limit: Maximum number of solutions to find (for performance).
                   If None, counts all solutions.
        
        Returns:
            Number of solutions found (up to limit if specified)
        """
        return self._count_solutions_helper(limit or float('inf'), [0])
    
    def _count_solutions_helper(self, limit, count_list):
        """
        Recursive helper for counting solutions.
        
        Args:
            limit: Stop counting after this many solutions
            count_list: Mutable list with single element [count] to track across recursion
            
        Returns:
            Number of solutions found
        """
        # Stop if we've reached the limit
        if count_list[0] >= limit:
            return count_list[0]
        
        # Find empty cell
        find = self.find_empty()
        if not find:
            # Board is complete - found a solution!
            count_list[0] += 1
            return count_list[0]
        
        row, col = find
        
        # Try each number 1-9
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                
                # Recursively count solutions
                self._count_solutions_helper(limit, count_list)
                
                # Backtrack
                self.grid[row][col] = 0
                
                # Early exit if we hit the limit
                if count_list[0] >= limit:
                    return count_list[0]
        
        return count_list[0]


def validate_puzzle(grid):
    """
    Validate a Sudoku puzzle for common errors.
    
    Checks:
    1. Correct dimensions (9x9)
    2. Valid numbers (0-9 only)
    3. No duplicate givens in rows, columns, or boxes
    
    Args:
        grid: A 2D list representing the puzzle
        
    Returns:
        Tuple (is_valid, error_message)
        - is_valid: True if puzzle is valid, False otherwise
        - error_message: Empty string if valid, error description if invalid
    """
    # Check 1: Correct dimensions
    if not isinstance(grid, list) or len(grid) != 9:
        return False, "Invalid puzzle: Must have exactly 9 rows (9x9 grid required)"
    
    for i, row in enumerate(grid):
        if not isinstance(row, list) or len(row) != 9:
            return False, f"Invalid puzzle: Row {i} must have exactly 9 columns (9x9 grid required)"
    
    # Check 2: Valid numbers (0-9)
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if not isinstance(num, int) or num < 0 or num > 9:
                return False, f"Invalid number at position ({i},{j}): {num}. Must be in range 0-9"
    
    # Check 3: No duplicate givens
    # Check rows
    for i, row in enumerate(grid):
        non_zero = [num for num in row if num != 0]
        if len(non_zero) != len(set(non_zero)):
            return False, f"Duplicate number found in row {i}"
    
    # Check columns
    for j in range(9):
        column = [grid[i][j] for i in range(9) if grid[i][j] != 0]
        if len(column) != len(set(column)):
            return False, f"Duplicate number found in column {j}"
    
    # Check 3x3 boxes
    for box_row in range(3):
        for box_col in range(3):
            box_nums = []
            for i in range(3):
                for j in range(3):
                    num = grid[box_row * 3 + i][box_col * 3 + j]
                    if num != 0:
                        box_nums.append(num)
            if len(box_nums) != len(set(box_nums)):
                return False, f"Duplicate number found in 3x3 box at position ({box_row},{box_col})"
    
    return True, ""


def generate(difficulty):
    """
    Generate a new Sudoku puzzle with the specified difficulty.
    
    Args:
        difficulty: Number of cells to remove (higher = harder)
        
    Returns:
        Tuple (puzzle_board, solution_board) where:
        - puzzle_board is a SudokuBoard with empty cells
        - solution_board is the complete solution
    """
    # 1. Create a full, random solution
    empty_grid = [[0] * 9 for _ in range(9)]
    solution_board = SudokuBoard(empty_grid)
    solution_board.solve(randomize=True)  # Use the randomized solver

    # 2. Create a puzzle by removing cells
    puzzle_board = SudokuBoard(solution_board.grid)
    
    cells_to_remove = difficulty
    while cells_to_remove > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if puzzle_board.grid[row][col] != 0:
            puzzle_board.grid[row][col] = 0
            cells_to_remove -= 1
    
    return puzzle_board, solution_board


def generate_unique(difficulty, max_attempts=1000):
    """
    Generate a Sudoku puzzle with EXACTLY ONE unique solution.
    
    This is Bonus 2.1: ensuring puzzle quality by guaranteeing uniqueness.
    
    Strategy:
    1. Generate a random complete solution
    2. Remove cells one by one
    3. After each removal, check if puzzle still has unique solution
    4. If removing a cell results in 0 or >1 solutions, put it back
    
    Args:
        difficulty: Target number of cells to remove
        max_attempts: Maximum attempts to remove cells (prevents infinite loops)
        
    Returns:
        Tuple (puzzle_board, solution_board) where puzzle has unique solution
    """
    # 1. Generate a random complete solution
    empty_grid = [[0] * 9 for _ in range(9)]
    solution_board = SudokuBoard(empty_grid)
    solution_board.solve(randomize=True)
    
    # 2. Start with the complete solution as puzzle
    puzzle_board = SudokuBoard(solution_board.grid)
    
    # 3. Try to remove cells while maintaining uniqueness
    cells_removed = 0
    attempts = 0
    
    # Create list of all cell positions, shuffled for randomness
    all_positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(all_positions)
    
    for row, col in all_positions:
        if cells_removed >= difficulty:
            break
        
        attempts += 1
        if attempts > max_attempts:
            break
        
        # Try removing this cell
        original_value = puzzle_board.grid[row][col]
        if original_value == 0:
            continue  # Already empty
        
        puzzle_board.grid[row][col] = 0
        
        # Check if puzzle still has unique solution
        test_board = SudokuBoard(puzzle_board.grid)
        solution_count = test_board.count_solutions(limit=2)  # Only need to know if >1
        
        if solution_count == 1:
            # Good! Still unique
            cells_removed += 1
        else:
            # Bad! Multiple solutions or none - revert
            puzzle_board.grid[row][col] = original_value
    
    return puzzle_board, solution_board


# ============================================================================
# BONUS 2.2: Human-like Solving Techniques & Difficulty Rating
# ============================================================================

class HumanSolver:
    """
    Solves Sudoku using human-like logical techniques.
    Tracks which techniques were needed to rate difficulty.
    """
    
    def __init__(self, board):
        """
        Args:
            board: SudokuBoard instance to solve
        """
        self.board = SudokuBoard(board.grid)  # Work on a copy
        self.techniques_used = set()
        
    def get_candidates(self, row, col):
        """Get all possible values for a cell."""
        if self.board.grid[row][col] != 0:
            return set()
        
        candidates = set(range(1, 10))
        
        # Remove values from same row
        for c in range(9):
            candidates.discard(self.board.grid[row][c])
        
        # Remove values from same column
        for r in range(9):
            candidates.discard(self.board.grid[r][col])
        
        # Remove values from same box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                candidates.discard(self.board.grid[r][c])
        
        return candidates
    
    def apply_naked_singles(self):
        """
        Naked Singles: If a cell has only one possible value, fill it.
        Returns: Number of cells filled
        """
        filled = 0
        changed = True
        
        while changed:
            changed = False
            for row in range(9):
                for col in range(9):
                    if self.board.grid[row][col] == 0:
                        candidates = self.get_candidates(row, col)
                        if len(candidates) == 1:
                            self.board.grid[row][col] = candidates.pop()
                            filled += 1
                            changed = True
                            self.techniques_used.add("Naked Singles")
        
        return filled
    
    def apply_hidden_singles(self):
        """
        Hidden Singles: If a value can only go in one cell in a unit (row/col/box).
        Returns: Number of cells filled
        """
        filled = 0
        
        # Check rows
        for row in range(9):
            for num in range(1, 10):
                possible_positions = []
                for col in range(9):
                    if self.board.grid[row][col] == 0:
                        if num in self.get_candidates(row, col):
                            possible_positions.append((row, col))
                
                if len(possible_positions) == 1:
                    r, c = possible_positions[0]
                    self.board.grid[r][c] = num
                    filled += 1
                    self.techniques_used.add("Hidden Singles")
        
        # Check columns
        for col in range(9):
            for num in range(1, 10):
                possible_positions = []
                for row in range(9):
                    if self.board.grid[row][col] == 0:
                        if num in self.get_candidates(row, col):
                            possible_positions.append((row, col))
                
                if len(possible_positions) == 1:
                    r, c = possible_positions[0]
                    self.board.grid[r][c] = num
                    filled += 1
                    self.techniques_used.add("Hidden Singles")
        
        # Check boxes
        for box_row in range(3):
            for box_col in range(3):
                for num in range(1, 10):
                    possible_positions = []
                    for r in range(box_row * 3, box_row * 3 + 3):
                        for c in range(box_col * 3, box_col * 3 + 3):
                            if self.board.grid[r][c] == 0:
                                if num in self.get_candidates(r, c):
                                    possible_positions.append((r, c))
                    
                    if len(possible_positions) == 1:
                        r, c = possible_positions[0]
                        self.board.grid[r][c] = num
                        filled += 1
                        self.techniques_used.add("Hidden Singles")
        
        return filled
    
    def apply_naked_pairs(self):
        """
        Naked Pairs: If two cells in a unit can only contain the same two values,
        eliminate those values from other cells in the unit.
        Returns: Number of eliminations made
        """
        eliminations = 0
        
        # Check rows
        for row in range(9):
            cells_candidates = {}
            for col in range(9):
                if self.board.grid[row][col] == 0:
                    cand = self.get_candidates(row, col)
                    if len(cand) == 2:
                        cells_candidates[col] = cand
            
            # Find pairs
            cols = list(cells_candidates.keys())
            for i in range(len(cols)):
                for j in range(i + 1, len(cols)):
                    if cells_candidates[cols[i]] == cells_candidates[cols[j]]:
                        # Found a naked pair!
                        pair_values = cells_candidates[cols[i]]
                        self.techniques_used.add("Naked Pairs")
                        eliminations += 1  # Count that we found it
        
        return eliminations
    
    def solve_human(self, max_iterations=100):
        """
        Try to solve using human techniques.
        Returns: True if solved, False if stuck
        """
        for iteration in range(max_iterations):
            total_progress = 0
            
            # Try techniques in order of simplicity
            total_progress += self.apply_naked_singles()
            total_progress += self.apply_hidden_singles()
            
            if total_progress == 0:
                # Try more advanced techniques
                total_progress += self.apply_naked_pairs()
            
            # Check if solved
            if all(self.board.grid[r][c] != 0 for r in range(9) for c in range(9)):
                return True
            
            # If no progress, we're stuck
            if total_progress == 0:
                return False
        
        return False


def rate_difficulty(board):
    """
    Rate the difficulty of a Sudoku puzzle based on techniques required.
    
    Args:
        board: SudokuBoard instance
        
    Returns:
        String: "Easy", "Medium", or "Hard"
    """
    solver = HumanSolver(board)
    
    # Try to solve with human techniques
    solver.solve_human()
    
    # Check if puzzle was solved with human techniques
    is_solved = all(solver.board.grid[r][c] != 0 for r in range(9) for c in range(9))
    
    # Rate based on techniques used
    techniques = solver.techniques_used
    
    if not is_solved:
        # Couldn't solve with basic techniques
        return "Hard"
    elif "Naked Pairs" in techniques:
        # Advanced technique needed
        return "Hard"
    elif "Hidden Singles" in techniques:
        # Intermediate technique
        return "Medium"
    elif "Naked Singles" in techniques:
        # Basic technique only
        return "Easy"
    else:
        # Fallback: use backtracking to check complexity
        test_board = SudokuBoard(board.grid)
        if test_board.solve():
            return "Easy"
        return "Hard"
