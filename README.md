# Algorithms Project 2026

Triangle Triplet Detection Problem

## Introduction

The purpose of this project is to determine whether a given array of integers contains any three numbers that can form a valid triangle.

For three sides to form a triangle:

* Side1 + Side2 > Side3
* Side2 + Side3 > Side1
* Side3 + Side1 > Side2

If at least one valid triplet exists, the algorithm returns `1`. Otherwise, it returns `0`.

---
## Example 1:

**Input:**
`[10 , 50 , 1]`
**Output:**
`0`
**Explanation:**
No valid triangle found in this input.
---
## Example 2:

**Input:**
`[10, 2, 5, 1, 8, 20]`

**Output:**
`1`

**Explanation:**
The values `10, 5, 8` form a valid triangle.

---

# Algorithm 1: Recursive Approach

## Idea

First, the array is sorted using Bubble Sort.

After sorting:
`a ≤ b ≤ c`

This means we only need to check:

`a + b > c`

instead of checking all three triangle conditions.

The recursive solution starts from the largest element and recursively checks possible pairs.

---

## Pseudo-code

FUNCTION bubble_sort(nums):
Sort the array in ascending order

FUNCTION recursive_triangle(nums):
bubble_sort(nums)
RETURN triangle_finder(nums, last index)

FUNCTION triangle_finder(nums, k):
IF k < 2:
RETURN 0

```
IF check_triangle(nums, 0, k-1, k):
    RETURN 1

RETURN triangle_finder(nums, k-1)
```

FUNCTION check_triangle(nums, i, j, k):
IF i >= j:
RETURN FALSE

```
IF nums[i] + nums[j] > nums[k]:
    RETURN TRUE

RETURN check_triangle(nums, i+1, j, k)
```

---

## Analysis

Time Complexity Explanation:
•	Bubble Sort requires O(N²) time because it uses nested loops to repeatedly compare and swap adjacent elements.
•	The outer recursive function triangle_finder() may run up to N times, once for each possible largest side.
•	For each recursive call, check_triangle() may scan through up to N smaller elements.
•	This creates approximately O(N × N) = O(N²) operations.
•	Since Bubble Sort is also O(N²), the total complexity remains O(N²).
Final Time Complexity: O(N²)

Space Complexity Explanation:
•	Bubble Sort works in-place and uses O(1) extra memory.
•	However, recursive calls are stored on the call stack.
•	In the worst case, recursion depth may reach O(N).
•	Therefore, total auxiliary space is O(N).
Final Space Complexity: O(N)


---

## Advantages

* Demonstrates recursion clearly
* Good for understanding recursive searching
* Fully manual implementation

---

## Disadvantages

* Uses more memory
* Slower for larger inputs
* Stack overflow possible

---

# Algorithm 2: Iterative Two-Pointer Approach

## Idea

This solution also sorts the array first.

Then:

* Choose the largest side
* Use two pointers to test smaller values

This avoids recursion and is generally safer.

---

## Pseudo-code

FUNCTION bubble_sort(nums):
Sort array

FUNCTION iterative_triangle(nums):
bubble_sort(nums)

```
FOR k from last index down to 2:
    i = 0
    j = k - 1

    WHILE i < j:
        IF nums[i] + nums[j] > nums[k]:
            RETURN 1
        ELSE:
            i = i + 1

RETURN 0
```

---

## Analysis

Time Complexity Explanation:
•	Bubble Sort still requires O(N²) time.
•	The outer loop iterates through possible largest sides, up to N times.
•	The inner while loop moves pointers through the array, requiring up to N operations per iteration.
•	Combined traversal gives O(N²) complexity.
•	Since sorting is O(N²), total complexity remains O(N²).
Final Time Complexity: O(N²)

Space Complexity Explanation:
•	Bubble Sort is performed in-place.
•	The algorithm only uses pointer variables (i, j, k).
•	No recursion or additional large data structures are required.
•	Thus, auxiliary memory usage is constant.
Final Space Complexity: O(1)


---

## Advantages

* Better memory efficiency
* No recursion
* More practical
* Easier to scale

---

## Disadvantages

* Still quadratic time complexity

---

# Why Sorting Helps

Sorting makes the problem easier because:

For:
`a ≤ b ≤ c`

Only:
`a + b > c`

needs to be checked.

This reduces unnecessary conditions and improves efficiency.

---

## Key Benefit

* Reduces triangle validation from 3 checks to 1
* Simplifies implementation
* Improves algorithm efficiency

---

# Comparison

| Feature          | Recursive | Iterative |
| ---------------- | --------- | --------- |
| Time Complexity  | O(N²)     | O(N²)     |
| Space Complexity | O(N)      | O(1)      |
| Memory Use       | Higher    | Lower     |
| Performance      | Slower    | Faster    |
| Simplicity       | Moderate  | Better    |

---

# Final Conclusion

Both algorithms solve the triangle triplet problem successfully.

**Recursive Approach:**
Useful for demonstrating recursion concepts.

**Iterative Approach:**
More efficient and practical.

---

## Recommended Solution

**Iterative Two-Pointer Approach**

Because it:

* Uses less memory
* Avoids recursion issues
* Is easier to apply for larger datasets

---

## Project Requirements Covered

* Recursive algorithm
* Non-recursive algorithm
* Manual implementation
* Pseudo-code
* **Analysis**
* Complexity calculation
* Comparison between algorithms
