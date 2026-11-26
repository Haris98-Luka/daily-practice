// Daily Practice Task 10
// Date: 2026-11-26
// Category: C++
//
// Task: Write a program to check whether a number is prime.
// Approach: Test divisors only up to sqrt(n).

#include <iostream>
using namespace std;

int main() {
    int n = 29;
    bool prime = n > 1;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) { prime = false; break; }
    }
    cout << n << (prime ? " is prime" : " is not prime") << endl;
    return 0;
}
