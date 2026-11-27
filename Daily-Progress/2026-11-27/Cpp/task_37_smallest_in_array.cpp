// Daily Practice Task 37
// Date: 2026-11-27
// Category: C++
//
// Task: Write a program to find the smallest element in an array.
// Approach: Start with arr[0] and update whenever a smaller value appears.

#include <iostream>
using namespace std;

int main() {
    int arr[] = {42, 7, 19, 3, 88};
    int n = sizeof(arr) / sizeof(arr[0]);
    int smallest = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] < smallest) smallest = arr[i];
    cout << "Smallest = " << smallest << endl;
    return 0;
}
