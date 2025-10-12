#!/usr/bin/env python3
"""
Sudoku Application Demo
Demonstrates the functionality of the Sudoku solver and generator
"""

from sudoku import SudokuBoard, generate


def print_board(board):
    """Pretty print a Sudoku board"""
    print("\n" + "=" * 37)
    for i, row in enumerate(board.grid):
        if i % 3 == 0 and i != 0:
            print("-" * 37)
        row_str = ""
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += " | "
            row_str += str(num) if num != 0 else "."
            row_str += " "
        print(row_str)
    print("=" * 37)


def demo_validation():
    """Demonstrate the validation engine"""
    print("\n🔍 DEMO 1: Validation Engine (isValid)")
    print("-" * 50)
    
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
    print("Initial Board:")
    print_board(board)
    
    # Test various validations
    tests = [
        (0, 2, 4, "Valid placement"),
        (0, 2, 5, "Row conflict (5 already in row 0)"),
        (0, 2, 8, "Column conflict (8 already in column 2)"),
        (1, 1, 9, "Box conflict (9 already in top-left box)")
    ]
    
    print("\nValidation Tests:")
    for row, col, num, description in tests:
        result = board.is_valid(row, col, num)
        status = "✓ Valid" if result else "✗ Invalid"
        print(f"  [{row},{col}] = {num}: {status} - {description}")


def demo_solver():
    """Demonstrate the solver"""
    print("\n\n🧩 DEMO 2: Backtracking Solver (solve)")
    print("-" * 50)
    
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
    
    print("Puzzle to Solve:")
    puzzle = SudokuBoard(puzzle_grid)
    print_board(puzzle)
    
    print("\nSolving...")
    if puzzle.solve():
        print("✓ Solution Found!")
        print_board(puzzle)
    else:
        print("✗ No solution exists")


def demo_generator():
    """Demonstrate the puzzle generator"""
    print("\n\n🎲 DEMO 3: Puzzle Generator (generate)")
    print("-" * 50)
    
    difficulties = [
        (30, "Easy"),
        (45, "Medium"),
        (60, "Hard")
    ]
    
    for difficulty, level in difficulties:
        print(f"\nGenerating {level} Puzzle (removing {difficulty} cells)...")
        puzzle_board, solution_board = generate(difficulty)
        
        print(f"Generated Puzzle ({level}):")
        print_board(puzzle_board)
        
        # Count empty cells
        empty_count = sum(row.count(0) for row in puzzle_board.grid)
        print(f"Empty cells: {empty_count}/{difficulty}")
        
        # Verify it's solvable
        test_board = SudokuBoard(puzzle_board.grid)
        if test_board.solve():
            print("✓ Puzzle is solvable")
        else:
            print("✗ Puzzle is not solvable (Error!)")


def demo_error_handling():
    """Demonstrate error handling and validation (Bonus 2.3)"""
    print("\n\n🛡️ DEMO 4: Error Handling & Validation (BONUS 2.3)")
    print("-" * 50)
    
    from sudoku import validate_puzzle
    
    # Test 1: Invalid number
    print("\n1. Testing puzzle with invalid number (10)...")
    invalid_num = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 10]  # Invalid!
    ]
    
    is_valid, error = validate_puzzle(invalid_num)
    print(f"   Result: {'✓ Valid' if is_valid else '✗ Invalid'}")
    print(f"   Error: {error}")
    
    # Test 2: Duplicate in row
    print("\n2. Testing puzzle with duplicate in row...")
    duplicate_row = [
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
    
    is_valid, error = validate_puzzle(duplicate_row)
    print(f"   Result: {'✓ Valid' if is_valid else '✗ Invalid'}")
    print(f"   Error: {error}")
    
    # Test 3: Wrong dimensions
    print("\n3. Testing puzzle with wrong dimensions...")
    wrong_size = [
        [5, 3, 0, 0, 7],  # Only 5 columns!
        [6, 0, 0, 1, 9]
    ]
    
    is_valid, error = validate_puzzle(wrong_size)
    print(f"   Result: {'✓ Valid' if is_valid else '✗ Invalid'}")
    print(f"   Error: {error}")
    
    # Test 4: Valid puzzle
    print("\n4. Testing valid puzzle...")
    valid = [
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
    
    is_valid, error = validate_puzzle(valid)
    print(f"   Result: {'✓ Valid' if is_valid else '✗ Invalid'}")
    if error:
        print(f"   Error: {error}")
    
    print("\n✓ Error handling demo completed")


def main():
    """Run all demos"""
    print("\n" + "=" * 50)
    print("   SUDOKU APPLICATION - TDD DEMONSTRATION")
    print("=" * 50)
    
    demo_validation()
    demo_solver()
    demo_generator()
    demo_error_handling()
    
    print("\n" + "=" * 50)
    print("   All Demos Completed Successfully!")
    print("   (Including Bonus 2.3 Features)")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
