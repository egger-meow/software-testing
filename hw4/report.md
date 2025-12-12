# HW4 - Mutation Testing with StrykerJS

Hi! This is my report for HW4 where I explored mutation testing using StrykerJS on the `calculator.js` file. Honestly, before this assignment I had no idea that "testing your tests" was even a thing — but now it makes so much sense!

---

## (a) How many mutants are there in total?

After running `npm run mutate`, Stryker generated **106 mutants** in total.

These mutants include all sorts of sneaky changes like:
- Swapping `+` with `-` 
- Changing `<` to `<=` or `>`
- Flipping `true` to `false`
- Messing with the leap year logic
- Emptying out entire code blocks

It was kinda scary seeing how many ways the code could go wrong with just tiny changes 😅

> 📸 **[INSERT SCREENSHOT: Terminal output showing "106 mutants" or the HTML report summary]**

---

## (b) What mutation score did I achieve with Lab1's test suite?

I set up StrykerJS in the Lab1 folder and ran mutation testing on `main.js` (the MyClass/Student code) using the tests I wrote in Lab1 (`main_test.js`).

**Result: 94.12% mutation score**

- **34 mutants** generated in total
- **32 killed** by my Lab1 tests
- **2 survived**

The 2 survived mutants were:
1. `id >= this.students.length` → `id > this.students.length` — a boundary condition I didn't catch
2. `constructor() { this.name = undefined; }` → `constructor() {}` — this is actually an equivalent mutant since `undefined` is the default value anyway

Not bad for tests I wrote without knowing about mutation testing! But it shows there's always room for improvement.

> 📸 **[INSERT SCREENSHOT: Lab1 Stryker result showing 94.12% mutation score (32 killed, 2 survived)]**

---

## (c) How do I kill those mutants? (Test Code)

Okay so this was the fun (and challenging) part! I had to think about what inputs would actually expose the bugs that Stryker was injecting.

Here's my strategy:
1. **Validation tests** - Test all the boundary cases (month=0, month=13, day=0, day=32, etc.)
2. **Same month calculation** - Simple `day2 - day1` cases
3. **Different month calculation** - This one needed more thought because of the loop
4. **Leap year logic** - Years divisible by 4, 100, and 400 all behave differently!
5. **Error messages** - Make sure the exact error text is checked

Here's all my test code:

