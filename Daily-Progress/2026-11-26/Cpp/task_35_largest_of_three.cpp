// Daily Practice Task 35
// Date: 2026-11-26
// Category: C++
//
// Task: Write a program to find the largest of three numbers.
// Approach: Assume the first is largest, then compare with the other two.

#include <iostream>
using namespace std;

int main() {
    int a = 12, b = 45, c = 30;
    int largest = a;
    if (b > largest) largest = b;
    if (c > largest) largest = c;
    cout << "Largest of " << a << ", " << b << ", " << c << " is " << largest << endl;
    return 0;
}
