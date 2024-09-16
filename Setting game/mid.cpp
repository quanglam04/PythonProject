#include <windows.h>
#include <tlhelp32.h>
#include <iostream>
#include <thread>
#include <chrono>

DWORD GetProcessIDByName(const char* processName) {
    PROCESSENTRY32 entry;
    entry.dwSize = sizeof(PROCESSENTRY32);

    HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL);

    if (Process32First(snapshot, &entry) == TRUE) {
        while (Process32Next(snapshot, &entry) == TRUE) {
            if (strcmp(entry.szExeFile, processName) == 0) {
                CloseHandle(snapshot);
                return entry.th32ProcessID;
            }
        }
    }

    CloseHandle(snapshot);
    return 0; // If process not found
}

bool IsProcessRunning(const char* processName) {
    return GetProcessIDByName(processName) != 0;
}

void TerminateProcessByName(const char* processName) {
    DWORD processID = GetProcessIDByName(processName);

    if (processID == 0) {
        std::cerr << "Process not found\n";
        return;
    }

    HANDLE hProcess = OpenProcess(PROCESS_TERMINATE, FALSE, processID);

    if (hProcess == NULL) {
        std::cerr << "Failed to open process. Error: " << GetLastError() << "\n";
        return;
    }

    if (TerminateProcess(hProcess, 0)) {
        std::cout << "Process terminated successfully.\n";
    } else {
        std::cerr << "Failed to terminate process. Error: " << GetLastError() << "\n";
    }
	std::cout << "Terminated process ID: " << processID << std::endl;
    CloseHandle(hProcess);
}
//void RunProcess(const char* processPath) {
//    STARTUPINFO si;
//    PROCESS_INFORMATION pi;
//
//    // Initialize memory for startup info and process info structures
//    ZeroMemory(&si, sizeof(si));
//    si.cb = sizeof(si); // Required for STARTUPINFO structure
//    ZeroMemory(&pi, sizeof(pi));
//
//    // Start the process
//    if (!CreateProcess(
//            processPath,   // Path to the executable file
//            NULL,          // Command line arguments (NULL if none)
//            NULL,          // Process handle not inheritable
//            NULL,          // Thread handle not inheritable
//            FALSE,         // Handle inheritance option
//            0,             // No creation flags
//            NULL,          // Use parent's environment block
//            NULL,          // Use parent's starting directory
//            &si,           // Pointer to STARTUPINFO structure
//            &pi))          // Pointer to PROCESS_INFORMATION structure
//    {
//        std::cerr << "CreateProcess failed. Error: " << GetLastError() << "\n";
//        return;
//    }
//
//    std::cout << "Process started successfully!\n";
//
//    // Wait until child process exits (optional)
//    WaitForSingleObject(pi.hProcess, INFINITE);
//
//    // Close process and thread handles
//    CloseHandle(pi.hProcess);
//    CloseHandle(pi.hThread);
//}
int main() {
	
    const char* processName = "settinggame.exe";

    while (IsProcessRunning(processName)) {
        std::cout << "Process is still running... attempting to terminate\n";
        TerminateProcessByName(processName);
    }
	
    
    return 0;
}
