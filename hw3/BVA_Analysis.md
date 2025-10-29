# Boundary Value Analysis for BoundedQueue

## Overview

Boundary Value Analysis (BVA) complements Input Space Partitioning by focusing on edge cases at partition boundaries. While ISP with BCC covers representative values from each block, BVA systematically tests the boundaries where defects are most likely to occur.

## Motivation

Research shows that a significant percentage of software defects occur at boundary conditions:
- Off-by-one errors in loop conditions
- Edge cases in conditional statements
- Overflow/underflow in capacity limits
- State transitions at min/max values

For BoundedQueue, critical boundaries include:
- **Capacity boundaries**: -1 (invalid), 0 (minimal valid), 1 (minimal non-trivial)
- **Size boundaries**: empty (0), one-from-empty (1), one-from-full (capacity-1), full (capacity)

---

## 1. Constructor Boundary Analysis

### Boundary Points Identified

| Boundary | Test Value | Rationale |
|----------|-----------|-----------|
| Below minimum | `-1` | Invalid negative capacity (already in BCC) |
| At minimum | `0` | Edge case: immediately full queue |
| Just above minimum | `1` | Minimal non-trivial queue |
| Typical value | `5` | Normal case (BCC base) |
| Large value | `1000` | Stress test (optional) |

### BVA Test Cases

| Test ID | Input | Expected Behavior | Boundary Tested |
|---------|-------|-------------------|-----------------|
| **BVA-C1** | `new BoundedQueue(-1)` | Throws RangeError | Below minimum (BCC covered) |
| **BVA-C2** | `new BoundedQueue(0)` | Success, is_full()=true immediately | At minimum (BCC covered) |
| **BVA-C3** | `new BoundedQueue(1)` | Success, can hold exactly 1 element | Just above minimum |

### Additional Observation: capacity=0 Bug

**Critical Finding**: When `capacity=0`, the modulo operation in `enqueue()` and `dequeue()` causes undefined behavior:
```javascript
this.back = (this.back + 1) % this.capacity;  // Division by zero! → NaN
```

While the queue correctly throws "queue is full" before reaching this line, the implementation is fragile. Attempting to bypass the check would corrupt the queue state.

---

## 2. Enqueue Boundary Analysis

### State Boundary Points

| Queue State | Size Value | Boundary |
|-------------|-----------|----------|
| Empty | `size = 0` | Minimum occupancy |
| One element | `size = 1` | Just above empty |
| One from full | `size = capacity - 1` | Just before full |
| Full | `size = capacity` | Maximum occupancy |

### Element Boundary Points

For numeric elements, boundaries depend on JavaScript number representation:
- **Valid**: Regular numbers (e.g., `42`, `-10`, `0`, `3.14`)
- **Edge**: `NaN` (invalid), `Infinity` (valid number but unusual)
- **Invalid**: Non-numbers (strings, objects, null, undefined)

### BVA Test Cases

| Test ID | Queue State | Element | Expected Result | Boundary |
|---------|------------|---------|-----------------|----------|
| **BVA-E1** | Empty (size=0) | Valid number | Success | Empty → One element |
| **BVA-E2** | One element (size=1) | Valid number | Success | Partial state |
| **BVA-E3** | One from full (size=capacity-1) | Valid number | Success, becomes full | Near-full → Full |
| **BVA-E4** | Full (size=capacity) | Valid number | Throws Error | At maximum |
| **BVA-E5** | Partial | `Infinity` | Success (valid JS number) | Numeric boundary |
| **BVA-E6** | Partial | `0` | Success | Zero value |
| **BVA-E7** | Partial | Negative number | Success | Negative valid value |

---

## 3. Dequeue Boundary Analysis

### State Boundary Points

| Queue State | Size Value | Boundary |
|-------------|-----------|----------|
| Empty | `size = 0` | Minimum occupancy |
| One element | `size = 1` | One element → Empty |
| One from full | `size = capacity - 1` | Near full state |
| Full | `size = capacity` | Maximum occupancy |

### BVA Test Cases

| Test ID | Queue State | Expected Result | Boundary |
|---------|------------|-----------------|----------|
| **BVA-D1** | Empty (size=0) | Throws Error | At minimum (BCC covered) |
| **BVA-D2** | One element (size=1) | Success, becomes empty | One → Empty transition |
| **BVA-D3** | One from full (size=capacity-1) | Success, returns first | Near-full state |
| **BVA-D4** | Full (size=capacity) | Success, no longer full | Full → Partial (BCC covered) |

---

## 4. Wrap-Around Boundary Testing

### Critical Circular Array Boundary

The circular buffer implementation uses modulo arithmetic to wrap indices:
```javascript
this.back = (this.back + 1) % this.capacity;
this.front = (this.front + 1) % this.capacity;
```

**Key Boundary**: When `back` or `front` reaches `capacity - 1`, next increment wraps to `0`.

### Wrap-Around Scenario

| Test ID | Operations | State Transitions | Boundary |
|---------|-----------|-------------------|----------|
| **BVA-W1** | 1. Fill queue (capacity=3)<br>2. Dequeue 2 elements<br>3. Enqueue 2 elements | front: 0→2 (wrapped)<br>back: 0→3→0→2 (wrapped twice) | Index wrap-around |

**Test Sequence**:
```javascript
const bq = new BoundedQueue(3);
// Fill: [1, 2, 3], front=0, back=0 (wrapped to 0 after 3rd enqueue)
bq.enqueue(1); bq.enqueue(2); bq.enqueue(3);

// Dequeue 2: [3], front=2, back=0
bq.dequeue(); // removes 1
bq.dequeue(); // removes 2

// Enqueue 2: [3, 4, 5], front=2, back=2
bq.enqueue(4); // back=1
bq.enqueue(5); // back=2

// Verify: front pointer at index 2, elements wrap around [4, 5, 3]
// Logical order: [3, 4, 5]
```

---

## 5. Observer Method Boundaries

### is_empty() Boundary

| Test | Size | Expected |
|------|------|----------|
| Just created | 0 | true |
| After 1 enqueue | 1 | false |
| After all dequeued | 0 | true |

### is_full() Boundary

| Test | Size vs Capacity | Expected |
|------|-----------------|----------|
| Just created | 0 < capacity | false |
| One from full | capacity-1 | false |
| At capacity | capacity | true |
| After one dequeue | capacity-1 | false |

---

## Summary: BVA Test Coverage

| Category | BCC Tests | BVA Additional Tests | Total |
|----------|-----------|---------------------|-------|
| Constructor | 3 | 1 (capacity=1) | 4 |
| Enqueue | 5 | 5 (boundaries + edge values) | 10 |
| Dequeue | 3 | 2 (one-element, near-full) | 5 |
| Wrap-around | 0 | 1 (circular buffer) | 1 |
| Observers | 0 (implicit) | 6 (explicit tests) | 6 |
| **Total** | **11** | **15** | **26** |

---

## Key Insights

1. **capacity=0 is a valid edge case** but creates an immediately-full queue
2. **capacity=1 testing** reveals minimal-functionality boundaries
3. **One-from-full transitions** are critical for capacity management
4. **Wrap-around logic** requires multi-step sequences to test properly
5. **Infinity is technically valid** as a JavaScript number (typeof === "number")

---

## Implementation Notes

BVA tests are implemented in `Bonus_Tests.js` as supplement to the core BCC suite in `BoundedQueue.test.js`. All boundary conditions identified above are tested systematically.

**Run BVA Tests**:
```bash
npm run test:bonus
```
