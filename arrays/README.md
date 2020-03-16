# Arrays

* [Find Index of Largest Number](#find-index-of-largest-number)
* [First Duplicate](#first-duplicate)
* [First Not Repeating Character](#first-not-repeating-character)
* [First Pivot Index](#first-pivot-index)
* [Intersection of Three Sorted Arrays](#intersection-of-three-sorted-arrays)
* [Largest Number At Least Twice of Others](#largest-number-at-least-twice-of-others)
* [Make Array Consecutive](#make-array-consecutive)
* [Move Zeros](#move-zeros)
* [Plus One](#plus-one)
* [Search Insert Position](#search-insert-position)

## Find Index of Largest Number

Find the index of the largest number in a list. Return a -1 if empty

```python
def find_index_largest_number(numbers: List[int]) -> int:
    if not numbers:
        return -1

    largest_index = numbers[0]

    for index in range(1, len(numbers)):
        if numbers[index] > numbers[largest_index]:
            largest_index = index
    return largest_index
```

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

Output: `3`

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

## Intersection of Three Sorted Arrays

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the
integers that appeared in all three arrays.

Example:

Input: `arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]`
Output: `[1,5]`

```python
def arrays_intersection(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    intersection = set(arr1)
    intersection = intersection.intersection(arr2)
    return sorted(list(intersection.intersection(arr3)))
```

```python
def arrays_intersection2(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    index1 = 0
    index2 = 0
    index3 = 0
    result = []

    while index1 < len(arr1) and index2 < len(arr2) and index3 < len(arr3):
        if arr1[index1] == arr2[index2] == arr3[index3]:
            result.append(arr1[index1])
            index1 += 1
            index2 += 1
            index3 += 1
            continue

        current_max = max(arr1[index1], arr2[index2], arr3[index3])

        if arr1[index1] < current_max:
            index1 += 1
        if arr2[index2] < current_max:
            index2 += 1
        if arr3[index3] < current_max:
            index3 += 1

    return result
```

## Largest Number At Least Twice of Others

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Input: `[3, 6, 1, 0]`

Output: `1`

```python
def largest_number_at_least_twice_of_others(nums: [int]) -> int:
    if len(nums) == 0:
        return -1

    largest = None
    next_largest = None

    for idx, num in enumerate(nums):
        if largest is None:
            largest = idx
            continue
        if num > nums[largest]:
            next_largest = largest
            largest = idx
            continue
        if next_largest is None or num > nums[next_largest]:
            next_largest = idx

    if next_largest is None or (nums[next_largest] * 2) <= nums[largest]:
        return largest
    return -1

```

With array manipulation and built-in functions. Slightly slower but easier to read

```python
def largest_number_at_least_twice_of_others2(nums: [int]) -> int:
    if len(nums) == 1:
        return 0

    max_index = nums.index(max(nums))
    max_val = nums.pop(max_index)
    next_max = max(nums)

    if next_max * 2 <= max_val:
        return max_index
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

## Move Zeros

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Example:

Input: `[0,1,0,3,12]`
Output: `[1,3,12,0,0]`
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

```python
def move_zeros(nums: List[int]) -> None:
    if not nums or len(nums) == 0:
        return

    current_index = 0
    last_num = None

    while current_index < len(nums):
        if nums[current_index] == 0:
            next_num = last_num if last_num else current_index + 1
            while next_num < len(nums):
                if nums[next_num] != 0:
                    nums[next_num], nums[current_index] = nums[current_index], nums[next_num]
                    last_num = next_num + 1
                    break
                next_num += 1
        current_index += 1
```

## Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array
contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: `[1,2,3]`
Output: `[1,2,4]`
Explanation: The array represents the integer 123.


```python
def plus_one(digits: List[int]) -> List[int]:
    """
    Increment array of digits by one as if a number
    [1, 2, 3] -> [1, 2, 4]

    :param digits: list of int numbers representing a non-negative number
    :return: incremented list
    """

    for i in reversed(range(len(digits))):
        digits[i] = (digits[i] + 1) % 10
        if digits[i] != 0:
            break
        if i == 0:
            digits.insert(0, 1)
            break
    return digits
```

## Search Insert Position

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