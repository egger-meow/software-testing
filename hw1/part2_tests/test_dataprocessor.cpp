#include <iostream>
#include <vector>
#include <string>
#include <fstream>

struct DataRecord {
    int id;
    char* data_buffer;
};

void processLargeFile(const std::string& filename) {
    std::cout << "Starting file processing for: " << filename << std::endl;
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filename << std::endl;
        return;
    }

    std::string line;
    int recordCount = 0;
    
    while (std::getline(file, line)) {
        // FAULT: Memory leak - allocated memory never freed
        DataRecord* newRecord = new DataRecord();
        newRecord->id = recordCount;
        newRecord->data_buffer = new char;
        recordCount++;
    }
    
    file.close();
    std::cout << "Finished processing " << recordCount << " records." << std::endl;
    std::cout << "\n*** MEMORY LEAK: " << recordCount << " DataRecord objects leaked ***" << std::endl;
    std::cout << "*** MEMORY LEAK: " << recordCount << " char allocations leaked ***" << std::endl;
}

int main() {
    std::cout << "=== DataProcessor Memory Leak Test ===\n" << std::endl;
    
    // Create test file
    std::ofstream dummyFile("test_data.txt");
    for (int i = 0; i < 10000; ++i) {
        dummyFile << "Record " << i << std::endl;
    }
    dummyFile.close();
    std::cout << "Created test file with 10,000 records\n" << std::endl;
    
    // Process file - this leaks memory
    processLargeFile("test_data.txt");
    
    std::cout << "\nTo verify memory leak, run:" << std::endl;
    std::cout << "  valgrind --leak-check=full ./test_dataprocessor" << std::endl;
    std::cout << "  or" << std::endl;
    std::cout << "  drmemory -- test_dataprocessor.exe" << std::endl;
    
    return 0;
}
