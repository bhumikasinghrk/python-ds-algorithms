# Integers

* [Palindrome Number](#palindrome-number)
* [Reverse Number](#reverse-number)
* [Two Sum](#two-sum)

## Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1: `121` -> `true`

Example 2: `-121` -> `false`

Explanation: From left to right, it reads `-121`. From right to left, it becomes `121-`. Therefore it is not a palindrome.

```python
def is_palindrome(x: int) -> bool:
    num = str(x)
    return num == num[::-1]
```

## Reverse Number

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: `123`

Output: `321`

```python
def reverse_number(number: int) -> int:
    reversed_number = int(str(abs(number))[::-1])

    if reversed_number > 2**31 - 1:  # Check for integer overflow (per question)
        return 0

    if number < 0:
        return -reversed_number
    return reversed_number
```

## Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given `nums = [2, 7, 11, 15], target = 9`,

Because `nums[0] + nums[1] = 2 + 7 = 9`, `return [0, 1]`.

Solution - Time: O(N)
```python
def two_sum(array: [int], target: int) -> [int]:
    complements = dict()

    for index, number in enumerate(array):
        complement = target - number
        if complement in complements:
            return [complements[complement], index]
        complements[number] = index

    return [-1, -1]
```

Alternate solution for sorted arrays - O(N)

```python
def two_sum_sorted(array: [], target: int) -> []:
    length = len(array)
    start = 0
    end = length - 1

    while start < end:
        if array[start] + array[end] > target:
            end -= 1
        elif array[start] + array[end] < target:
            start += 1
        else:
            return [start, end]

    return [start, end]
```
 