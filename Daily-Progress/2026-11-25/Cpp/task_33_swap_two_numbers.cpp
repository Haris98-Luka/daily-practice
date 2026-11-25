// Daily Practice Task 33
// Date: 2026-11-25
// Category: C++
//
// Task: Write a program to swap two numbers.
// Approach: Use a temporary variable to hold one value.

#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20;
    cout << "Before: a = " << a << ", b = " << b << endl;
    int temp = a;
    a = b;
    b = temp;
    cout << "After:  a = " << a << ", b = " << b << endl;
    return 0;
}
