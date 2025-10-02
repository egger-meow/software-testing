#include <iostream>
#include <thread>
#include <vector>
#include <chrono>

// FAULT: Unprotected shared variable
int total_logs_processed = 0;

void processLogs(int thread_id, int num_logs_to_process) {
    std::cout << "Thread " << thread_id << " starting..." << std::endl;
    
    for (int i = 0; i < num_logs_to_process; ++i) {
        // RACE CONDITION: Multiple threads increment without synchronization
        total_logs_processed++;
        std::this_thread::sleep_for(std::chrono::nanoseconds(1));
    }
    
    std::cout << "Thread " << thread_id << " finished." << std::endl;
}

void startProcessing(int num_threads, int logs_per_thread) {
    int expected = num_threads * logs_per_thread;
    std::cout << "Expected total logs: " << expected << std::endl;
    std::cout << "Starting " << num_threads << " threads...\n" << std::endl;
    
    std::vector<std::thread> threads;
    for (int i = 0; i < num_threads; ++i) {
        threads.push_back(std::thread(processLogs, i, logs_per_thread));
    }
    
    for (auto& t : threads) {
        t.join();
    }
    
    std::cout << "\n=== RESULTS ===" << std::endl;
    std::cout << "Expected: " << expected << std::endl;
    std::cout << "Actual:   " << total_logs_processed << std::endl;
    
    if (total_logs_processed != expected) {
        std::cout << "*** RACE CONDITION DETECTED ***" << std::endl;
        std::cout << "Lost updates: " << (expected - total_logs_processed) << std::endl;
    } else {
        std::cout << "No race detected this run (but fault still exists)" << std::endl;
    }
}

int main() {
    std::cout << "=== LoggingSystem Race Condition Test ===\n" << std::endl;
    std::cout << "Running multiple trials to demonstrate race condition:\n" << std::endl;
    
    for (int trial = 1; trial <= 5; ++trial) {
        total_logs_processed = 0;
        std::cout << "--- Trial " << trial << " ---" << std::endl;
        startProcessing(10, 10000);
        std::cout << std::endl;
    }
    
    std::cout << "\nTo detect with thread sanitizer, compile with:" << std::endl;
    std::cout << "  g++ -fsanitize=thread -g test_loggingsystem.cpp -pthread" << std::endl;
    
    return 0;
}
