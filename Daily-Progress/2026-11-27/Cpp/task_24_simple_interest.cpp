// Daily Practice Task 24
// Date: 2026-11-27
// Category: C++
//
// Task: Write a program to calculate simple interest.
// Approach: Formula: SI = (P * R * T) / 100.

#include <iostream>
using namespace std;

int main() {
    double principal = 10000, rate = 5, time = 3;
    double interest = (principal * rate * time) / 100;
    cout << "Simple Interest = " << interest << endl;
    return 0;
}
