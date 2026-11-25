"""Daily practice generator: every task comes with a working solution.

Each run creates 25-50 unique tasks (no repeats in a day). Every task is a
separate, runnable file (.cpp / .py / .sql) with the problem written at the top.
"""

from datetime import datetime
from pathlib import Path
import random

SQL_SETUP = """CREATE TABLE Student (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT,
    marks INTEGER
);

INSERT INTO Student (id, name, class, marks) VALUES
    (1, 'Ali', '10-A', 85),
    (2, 'Sara', '10-A', 92),
    (3, 'Usman', '10-B', 74),
    (4, 'Ayesha', '10-B', 88),
    (5, 'Bilal', '10-A', 67);
"""

# Each task: (slug, title, approach, code)
TASKS = {
    # ------------------------------------------------------------------ C++
    "Cpp": [
        ("largest_of_three", "Write a program to find the largest of three numbers.",
         "Assume the first is largest, then compare with the other two.",
         r'''#include <iostream>
using namespace std;

int main() {
    int a = 12, b = 45, c = 30;
    int largest = a;
    if (b > largest) largest = b;
    if (c > largest) largest = c;
    cout << "Largest of " << a << ", " << b << ", " << c << " is " << largest << endl;
    return 0;
}
'''),
        ("factorial", "Write a program to calculate factorial of a number.",
         "Multiply 1 * 2 * ... * n in a loop.",
         r'''#include <iostream>
using namespace std;

int main() {
    int n = 10;
    long long fact = 1;
    for (int i = 2; i <= n; i++) fact *= i;
    cout << n << "! = " << fact << endl;
    return 0;
}
'''),
        ("prime_check", "Write a program to check whether a number is prime.",
         "Test divisors only up to sqrt(n).",
         r'''#include <iostream>
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
'''),
        ("reverse_number", "Write a program to reverse a number.",
         "Take the last digit with % 10 and build the reversed number.",
         r'''#include <iostream>
using namespace std;

int main() {
    int n = 12345, reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    cout << "Reversed: " << reversed << endl;
    return 0;
}
'''),
        ("palindrome_number", "Write a program to check whether a number is palindrome.",
         "Reverse the number and compare it with the original.",
         r'''#include <iostream>
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
'''),
        ("sum_of_array", "Write a program to calculate the sum of array elements.",
         "Loop through the array and keep a running total.",
         r'''#include <iostream>
using namespace std;

int main() {
    int arr[] = {5, 10, 15, 20, 25};
    int n = sizeof(arr) / sizeof(arr[0]);
    int sum = 0;
    for (int i = 0; i < n; i++) sum += arr[i];
    cout << "Sum = " << sum << endl;
    return 0;
}
'''),
        ("smallest_in_array", "Write a program to find the smallest element in an array.",
         "Start with arr[0] and update whenever a smaller value appears.",
         r'''#include <iostream>
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
'''),
        ("count_even_odd", "Write a program to count even and odd numbers.",
         "Use % 2 to separate even and odd values.",
         r'''#include <iostream>
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
'''),
        ("swap_two_numbers", "Write a program to swap two numbers.",
         "Use a temporary variable to hold one value.",
         r'''#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20;
    cout << "Before: a = " << a << ", b = " << b << endl;
    int temp = a;
    a = b;
    b = temp;
    cout << "After:  a = " << a << ", b = " << b << endl;
    return 0;
}
'''),
        ("simple_interest", "Write a program to calculate simple interest.",
         "Formula: SI = (P * R * T) / 100.",
         r'''#include <iostream>
using namespace std;

int main() {
    double principal = 10000, rate = 5, time = 3;
    double interest = (principal * rate * time) / 100;
    cout << "Simple Interest = " << interest << endl;
    return 0;
}
'''),
        ("fibonacci_series", "Write a program to print the first 10 Fibonacci numbers.",
         "Each number is the sum of the previous two.",
         r'''#include <iostream>
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
'''),
        ("gcd_of_two_numbers", "Write a program to find the GCD of two numbers.",
         "Euclid's algorithm: replace (a, b) with (b, a % b) until b is 0.",
         r'''#include <iostream>
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
'''),
        ("armstrong_number", "Write a program to check whether a number is an Armstrong number.",
         "Sum each digit raised to the number of digits and compare.",
         r'''#include <iostream>
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
'''),
    ],

    # --------------------------------------------------------------- Python
    "Python": [
        ("largest_in_list", "Write a program to find the largest number in a list.",
         "Keep track of the biggest value while looping.",
         r'''numbers = [14, 92, 37, 58, 3]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest:", largest)
'''),
        ("reverse_string", "Write a program to reverse a string.",
         "Slicing with [::-1] walks the string backwards.",
         r'''text = "practice"
print("Original:", text)
print("Reversed:", text[::-1])
'''),
        ("count_vowels", "Write a program to count vowels in a string.",
         "Check every character against the set of vowels.",
         r'''text = "Daily practice makes perfect"
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Vowels:", count)
'''),
        ("factorial", "Write a program to calculate factorial.",
         "Multiply numbers from 1 to n.",
         r'''def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print("5! =", factorial(5))
print("10! =", factorial(10))
'''),
        ("prime_check", "Write a program to check whether a number is prime.",
         "A prime has no divisor between 2 and sqrt(n).",
         r'''def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


for number in (2, 17, 18, 29, 100):
    print(number, "is prime" if is_prime(number) else "is not prime")
'''),
        ("sum_of_list", "Write a program to find the sum of list elements.",
         "Add each element to a running total.",
         r'''numbers = [4, 8, 15, 16, 23, 42]
total = 0
for n in numbers:
    total += n
print("Sum:", total)
'''),
        ("remove_duplicates", "Write a program to remove duplicates from a list.",
         "Keep an item only the first time it is seen (order preserved).",
         r'''items = [1, 3, 3, 2, 1, 5, 2, 4]
seen = set()
unique = []
for x in items:
    if x not in seen:
        seen.add(x)
        unique.append(x)
print("Without duplicates:", unique)
'''),
        ("count_words", "Write a program to count words in a sentence.",
         "split() breaks the sentence on whitespace.",
         r'''sentence = "Consistency beats intensity every single time"
words = sentence.split()
print("Word count:", len(words))
'''),
        ("smallest_in_list", "Write a program to find the smallest number in a list.",
         "Start with the first value and update when a smaller one appears.",
         r'''numbers = [27, 4, 91, 13, 8]
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print("Smallest:", smallest)
'''),
        ("average_of_numbers", "Write a program to calculate the average of numbers.",
         "Average = sum / count.",
         r'''numbers = [70, 85, 90, 65, 100]
average = sum(numbers) / len(numbers)
print("Average:", average)
'''),
        ("palindrome_string", "Write a program to check whether a string is a palindrome.",
         "Compare the cleaned string with its reverse.",
         r'''def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


for word in ("level", "Was it a car or a cat I saw", "python"):
    print(repr(word), "->", is_palindrome(word))
'''),
        ("fizzbuzz", "Write a program to print FizzBuzz from 1 to 20.",
         "Check divisibility by 15 first, then 3, then 5.",
         r'''for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''),
        ("second_largest", "Write a program to find the second largest number in a list.",
         "Remove duplicates, sort, and take the second last item.",
         r'''numbers = [12, 35, 1, 10, 34, 1, 35]
unique = sorted(set(numbers))
if len(unique) >= 2:
    print("Second largest:", unique[-2])
else:
    print("Not enough distinct numbers")
'''),
    ],

    # ------------------------------------------------------ Data Structures
    "Data-Structures": [
        ("linear_search", "Implement linear search.",
         "Check each element one by one. Time O(n).",
         r'''def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


data = [7, 3, 9, 1, 5]
print("Index of 9:", linear_search(data, 9))
print("Index of 4:", linear_search(data, 4))
'''),
        ("binary_search", "Implement binary search.",
         "Repeatedly halve a sorted array. Time O(log n).",
         r'''def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


data = [1, 3, 5, 7, 9, 11, 13]
print("Index of 7:", binary_search(data, 7))
print("Index of 4:", binary_search(data, 4))
'''),
        ("create_and_display_array", "Create and display an array.",
         "Create a list, then print every element with its index.",
         r'''arr = [10, 20, 30, 40, 50]

print("Array:", arr)
for index, value in enumerate(arr):
    print(f"arr[{index}] = {value}")
print("Length:", len(arr))
'''),
        ("stack_using_array", "Implement stack using an array.",
         "LIFO: push and pop happen at the end of the list.",
         r'''class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            raise IndexError("stack is empty")
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None


s = Stack()
for v in (10, 20, 30):
    s.push(v)
print("Top:", s.peek())
print("Popped:", s.pop())
print("Top now:", s.peek())
'''),
        ("queue_using_array", "Implement queue using an array.",
         "FIFO: add at the back, remove from the front.",
         r'''class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            raise IndexError("queue is empty")
        return self.items.pop(0)

    def front(self):
        return self.items[0] if self.items else None


q = Queue()
for v in ("A", "B", "C"):
    q.enqueue(v)
print("Front:", q.front())
print("Dequeued:", q.dequeue())
print("Front now:", q.front())
'''),
        ("insert_into_array", "Insert an element into an array.",
         "Shift elements right to make space, then place the value.",
         r'''arr = [10, 20, 30, 40, 50]
position, value = 2, 99

arr.append(None)  # make room
for i in range(len(arr) - 1, position, -1):
    arr[i] = arr[i - 1]
arr[position] = value

print("After insert:", arr)
'''),
        ("delete_from_array", "Delete an element from an array.",
         "Shift elements left over the deleted position, then drop the last slot.",
         r'''arr = [10, 20, 30, 40, 50]
position = 1

for i in range(position, len(arr) - 1):
    arr[i] = arr[i + 1]
arr.pop()

print("After delete:", arr)
'''),
        ("traverse_linked_list", "Traverse a linked list.",
         "Start at head and follow .next until None.",
         r'''class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

current = head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
'''),
        ("create_singly_linked_list", "Create a singly linked list.",
         "Append new nodes at the tail.",
         r'''class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def display(self):
        values, current = [], self.head
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values) + " -> None")


ll = LinkedList()
for v in (5, 10, 15, 20):
    ll.append(v)
ll.display()
'''),
        ("count_nodes_linked_list", "Count nodes in a linked list.",
         "Walk the list and increase a counter for each node.",
         r'''class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(4)
head.next = Node(8)
head.next.next = Node(15)
head.next.next.next = Node(16)

count, current = 0, head
while current:
    count += 1
    current = current.next
print("Number of nodes:", count)
'''),
        ("reverse_linked_list", "Reverse a singly linked list.",
         "Re-point each node's next to the previous node. Time O(n), space O(1).",
         r'''class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


def reverse(head):
    previous = None
    while head:
        head.next, previous, head = previous, head, head.next
    return previous


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original:", to_list(head))
print("Reversed:", to_list(reverse(head)))
'''),
        ("bubble_sort", "Implement bubble sort.",
         "Repeatedly swap neighbours that are out of order. Time O(n^2).",
         r'''def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
'''),
        ("middle_of_linked_list", "Find the middle node of a linked list.",
         "Two pointers: slow moves 1 step, fast moves 2. When fast ends, slow is in the middle.",
         r'''class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(1)
current = head
for v in (2, 3, 4, 5):
    current.next = Node(v)
    current = current.next

slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print("Middle node value:", slow.value)
'''),
    ],

    # ------------------------------------------------------------------ SQL
    "SQL": [
        ("create_student_table", "Create a Student table.",
         "CREATE TABLE defines columns, types and the primary key.",
         """CREATE TABLE Student (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT,
    marks INTEGER
);

-- Check the table structure
PRAGMA table_info(Student);
"""),
        ("insert_five_students", "Insert five student records.",
         "One INSERT with several value rows.",
         SQL_SETUP + """
-- Verify
SELECT COUNT(*) AS total_rows FROM Student;
"""),
        ("display_all_students", "Display all students.",
         "SELECT * returns every column and row.",
         SQL_SETUP + """
SELECT * FROM Student;
"""),
        ("marks_greater_than_80", "Find students with marks greater than 80.",
         "Filter rows with WHERE.",
         SQL_SETUP + """
SELECT name, marks FROM Student WHERE marks > 80;
"""),
        ("update_student_marks", "Update a student's marks.",
         "UPDATE ... SET ... WHERE (never forget WHERE).",
         SQL_SETUP + """
UPDATE Student SET marks = 95 WHERE name = 'Bilal';

SELECT name, marks FROM Student WHERE name = 'Bilal';
"""),
        ("delete_student_record", "Delete a student record.",
         "DELETE FROM ... WHERE removes matching rows only.",
         SQL_SETUP + """
DELETE FROM Student WHERE id = 3;

SELECT * FROM Student;
"""),
        ("sort_by_marks", "Sort students by marks.",
         "ORDER BY marks DESC puts the highest first.",
         SQL_SETUP + """
SELECT name, marks FROM Student ORDER BY marks DESC;
"""),
        ("count_total_students", "Count total students.",
         "COUNT(*) counts rows.",
         SQL_SETUP + """
SELECT COUNT(*) AS total_students FROM Student;
"""),
        ("find_maximum_marks", "Find the maximum marks.",
         "MAX() returns the largest value in a column.",
         SQL_SETUP + """
SELECT MAX(marks) AS highest_marks FROM Student;
"""),
        ("find_average_marks", "Find the average marks.",
         "AVG() returns the mean of a column.",
         SQL_SETUP + """
SELECT AVG(marks) AS average_marks FROM Student;
"""),
        ("students_per_class", "Count students in each class.",
         "GROUP BY groups rows so COUNT works per class.",
         SQL_SETUP + """
SELECT class, COUNT(*) AS total FROM Student GROUP BY class;
"""),
        ("top_three_students", "Find the top 3 students by marks.",
         "Sort descending and keep only 3 rows with LIMIT.",
         SQL_SETUP + """
SELECT name, marks FROM Student ORDER BY marks DESC LIMIT 3;
"""),
        ("names_starting_with_a", "Find students whose name starts with 'A'.",
         "LIKE 'A%' matches any text beginning with A.",
         SQL_SETUP + """
SELECT name FROM Student WHERE name LIKE 'A%';
"""),
    ],
}

CATEGORY_LABEL = {
    "Cpp": "C++",
    "Python": "Python",
    "Data-Structures": "Data Structures",
    "SQL": "SQL",
}
EXTENSION = {"Cpp": "cpp", "Python": "py", "Data-Structures": "py", "SQL": "sql"}
COMMENT = {"cpp": "//", "py": "#", "sql": "--"}


def build_file(category, number, title, approach, code, today):
    ext = EXTENSION[category]
    c = COMMENT[ext]
    header = (
        f"{c} Daily Practice Task {number}\n"
        f"{c} Date: {today}\n"
        f"{c} Category: {CATEGORY_LABEL[category]}\n"
        f"{c}\n"
        f"{c} Task: {title}\n"
        f"{c} Approach: {approach}\n\n"
    )
    return header + code


def main():
    today = datetime.now().strftime("%Y-%m-%d")

    pool = [(cat, task) for cat, items in TASKS.items() for task in items]
    total_tasks = random.randint(25, 50)
    chosen = random.sample(pool, total_tasks)  # unique: no repeats in a day

    base_folder = Path("Daily-Progress") / today
    base_folder.mkdir(parents=True, exist_ok=True)

    rows = []
    for number, (category, (slug, title, approach, code)) in enumerate(chosen, start=1):
        folder = base_folder / category
        folder.mkdir(parents=True, exist_ok=True)

        filename = f"task_{number:02d}_{slug}.{EXTENSION[category]}"
        (folder / filename).write_text(
            build_file(category, number, title, approach, code, today),
            encoding="utf-8",
        )
        rows.append((number, CATEGORY_LABEL[category], title, f"{category}/{filename}"))

    lines = [
        f"# Daily Practice - {today}",
        "",
        f"Total tasks solved today: **{total_tasks}**",
        "",
        "| # | Category | Task | Solution |",
        "|---|----------|------|----------|",
    ]
    for number, label, title, path in rows:
        lines.append(f"| {number} | {label} | {title} | [{Path(path).name}]({path}) |")
    lines += ["", "Every solution is a runnable file with the task and approach at the top.", ""]

    (base_folder / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Successfully generated {total_tasks} tasks with solutions for {today}.")


if __name__ == "__main__":
    main()
