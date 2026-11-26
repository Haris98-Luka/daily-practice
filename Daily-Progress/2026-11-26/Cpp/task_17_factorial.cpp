// Daily Practice Task 17
// Date: 2026-11-26
// Category: C++
//
// Task: Write a program to calculate factorial of a number.
// Approach: Multiply 1 * 2 * ... * n in a loop.

#include <iostream>
using namespace std;

int main() {
    int n = 10;
    long long fact = 1;
    for (int i = 2; i <= n; i++) fact *= i;
    cout << n << "! = " << fact << endl;
    return 0;
}
