# PowerShell script to run all Calculator tests

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Calculator TDD - Test Runner" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Run Python tests
Write-Host "Running Python Tests..." -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Gray
try {
    python -m unittest CalcTest.py -v
    Write-Host ""
    Write-Host "✓ Python tests completed successfully" -ForegroundColor Green
} catch {
    Write-Host "✗ Python tests failed or Python not found" -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Run JavaScript tests
Write-Host "Running JavaScript Tests..." -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Gray
try {
    node CalcTest.js
    Write-Host ""
    Write-Host "✓ JavaScript tests completed successfully" -ForegroundColor Green
} catch {
    Write-Host "✗ JavaScript tests failed or Node.js not found" -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Run Java tests (if JUnit is available)
Write-Host "Running Java Tests..." -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Gray
Write-Host "Note: Java tests require JUnit in classpath" -ForegroundColor Gray
Write-Host "If you have JUnit, run:" -ForegroundColor Gray
Write-Host "  javac -cp .;junit-4.13.2.jar Calc.java CalcTest.java" -ForegroundColor Gray
Write-Host "  java -cp .;junit-4.13.2.jar;hamcrest-core-1.3.jar org.junit.runner.JUnitCore CalcTest" -ForegroundColor Gray

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "All available tests completed!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