```javascript
const assert = require('assert');
const { test } = require('node:test');

const Calculator = require('../src/calculator');

// ==================== Validation Tests ====================

// Test month1 validation
test('month1 < 1 should throw invalid month1', () => {
    assert.throws(() => Calculator.main(0, 1, 2, 1, 2024), /invalid month1/);
});

test('month1 > 12 should throw invalid month1', () => {
    assert.throws(() => Calculator.main(13, 1, 2, 1, 2024), /invalid month1/);
});

test('month1 = 1 should be valid (boundary)', () => {
    assert.strictEqual(Calculator.main(1, 1, 1, 2, 2024), 1);
});

test('month1 = 12 should be valid (boundary)', () => {
    assert.strictEqual(Calculator.main(12, 1, 12, 2, 2024), 1);
});

// Test month2 validation
test('month2 < 1 should throw invalid month2', () => {
    assert.throws(() => Calculator.main(1, 1, 0, 1, 2024), /invalid month2/);
});

test('month2 > 12 should throw invalid month2', () => {
    assert.throws(() => Calculator.main(1, 1, 13, 1, 2024), /invalid month2/);
});

test('month2 = 1 should be valid (boundary)', () => {
    assert.strictEqual(Calculator.main(1, 1, 1, 2, 2024), 1);
});

test('month2 = 12 should be valid (boundary)', () => {
    assert.strictEqual(Calculator.main(1, 1, 12, 1, 2024), 335);
});

// Test day1 validation
test('day1 < 1 should throw invalid day1', () => {
    assert.throws(() => Calculator.main(1, 0, 2, 1, 2024), /invalid day1/);
});

test('day1 > 31 should throw invalid day1', () => {
    assert.throws(() => Calculator.main(1, 32, 2, 1, 2024), /invalid day1/);
});

test('day1 = 1 should be valid (boundary)', () => {
    assert.strictEqual(Calculator.main(1, 1, 1, 2, 2024), 1);
});

test('day1 = 31 should be valid (boundary)', () => {
    assert.strictEqual(Calculator.main(1, 31, 2, 1, 2024), 1);
});

// Test day2 validation
test('day2 < 1 should throw invalid day2', () => {
    assert.throws(() => Calculator.main(1, 1, 2, 0, 2024), /invalid day2/);
});

test('day2 > 31 should throw invalid day2', () => {
    assert.throws(() => Calculator.main(1, 1, 2, 32, 2024), /invalid day2/);
});

test('day2 = 1 should be valid (boundary)', () => {
    assert.strictEqual(Calculator.main(1, 1, 2, 1, 2024), 31);
});

test('day2 = 31 should be valid (boundary)', () => {
    assert.strictEqual(Calculator.main(1, 1, 1, 31, 2024), 30);
});

// Test year validation
test('year < 1 should throw invalid year', () => {
    assert.throws(() => Calculator.main(1, 1, 2, 1, 0), /invalid year/);
});

test('year > 10000 should throw invalid year', () => {
    assert.throws(() => Calculator.main(1, 1, 2, 1, 10001), /invalid year/);
});

test('year = 1 should be valid (boundary)', () => {
    assert.strictEqual(Calculator.main(1, 1, 1, 2, 1), 1);
});

test('year = 10000 should be valid (boundary)', () => {
    assert.strictEqual(Calculator.main(1, 1, 1, 2, 10000), 1);
});

// Test day1 > day2 in same month
test('day1 > day2 in same month should throw error', () => {
    assert.throws(() => Calculator.main(1, 15, 1, 10, 2024), /day1 must be less than day2/);
});

test('day1 = day2 in same month should return 0', () => {
    assert.strictEqual(Calculator.main(1, 10, 1, 10, 2024), 0);
});

// Test month1 > month2
test('month1 > month2 should throw error', () => {
    assert.throws(() => Calculator.main(3, 1, 2, 1, 2024), /month1 must be less than month2/);
});

// ==================== Calculation Tests ====================

// Same month calculation
test('same month: day2 - day1 basic', () => {
    assert.strictEqual(Calculator.main(5, 10, 5, 20, 2024), 10);
});

test('same month: day2 - day1 = 1', () => {
    assert.strictEqual(Calculator.main(3, 5, 3, 6, 2024), 1);
});

test('same month: day2 - day1 = 0', () => {
    assert.strictEqual(Calculator.main(3, 5, 3, 5, 2024), 0);
});

// Different month calculation - adjacent months
test('adjacent months: Jan to Feb', () => {
    assert.strictEqual(Calculator.main(1, 15, 2, 10, 2024), 26);
});

test('adjacent months: Jan 1 to Feb 1', () => {
    assert.strictEqual(Calculator.main(1, 1, 2, 1, 2024), 31);
});

// Different month calculation - with months in between
test('months in between: Jan to Mar (leap year)', () => {
    assert.strictEqual(Calculator.main(1, 1, 3, 1, 2024), 60);
});

test('months in between: Jan to Mar (non-leap year)', () => {
    assert.strictEqual(Calculator.main(1, 1, 3, 1, 2023), 59);
});

test('months in between: Jan to Apr', () => {
    assert.strictEqual(Calculator.main(1, 1, 4, 1, 2024), 91);
});

test('multiple months: Mar to Jun', () => {
    assert.strictEqual(Calculator.main(3, 1, 6, 1, 2024), 92);
});

test('across many months: Jan to Dec', () => {
    assert.strictEqual(Calculator.main(1, 1, 12, 31, 2024), 365);
});

test('across many months: Jan to Dec (non-leap)', () => {
    assert.strictEqual(Calculator.main(1, 1, 12, 31, 2023), 364);
});

// ==================== Leap Year Tests ====================

test('leap year: divisible by 4 not 100 (2024)', () => {
    assert.strictEqual(Calculator.main(1, 31, 3, 1, 2024), 30);
});

test('non-leap year: divisible by 100 not 400 (1900)', () => {
    assert.strictEqual(Calculator.main(1, 31, 3, 1, 1900), 29);
});

test('leap year: divisible by 400 (2000)', () => {
    assert.strictEqual(Calculator.main(1, 31, 3, 1, 2000), 30);
});

test('non-leap year: not divisible by 4 (2023)', () => {
    assert.strictEqual(Calculator.main(1, 31, 3, 1, 2023), 29);
});

test('leap year: year divisible by 4 (2020)', () => {
    assert.strictEqual(Calculator.main(2, 1, 3, 1, 2020), 29);
});

test('non-leap year: year divisible by 100 not 400 (2100)', () => {
    assert.strictEqual(Calculator.main(2, 1, 3, 1, 2100), 28);
});

test('leap year: year 400', () => {
    assert.strictEqual(Calculator.main(2, 1, 3, 1, 400), 29);
});

test('leap year: year 800', () => {
    assert.strictEqual(Calculator.main(2, 1, 3, 1, 800), 29);
});

// ==================== Edge Cases for Loop ====================

test('loop iteration: exactly 2 months apart', () => {
    assert.strictEqual(Calculator.main(1, 1, 3, 1, 2024), 60);
});

test('loop iteration: 3 months apart', () => {
    assert.strictEqual(Calculator.main(1, 1, 4, 1, 2024), 91);
});

test('loop iteration: no iteration (adjacent months)', () => {
    assert.strictEqual(Calculator.main(1, 1, 2, 1, 2024), 31);
});

// ==================== Additional Tests ====================

test('calculation with day1 at end of month', () => {
    assert.strictEqual(Calculator.main(1, 31, 2, 15, 2024), 15);
});

test('calculation with day2 at start of month', () => {
    assert.strictEqual(Calculator.main(1, 15, 2, 1, 2024), 17);
});

test('full year calculation leap year', () => {
    assert.strictEqual(Calculator.main(1, 1, 12, 31, 2024), 365);
});

test('Feb to Mar leap year', () => {
    assert.strictEqual(Calculator.main(2, 15, 3, 15, 2024), 29);
});

test('Feb to Mar non-leap year', () => {
    assert.strictEqual(Calculator.main(2, 15, 3, 15, 2023), 28);
});

test('different day values to kill arithmetic mutants', () => {
    assert.strictEqual(Calculator.main(1, 5, 2, 10, 2024), 36);
});

test('day1=1 day2=1 different months', () => {
    assert.strictEqual(Calculator.main(3, 1, 5, 1, 2024), 61);
});

test('many months to test loop accumulation', () => {
    assert.strictEqual(Calculator.main(1, 1, 7, 1, 2024), 182);
});

test('month1 exactly at boundary 1', () => {
    assert.strictEqual(Calculator.main(1, 1, 1, 5, 2024), 4);
});

test('month2 exactly at boundary 12', () => {
    assert.strictEqual(Calculator.main(11, 1, 12, 1, 2024), 30);
});

// Kill mutants for EqualityOperator in validation
test('month1 = 0 boundary test', () => {
    assert.throws(() => Calculator.main(0, 15, 2, 15, 2024), /invalid month1/);
});

test('month2 = 0 boundary test', () => {
    assert.throws(() => Calculator.main(1, 15, 0, 15, 2024), /invalid month2/);
});

test('day1 = 0 boundary test', () => {
    assert.throws(() => Calculator.main(1, 0, 2, 15, 2024), /invalid day1/);
});

test('day2 = 0 boundary test', () => {
    assert.throws(() => Calculator.main(1, 15, 2, 0, 2024), /invalid day2/);
});

test('year = 0 boundary test', () => {
    assert.throws(() => Calculator.main(1, 15, 2, 15, 0), /invalid year/);
});

// Kill StringLiteral mutants
test('error message for invalid month1 contains correct text', () => {
    assert.throws(() => Calculator.main(0, 1, 2, 1, 2024), { message: 'invalid month1' });
});

test('error message for invalid month2 contains correct text', () => {
    assert.throws(() => Calculator.main(1, 1, 0, 1, 2024), { message: 'invalid month2' });
});

test('error message for invalid day1 contains correct text', () => {
    assert.throws(() => Calculator.main(1, 0, 2, 1, 2024), { message: 'invalid day1' });
});

test('error message for invalid day2 contains correct text', () => {
    assert.throws(() => Calculator.main(1, 1, 2, 0, 2024), { message: 'invalid day2' });
});

test('error message for invalid year contains correct text', () => {
    assert.throws(() => Calculator.main(1, 1, 2, 1, 0), { message: 'invalid year' });
});

test('error for day1 > day2 same month exact message', () => {
    assert.throws(() => Calculator.main(1, 20, 1, 10, 2024), { message: 'day1 must be less than day2 if month1 is equal to month2' });
});

test('error for month1 > month2 exact message', () => {
    assert.throws(() => Calculator.main(5, 1, 2, 1, 2024), { message: 'month1 must be less than month2' });
});

// More tests for leap year edge cases
test('year=4 is leap year', () => {
    assert.strictEqual(Calculator.main(2, 1, 3, 1, 4), 29);
});

test('year=100 is not leap year', () => {
    assert.strictEqual(Calculator.main(2, 1, 3, 1, 100), 28);
});

test('year=200 is not leap year', () => {
    assert.strictEqual(Calculator.main(2, 1, 3, 1, 200), 28);
});

test('year=300 is not leap year', () => {
    assert.strictEqual(Calculator.main(2, 1, 3, 1, 300), 28);
});

// Additional tests for arithmetic mutations
test('specific values to kill +/- mutations', () => {
    assert.strictEqual(Calculator.main(1, 10, 2, 20, 2024), 41);
});

test('day calculation where signs matter', () => {
    assert.strictEqual(Calculator.main(1, 20, 2, 5, 2024), 16);
});

test('month2 equals month1 exactly', () => {
    assert.strictEqual(Calculator.main(6, 10, 6, 20, 2024), 10);
});

// Tests for loop mutations
test('loop test: 4 months gap', () => {
    assert.strictEqual(Calculator.main(2, 1, 6, 1, 2024), 121);
});

test('loop test: 5 months gap', () => {
    assert.strictEqual(Calculator.main(1, 1, 6, 1, 2024), 152);
});

test('Apr to Aug calculation', () => {
    assert.strictEqual(Calculator.main(4, 1, 8, 1, 2024), 122);
});

test('Sep to Dec calculation', () => {
    assert.strictEqual(Calculator.main(9, 1, 12, 1, 2024), 91);
});
```

