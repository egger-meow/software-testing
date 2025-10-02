# Homework 1: Faulty Programs with Faults and Failures
## Part 1: Analysis of Four Faulty Programs

---

## Program 1: findLast

### Code Analysis
```javascript
function findLast(x, y) {
    if (!Array.isArray(x)) {
        throw new TypeError('The first parameter must be an array');
    }
    if (typeof y !== 'number') {
        throw new TypeError('The second parameter must be a number');
    }
    for (let i = x.length - 1; i > 0; i--) {  // FAULT HERE
        if (x[i] === y) {
            return i;
        }
    }
    return -1;
}
// test: x = [2, 3, 5]; y = 2; Expected = 0
```

### (a) Fault Description
**What is wrong:** The loop condition `i > 0` should be `i >= 0`. The current condition stops the loop when `i` becomes 0, so index 0 is never checked.

**Proposed modification:**
```javascript
for (let i = x.length - 1; i >= 0; i--) {  // Change > to >=
```

### (b) Test case that does not execute the fault
**Test case:** `x = [], y = 2`

**Explanation:** When the array is empty, `x.length - 1 = -1`, so the loop condition `i > 0` is false from the start. The loop body never executes, so the fault (line with the condition) is not executed. The function correctly returns -1.

### (c) Test case that executes the fault but does not result in an error state
**Test case:** `x = [3, 5, 7], y = 2`

**Expected output:** -1  
**Actual output:** -1

**Explanation:** The loop executes (fault is executed), but since the target value 2 is not in the array at all, the function correctly returns -1. The fault doesn't matter because the answer doesn't depend on checking index 0.

### (d) Test case that results in an error state but not a failure
**Test case:** `x = [1, 2, 3, 4], y = 2`

**Expected output:** 1  
**Actual output:** 1

**Explanation:** The fault is executed (loop runs from index 3 down to 1). The function finds 2 at index 1 and returns 1, which happens to be correct. However, an error state exists during execution because if 2 were only at index 0, it would be missed.

### (e) First error state description
**Complete state at the point of error:**
- When the loop finishes: `i = 0` (loop terminates without checking index 0)
- Variable `x = [1, 2, 3, 4]`
- Variable `y = 2`
- The loop has checked indices 3, 2, 1 but **not index 0**
- The program is about to execute `return -1` or has found a match at a higher index
- **Error:** The state is incorrect because index 0 was never examined, violating the function's specification to find the LAST index by searching from the end

---

## Program 2: lastZero

### Code Analysis
```javascript
function lastZero(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    for (let i = 0; i < x.length; i++) {  // FAULT HERE - should search backwards
        if (x[i] === 0) {
            return i;
        }
    }
    return -1;
}
// test: x = [0, 1, 0]; Expected = 2
```

### (a) Fault Description
**What is wrong:** The loop searches forward (from index 0 to end) but the function should find the LAST zero. It currently returns the FIRST zero instead.

**Proposed modification:**
```javascript
for (let i = x.length - 1; i >= 0; i--) {  // Search backwards
```

### (b) Test case that does not execute the fault
**Test case:** `x = []`

**Explanation:** When the array is empty, the loop condition `i < x.length` (i.e., `0 < 0`) is false from the start. The loop body never executes, so the fault is not executed. The function correctly returns -1.

### (c) Test case that executes the fault but does not result in an error state
**Test case:** `x = [1, 2, 3]`

**Expected output:** -1  
**Actual output:** -1

**Explanation:** The loop executes forward through the array (fault is executed), but since there are no zeros in the array, the function correctly returns -1. The direction of search doesn't matter when the target is absent.

### (d) Test case that results in an error state but not a failure
**Test case:** `x = [0, 1, 2]`

**Expected output:** 0  
**Actual output:** 0

**Explanation:** The fault is executed (loop searches forward). There is only one zero at index 0, which is both the first and last zero. The function returns 0, which is correct, but an error state exists because the algorithm uses the wrong search direction.

### (e) First error state description
**Complete state at the point of error:**
- When `i = 0` and `x[0] === 0` is true
- Variable `x = [0, 1, 2]`
- Loop variable `i = 0`
- The function is about to `return i` (which is 0)
- **Error:** The algorithm searched forward instead of backward. While the answer is correct for this input, the internal state/logic is wrong. If there were multiple zeros, this forward search would return the wrong index.

---

## Program 3: countPositive

### Code Analysis
```javascript
function countPositive(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    let count = 0;
    for (let i = 0; i < x.length; i++) {
        if (x[i] >= 0) {  // FAULT HERE - should be > 0
            count++;
        }
    }
    return count;
}
// test: x = [-4, 2, 0, 2]; Expected = 2
```

### (a) Fault Description
**What is wrong:** The condition `x[i] >= 0` counts zero as positive, but zero is neither positive nor negative. It should only count strictly positive numbers.

**Proposed modification:**
```javascript
if (x[i] > 0) {  // Change >= to >
```

### (b) Test case that does not execute the fault
**Test case:** `x = []`

**Explanation:** When the array is empty, the loop condition `i < x.length` (i.e., `0 < 0`) is false. The loop body never executes, so the fault is not executed. The function correctly returns 0.

