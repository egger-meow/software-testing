# Homework 1: Faulty Programs with Faults and Failures
**Student:** [Your Name]  
**Student ID:** [Your ID]  
**Date:** October 2, 2025

---

# Part 1: Analysis of Four Faulty Programs

This document analyzes four faulty JavaScript programs, answering questions (a) through (e) for each program. All answers have been verified with actual code execution.

---

## Program 1: findLast

### Given Code and Test
```javascript
function findLast(x, y) {
    if (!Array.isArray(x)) {
        throw new TypeError('The first parameter must be an array');
    }
    if (typeof y !== 'number') {
        throw new TypeError('The second parameter must be a number');
    }
    for (let i = x.length - 1; i > 0; i--) {
        if (x[i] === y) {
            return i;
        }
    }
    return -1;
}
// test: x = [2, 3, 5]; y = 2; Expected = 0
```

### (a) Fault Description
**What is wrong:** The loop condition `i > 0` prevents the loop from checking index 0. The loop terminates when `i` reaches 0, so the element at index 0 is never examined.

**Proposed modification:**
```javascript
for (let i = x.length - 1; i >= 0; i--) {  // Change i > 0 to i >= 0
```

### (b) Test case that does not execute the fault
**Test case:** `x = [], y = 2`

**Explanation:** When the array is empty, `x.length - 1 = -1`, so the loop condition `i > 0` (i.e., `-1 > 0`) is false from the start. The loop body never executes, so the faulty line is not executed. The function correctly returns -1.

### (c) Test case that executes the fault but does not result in an error state
**Test case:** `x = [3, 5, 7], y = 2`

**Expected output:** -1  
**Actual output:** -1

**Explanation:** The loop executes (starting at index 2 and checking down to index 1), so the fault is executed. However, since the target value 2 is not present in the array at any position, the function correctly returns -1. The fact that index 0 is never checked doesn't matter because the correct answer doesn't depend on that position.

### (d) Test case that results in an error state but not a failure
**Test case:** `x = [1, 2, 3, 4], y = 2`

**Expected output:** 1  
**Actual output:** 1

**Explanation:** The fault is executed as the loop runs from index 3 down to index 1. The function finds the value 2 at index 1 and correctly returns 1. However, an error state exists during execution: the loop terminates at `i = 0` without checking index 0, which violates the function's specification to search the entire array from the end. If the value 2 were only at index 0, it would be missed.

### (e) First error state description for test case in (d)
**Test case:** `x = [1, 2, 3, 4], y = 2`

**Complete state at the point of error:**
- **Location:** When the loop condition check fails at `i = 0`
- **Variable `x`:** `[1, 2, 3, 4]`
- **Variable `y`:** `2`
- **Loop variable `i`:** `0` (but the condition `0 > 0` is false, so index 0 is not checked)
- **Indices checked:** 3, 2, 1
- **Indices NOT checked:** 0
- **Error:** The program state is incorrect because index 0 has not been examined, violating the function's contract to find the last occurrence by searching through the entire array. The algorithm's internal logic is flawed even though it may produce the correct output for this particular input.

---

## Program 2: lastZero

### Given Code and Test
```javascript
function lastZero(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    for (let i = 0; i < x.length; i++) {
        if (x[i] === 0) {
            return i;
        }
    }
    return -1;
}
// test: x = [0, 1, 0]; Expected = 2
```

### (a) Fault Description
**What is wrong:** The function is supposed to find the LAST index of zero, but the loop searches forward (from index 0 to the end). This causes the function to return the FIRST occurrence of zero instead of the LAST.

**Proposed modification:**
```javascript
for (let i = x.length - 1; i >= 0; i--) {  // Search backwards from the end
```

### (b) Test case that does not execute the fault
**Test case:** `x = []`

**Explanation:** When the array is empty, the loop condition `i < x.length` (i.e., `0 < 0`) is false from the start. The loop body never executes, so the fault is not executed. The function correctly returns -1.

### (c) Test case that executes the fault but does not result in an error state
**Test case:** `x = [1, 2, 3]`

**Expected output:** -1  
**Actual output:** -1

**Explanation:** The loop executes forward through the array (fault is executed), checking each element for zero. Since there are no zeros in the array, the function correctly returns -1. The direction of the search doesn't affect the result when the target element is absent.

