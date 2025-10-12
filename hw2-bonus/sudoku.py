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
