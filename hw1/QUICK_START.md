# Quick Start Guide

## For Students

### 📥 What to Submit
Submit these files from the `solutions/` folder:
- `HOMEWORK1_COMPLETE_SUBMISSION.md` (recommended - combines both parts)
- OR `Homework1_Part1_Solution.md` + `Part2_Solution.md` separately

### ✅ How to Verify Your Work

**Part 1 (JavaScript):**
```bash
cd part1_tests
node test_faulty_programs.js
node corrected_programs.js
```

**Part 2 (C++/Python):**
```bash
cd part2_tests

# Memory Leak Test
g++ -o test1 test_dataprocessor.cpp && valgrind --leak-check=full ./test1

# Race Condition Test
g++ -o test2 test_loggingsystem.cpp -pthread -fsanitize=thread && ./test2

# Const Violation Test
g++ -o test3 test_matrixprocessor.cpp -Wall && ./test3

# Buffer Overflow Test
g++ -o test4 test_profileupdater.cpp -fsanitize=address && ./test4

# Deadlock Test
python test_resourcescheduler.py  # Press Ctrl+C after it hangs
```

---

## For TAs

### 📂 Key Files
- **Main README:** `README.md` (full documentation)
- **Submissions:** `solutions/` folder
- **Tests:** `part1_tests/` and `part2_tests/` folders

### 🔍 Quick Verification

**Part 1 (4 programs):**
- All analyses in `solutions/Homework1_Part1_Solution.md`
- Run `node part1_tests/test_faulty_programs.js` to see faults
- Expected faults: loop boundary, search direction, zero comparison, modulo operator

**Part 2 (5 programs):**
- All analyses in `solutions/Part2_Solution.md`
- Test files in `part2_tests/`
- Expected faults: memory leak, race condition, const violation, buffer overflow, deadlock

### 📊 Grading Checklist

**Part 1 (50 points):**
- [ ] Question (a): Fault identification and fix - 10 pts
- [ ] Question (b): Test case not executing fault - 10 pts
- [ ] Question (c): Fault executed, no error state - 10 pts
- [ ] Question (d): Error state, no failure - 10 pts
- [ ] Question (e): Error state description - 10 pts

**Part 2 Bonus (20 points):**
- [ ] DataProcessor: Memory leak identified - 4 pts
- [ ] LoggingSystem: Race condition identified - 4 pts
- [ ] MatrixProcessor: Const violation identified - 4 pts
- [ ] ProfileUpdater: Buffer overflow identified - 4 pts
- [ ] ResourceScheduler: Deadlock identified - 4 pts

### ✨ Quality Indicators
- ✅ Executable test cases provided
- ✅ Tool-based verification (Valgrind, sanitizers)
- ✅ Clear documentation with examples
- ✅ Root cause analysis included
- ✅ Fixes provided for all faults
- ✅ AI assistance transparently documented

---

## 🛠️ Tools Required

**For Part 1:**
- Node.js (any recent version)

**For Part 2:**
- GCC/G++ with C++11 support
- Valgrind (Linux/Mac) or DrMemory (Windows)
- Sanitizers: `-fsanitize=thread`, `-fsanitize=address`
- Python 3.x

**Windows Users:**
- Use MinGW-w64 or WSL for sanitizers
- Or verify on Linux VM

---

## 📞 Support

**For students:** Check `README.md` and `docs/README_PART2.md`  
**For TAs:** All information in main `README.md`

---

Generated: October 2, 2025
