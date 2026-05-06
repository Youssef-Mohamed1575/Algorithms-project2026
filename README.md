# Algorithms-project2026
Algoritms project assigned to CS students of Fcaih 2025/2026 - year 2

# Triangle Triplet Detection

## Problem Overview
Given a zero-indexed array A consisting of N integers, determine if there exists a triangular triplet.
A triplet $(P, Q, R)$ is considered triangular if $0 \leq P < Q < R < N$ and the following conditions are met:
$A[P] + A[Q] > A[R]$
$A[Q] + A[R] > A[P]$
$A[R] + A[P] > A[Q]$
Goal: Return 1 if a triangular triplet exists in the array, otherwise return 0.

## Examples
**Example 1:**
Input: nums = [10, 50, 1]  
Output: 0 (No combination of sides can form a triangle).

**Example 2:**
Input: nums = [10, 2, 5, 1, 8, 20]  
Output: 1 (Triplet (0, 2, 4) corresponds to values 10, 5, 8 which can form a triangle).

---

# Algorithm 1: Recursive Approach
This approach sorts the array first. Sorting ensures that for any three elements $A[i] \leq A[j] \leq A[k]$, the conditions $A[j] + A[k] > A[i]$ and $A[i] + A[k] > A[j]$ are always true. Thus, we only need to verify if $A[i] + A[j] > A[k]$. The algorithm uses recursion to traverse the array backward and checks pairs.

## Pseudo-code
FUNCTION RecursiveTriangleFinder(nums):
SORT nums in ascending order
RETURN Triangle_finder(nums, length(nums) - 1)

FUNCTION Triangle_finder(nums, k):
IF k < 2:
RETURN 0

IF check_triangle(nums, 0, k - 1, k) is TRUE:
RETURN 1

RETURN Triangle_finder(nums, k - 1)

FUNCTION check_triangle(nums, i, j, k):
IF i >= j:
RETURN FALSE

IF nums[i] + nums[j] > nums[k]:
PRINT "Triangle sides = ", nums[i], nums[j], nums[k]
RETURN TRUE

RETURN check_triangle(nums, i + 1, j, k)


## Complexity Analysis
**Time Complexity:** $O(N^2)$  
- Sorting the array takes $O(N \log N)$ time.  
- The outer recursive function (Triangle_finder) executes $O(N)$ times.  
- For each execution, the inner recursive function (check_triangle) executes up to $O(N)$ times.  
- The dominant operation is $O(N) \times O(N) = O(N^2)$.

**Space Complexity:** $O(N)$  
- The space complexity is governed by the maximum depth of the recursion tree. Both Triangle_finder and check_triangle can go up to $N$ levels deep, requiring $O(N)$ space on the call stack.

---

# Algorithm 2: Iterative Two-Pointer Approach
This algorithm improves upon the recursive solution by using iterative loops and two pointers. After sorting the array, it sets k as the largest element's index and uses two pointers (i at the start, and j just before k) to search for a valid pair.

## Pseudo-code
FUNCTION triangleNumber(nums):
SORT nums in ascending order

FOR k FROM length(nums) - 1 DOWN TO 2:
i = 0
j = k - 1

WHILE i < j:
IF nums[i] + nums[j] > nums[k]:
RETURN 1
ELSE:
i = i + 1

RETURN 0


## Complexity Analysis
**Time Complexity:** $O(N^2)$  
- Sorting the array takes $O(N \log N)$ time.  
- The outer FOR loop runs $O(N)$ times.  
- The inner WHILE loop traverses the array using pointer i up to j, taking up to $O(N)$ time in the worst case.  
- Total time complexity is $O(N^2)$.

**Space Complexity:** $O(1)$ auxiliary space  
- This algorithm evaluates the array in-place using loops and pointers, requiring no extra memory outside of the space required by the sorting algorithm.

---

# Algorithm 3: Optimal Greedy Approach (Adjacent Elements)
Since we only need to return 1 if any single triangle exists (rather than counting all possible triangles), we can optimize further. After sorting the array, if a triangle exists anywhere, it must exist between three adjacent elements.

**Mathematical Proof:** If $A[i] + A[i+1] \leq A[i+2]$, then $A[i] + A[i+1]$ will also be less than or equal to any element further down the sorted array (e.g., $A[i+3], A[i+4]$). Therefore, checking non-adjacent elements is unnecessary for a simple true/false existence check. We only need to check if $A[i] + A[i+1] > A[i+2]$.

## Pseudo-code
FUNCTION hasTriangle(nums):
IF length(nums) < 3:
RETURN 0

SORT nums in ascending order

FOR i FROM 0 TO length(nums) - 3:
IF nums[i] + nums[i+1] > nums[i+2]:
RETURN 1

RETURN 0


## Complexity Analysis
**Time Complexity:** $O(N \log N)$  
- Sorting the array takes $O(N \log N)$ time.  
- The single FOR loop iterates through the array exactly once, taking $O(N)$ time.  
- The dominant operation is the sort, making the total time complexity $O(N \log N)$.

**Space Complexity:** $O(1)$ auxiliary space  
- This algorithm evaluates the array in-place, requiring no extra memory outside of the space required by the sorting algorithm.

---

# Comparison

| Feature | Algorithm 1 (Recursive) | Algorithm 2 (Iterative Two-Pointer) | Alg 3: Optimal Greedy |
|---|---:|---:|---:|
| Paradigm | Recursion | Iteration (Two-Pointer) | Greedy / Linear Scan |
| Time Complexity | O(N^2) | O(N^2) | O(N \log N) |
| Space Complexity | O(N) (Call Stack) | O(1) (In-place) | O(1) (In-place) |
| Performance Risk | High: Stack Overflow and O(N^2) slow-down on large inputs. | Medium: O(N^2) can be slow for N > 10,000. | Very Low: Only risks integer overflow in non-Python languages. |
| Conclusion | Good for demonstrating functional programming concepts, but inefficient for memory. | Recommended Solution. It is memory-safe and avoids the heavy overhead of recursive function calls. | Best Solution. Most efficient for checking the existence of a triangle. |




