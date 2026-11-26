// Daily Practice Task 19
// Date: 2026-11-26
// Category: C++
//
// Task: Write a program to count even and odd numbers.
// Approach: Use % 2 to separate even and odd values.

#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    int even = 0, odd = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) even++;
        else odd++;
    }
    cout << "Even: " << even << ", Odd: " << odd << endl;
    return 0;
}
