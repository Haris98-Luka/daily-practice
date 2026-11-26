// Daily Practice Task 24
// Date: 2026-11-26
// Category: C++
//
// Task: Write a program to reverse a number.
// Approach: Take the last digit with % 10 and build the reversed number.

#include <iostream>
using namespace std;

int main() {
    int n = 12345, reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    cout << "Reversed: " << reversed << endl;
    return 0;
}
