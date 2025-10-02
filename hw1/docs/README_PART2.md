# Homework 1 - Part 2 Testing Guide

## Overview

This directory contains complete analysis and test cases for Part 2 (Bonus) - five larger faulty programs.

## Files Structure

### Solution Documents
- **`Part2_Solution.md`** - Concise summary (recommended for homework submission)
- **`Homework1_Part2_Complete.md`** - Detailed comprehensive analysis (partial)

### Test Files (Executable)
- `test_dataprocessor.cpp` - Demonstrates memory leak
- `test_loggingsystem.cpp` - Demonstrates race condition
- `test_matrixprocessor.cpp` - Demonstrates const violation
- `test_profileupdater.cpp` - Demonstrates buffer overflow
- `test_resourcescheduler.py` - Demonstrates deadlock

### Original Faulty Programs
- `faulty_programs/DataProcessor.cpp`
- `faulty_programs/LoggingSystem.cpp`
- `faulty_programs/MatrixProcessor.cpp`
- `faulty_programs/ProfileUpdater.cpp`
- `faulty_programs/ResourceScheduler.py`

## Quick Start

### Prerequisites

**For C++ programs:**
- GCC/G++ compiler
- Valgrind (for memory leak detection) - Linux/Mac
- DrMemory (for Windows) - optional

**For Python program:**
- Python 3.x

### Running Tests

#### 1. DataProcessor - Memory Leak Test

```bash
# Compile
g++ -o test_dataprocessor test_dataprocessor.cpp

# Run basic test
./test_dataprocessor

# Run with Valgrind to detect memory leaks (Linux/Mac)
valgrind --leak-check=full --show-leak-kinds=all ./test_dataprocessor

# Expected: Reports "definitely lost: 160,000 bytes in 20,000 blocks"
```

#### 2. LoggingSystem - Race Condition Test

```bash
# Compile with thread support
g++ -o test_loggingsystem test_loggingsystem.cpp -pthread

# Run basic test (may need multiple runs to see race)
./test_loggingsystem

# Compile with Thread Sanitizer for guaranteed detection
g++ -o test_loggingsystem test_loggingsystem.cpp -pthread -fsanitize=thread -g

# Run with Thread Sanitizer
./test_loggingsystem

# Expected: "WARNING: ThreadSanitizer: data race"
```

#### 3. MatrixProcessor - Const Violation Test

```bash
# Compile with warnings
g++ -o test_matrixprocessor test_matrixprocessor.cpp -Wall

# Run
./test_matrixprocessor

# Expected: Shows const_cast usage and incorrect pointer assignment
```

#### 4. ProfileUpdater - Buffer Overflow Test

```bash
# Compile with AddressSanitizer
g++ -o test_profileupdater test_profileupdater.cpp -fsanitize=address -g

# Run
./test_profileupdater

# Expected: "ERROR: AddressSanitizer: stack-buffer-overflow"
```

#### 5. ResourceScheduler - Deadlock Test

```bash
# Run Python script
python test_resourcescheduler.py

# Expected: Program hangs after both threads acquire their first lock
# Press Ctrl+C to terminate

# Or use timeout
timeout 10s python test_resourcescheduler.py
```

## Summary of Faults

| Program | Fault | How to Detect |
|---------|-------|---------------|
| **DataProcessor** | Memory leak (lines 39, 41) | Valgrind shows leaked memory |
| **LoggingSystem** | Race condition (line 17) | ThreadSanitizer or variable results |
| **MatrixProcessor** | Const violation (23) + wrong syntax (27) | Code inspection, incorrect results |
| **ProfileUpdater** | Buffer overflow (lines 11, 41) | AddressSanitizer detects overflow |
| **ResourceScheduler** | Deadlock (lines 36-65) | Program hangs indefinitely |

## Expected Test Results

### DataProcessor
```
Finished processing 10000 records.
*** MEMORY LEAK: 10000 DataRecord objects leaked ***
*** MEMORY LEAK: 10000 char allocations leaked ***
```

### LoggingSystem
```
Expected: 100000
Actual:   97823  (or similar, varies per run)
*** RACE CONDITION DETECTED ***
Lost updates: 2177
```

### MatrixProcessor
```
*** FAULT 1: Using const_cast to remove const protection ***
*** FAULT 2: Incorrect assignment - assigns to pointer, not value ***
Original pointer: 0x55cf8b2e92c0
New pointer value: 0x3e7 (invalid address!)
```

### ProfileUpdater
```
Username length: 10 chars
Buffer capacity: 1 bytes
Overflow: 10 bytes
*** BUFFER OVERFLOW OCCURRED ***
User ID changed from 12345 to 1701277281 (CORRUPTED)
```

### ResourceScheduler
```
Thread-A acquired Resource A
Thread-B acquired Resource B
Thread-A trying to acquire Resource B...
Thread-B trying to acquire Resource A...
[HANGS HERE - DEADLOCK]
```

## Troubleshooting

### Windows-Specific Issues

**If you don't have Valgrind:**
- Use DrMemory: https://drmemory.org/
- Or use Visual Studio's built-in memory leak detection

**If sanitizers don't work:**
- Use MinGW-w64 or WSL (Windows Subsystem for Linux)
- Or compile in Linux VM

### Compilation Issues

**If pthread not found:**
```bash
# Use -lpthread flag
g++ test_loggingsystem.cpp -lpthread -o test_loggingsystem
```

**If sanitizers not available:**
- Update GCC/Clang to newer version
- Or run tests without sanitizers (faults still visible)

## Verification Checklist

- [ ] DataProcessor: Valgrind reports memory leaks
- [ ] LoggingSystem: Final count < expected (or TSan reports race)
- [ ] MatrixProcessor: Pointer changed to 0x3e7
- [ ] ProfileUpdater: user_id corrupted from 12345
- [ ] ResourceScheduler: Program hangs, requires Ctrl+C

## Additional Notes

- All tests are designed to reliably trigger the faults
- Some tests (race condition, deadlock) may require multiple runs
- Use appropriate detection tools for best results
- Test files include detailed output explaining each fault

## For Homework Submission

**Recommended documents to submit:**
1. `Part2_Solution.md` - Main solution (concise and complete)
2. All test files (`test_*.cpp`, `test_*.py`)
3. Screenshots or log output from running tests

**Optional:**
- `Homework1_Part2_Complete.md` - Extended analysis

## Questions?

If tests don't work as expected:
1. Check compilation commands carefully
2. Verify tool availability (valgrind, sanitizers)
3. Run on Linux if Windows has issues
4. Check that test files match the provided versions
