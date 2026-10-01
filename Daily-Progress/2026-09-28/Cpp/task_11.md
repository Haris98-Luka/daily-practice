# Daily Practice Task 11

**Date:** 2026-09-28

**Category:** Cpp

## Task

Write a program to calculate factorial of a number.
#include <iostream>
using namespace std;

int main()
{
    int n;
    long long factorial = 1;

    cout << "Enter a number: ";
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        factorial = factorial * i;
    }

    cout << "Factorial = " << factorial;

    return 0;
}
## Practice Status

- [ yes] Started
- [ ] Solved
- [ ] Understood
