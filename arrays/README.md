# Arrays

* [First Duplicate](#first-duplicate)
* [First Not Repeating Character](#first-not-repeating-character)
* [First Pivot Index](#first-pivot-index)
* [Make Array Consecutive](#make-array-consecutive)
* [Search Insert Position](#search-insert-position)

## First Duplicate

Given an array a that contains only numbers in the range from `1` to `a.length`, find
the first duplicate number for which the second occurrence has the minimal index.
In other words, if there are more than 1 duplicated numbers, return the number for
which the second occurrence has a smaller index than the second occurrence of
the other number does. If there are no such elements, return `-1`.

First Duplicate w/ Set

```python
def first_duplicate(a: [int]) -> int:
    unique_set = set()
    for value in a:
        if value in unique_set:
            return value
        else:
            unique_set.add(value)
    return -1
```

First Duplicate (In-Place)

```python
def first_duplicate_in_place(array: [int]) -> int:
    while len(array) > 0:
        value = array.pop(0)
        if value in array:
            return value
    return -1
```

## First Not Repeating Character

Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you
would be asked to do during a real interview.

Given a string `s`, find and return the first instance of a non-repeating character in it. If there is no such 
character, return `_`.

With Set:

```python
def first_not_repeating_character(s: str) -> str:
    #  skip characters we've already checked.
    checked_chars = set()
    for char in s:
        if char not in checked_chars and s.index(char) == s.rindex(char):
            return char
        checked_chars.add(char)
    return '_'
```

With Array Slices (less optimal):

```python
def first_not_repeating_character(s: str) -> str:
    length = len(s)
    index = 0
    while index < length:
        if s[index] not in s[:index] and s[index] not in s[index + 1:]:
            return s[index]
        index += 1
    return '_'
```

## First Pivot Index

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the 
numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot 
index.

Input: `[1, 7, 3, 6, 5, 6]`

Output: 3

```python
def find_pivot_index(nums: [int]) -> int:
    total = sum(nums)
    left_sum = 0

    for index, value in enumerate(nums):
        if left_sum == total - left_sum - value:
            return index
        left_sum += value
    return -1
```

## Make Array Consecutive

Find the number of elements that would need to be added so that each array value is separated by one.

`[1,2,3,5] -> 1 #4 needs to be added to the array`

```python
def make_array_consecutive(arr: [int]) -> int:
    length = len(arr)
    numbers_needed = 0

    if length <= 1:
        return numbers_needed

    sorted_numbers = sorted(arr)

    for i in range(1, length):
        numbers_needed += (sorted_numbers[i] - sorted_numbers[i - 1]) - 1

    return numbers_needed
``` 

## Search Insert Position

[Leetcode: Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it 
would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: `[1,3,5,6], 5`
Output: `2`

```python
def search_insert(nums: [int], target: int) -> int:
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        middle = int((left_index + right_index) / 2)

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left_index = middle + 1
        else:
            right_index = middle - 1

    return left_index
```