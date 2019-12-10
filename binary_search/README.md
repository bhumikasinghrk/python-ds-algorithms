# Binary Search

- [Search Insert Position](#search-insert-position)

## Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5

Output: 2


```python
def search_insert(nums: [int], target: int) -> int:
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        middle = int((left_index + right_index) / 2)

        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            left_index = middle + 1
        else:
            right_index = middle - 1

    return left_index
```