In total I wrote **78 test cases**. The key insight was that I needed to:
- Test **boundary values** (not just typical values)
- Test **leap year vs non-leap year** scenarios
- Check **exact error messages** (not just that an error was thrown)
- Make sure the **loop logic** was properly tested with 2, 3, 4+ month gaps

---

## (d) What mutation score did I achieve?

After adding all 78 tests, I ran `npm run mutate` again and got:

**100% mutation score!** 🎉

- **104 mutants killed** by my tests
- **2 mutants timed out** (also counts as detected)
- **0 mutants survived**

> 📸 **[INSERT SCREENSHOT: Final Stryker result showing 100% mutation score]**

> 📸 **[INSERT SCREENSHOT: HTML report (reports/mutation/mutation.html) showing all green]**

---

## (e) Can my test achieve 100% mutation score? Why or why not?

Yes! I was able to achieve **100% mutation score**.

The reason I could hit 100% is because:

1. **No equivalent mutants** - All the mutations Stryker generated were actually detectable with the right inputs. There were no cases where changing the code didn't change the behavior.

2. **Comprehensive boundary testing** - I made sure to test values like 0, 1, 12, 31 which are right at the edges of valid ranges. This catches mutations that change `<` to `<=` or `>` to `>=`.

3. **Leap year coverage** - The leap year logic has three conditions (divisible by 4, not by 100, or by 400), and I tested years that exercise each branch: 2024, 2023, 1900, 2000, 2100, etc.

