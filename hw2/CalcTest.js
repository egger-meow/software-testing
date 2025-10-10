const Calc = require('./Calc');

// Simple test framework
function test(name, fn) {
    try {
        fn();
        console.log(`✓ ${name}`);
    } catch (error) {
        console.error(`✗ ${name}: ${error.message}`);
        process.exitCode = 1;
    }
}

function assertEqual(actual, expected, message) {
    if (actual !== expected) {
        throw new Error(`${message}: expected ${expected}, got ${actual}`);
    }
}

function assertThrows(fn, message) {
    try {
        fn();
        throw new Error(`${message}: expected to throw but didn't`);
    } catch (error) {
        if (error.message.includes("expected to throw")) {
            throw error;
        }
        // Expected exception thrown
    }
}

// Run tests
console.log("Running Calc tests...\n");

test("test_add", () => {
    assertEqual(Calc.add(2, 3), 5, "Addition failed");
});

// TDD Step 1: Test for subtract (FAILING TEST)
test("test_subtract", () => {
    assertEqual(Calc.subtract(5, 3), 2, "Subtraction failed");
});

// TDD Step 2: Test for multiply (FAILING TEST)
test("test_multiply", () => {
    assertEqual(Calc.multiply(4, 3), 12, "Multiplication failed");
});

// TDD Step 3: Test for divide (FAILING TEST)
test("test_divide", () => {
    assertEqual(Calc.divide(10, 2), 5.0, "Division failed");
});

// TDD Step 4: Test for divide by zero (edge case)
test("test_divide_by_zero", () => {
    assertThrows(() => Calc.divide(10, 0), "Divide by zero should throw error");
});

console.log("\nAll tests completed!");
