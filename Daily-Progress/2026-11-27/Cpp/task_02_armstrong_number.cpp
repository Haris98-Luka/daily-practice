// Daily Practice Task 2
// Date: 2026-11-27
// Category: C++
//
// Task: Write a program to check whether a number is an Armstrong number.
// Approach: Sum each digit raised to the number of digits and compare.

#include <iostream>
using namespace std;

int power(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) result *= base;
    return result;
}

int main() {
    int n = 153, temp = n, digits = 0;
    while (temp > 0) { digits++; temp /= 10; }

    temp = n;
    int sum = 0;
    while (temp > 0) {
        sum += power(temp % 10, digits);
        temp /= 10;
    }
    cout << n << (sum == n ? " is an Armstrong number" : " is not an Armstrong number") << endl;
    return 0;
}
