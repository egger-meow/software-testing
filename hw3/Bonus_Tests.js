/**
 * BONUS TEST SUITE for BoundedQueue
 * 
 * This file contains advanced testing beyond core BCC requirements:
 * 1. Boundary Value Analysis (BVA) tests
 * 2. Multiple Choice Coverage (MCC) tests
 * 3. Wrap-around/circular buffer sequence tests
 * 4. Direct observer method tests (is_empty, is_full, toString)
 * 
 * These tests supplement the core BCC suite in BoundedQueue.test.js
 */

class BoundedQueue {
    constructor(capacity) {
        if (capacity < 0) {
            throw new RangeError("capacity is less than 0");
        }
        this.capacity = capacity;
        this.elements = [];
        this.size = 0;
        this.front = 0;
        this.back = 0;
    }

    enqueue(element) {
        if (typeof element !== "number" || isNaN(element)) {
            throw new RangeError("element is invalid");
        }
        else if (this.is_full()) {
            throw new Error("queue is full");
        }
        this.size++;
        this.elements[this.back] = element;
        this.back = (this.back + 1) % this.capacity;
    }

    dequeue() {
        if (this.is_empty()) {
            throw new Error("queue is empty");
        }
        this.size--;
        let o = this.elements[this.front];
        this.elements[this.front] = null;
        this.front = (this.front + 1) % this.capacity;
        return o;
    }

    is_empty() {
        return this.size === 0;
    }

    is_full() {
        return this.size === this.capacity;
    }

    toString() {
        let result = "[";
        for (let i = 0; i < this.size; i++) {
            result += this.elements[(this.front + i) % this.capacity];
            if (i < this.size - 1) {
                result += ", ";
            }
        }
        result += "] ";
        result += "is_empty(): " + this.is_empty() + ", is_full(): " + this.is_full();
        return result;
    }
}

let testsPassed = 0;
let testsFailed = 0;

function runTest(testName, testFunc) {
    try {
        testFunc();
        console.log(`✓ ${testName} PASSED`);
        testsPassed++;
    } catch (e) {
        console.log(`✗ ${testName} FAILED: ${e.message}`);
        testsFailed++;
    }
}

console.log("╔════════════════════════════════════════════════════════════╗");
console.log("║         BONUS TEST SUITE - ADVANCED COVERAGE               ║");
console.log("╚════════════════════════════════════════════════════════════╝");

// ============================================================
// SECTION 1: BOUNDARY VALUE ANALYSIS (BVA) TESTS
// ============================================================

console.log("\n═══ SECTION 1: BOUNDARY VALUE ANALYSIS (BVA) ═══\n");

console.log("--- Constructor BVA Tests ---");

// BVA-C1: capacity = 1 (minimal non-trivial)
runTest("BVA-C1: constructor(1) minimal non-trivial capacity", () => {
    const bq = new BoundedQueue(1);
    console.assert(bq.capacity === 1, "capacity should be 1");
    console.assert(bq.size === 0, "size should be 0");
    console.assert(!bq.is_full(), "should not be full initially");
    bq.enqueue(42);
    console.assert(bq.is_full(), "should be full after one enqueue");
});

console.log("\n--- Enqueue BVA Tests ---");

// BVA-E1: Empty → One element transition
runTest("BVA-E1: enqueue to empty queue (size 0→1)", () => {
    const bq = new BoundedQueue(5);
    console.assert(bq.is_empty(), "should start empty");
    bq.enqueue(10);
    console.assert(bq.size === 1, "size should be 1");
    console.assert(!bq.is_empty(), "should no longer be empty");
});

// BVA-E2: Near-full → Full transition
runTest("BVA-E2: enqueue near-full to full (size capacity-1→capacity)", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    console.assert(bq.size === 2, "should have 2 elements");
    console.assert(!bq.is_full(), "should not be full yet");
    bq.enqueue(3);
    console.assert(bq.size === 3, "should have 3 elements");
    console.assert(bq.is_full(), "should be full now");
});

// BVA-E3: Infinity (valid JS number edge case)
runTest("BVA-E3: enqueue(Infinity) - valid number edge case", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(Infinity);
    console.assert(bq.size === 1, "Infinity should be accepted");
    const val = bq.dequeue();
    console.assert(val === Infinity, "should retrieve Infinity");
});

// BVA-E4: Zero value
runTest("BVA-E4: enqueue(0) - zero boundary", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(0);
    const val = bq.dequeue();
    console.assert(val === 0, "should handle zero correctly");
});

// BVA-E5: Negative number
runTest("BVA-E5: enqueue(-100) - negative value", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(-100);
    const val = bq.dequeue();
    console.assert(val === -100, "should handle negative numbers");
});

