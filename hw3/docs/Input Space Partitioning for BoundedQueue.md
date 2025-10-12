# **Software Testing Homework: Input Space Partitioning for BoundedQueue**

## **Task Overview: Input Space Partitioning (ISP)**

This assignment requires you to apply the Input Space Partitioning (ISP) technique to derive a thorough set of test inputs for the BoundedQueue class provided in the BoundedQueue.js file. Your goal is to systematically partition the input domain, including state variables, and create a test suite that satisfies Base Choice Coverage (BCC).

The class methods to be tested are:

* constructor(capacity)  
* enqueue(element)  
* dequeue()  
* is\_empty()  
* is\_full()

Assume the usual **FIFO (First-In, First-Out)** semantics for a queue with a fixed, maximal capacity. Try to keep your partitioning simple—choose a small, manageable number of partitions and blocks.

### **Deliverables (The ISP Process)**

For the constructor, enqueue, and dequeue methods, complete the following steps:

(a) List all of the Input Variables  
Identify all variables that affect the behavior of the method. This includes formal parameters (e.g., capacity, element) and abstract state variables (e.g., the current size of the queue, or the queue's capacity).  
(b) Define the Characteristics  
For each input variable listed in (a), define the characteristic(s) that describe its possible values or conditions. Ensure you cover all relevant aspects, especially those that trigger different execution paths (including successful execution and exceptions).  
(c) Partition the Characteristics into Blocks  
Divide the values of each characteristic into non-overlapping blocks (partitions). Designate one block in each partition as the "Base" block, which represents the most typical or common usage case. Ensure partitions cover both valid and invalid/exception-causing inputs.  
(d) Define Values for Each Block  
Select a specific, representative test value for every block you defined in (c). This value will be used in your final test set.  
(e) Define a Test Set (Base Choice Coverage \- BCC)  
Define a minimal set of test cases that satisfies Base Choice Coverage (BCC). This means every non-Base block must be covered by at least one test case, and every test case must use the Base block for all other partitions.

| Test ID | Sequence of Operations | Expected Result (Oracle) | BCC Choice(s) Covered |
| :---- | :---- | :---- | :---- |
| **C-B2** | new BoundedQueue(0) | Capacity is 0; no exception thrown. | capacity:  |
| **E-B3** |   bq.enqueue(10) | Throws Error: queue is full. | Queue\_Size:  |

Be sure to include the **test oracles**—the expected outcomes, return values, new state of the queue, or expected exceptions—for every test.

---

## **Suggestions for Further Exploration (Bonus/Advanced)**

To deepen your understanding of software testing, consider the following tasks after completing the core BCC assignment.

### **1\. Boundary Value Analysis (BVA) 📏**

ISP often misses critical boundary conditions. **Boundary Value Analysis (BVA)** focuses on the edges of the input domain. Augment your test plan by explicitly listing and testing the following boundary conditions:

* **Capacity:** Test capacity \= \-1 (invalid), capacity \= 0 (minimum valid), and capacity \= 1 (minimal non-trivial).  
* **Queue Size:** Test when the queue is exactly **empty** (), exactly **full** (), and one element away from these boundaries ( and ).

### **2\. Sequence/State-Based Testing 🔄**

The BoundedQueue is a **state-dependent** data structure. Design tests that focus on the circular array implementation and transitions between states.

* **Wrap-Around Logic:** Create a sequence of operations that forces the queue to fill, then empty, and then refill elements that wrap around the array indices (i.e., the front and back pointers reset to 0). For example:  
  1. Fill the queue (enqueue ).  
  2. Remove a few elements (dequeue ).  
  3. Add new elements (enqueue ) to test if the back pointer correctly wraps around.  
* **Mutator/Observer Pairs:** Design tests where the result of a **mutator** (enqueue, dequeue) is immediately checked by an **observer** (is\_empty, is\_full, toString).

### **3\. Multiple Choice Coverage (MCC) 🧩**

The BCC test set is minimal but weak. Derive a test set that achieves **Multiple Choice Coverage (MCC)** for the enqueue(element) method. MCC requires testing **every combination** of blocks from all partitions.

* *Example:* If enqueue has partitions for  (3 blocks: empty, partial, full) and  (3 blocks: valid, NaN, string), an MCC test set requires  test cases.