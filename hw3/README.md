# HW3: Input Space Partitioning for BoundedQueue

## Quick Start

```bash
# Run BCC test suite
npm test

# Run demo
npm run demo
```

## Deliverables

### Core Files
- **`ISP_Analysis.md`** - Complete ISP breakdown (steps a-e) for constructor, enqueue, dequeue
- **`BoundedQueue.test.js`** - 11 BCC test cases (all passing ✓)
- **`HW3_Report.md`** - Condensed analysis report

### Source Files
- **`BoundedQueue.js`** - Implementation with demo code
- **`package.json`** - Project configuration

## Test Coverage

| Method | Tests | Coverage |
|--------|-------|----------|
| constructor | 3 | All blocks (negative, zero, positive capacity) |
| enqueue | 5 | Element validity × Queue state combinations |
| dequeue | 3 | All queue states (empty, partial, full) |
| **Total** | **11** | **Base Choice Coverage achieved** |

## Structure

```
hw3/
├── ISP_Analysis.md          # Detailed ISP process
├── HW3_Report.md            # Condensed submission report
├── BoundedQueue.test.js     # Test suite (executable)
├── BoundedQueue.js          # Implementation
├── package.json             # Project config
├── README.md                # This file
└── docs/
    ├── Input Space Partitioning for BoundedQueue.md
    └── require.png
```

## Notes

- Test suite uses native Node.js assertions (no external dependencies)
- All 11 tests validate both success and failure paths
- BCC methodology ensures minimal yet complete coverage
- Report follows concise CS student style per requirements
