/**
 * Test file for the four faulty programs
 * Run with: node test_faulty_programs.js
 */

// ============================================
// PROGRAM 1: findLast
// ============================================
function findLast(x, y) {
    if (!Array.isArray(x)) {
        throw new TypeError('The first parameter must be an array');
    }
    if (typeof y !== 'number') {
        throw new TypeError('The second parameter must be a number');
    }
    for (let i = x.length - 1; i > 0; i--) {  // FAULT: should be i >= 0
        if (x[i] === y) {
            return i;
        }
    }
    return -1;
}

console.log("=== PROGRAM 1: findLast ===");
console.log("Given failing test: x=[2,3,5], y=2");
console.log("Expected: 0, Actual:", findLast([2, 3, 5], 2));

console.log("\n(b) Does not execute fault: x=[], y=2");
console.log("Expected: -1, Actual:", findLast([], 2));

console.log("\n(c) Executes fault, no error state: x=[3,5,7], y=2");
console.log("Expected: -1, Actual:", findLast([3, 5, 7], 2));

console.log("\n(d) Error state, no failure: x=[1,2,3,4], y=2");
console.log("Expected: 1, Actual:", findLast([1, 2, 3, 4], 2));

// ============================================
// PROGRAM 2: lastZero
// ============================================
function lastZero(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    for (let i = 0; i < x.length; i++) {  // FAULT: should search backwards
        if (x[i] === 0) {
            return i;
        }
    }
    return -1;
}

console.log("\n\n=== PROGRAM 2: lastZero ===");
console.log("Given failing test: x=[0,1,0]");
console.log("Expected: 2, Actual:", lastZero([0, 1, 0]));

console.log("\n(b) Does not execute fault: x=[]");
console.log("Expected: -1, Actual:", lastZero([]));

console.log("\n(c) Executes fault, no error state: x=[1,2,3]");
console.log("Expected: -1, Actual:", lastZero([1, 2, 3]));

console.log("\n(d) Error state, no failure: x=[0,1,2]");
console.log("Expected: 0, Actual:", lastZero([0, 1, 2]));

// ============================================
// PROGRAM 3: countPositive
// ============================================
function countPositive(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    let count = 0;
    for (let i = 0; i < x.length; i++) {
        if (x[i] >= 0) {  // FAULT: should be > 0
            count++;
        }
    }
    return count;
}

console.log("\n\n=== PROGRAM 3: countPositive ===");
console.log("Given failing test: x=[-4,2,0,2]");
console.log("Expected: 2, Actual:", countPositive([-4, 2, 0, 2]));

console.log("\n(b) Does not execute fault: x=[]");
console.log("Expected: 0, Actual:", countPositive([]));

console.log("\n(c) Executes fault, no error state: x=[1,2,3]");
console.log("Expected: 3, Actual:", countPositive([1, 2, 3]));

console.log("\n(d) Error state, no failure: NOT POSSIBLE");
console.log("Any input with zero causes both error state AND failure.");

// ============================================
// PROGRAM 4: oddOrPos
// ============================================
function oddOrPos(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    let count = 0;
    for (let i = 0; i < x.length; i++) {
        if (x[i] % 2 === 1 || x[i] > 0) {  // FAULT: % 2 === 1 doesn't work for negative odds
            count++;
        }
    }
    return count;
}

console.log("\n\n=== PROGRAM 4: oddOrPos ===");
console.log("Given failing test: x=[-3,-2,0,1,4]");
console.log("Expected: 3, Actual:", oddOrPos([-3, -2, 0, 1, 4]));

console.log("\n(b) Does not execute fault: x=[]");
console.log("Expected: 0, Actual:", oddOrPos([]));

console.log("\n(c) Executes fault, no error state: x=[1,3,5]");
console.log("Expected: 3, Actual:", oddOrPos([1, 3, 5]));

console.log("\n(d) Error state, no failure: NOT POSSIBLE");
console.log("Any input with negative odd numbers causes both error state AND failure.");

console.log("\n\n=== ADDITIONAL TESTS ===");
console.log("Verify: -3 % 2 =", -3 % 2, "(should be -1, not 1)");
console.log("Verify: -5 % 2 =", -5 % 2, "(should be -1, not 1)");
console.log("Verify: 3 % 2 =", 3 % 2, "(should be 1)");
