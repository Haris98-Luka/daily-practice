// Daily Practice Task 36
// Date: 2026-11-26
// Category: C++
//
// Task: Write a program to check whether a number is palindrome.
// Approach: Reverse the number and compare it with the original.

#include <iostream>
using namespace std;

int main() {
    int n = 12321, original = n, reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    cout << original << (original == reversed ? " is a palindrome" : " is not a palindrome") << endl;
    return 0;
}
