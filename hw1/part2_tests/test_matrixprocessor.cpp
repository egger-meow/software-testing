#include <iostream>

void process_matrix(const int* const* matrix, int rows, int cols) {
    std::cout << "Processing matrix..." << std::endl;
    
    std::cout << "\nOriginal matrix values:" << std::endl;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            std::cout << "  [" << i << "][" << j << "] = " << matrix[i][j] << std::endl;
        }
    }
    
    // FAULT 1: Violate const correctness with const_cast
    std::cout << "\n*** FAULT 1: Using const_cast to remove const protection ***" << std::endl;
    int** non_const_matrix = const_cast<int**>(matrix);
    std::cout << "Original pointer: " << non_const_matrix << std::endl;
    
    // FAULT 2: Incorrect pointer assignment (should be non_const_matrix[0][0] = 999)
    std::cout << "\n*** FAULT 2: Incorrect assignment - assigns to pointer, not value ***" << std::endl;
    std::cout << "Code: non_const_matrix = 999" << std::endl;
    std::cout << "This changes the pointer itself, not the matrix values!" << std::endl;
    
    // Demonstrate the fault
    non_const_matrix = reinterpret_cast<int**>(999);
    std::cout << "New pointer value: " << non_const_matrix << " (invalid address!)" << std::endl;
    
    std::cout << "\nCorrect syntax would be: non_const_matrix[0][0] = 999" << std::endl;
}

int main() {
    std::cout << "=== MatrixProcessor Fault Test ===\n" << std::endl;
    
    const int ROWS = 2;
    const int COLS = 3;
    
    // Create matrix
    int** matrix = new int*[ROWS];
    for (int i = 0; i < ROWS; ++i) {
        matrix[i] = new int[COLS];
        for (int j = 0; j < COLS; ++j) {
            matrix[i][j] = 10 * i + j;
        }
    }
    
    // Call faulty function
    process_matrix(const_cast<const int* const*>(matrix), ROWS, COLS);
    
    // Matrix remains unchanged (pointer was changed, not values)
    std::cout << "\nMatrix values after faulty function (unchanged):" << std::endl;
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            std::cout << "  [" << i << "][" << j << "] = " << matrix[i][j] << std::endl;
        }
    }
    
    std::cout << "\n=== SUMMARY ===" << std::endl;
    std::cout << "1. const_cast violated function contract" << std::endl;
    std::cout << "2. Wrong syntax: pointer assignment instead of value modification" << std::endl;
    
    // Cleanup
    for (int i = 0; i < ROWS; ++i) {
        delete[] matrix[i];
    }
    delete[] matrix;
    
    return 0;
}
