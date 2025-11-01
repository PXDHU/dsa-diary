# 1929. Concatenation of Array

**Link:** [LeetCode Problem - 1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/description/)

---

## Problem Statement

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where  
`ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (0-indexed).

Specifically, `ans` is the concatenation of two `nums` arrays.

Return the array `ans`.

---

## Example 1

**Input:**
nums = [1,2,1]

makefile
Copy code

**Output:**
[1,2,1,1,2,1]

makefile
Copy code

**Explanation:**
ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]
ans = [1,2,1,1,2,1]

yaml
Copy code

---

## Example 2

**Input:**
nums = [1,3,2,1]

makefile
Copy code

**Output:**
[1,3,2,1,1,3,2,1]

makefile
Copy code

**Explanation:**
ans = [nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]
ans = [1,3,2,1,1,3,2,1]

yaml
Copy code

---

## Constraints

- `n == nums.length`
- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`