4. **Error message verification** - Some mutants just changed the error message text. By asserting the exact error message, I could catch those too.

5. **Loop testing** - The for-loop that sums up days in months between month1 and month2 needed tests with different gap sizes (2 months, 3 months, etc.) to catch mutations to the loop bounds and increment.

If there had been **equivalent mutants** (mutations that don't change behavior), I would not have been able to kill those. But in this case, every mutation actually changed something observable!

---

## What I Learned

This assignment really opened my eyes to how **code coverage isn't everything**. You can have 100% line coverage but still miss bugs if your assertions are weak. Mutation testing forces you to write tests that actually check things properly.

Also, the RIPR model from the slides helped me think about why some mutants survive:
- **R**eachability - Does my test even run that line?
- **I**nfection - Does my input make the mutant behave differently?
- **P**ropagation - Does the wrong value actually affect the output?
- **R**evealability - Does my assertion catch the wrong output?

Pretty cool stuff!

---

## Appendix: AI Interaction Records

**Tool used:** Claude (via Windsurf/Cascade)  
**Date:** 2024/12/13  
**Purpose:** Help with test generation and mutation killing strategy

### Summary of AI interaction:
- Asked AI to help set up StrykerJS and run baseline mutation test
- AI helped identify that there were 106 mutants total
- Discussed strategy for killing mutants (boundary testing, leap year cases, etc.)
- AI generated initial test cases, which I reviewed and understood
- Ran mutation tests iteratively until reaching 100% score

The AI was helpful for understanding the mutation testing workflow and generating comprehensive test cases. I made sure to understand *why* each test was needed rather than just copying blindly.

---

*End of report*