### (c) Test case that executes the fault but does not result in an error state
**Test case:** `x = [1, 2, 3]`

**Expected output:** 3  
**Actual output:** 3

**Explanation:** The loop executes and checks the condition `x[i] >= 0` for each element (fault is executed). Since all elements are positive (no zeros), the function correctly returns 3. The faulty condition doesn't cause an error because there are no zeros to miscount.

### (d) Test case that results in an error state but not a failure
**Answer:** Not possible.

**Explanation:** For this program, any test case containing zero will execute the fault (`x[i] >= 0` when x[i] is 0) and create an error state (count is incremented when it shouldn't be), which will also cause a failure (final count is wrong). Any test case without zeros will not create an error state at all. Therefore, it's impossible to have an error state without a corresponding failure.

### (e) First error state description
For the given failing test case: `x = [-4, 2, 0, 2]`

**Complete state at the point of error:**
- When the loop processes `i = 2` and encounters `x[2] = 0`
- Variable `x = [-4, 2, 0, 2]`
- Loop variable `i = 2`
- Variable `count = 2` (already counted x[1]=2)
- The condition `x[2] >= 0` evaluates to `true` (0 >= 0 is true)
- **Error:** The count is about to be incremented to 3, but it should remain at 2 because zero is not a positive number. After executing `count++`, we have `count = 3` which is incorrect. The correct internal state should have `count = 2` at this point (only having counted x[1]=2 and x[3]=2).

---

## Program 4: oddOrPos

### Code Analysis
```javascript
function oddOrPos(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    let count = 0;
    for (let i = 0; i < x.length; i++) {
        if (x[i] % 2 === 1 || x[i] > 0) {  // FAULT HERE
            count++;
        }
    }
    return count;
}
// test: x = [-3, -2, 0, 1, 4]; Expected = 3
```

### (a) Fault Description
**What is wrong:** The condition `x[i] % 2 === 1` only works for positive odd numbers. For negative odd numbers, the modulo operation returns -1, not 1. For example, `-3 % 2 === -1`, not 1.

**Proposed modification:**
```javascript
if (x[i] % 2 !== 0 || x[i] > 0) {  // Change === 1 to !== 0
// OR
if (x[i] % 2 === 1 || x[i] % 2 === -1 || x[i] > 0)
```

### (b) Test case that does not execute the fault
**Test case:** `x = []`

**Explanation:** When the array is empty, the loop condition `i < x.length` is false from the start. The loop body never executes, so the fault is not executed. The function correctly returns 0.

### (c) Test case that executes the fault but does not result in an error state
**Test case:** `x = [1, 3, 5]`

**Expected output:** 3  
**Actual output:** 3

**Explanation:** The loop executes and checks the condition for each element (fault is executed). All elements are positive odd numbers, so `x[i] % 2 === 1` evaluates to true for all. The function correctly returns 3. The fault doesn't cause an error because there are no negative odd numbers.

### (d) Test case that results in an error state but not a failure
**Answer:** Not possible.

**Explanation:** The fault only affects negative odd numbers. When a negative odd number is present in the array, the faulty condition `x[i] % 2 === 1` evaluates to false (since negative_odd % 2 returns -1, not 1), causing the number not to be counted unless it passes the second condition `x[i] > 0` (which it won't, being negative). This creates an error state (incorrect count), which directly leads to a failure (wrong final output). Without negative odd numbers, there is no error state. Therefore, it's impossible to have an error state without a corresponding failure for this program.

### (e) First error state description
Using the given failing test case: `x = [-3, -2, 0, 1, 4]`

**Complete state at the point of error:**
- When the loop processes `i = 0` and `x[0] = -3`
- Variable `x = [-3, -2, 0, 1, 4]`
- Loop variable `i = 0`
- Variable `count = 0` (should be 1 after processing -3)
- The condition `x[0] % 2 === 1` evaluates to `false` (because `-3 % 2 === -1`)
- The condition `x[0] > 0` evaluates to `false`
- **Error:** The combined condition is false, so count is not incremented. However, -3 is an odd number and should be counted according to the function specification ("odd OR positive"). The error occurs immediately after checking the condition for x[0], where count remains 0 instead of becoming 1.

---

## Summary Table

| Program | Fault Description | Fix |
|---------|------------------|-----|
| **findLast** | Loop condition `i > 0` excludes index 0 | Change to `i >= 0` |
| **lastZero** | Searches forward instead of backward | Change loop to `for (let i = x.length - 1; i >= 0; i--)` |
| **countPositive** | Condition `>= 0` incorrectly counts zero as positive | Change to `> 0` |
| **oddOrPos** | Condition `% 2 === 1` fails for negative odd numbers | Change to `% 2 !== 0` |

## Key Insights

All four programs have been analyzed with detailed answers to questions (a) through (e). Key findings:

1. **findLast**: Loop condition excludes index 0 - can have error state without failure when target is found at a higher index
2. **lastZero**: Searches forward instead of backward - can have error state without failure when only one zero exists
3. **countPositive**: Counts zero as positive - **cannot** have error state without failure (error directly causes wrong output)
4. **oddOrPos**: Modulo operator returns -1 for negative odd numbers, not 1 - **cannot** have error state without failure (error directly causes wrong output)
