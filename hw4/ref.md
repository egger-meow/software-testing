## 1) The one idea you must internalize

**Coverage tells you code ran. Mutation tells you tests can *detect wrong behavior*.** A suite can hit 100% lines/branches but still verify nothing if assertions are weak or missing (the “assertion-free paradox”). 

**Mutation testing = “test your tests.”** It injects small changes (*mutants*) into code and checks whether your tests fail. If tests fail → **killed**; if tests still pass → **survived** (your tests missed something). 

---

## 2) Core terms (what your report/output is really saying)

### Mutants and outcomes

Stryker will classify each mutant roughly like this (HTML is the best place to read it):

* **Killed (green):** tests caught the bug (good)
* **Survived (red):** tests didn’t catch the bug (gap)
* **No Coverage (grey):** your tests never executed the mutated line
* **Timeout (yellow):** mutation caused hang/perf blowup; still counted as “detected” in many scoring formulas 

### Mutation score (be careful: different formulas exist)

Your HW slides present a simple version: killed / total. 
A more “Stryker-style” practical metric often used is:

[
\text{Mutation Score} = \frac{\text{Killed}+\text{Timeout}}{\text{Total}-\text{CompileErrors}} \times 100%
]



Takeaway: **the goal isn’t “100% at all costs”** because equivalent mutants exist (next section). 

---

## 3) Why small mutants matter (the theory your TA expects you to “get”)

Mutation testing is justified by two big ideas:

### Competent Programmer Hypothesis (CPH)

Real bugs are often “small deviations” (wrong operator, boundary check, boolean flip), not totally random code. Mutation operators simulate exactly these likely mistakes. 

### Coupling Effect

If your tests can detect simple faults, they’re **likely** able to detect more complex real faults too. 

---

## 4) The RIPR model = your universal “why did this mutant survive?” debugger

For a mutant to be killed, tests must satisfy **all four**:

1. **Reachability**: test executes the mutated line (otherwise it’s “No Coverage”) 
2. **Infection**: the mutation must actually create a wrong internal state for your chosen input 
3. **Propagation**: the wrong state must flow to some observable output (not masked) 
4. **Revealability**: your assertions must check the *specific* wrong output strongly enough (not just “is defined”) 

**Use RIPR as your step-by-step playbook for every survived mutant.** It turns “random red dots” into a deterministic fix plan.

---

## 5) HW4 practical workflow (exactly what to do)

Your homework slides basically want this loop:

### Step A — Setup & baseline

* Go to your fork → directory `hw4` 
* Install deps: `npm i` 
* Run baseline tests: `npm run test` (uses Node’s built-in test runner: `node --test`) 

### Step B — Run mutation

* `npm run mutate` (runs `npx stryker run`) 

### Step C — Read results properly

* Terminal output + HTML report are generated 
* HW slide explicitly points you to HTML: `reports/mutation/mutation.html` 
* Find “survived list” and use the mutation diff to adjust tests 

That last line is basically the assignment’s real requirement: **observe survived mutants → strengthen tests accordingly.** 

---

## 6) How to kill survived mutants (a systematic recipe)

When you see a **Survived** mutant in the HTML diff (red dot), do this:

### 6.1 Decide which RIPR link failed

**(1) Reachability failed**

* Symptom: mutant is **No Coverage** (grey) in HTML. 
* Fix: add a test that *actually hits that line/branch*.

  * Typical missing areas: `else` branches, early returns, error handling, edge-case guards.

**(2) Infection failed**

* Symptom: your test hits the line but chosen inputs don’t make mutant behave differently.
* Fix: choose inputs that force divergence.

  * Example from RIPR text: `a=b+1` vs `a=b-1` won’t diverge if your chosen `b` accidentally makes results equal in some edge scenario. 
  * Practical tactic: try **0, 1, -1, boundary values**, and values just above/below thresholds.

**(3) Propagation failed**

* Symptom: state is wrong but later logic “masks” it (e.g., multiplied by zero, overwritten, unused). 
* Fix options:

  * Assert on a value *before* it gets masked (if API allows).
  * Drive execution so the infected value is used (choose different path/input).
  * If design truly hides it and it’s not observable, it may be a sign of **testability/design issue** (or sometimes an equivalent-ish scenario).

**(4) Revealability failed (most common)**

* Symptom: test runs and checks something, but assertion is too weak (e.g., “defined”, “truthy”, “no crash”). 
* Fix: replace vague checks with **specific assertions**:

  * exact values
  * exact thrown error type/message (if spec’d)
  * deep equality of objects/arrays
  * explicit side-effect verification (file write, DB call mocked count, etc.)

---

## 7) Common mutation operator patterns → what tests you should add

Your HW slides list common operators like:

* arithmetic operator swap `+`→`-`
* condition swap `>`→`<`
* boolean flip
* remove method calls 

Here’s how to reliably kill these:

### Arithmetic operator mutants

Add tests that:

* include **negative numbers**
* include **zero and one** (identity elements reveal masking)
* include **non-commutative checks** if applicable (subtraction/division)
* verify exact outputs, not just “returns number”

### Relational / boundary mutants (`>=`→`>`, `==`→`!=`, etc.)

Add **boundary tests**:

* exactly equal to threshold
* just below
* just above

This is the #1 reason mutants survive: people only test “typical” values, not edges.

### Boolean flip / logical operator mutants (`&&`↔`||`, `true`↔`false`)

Add tests that:

* independently toggle each condition
* cover cases where only one side is true
* ensure short-circuit behavior doesn’t hide bugs (especially if side effects exist)

### “Remove method call” / “remove block” style mutants

Add tests that assert the **effect** of the call:

* state change
* return value changes
* side effects happen (or must not happen)

---

## 8) Equivalent mutants (the “red dot but nothing is actually wrong” case)

**Equivalent mutant = syntactically different but semantically identical** → impossible for any test to kill. 
Detecting equivalence automatically is undecidable in general, so tools just report them as “Survived” and humans must decide. 

Examples you should recognize:

* Loop boundary `i < 10` vs `i != 10` (with i++), same behavior 
* `i++` vs `++i` as standalone statement (same side effect) 
* Redundant logic where equality case is impossible by constraints (`>=` vs `>`) 

### How to handle equivalents (best practice)

Use **inline Stryker disable comments** so the report documents *why* you ignored it: 

* `// Stryker disable next-line <MutatorName>: reason`
* `// Stryker disable all: reason`
* `// Stryker restore all`

This keeps your mutation score meaningful by removing invalid targets from the denominator. 

---

## 9) How Stryker stays fast (so you don’t panic when you see many mutants)

Stryker avoids “compile-per-mutant” using **mutation switching (Mutant Schemata)**: it instruments code once and toggles which mutant is active at runtime. 
It also uses **sandboxed parallel workers** to isolate state and speed up. 
And it can run only relevant tests via coverage analysis (`perTest` is most optimized). 

---

## 10) Speed/quality knobs you might mention in your HW writeup (optional but impressive)

* **Incremental mode:** `npx stryker run --incremental` reuses prior results when files/tests unchanged. 
* **ignoreStatic:** can speed up projects by skipping static mutants, with tradeoffs. 
* **concurrency tuning:** too much parallelism can cause false timeouts; set concurrency to 2–4 in weak CI machines. 

---

## 11) About your 3rd PDF (StrykerJS “deep dive” visuals)

That file is image-based (no extractable text), but it’s essentially a visual summary of the same ideas: killed vs survived, “coverage ≠ verification”, RIPR chain, and Stryker workflow. 

