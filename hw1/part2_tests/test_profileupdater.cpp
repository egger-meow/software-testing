#include <iostream>
#include <string>
#include <cstring>

struct UserProfile {
    char username[1];     // FAULT: Buffer too small - only 1 byte!
    int user_id;
    char profile_status;
    bool is_active;
    int last_login_year;
    
    UserProfile() : user_id(12345), profile_status('A'), is_active(true), last_login_year(2025) {
        memset(username, 0, sizeof(username));
    }
};

void printProfile(const UserProfile& profile) {
    std::cout << "--- User Profile ---" << std::endl;
    std::cout << "Username: " << profile.username << std::endl;
    std::cout << "User ID: " << profile.user_id << std::endl;
    std::cout << "Status: " << profile.profile_status << std::endl;
    std::cout << "Active: " << (profile.is_active ? "Yes" : "No") << std::endl;
    std::cout << "Last Login: " << profile.last_login_year << std::endl;
    std::cout << "--------------------" << std::endl;
}

void updateUserProfile(UserProfile& profile, const std::string& newUsername) {
    std::cout << "\nAttempting to update username..." << std::endl;
    std::cout << "New username: \"" << newUsername << "\"" << std::endl;
    std::cout << "Username length: " << newUsername.length() << " chars" << std::endl;
    std::cout << "Buffer capacity: " << sizeof(profile.username) << " bytes" << std::endl;
    std::cout << "Overflow: " << (newUsername.length() + 1 - sizeof(profile.username)) << " bytes" << std::endl;
    
    // BUFFER OVERFLOW: strcpy has no bounds checking
    strcpy(profile.username, newUsername.c_str());
    
    std::cout << "*** BUFFER OVERFLOW OCCURRED ***" << std::endl;
}

int main() {
    std::cout << "=== ProfileUpdater Buffer Overflow Test ===\n" << std::endl;
    
    UserProfile profile;
    
    std::cout << "1. Initial profile state:" << std::endl;
    printProfile(profile);
    
    std::cout << "\n2. Memory layout:" << std::endl;
    std::cout << "username at:         " << (void*)&profile.username << std::endl;
    std::cout << "user_id at:          " << (void*)&profile.user_id << std::endl;
    std::cout << "profile_status at:   " << (void*)&profile.profile_status << std::endl;
    std::cout << "is_active at:        " << (void*)&profile.is_active << std::endl;
    std::cout << "last_login_year at:  " << (void*)&profile.last_login_year << std::endl;
    
    std::cout << "\n3. Triggering buffer overflow..." << std::endl;
    std::string longUsername = "JohnDoe123";
    updateUserProfile(profile, longUsername);
    
    std::cout << "\n4. Profile state after overflow:" << std::endl;
    printProfile(profile);
    
    std::cout << "\n=== ANALYSIS ===" << std::endl;
    std::cout << "Buffer size: 1 byte (can only hold null terminator)" << std::endl;
    std::cout << "Data written: " << (longUsername.length() + 1) << " bytes" << std::endl;
    std::cout << "Adjacent memory CORRUPTED:" << std::endl;
    std::cout << "  - user_id changed from 12345 to " << profile.user_id << std::endl;
    std::cout << "  - Other fields also corrupted" << std::endl;
    
    std::cout << "\nTo detect with address sanitizer:" << std::endl;
    std::cout << "  g++ -fsanitize=address -g test_profileupdater.cpp" << std::endl;
    
    return 0;
}
