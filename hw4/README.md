# HW4 - Mutation Testing with StrykerJS

This homework explores **mutation testing** using StrykerJS to test the quality of our test suites.

## Structure

```
hw4/
├── hw4/          # Main calculator.js mutation testing
│   ├── src/calculator.js
│   ├── test/calculator_test.js
│   └── stryker.config.json
├── Lab1/         # Lab1 code with mutation testing setup
│   ├── main.js
│   ├── main_test.js
│   └── stryker.config.json
└── report.md     # Final report
```

## Quick Start

### For calculator.js (hw4/hw4)
```bash
cd hw4
npm install
npm run test      # Run tests
npm run mutate    # Run mutation testing
```

### For Lab1
```bash
cd Lab1
npm install
npm run test
npm run mutate
```

## Results

| Target | Mutants | Killed | Score |
|--------|---------|--------|-------|
| calculator.js | 106 | 106 | 100% |
| Lab1 main.js | 34 | 32 | 94.12% |

## What is Mutation Testing?

Mutation testing injects small bugs (mutants) into your code and checks if your tests catch them. If tests fail → mutant killed (good). If tests pass → mutant survived (your tests missed something).

It's basically **testing your tests**!
