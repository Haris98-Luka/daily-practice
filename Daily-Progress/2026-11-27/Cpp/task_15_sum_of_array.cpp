// Daily Practice Task 15
// Date: 2026-11-27
// Category: C++
//
// Task: Write a program to calculate the sum of array elements.
// Approach: Loop through the array and keep a running total.

#include <iostream>
using namespace std;

int main() {
    int arr[] = {5, 10, 15, 20, 25};
    int n = sizeof(arr) / sizeof(arr[0]);
    int sum = 0;
    for (int i = 0; i < n; i++) sum += arr[i];
    cout << "Sum = " << sum << endl;
    return 0;
}
