# Input Space Partitioning Analysis for BoundedQueue

## 1. Constructor: `constructor(capacity)`

### (a) Input Variables
- `capacity` (parameter): Queue's maximum capacity

### (b) Characteristics
- **C1: Capacity Value Range**
  - Valid capacity values for queue initialization

### (c) Partition into Blocks
| Characteristic | Block ID | Description | Base? |
|---------------|----------|-------------|-------|
| C1: Capacity Value Range | B1 | `capacity < 0` (invalid) | |
| | B2 | `capacity = 0` (edge case) | |
| | B3 | `capacity > 0` (typical) | ✓ |

### (d) Test Values
| Block | Test Value |
|-------|------------|
| B1 | `-1` |
| B2 | `0` |
| B3 | `5` |

### (e) BCC Test Set
| Test ID | Operations | Expected Result | BCC Coverage |
|---------|-----------|-----------------|--------------|
| **C-T1** | `new BoundedQueue(5)` | Queue created with capacity=5, size=0 | B3 (Base) |
| **C-T2** | `new BoundedQueue(-1)` | Throws `RangeError: capacity is less than 0` | B1 |
| **C-T3** | `new BoundedQueue(0)` | Queue created with capacity=0, size=0 | B2 |

---

## 2. Method: `enqueue(element)`

### (a) Input Variables
- `element` (parameter): Value to add to queue
- `queue_size` (state): Current number of elements
- `capacity` (state): Maximum queue capacity

### (b) Characteristics
- **C1: Element Type/Validity**
  - Nature of the element being enqueued
- **C2: Queue Size Relative to Capacity**
  - Current fullness state of the queue

### (c) Partition into Blocks
| Characteristic | Block ID | Description | Base? |
|---------------|----------|-------------|-------|
| C1: Element Type | B1 | Valid number (not NaN) | ✓ |
| | B2 | NaN | |
| | B3 | Non-number (e.g., string) | |
| C2: Queue Size | B1 | Empty (`size = 0`) | |
| | B2 | Partial (`0 < size < capacity`) | ✓ |
| | B3 | Full (`size = capacity`) | |

### (d) Test Values
| Block | Test Value |
|-------|------------|
| C1-B1 | `42` |
| C1-B2 | `NaN` |
| C1-B3 | `"invalid"` |
| C2-B1 | Queue with size=0, capacity=3 |
| C2-B2 | Queue with size=1, capacity=3 |
| C2-B3 | Queue with size=3, capacity=3 |

### (e) BCC Test Set
| Test ID | Setup | Operation | Expected Result | BCC Coverage |
|---------|-------|-----------|-----------------|--------------|
| **E-T1** | `capacity=3, size=1` | `enqueue(42)` | Success, size=2, element added | C1-B1, C2-B2 (Both Base) |
| **E-T2** | `capacity=3, size=1` | `enqueue(NaN)` | Throws `RangeError: element is invalid` | C1-B2 |
| **E-T3** | `capacity=3, size=1` | `enqueue("test")` | Throws `RangeError: element is invalid` | C1-B3 |
| **E-T4** | `capacity=3, size=0` | `enqueue(10)` | Success, size=1, element added | C2-B1 |
| **E-T5** | `capacity=3, size=3` | `enqueue(99)` | Throws `Error: queue is full` | C2-B3 |

---

## 3. Method: `dequeue()`

### (a) Input Variables
- `queue_size` (state): Current number of elements
- `capacity` (state): Maximum queue capacity

### (b) Characteristics
- **C1: Queue Size**
  - Current state of queue occupancy

### (c) Partition into Blocks
| Characteristic | Block ID | Description | Base? |
|---------------|----------|-------------|-------|
| C1: Queue Size | B1 | Empty (`size = 0`) | |
| | B2 | Partial (`0 < size < capacity`) | ✓ |
| | B3 | Full (`size = capacity`) | |

### (d) Test Values
| Block | Test Value |
|-------|------------|
| B1 | Queue with size=0, capacity=3 |
| B2 | Queue with size=2, capacity=3 |
| B3 | Queue with size=3, capacity=3 |

### (e) BCC Test Set
| Test ID | Setup | Operation | Expected Result | BCC Coverage |
|---------|-------|-----------|-----------------|--------------|
| **D-T1** | `capacity=3, size=2` (has [10, 20]) | `dequeue()` | Returns `10`, size=1, queue=[20] | B2 (Base) |
| **D-T2** | `capacity=3, size=0` | `dequeue()` | Throws `Error: queue is empty` | B1 |
| **D-T3** | `capacity=3, size=3` (has [1, 2, 3]) | `dequeue()` | Returns `1`, size=2, queue=[2, 3] | B3 |

---

## Summary

**Total BCC Test Cases: 11**
- Constructor: 3 tests
- Enqueue: 5 tests  
- Dequeue: 3 tests

All non-base blocks are covered with exactly one test case that varies only that specific partition while keeping others at base values, satisfying Base Choice Coverage criteria.
