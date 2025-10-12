/**
 * BCC Test Suite for BoundedQueue
 * Based on Input Space Partitioning Analysis
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

// ============================================================
// CONSTRUCTOR TESTS
// ============================================================

console.log("=== CONSTRUCTOR TESTS ===");

// C-T1: Base case - normal positive capacity
try {
    const bq = new BoundedQueue(5);
    console.assert(bq.capacity === 5, "C-T1 FAILED: capacity should be 5");
    console.assert(bq.size === 0, "C-T1 FAILED: size should be 0");
    console.log("✓ C-T1 PASSED: constructor(5) creates queue with capacity=5, size=0");
} catch (e) {
    console.log("✗ C-T1 FAILED:", e.message);
}

// C-T2: Invalid capacity (negative)
try {
    new BoundedQueue(-1);
    console.log("✗ C-T2 FAILED: Should throw RangeError");
} catch (e) {
    console.assert(e instanceof RangeError, "C-T2 FAILED: Wrong error type");
    console.assert(e.message === "capacity is less than 0", "C-T2 FAILED: Wrong error message");
    console.log("✓ C-T2 PASSED: constructor(-1) throws RangeError");
}

// C-T3: Edge case - capacity = 0
try {
    const bq = new BoundedQueue(0);
    console.assert(bq.capacity === 0, "C-T3 FAILED: capacity should be 0");
    console.assert(bq.size === 0, "C-T3 FAILED: size should be 0");
    console.log("✓ C-T3 PASSED: constructor(0) creates queue with capacity=0");
} catch (e) {
    console.log("✗ C-T3 FAILED:", e.message);
}

// ============================================================
// ENQUEUE TESTS
// ============================================================

console.log("\n=== ENQUEUE TESTS ===");

// E-T1: Base case - valid number, partial queue
try {
    const bq = new BoundedQueue(3);
    bq.enqueue(10);
    bq.enqueue(42);
    console.assert(bq.size === 2, "E-T1 FAILED: size should be 2");
    console.log("✓ E-T1 PASSED: enqueue(42) on partial queue succeeds");
} catch (e) {
    console.log("✗ E-T1 FAILED:", e.message);
}

// E-T2: Invalid element - NaN
try {
    const bq = new BoundedQueue(3);
    bq.enqueue(10);
    bq.enqueue(NaN);
    console.log("✗ E-T2 FAILED: Should throw RangeError for NaN");
} catch (e) {
    console.assert(e instanceof RangeError, "E-T2 FAILED: Wrong error type");
    console.assert(e.message === "element is invalid", "E-T2 FAILED: Wrong error message");
    console.log("✓ E-T2 PASSED: enqueue(NaN) throws RangeError");
}

// E-T3: Invalid element - non-number
try {
    const bq = new BoundedQueue(3);
    bq.enqueue(10);
    bq.enqueue("test");
    console.log("✗ E-T3 FAILED: Should throw RangeError for string");
} catch (e) {
    console.assert(e instanceof RangeError, "E-T3 FAILED: Wrong error type");
    console.assert(e.message === "element is invalid", "E-T3 FAILED: Wrong error message");
    console.log("✓ E-T3 PASSED: enqueue('test') throws RangeError");
}

// E-T4: Enqueue to empty queue
try {
    const bq = new BoundedQueue(3);
    bq.enqueue(10);
    console.assert(bq.size === 1, "E-T4 FAILED: size should be 1");
    console.assert(bq.is_empty() === false, "E-T4 FAILED: queue should not be empty");
    console.log("✓ E-T4 PASSED: enqueue(10) on empty queue succeeds");
} catch (e) {
    console.log("✗ E-T4 FAILED:", e.message);
}

// E-T5: Enqueue to full queue
try {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    bq.enqueue(3);
    bq.enqueue(99);
    console.log("✗ E-T5 FAILED: Should throw Error for full queue");
} catch (e) {
    console.assert(e instanceof Error, "E-T5 FAILED: Wrong error type");
    console.assert(e.message === "queue is full", "E-T5 FAILED: Wrong error message");
    console.log("✓ E-T5 PASSED: enqueue(99) on full queue throws Error");
}

// ============================================================
// DEQUEUE TESTS
// ============================================================

console.log("\n=== DEQUEUE TESTS ===");

// D-T1: Base case - dequeue from partial queue
try {
    const bq = new BoundedQueue(3);
    bq.enqueue(10);
    bq.enqueue(20);
    const val = bq.dequeue();
    console.assert(val === 10, "D-T1 FAILED: should return 10");
    console.assert(bq.size === 1, "D-T1 FAILED: size should be 1");
    console.log("✓ D-T1 PASSED: dequeue() from partial queue returns 10");
} catch (e) {
    console.log("✗ D-T1 FAILED:", e.message);
}

// D-T2: Dequeue from empty queue
try {
    const bq = new BoundedQueue(3);
    bq.dequeue();
    console.log("✗ D-T2 FAILED: Should throw Error for empty queue");
} catch (e) {
    console.assert(e instanceof Error, "D-T2 FAILED: Wrong error type");
    console.assert(e.message === "queue is empty", "D-T2 FAILED: Wrong error message");
    console.log("✓ D-T2 PASSED: dequeue() on empty queue throws Error");
}

// D-T3: Dequeue from full queue
try {
    const bq = new BoundedQueue(3);
    bq.enqueue(1);
    bq.enqueue(2);
    bq.enqueue(3);
    const val = bq.dequeue();
    console.assert(val === 1, "D-T3 FAILED: should return 1");
    console.assert(bq.size === 2, "D-T3 FAILED: size should be 2");
    console.assert(bq.is_full() === false, "D-T3 FAILED: queue should not be full");
    console.log("✓ D-T3 PASSED: dequeue() from full queue returns 1");
} catch (e) {
    console.log("✗ D-T3 FAILED:", e.message);
}

// ============================================================
// SUMMARY
// ============================================================

console.log("\n=== TEST SUMMARY ===");
console.log("Total BCC Tests: 11 (3 Constructor + 5 Enqueue + 3 Dequeue)");
console.log("All tests validate Base Choice Coverage requirements");