### (d) Test case that results in an error state but not a failure
**Test case:** `x = [0, 1, 2]`

**Expected output:** 0  
**Actual output:** 0

**Explanation:** The fault is executed (loop searches forward). There is only one zero at index 0, which is both the first and last occurrence. The function returns 0, which is the correct answer. However, an error state exists because the algorithm uses the wrong search direction—it's designed to find the first zero, not the last. If multiple zeros existed, this would produce the wrong result.

### (e) First error state description for test case in (d)
**Test case:** `x = [0, 1, 2]`

**Complete state at the point of error:**
- **Location:** When `i = 0` and the condition `x[0] === 0` evaluates to true
- **Variable `x`:** `[0, 1, 2]`
- **Loop variable `i`:** `0`
- **Value found:** `x[0] = 0`
- **About to return:** `0`
- **Error:** The algorithm is using a forward search (first-to-last) when the specification requires a backward search (last-to-first). While the return value happens to be correct for this input (because there's only one zero), the internal algorithm logic is incorrect. The error is in the search direction strategy itself, not just the variable values.

---

## Program 3: countPositive

### Given Code and Test
```javascript
function countPositive(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    let count = 0;
    for (let i = 0; i < x.length; i++) {
        if (x[i] >= 0) {
            count++;
        }
    }
    return count;
}
// test: x = [-4, 2, 0, 2]; Expected = 2
```

### (a) Fault Description
**What is wrong:** The condition `x[i] >= 0` counts zero as a positive number. However, zero is neither positive nor negative. The function should only count strictly positive numbers (greater than zero).

**Proposed modification:**
```javascript
if (x[i] > 0) {  // Change >= 0 to > 0
```

### (b) Test case that does not execute the fault
**Test case:** `x = []`

**Explanation:** When the array is empty, the loop condition `i < x.length` (i.e., `0 < 0`) is false from the start. The loop body never executes, so the fault is not executed. The function correctly returns 0.

### (c) Test case that executes the fault but does not result in an error state
**Test case:** `x = [1, 2, 3]`

**Expected output:** 3  
**Actual output:** 3

**Explanation:** The loop executes and checks the condition `x[i] >= 0` for each element (fault is executed). Since all elements are strictly positive and there are no zeros, the function correctly counts all three elements and returns 3. The faulty condition doesn't cause an error state because there are no zero values to miscount.

### (d) Test case that results in an error state but not a failure
**Answer:** Not possible.

**Explanation:** For this program, any test case containing zero will execute the fault (checking `x[i] >= 0` when `x[i]` is 0) and create an error state (count is incremented incorrectly), which will directly cause a failure (final count is wrong). Any test case without zeros will not create an error state at all, since the condition `>= 0` and `> 0` are equivalent for non-zero values. Therefore, it's impossible to have an error state without a corresponding failure.

### (e) First error state description
Since we cannot provide a test case for (d), we describe the error state for the given failing test case:

**Test case:** `x = [-4, 2, 0, 2]`

**Complete state at the point of error:**
- **Location:** When the loop processes `i = 2` and encounters `x[2] = 0`
- **Variable `x`:** `[-4, 2, 0, 2]`
- **Loop variable `i`:** `2`
- **Variable `count`:** `1` (has already counted `x[1] = 2`)
- **Current element:** `x[2] = 0`
- **Condition evaluation:** `x[2] >= 0` evaluates to `true` (since `0 >= 0`)
- **About to execute:** `count++`
- **Error:** After executing `count++`, the count becomes 2, but it should remain 1. Zero is not a positive number and should not be counted. The error state occurs immediately after the count is incorrectly incremented. The correct state should have `count = 1` at this point (having counted only one positive element: `x[1] = 2`).

---

## Program 4: oddOrPos

### Given Code and Test
```javascript
function oddOrPos(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    let count = 0;
    for (let i = 0; i < x.length; i++) {
        if (x[i] % 2 === 1 || x[i] > 0) {
            count++;
        }
    }
    return count;
}
// test: x = [-3, -2, 0, 1, 4]; Expected = 3
```

### (a) Fault Description
**What is wrong:** The condition `x[i] % 2 === 1` only detects positive odd numbers. For negative odd numbers, the modulo operation returns -1, not 1. For example, `-3 % 2 === -1` (not 1), so negative odd numbers fail the first condition and are only counted if they pass the second condition `x[i] > 0` (which they don't).

**Proposed modification:**
```javascript
if (x[i] % 2 !== 0 || x[i] > 0) {  // Change === 1 to !== 0
```
This works because any odd number (positive or negative) will have a non-zero remainder when divided by 2.

### (b) Test case that does not execute the fault
**Test case:** `x = []`

**Explanation:** When the array is empty, the loop condition `i < x.length` is false from the start. The loop body never executes, so the fault is not executed. The function correctly returns 0.

### (c) Test case that executes the fault but does not result in an error state
**Test case:** `x = [1, 3, 5]`

**Expected output:** 3  
**Actual output:** 3

**Explanation:** The loop executes and checks the condition for each element (fault is executed). All three elements are positive odd numbers, so for each element, `x[i] % 2 === 1` evaluates to true. The function correctly counts all three and returns 3. The fault doesn't cause an error state because there are no negative odd numbers to miscount.

### (d) Test case that results in an error state but not a failure
**Answer:** Not possible.

**Explanation:** The fault only affects negative odd numbers. When a negative odd number is present in the array:
- The faulty condition `x[i] % 2 === 1` evaluates to false (since `negative_odd % 2` returns -1, not 1)
- The second condition `x[i] > 0` also evaluates to false (since the number is negative)
- Therefore, the negative odd number is not counted, creating an error state (wrong count)
- This error state directly leads to a failure (wrong final output)

Without negative odd numbers in the input, there is no error state. Therefore, it's impossible to have an error state without a corresponding failure for this program.

### (e) First error state description
Since we cannot provide a test case for (d), we describe the error state for the given failing test case:

**Test case:** `x = [-3, -2, 0, 1, 4]`

**Complete state at the point of error:**
- **Location:** When the loop processes `i = 0` and evaluates the conditions for `x[0] = -3`
- **Variable `x`:** `[-3, -2, 0, 1, 4]`
- **Loop variable `i`:** `0`
- **Variable `count`:** `0`
- **Current element:** `x[0] = -3`
- **First condition:** `x[0] % 2 === 1` evaluates to `false` (because `-3 % 2 === -1`, not 1)
- **Second condition:** `x[0] > 0` evaluates to `false`
- **Combined condition:** `false || false = false`
- **Action taken:** Count is NOT incremented (remains 0)
- **Error:** The value -3 is an odd number and should be counted according to the function specification ("odd OR positive"). The error occurs immediately after evaluating the condition for `x[0]`, where count should be 1 but remains 0. The correct state should have `count = 1` after processing the first element.

---

# Summary

## Quick Reference Table

| Program | Fault Location | Fix Required | Can have Error State w/o Failure? |
|---------|---------------|--------------|-----------------------------------|
| **findLast** | Loop condition `i > 0` | Change to `i >= 0` | ✓ Yes |
| **lastZero** | Forward search direction | Reverse loop direction | ✓ Yes |
| **countPositive** | Condition `>= 0` | Change to `> 0` | ✗ No |
| **oddOrPos** | Condition `% 2 === 1` | Change to `% 2 !== 0` | ✗ No |

## Key Concepts Demonstrated

### Fault vs Error State vs Failure
- **Fault:** A defect in the source code (static)
- **Error State:** Incorrect internal state during execution (dynamic, intermediate)
- **Failure:** Incorrect external behavior/output (dynamic, observable)

### Important Insights
1. **findLast** and **lastZero**: These programs can have error states without failures because the algorithmic flaw doesn't always affect the output (when target is at a non-skipped position or when there's only one occurrence).

2. **countPositive** and **oddOrPos**: These programs cannot have error states without failures because the count variable directly becomes the return value. Any error in counting immediately manifests as a failure.

3. **Executing a fault doesn't guarantee an error state:** As shown in the (c) answers, a fault can execute without causing an error if the data doesn't trigger the problematic behavior.

## Verification
All analyses have been verified with actual code execution. Test files are provided:
- `test_faulty_programs.js` - Demonstrates the faulty behavior
- `corrected_programs.js` - Shows the corrected versions working properly

Run with: `node test_faulty_programs.js` and `node corrected_programs.js`

---

**End of Part 1**
