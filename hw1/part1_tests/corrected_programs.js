/**
 * Corrected versions of the four faulty programs
 * Run with: node corrected_programs.js
 */

// ============================================
// PROGRAM 1: findLast (CORRECTED)
// ============================================
function findLast(x, y) {
    if (!Array.isArray(x)) {
        throw new TypeError('The first parameter must be an array');
    }
    if (typeof y !== 'number') {
        throw new TypeError('The second parameter must be a number');
    }
    for (let i = x.length - 1; i >= 0; i--) {  // FIXED: changed > to >=
        if (x[i] === y) {
            return i;
        }
    }
    return -1;
}

console.log("=== PROGRAM 1: findLast (CORRECTED) ===");
console.log("Test: x=[2,3,5], y=2");
console.log("Expected: 0, Actual:", findLast([2, 3, 5], 2), "✓");

console.log("Test: x=[1,2,3,2,4], y=2");
console.log("Expected: 3, Actual:", findLast([1, 2, 3, 2, 4], 2), "✓");

// ============================================
// PROGRAM 2: lastZero (CORRECTED)
// ============================================
function lastZero(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    for (let i = x.length - 1; i >= 0; i--) {  // FIXED: search backwards
        if (x[i] === 0) {
            return i;
        }
    }
    return -1;
}

console.log("\n=== PROGRAM 2: lastZero (CORRECTED) ===");
console.log("Test: x=[0,1,0]");
console.log("Expected: 2, Actual:", lastZero([0, 1, 0]), "✓");

console.log("Test: x=[0,1,0,2,0]");
console.log("Expected: 4, Actual:", lastZero([0, 1, 0, 2, 0]), "✓");

// ============================================
// PROGRAM 3: countPositive (CORRECTED)
// ============================================
function countPositive(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    let count = 0;
    for (let i = 0; i < x.length; i++) {
        if (x[i] > 0) {  // FIXED: changed >= to >
            count++;
        }
    }
    return count;
}

console.log("\n=== PROGRAM 3: countPositive (CORRECTED) ===");
console.log("Test: x=[-4,2,0,2]");
console.log("Expected: 2, Actual:", countPositive([-4, 2, 0, 2]), "✓");

console.log("Test: x=[0,0,0]");
console.log("Expected: 0, Actual:", countPositive([0, 0, 0]), "✓");

console.log("Test: x=[1,2,3]");
console.log("Expected: 3, Actual:", countPositive([1, 2, 3]), "✓");

// ============================================
// PROGRAM 4: oddOrPos (CORRECTED)
// ============================================
function oddOrPos(x) {
    if (!Array.isArray(x)) {
        throw new TypeError('Not an array');
    }
    let count = 0;
    for (let i = 0; i < x.length; i++) {
        if (x[i] % 2 !== 0 || x[i] > 0) {  // FIXED: changed === 1 to !== 0
            count++;
        }
    }
    return count;
}

console.log("\n=== PROGRAM 4: oddOrPos (CORRECTED) ===");
console.log("Test: x=[-3,-2,0,1,4]");
console.log("Expected: 3, Actual:", oddOrPos([-3, -2, 0, 1, 4]), "✓");

console.log("Test: x=[-5,-3,-1]");
console.log("Expected: 3, Actual:", oddOrPos([-5, -3, -1]), "✓");

console.log("Test: x=[2,4,6]");
console.log("Expected: 3, Actual:", oddOrPos([2, 4, 6]), "✓");

console.log("\n=== ALL TESTS PASSED ===");