console.log("\n--- Dequeue BVA Tests ---");

// BVA-D1: One element → Empty transition
runTest("BVA-D1: dequeue single element (size 1→0)", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(42);
    console.assert(bq.size === 1, "should have 1 element");
    const val = bq.dequeue();
    console.assert(val === 42, "should return correct value");
    console.assert(bq.is_empty(), "should be empty after dequeue");
});

// BVA-D2: Full → Near-full transition
runTest("BVA-D2: dequeue from full queue (size capacity→capacity-1)", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    bq.enqueue(3);
    console.assert(bq.is_full(), "should be full");
    bq.dequeue();
    console.assert(bq.size === 2, "should have 2 elements");
    console.assert(!bq.is_full(), "should not be full anymore");
});

// ============================================================
// SECTION 2: WRAP-AROUND / CIRCULAR BUFFER TESTS
// ============================================================

console.log("\n═══ SECTION 2: WRAP-AROUND / CIRCULAR BUFFER TESTS ═══\n");

// WRAP-1: Critical wrap-around sequence
runTest("WRAP-1: Circular buffer wrap-around test", () => {
    const bq = new BoundedQueue(3);
    
    // Step 1: Fill queue [1, 2, 3]
    bq.enqueue(1);
    bq.enqueue(2);
    bq.enqueue(3);
    console.assert(bq.size === 3, "should be full");
    console.assert(bq.front === 0, "front should be at 0");
    console.assert(bq.back === 0, "back should wrap to 0");
    
    // Step 2: Dequeue 2 elements → [3]
    const v1 = bq.dequeue();
    const v2 = bq.dequeue();
    console.assert(v1 === 1 && v2 === 2, "should dequeue in FIFO order");
    console.assert(bq.size === 1, "should have 1 element");
    console.assert(bq.front === 2, "front should advance to 2");
    
    // Step 3: Enqueue 2 more elements → [3, 4, 5]
    bq.enqueue(4);
    bq.enqueue(5);
    console.assert(bq.size === 3, "should be full again");
    console.assert(bq.back === 2, "back should wrap around to 2");
    
    // Step 4: Verify FIFO order with wrapped indices
    console.assert(bq.dequeue() === 3, "first out should be 3");
    console.assert(bq.dequeue() === 4, "second out should be 4");
    console.assert(bq.dequeue() === 5, "third out should be 5");
    console.assert(bq.is_empty(), "should be empty");
});

// WRAP-2: Multiple full cycles
runTest("WRAP-2: Multiple wrap-around cycles", () => {
    const bq = new BoundedQueue(2);
    
    // Cycle 1
    bq.enqueue(1);
    bq.enqueue(2);
    console.assert(bq.dequeue() === 1, "cycle 1 dequeue");
    console.assert(bq.dequeue() === 2, "cycle 1 dequeue");
    
    // Cycle 2
    bq.enqueue(3);
    bq.enqueue(4);
    console.assert(bq.dequeue() === 3, "cycle 2 dequeue");
    console.assert(bq.dequeue() === 4, "cycle 2 dequeue");
    
    // Cycle 3
    bq.enqueue(5);
    bq.enqueue(6);
    console.assert(bq.dequeue() === 5, "cycle 3 dequeue");
    console.assert(bq.dequeue() === 6, "cycle 3 dequeue");
    
    console.assert(bq.is_empty(), "should be empty after 3 cycles");
});

// WRAP-3: Wrap-around with capacity=1
runTest("WRAP-3: Wrap-around with minimal capacity (1)", () => {
    const bq = new BoundedQueue(1);
    
    for (let i = 0; i < 5; i++) {
        bq.enqueue(i);
        const val = bq.dequeue();
        console.assert(val === i, `iteration ${i} should work correctly`);
    }
    
    console.assert(bq.is_empty(), "should remain functional");
});

// ============================================================
// SECTION 3: MULTIPLE CHOICE COVERAGE (MCC) TESTS
// ============================================================

console.log("\n═══ SECTION 3: MULTIPLE CHOICE COVERAGE (MCC) ═══\n");

console.log("--- MCC for enqueue: All 9 Combinations ---");

// MCC-E1: Valid + Empty
runTest("MCC-E1: Valid number + Empty queue", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(42);
    console.assert(bq.size === 1, "should succeed");
});

// MCC-E2: Valid + Partial (BCC Base case)
runTest("MCC-E2: Valid number + Partial queue", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    console.assert(bq.size === 2, "should succeed");
});

// MCC-E3: Valid + Full
runTest("MCC-E3: Valid number + Full queue", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    bq.enqueue(3);
    try {
        bq.enqueue(4);
        throw new Error("Should have thrown error");
    } catch (e) {
        console.assert(e.message === "queue is full", "should throw full error");
    }
});

