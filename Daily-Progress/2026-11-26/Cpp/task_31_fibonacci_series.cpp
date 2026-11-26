// Daily Practice Task 31
// Date: 2026-11-26
// Category: C++
//
// Task: Write a program to print the first 10 Fibonacci numbers.
// Approach: Each number is the sum of the previous two.

#include <iostream>
using namespace std;

int main() {
    int n = 10;
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        cout << a << " ";
        long long next = a + b;
        a = b;
        b = next;
    }
    cout << endl;
    return 0;
}
