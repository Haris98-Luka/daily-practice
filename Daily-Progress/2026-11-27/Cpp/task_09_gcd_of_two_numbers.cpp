// Daily Practice Task 9
// Date: 2026-11-27
// Category: C++
//
// Task: Write a program to find the GCD of two numbers.
// Approach: Euclid's algorithm: replace (a, b) with (b, a % b) until b is 0.

#include <iostream>
using namespace std;

int main() {
    int a = 48, b = 18;
    int x = a, y = b;
    while (y != 0) {
        int r = x % y;
        x = y;
        y = r;
    }
    cout << "GCD of " << a << " and " << b << " is " << x << endl;
    return 0;
}