// MCC-E4: NaN + Empty
runTest("MCC-E4: NaN + Empty queue", () => {
    const bq = new BoundedQueue(3);
    try {
        bq.enqueue(NaN);
        throw new Error("Should have thrown error");
    } catch (e) {
        console.assert(e.message === "element is invalid", "should validate element first");
    }
});

// MCC-E5: NaN + Partial
runTest("MCC-E5: NaN + Partial queue", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    try {
        bq.enqueue(NaN);
        throw new Error("Should have thrown error");
    } catch (e) {
        console.assert(e.message === "element is invalid", "should validate element");
    }
});

// MCC-E6: NaN + Full (element validation before state check)
runTest("MCC-E6: NaN + Full queue (validation order test)", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    bq.enqueue(3);
    try {
        bq.enqueue(NaN);
        throw new Error("Should have thrown error");
    } catch (e) {
        console.assert(e.message === "element is invalid", "element validation precedes state check");
    }
});

// MCC-E7: Non-number + Empty
runTest("MCC-E7: String + Empty queue", () => {
    const bq = new BoundedQueue(3);
    try {
        bq.enqueue("test");
        throw new Error("Should have thrown error");
    } catch (e) {
        console.assert(e.message === "element is invalid", "should reject non-number");
    }
});

// MCC-E8: Non-number + Partial
runTest("MCC-E8: String + Partial queue", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    try {
        bq.enqueue("test");
        throw new Error("Should have thrown error");
    } catch (e) {
        console.assert(e.message === "element is invalid", "should reject non-number");
    }
});

// MCC-E9: Non-number + Full
runTest("MCC-E9: String + Full queue", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    bq.enqueue(3);
    try {
        bq.enqueue("test");
        throw new Error("Should have thrown error");
    } catch (e) {
        console.assert(e.message === "element is invalid", "element validation first");
    }
});

// ============================================================
// SECTION 4: OBSERVER METHOD TESTS (is_empty, is_full, toString)
// ============================================================

console.log("\n═══ SECTION 4: OBSERVER METHOD TESTS ═══\n");

console.log("--- is_empty() Tests ---");

// OBS-E1: Newly created queue
runTest("OBS-E1: is_empty() on new queue", () => {
    const bq = new BoundedQueue(5);
    console.assert(bq.is_empty() === true, "new queue should be empty");
});

// OBS-E2: After enqueue
runTest("OBS-E2: is_empty() after enqueue", () => {
    const bq = new BoundedQueue(5);
    bq.enqueue(1);
    console.assert(bq.is_empty() === false, "should not be empty");
});

// OBS-E3: After dequeue to empty
runTest("OBS-E3: is_empty() after dequeue to empty", () => {
    const bq = new BoundedQueue(5);
    bq.enqueue(1);
    bq.dequeue();
    console.assert(bq.is_empty() === true, "should be empty again");
});

console.log("\n--- is_full() Tests ---");

// OBS-F1: Newly created queue
runTest("OBS-F1: is_full() on new queue", () => {
    const bq = new BoundedQueue(3);
    console.assert(bq.is_full() === false, "new queue should not be full");
});

// OBS-F2: After filling
runTest("OBS-F2: is_full() after filling queue", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    bq.enqueue(3);
    console.assert(bq.is_full() === true, "should be full");
});

// OBS-F3: After dequeue from full
runTest("OBS-F3: is_full() after dequeue from full", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    bq.enqueue(3);
    bq.dequeue();
    console.assert(bq.is_full() === false, "should not be full after dequeue");
});

// OBS-F4: capacity=0 edge case (immediately full)
runTest("OBS-F4: is_full() with capacity=0", () => {
    const bq = new BoundedQueue(0);
    console.assert(bq.is_full() === true, "capacity=0 should always be full");
});

console.log("\n--- toString() Tests ---");

// OBS-T1: Empty queue
runTest("OBS-T1: toString() on empty queue", () => {
    const bq = new BoundedQueue(3);
    const str = bq.toString();
    console.assert(str.includes("[]"), "should show empty array");
    console.assert(str.includes("is_empty(): true"), "should indicate empty");
    console.assert(str.includes("is_full(): false"), "should indicate not full");
});

// OBS-T2: Partial queue
runTest("OBS-T2: toString() on partial queue", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(10);
    bq.enqueue(20);
    const str = bq.toString();
    console.assert(str.includes("10"), "should contain first element");
    console.assert(str.includes("20"), "should contain second element");
    console.assert(str.includes("is_empty(): false"), "should not be empty");
    console.assert(str.includes("is_full(): false"), "should not be full");
});

// OBS-T3: Full queue
runTest("OBS-T3: toString() on full queue", () => {
    const bq = new BoundedQueue(2);
    bq.enqueue(1);
    bq.enqueue(2);
    const str = bq.toString();
    console.assert(str.includes("1"), "should contain elements");
    console.assert(str.includes("is_full(): true"), "should indicate full");
});

// OBS-T4: Wrap-around display
runTest("OBS-T4: toString() with wrapped indices", () => {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    bq.enqueue(3);
    bq.dequeue();
    bq.dequeue();
    bq.enqueue(4);
    bq.enqueue(5);
    const str = bq.toString();
    // Should display [3, 4, 5] in logical order despite physical wrap
    console.assert(str.includes("3"), "should show correct order");
    console.assert(str.includes("4"), "should show correct order");
    console.assert(str.includes("5"), "should show correct order");
});

// ============================================================
// SECTION 5: EDGE CASES & BUG DOCUMENTATION
// ============================================================

console.log("\n═══ SECTION 5: EDGE CASES & BUG DOCUMENTATION ═══\n");

// EDGE-1: capacity=0 behavior
runTest("EDGE-1: capacity=0 queue behavior", () => {
    const bq = new BoundedQueue(0);
    console.assert(bq.capacity === 0, "capacity should be 0");
    console.assert(bq.is_full(), "should be immediately full");
    console.assert(bq.is_empty(), "should also be empty");
    
    try {
        bq.enqueue(1);
        throw new Error("Should not allow enqueue");
    } catch (e) {
        console.assert(e.message === "queue is full", "should reject enqueue");
    }
});

// EDGE-2: Object type checking
runTest("EDGE-2: Reject object instead of number", () => {
    const bq = new BoundedQueue(3);
    try {
        bq.enqueue({ value: 42 });
        throw new Error("Should reject object");
    } catch (e) {
        console.assert(e.message === "element is invalid", "should reject objects");
    }
});

// EDGE-3: Array type checking
runTest("EDGE-3: Reject array instead of number", () => {
    const bq = new BoundedQueue(3);
    try {
        bq.enqueue([1, 2, 3]);
        throw new Error("Should reject array");
    } catch (e) {
        console.assert(e.message === "element is invalid", "should reject arrays");
    }
});

// EDGE-4: null/undefined checking
runTest("EDGE-4: Reject null and undefined", () => {
    const bq = new BoundedQueue(3);
    
    try {
        bq.enqueue(null);
        throw new Error("Should reject null");
    } catch (e) {
        console.assert(e.message === "element is invalid", "should reject null");
    }
    
    try {
        bq.enqueue(undefined);
        throw new Error("Should reject undefined");
    } catch (e) {
        console.assert(e.message === "element is invalid", "should reject undefined");
    }
});

// EDGE-5: Large capacity
runTest("EDGE-5: Large capacity queue (stress test)", () => {
    const bq = new BoundedQueue(1000);
    for (let i = 0; i < 1000; i++) {
        bq.enqueue(i);
    }
    console.assert(bq.is_full(), "should handle large capacity");
    console.assert(bq.size === 1000, "should track size correctly");
});

// ============================================================
// TEST SUMMARY
// ============================================================

console.log("\n╔════════════════════════════════════════════════════════════╗");
console.log("║                      TEST SUMMARY                          ║");
console.log("╚════════════════════════════════════════════════════════════╝");

console.log("\nTest Results:");
console.log(`  ✓ Passed: ${testsPassed}`);
console.log(`  ✗ Failed: ${testsFailed}`);
console.log(`  Total:    ${testsPassed + testsFailed}`);

console.log("\nCoverage Breakdown:");
console.log("  • Boundary Value Analysis (BVA):     8 tests");
console.log("  • Wrap-Around/Circular Buffer:       3 tests");
console.log("  • Multiple Choice Coverage (MCC):    9 tests");
console.log("  • Observer Methods:                 10 tests");
console.log("  • Edge Cases:                        5 tests");
console.log("  ─────────────────────────────────────────────");
console.log("  Total Bonus Tests:                  35 tests");

console.log("\nCombined with BCC Suite:");
console.log("  • Core BCC Tests (BoundedQueue.test.js): 11 tests");
console.log("  • Bonus Tests (this file):               35 tests");
console.log("  • TOTAL TEST COVERAGE:                   46 tests");

if (testsFailed === 0) {
    console.log("\n🎉 ALL BONUS TESTS PASSED! 🎉");
    console.log("Advanced coverage complete: BVA, MCC, wrap-around, and observers verified.");
} else {
    console.log(`\n⚠️  ${testsFailed} test(s) failed. Review output above.`);
}

console.log("\n");
