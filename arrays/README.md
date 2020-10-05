# Arrays

* [Check Double](#check-double)
* [Container With Max Area](#container-with-max-area)
* [Count Elements](#count-elements)
* [Duplicate Zeros](#duplicate-zeros)
* [Find Index of Largest Number](#find-index-of-largest-number)
* [Find Smallest Positive Integer](#find-smallest-positive-integer)
* [First Duplicate](#first-duplicate)
* [First Not Repeating Character](#first-not-repeating-character)
* [First Pivot Index](#first-pivot-index)
* [Intersection of Three Sorted Arrays](#intersection-of-three-sorted-arrays)
* [Intersection of Two Arrays](#intersection-of-two-arrays)
* [Largest Number At Least Twice of Others](#largest-number-at-least-twice-of-others)
* [Make Array Consecutive](#make-array-consecutive)
* [Max Consecutive Ones](#max-consecutive-ones)
* [Merge Sorted Array](#merge-sorted-array)
* [Move Zeros](#move-zeros)
* [Peaks](#peaks)
* [Plus One](#plus-one)
* [Remove Duplicates](#remove-duplicates)
* [Remove Element](#remove-element)
* [Replace Elements With Greatest Element On Right Side](#replace-elements-with-greatest-element-on-right-side)
* [Rotate Array](#rotate-array)
* [Search Insert Position](#search-insert-position)
* [Single Number](#single-number)
* [Sorted Squares](#sorted-squares)
* [Valid Mountain Array](#valid-mountain-array)

## Check Double

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

`i != j`
`arr[i] == 2 * arr[j]`
 
Example 1:

Input: `[10,2,5,3]`
Output: `true`
Explanation: `N = 10 is the double of M = 5,that is, 10 = 2 * 5.`

```python
def check_double(arr: List[int]) -> bool:
    elements = set()

    for num in arr:
        if num * 2 in elements:
            return True
        if num % 2 == 0 and num / 2 in elements:
            return True
        elements.add(num)
    return False
```

## Container With Max Area

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are
drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
container, such that the container contains the most water.

```python
def container_with_max_area(height: List[int]) -> int:
    length = len(height)
    left = 0
    right = length - 1
    max_area = 0

    while left < right:
        lowest = min(height[left], height[right])
        max_area = max(max_area, lowest * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

## Count Elements

Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.

If there're duplicates in arr, count them separately.

```python
def count_elements(arr: List[int]) -> int:
    elements = set()
    counter = 0

    for element in arr:
        elements.add(element)

    for element in arr:
        if element + 1 in elements:
            counter += 1

    return counter
```

## Duplicate Zeros

Duplicate the zeros in the supplied array. Excess values should be discarded so that the array remains the same size

Example: `[1, 0, 2, 3, 0, 4, 5, 6]` -> `[1, 0, 0, 2, 3, 0, 0, 4]`

Time: O(N), Space: O(N)

```python
def duplicate_zeros(arr: List[int]) -> List[int]:
    stack = []
    index = 0
    length = len(arr)

    while len(stack) < length:
        stack.append(arr[index])

        if len(stack) < length and arr[index] == 0:
            stack.append(0)
        index += 1

    for i in range(length - 1, -1, -1):
        arr[i] = stack.pop()

    return arr
```

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

## Find Smallest Positive Integer

Find the smallest positive integer in an array. Return zero if no positive integers

Input: `[1, -2, 3]`
Output: `1`

```python
def find_smallest_positive_integer(arr: List[int]) -> int:
    length = len(arr)

    if length == 0:
        return 0

    smallest = None

    for i in range(length):
        if arr[i] > 0:
            if smallest is None:
                smallest = arr[i]
            elif arr[i] < smallest:
                smallest = arr[i]

    if smallest is None:
        return 0
    return smallest
```

## First Duplicate

Given an array a that contains only numbers in the range from `1` to `a.length`, find
the first duplicate number for which the second occurrence has the minimal index.
In other words, if there are more than 1 duplicated numbers, return the number for
which the second occurrence has a smaller index than the second occurrence of
the other number does. If there are no such elements, return `-1`.

First Duplicate w/ Set

```python
def first_duplicate(array: [int]) -> int:
    number_counter = dict()
    for value in array:
        if value in number_counter:
            number_counter[value] += 1
        else:
            number_counter[value] = 1

    for value in array:
        if number_counter[value] > 1:
            return value
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

## Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = `[1,2,2,1]`, nums2 = `[2,2]`
Output: `[2,2]`

```python
def intersection_of_two_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    intersection = []
    nums1_map = {}

    for num in nums1:
        if num in nums1_map:
            nums1_map[num] += 1
        else:
            nums1_map[num] = 1

    for num in nums2:
        if num in nums1_map and nums1_map[num] > 0:
            intersection.append(num)
            nums1_map[num] -= 1

    return intersection
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

## Max Consecutive Ones

Return the largest number of consecutive 1s from an array of binary integers

Input: `[1, 1, 0, 1, 1, 1, 0, 0, 1]`
Output: `3`

```python
def max_consecutive_ones(nums: List[int]) -> int:
    max_ones, count = 0, 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            max_ones = max(max_ones, count)
            count = 0

    return max(max_ones, count)
```

## Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
`nums1 = [1,2,3,0,0,0], m = 3`
`nums2 = [2,5,6],       n = 3`

Output: `[1,2,2,3,5,6]`

```python
def merge_sorted_array(nums1: List[int], nums1_length: int, nums2: List[int], nums2_length: int) -> List[int]:
    index_nums1 = nums1_length - 1
    index_nums2 = nums2_length - 1
    current_index = nums1_length + nums2_length - 1

    while index_nums2 >= 0:
        if index_nums1 < 0 <= index_nums2:
            nums1[current_index] = nums2[index_nums2]
            index_nums2 -= 1
        elif nums1[index_nums1] > nums2[index_nums2]:
            nums1[current_index] = nums1[index_nums1]
            index_nums1 -= 1
        else:
            nums1[current_index] = nums2[index_nums2]
            index_nums2 -= 1

        current_index -= 1

    return nums1
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

## Peaks

Given an array of integers return the values that are between two smaller values.

Example: `[1, 3, 2] -> [3]`

```python
def peaks(numbers: List[int]) -> List[int]:
    length = len(numbers)
    peak_nums = []

    if length < 3:
        return peak_nums

    for index in range(1, length - 1):
        if numbers[index - 1] < numbers[index] and numbers[index] > numbers[index + 1]:
            peak_nums.append(numbers[index])

    return peak_nums
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

## Remove Duplicates

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new
length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra
memory.

Example:

Input: `[1, 1, 2`
Output: `[1, 2, 2], count: 2`

```python
def remove_duplicates(nums: List[int]) -> int:
    length = len(nums)
    if length <= 1:
        return length

    last_index = 0

    for index in range(1, length):
        if nums[index] == nums[last_index]:
            continue
        last_index += 1
        nums[last_index] = nums[index]

    return last_index + 1
```

## Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
`nums = [3,2,2,3]`, `val = 3`,

Your function should return `2`, with the array being mutated to `[2, 2, 2, 3]`

```python
def remove_element(nums: List[int], val: int) -> int:
    index = 0
    count = 0
    length = len(nums)

    while index < length:
        if nums[index] == val:
            count += 1
        else:
            nums[index - count] = nums[index]
        index += 1
    return length - count
```

## Replace Elements with Greatest Element on Right Side 

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

Example 1:

Input: `[17,18,5,4,6,1]`
Output: `[18,6,6,6,1,-1]`
 
Constraints:

`1 <= arr.length <= 10^4`
`1 <= arr[i] <= 10^5`

```python
def replace_elements_with_greatest(arr: List[int]) -> List[int]:
    length = len(arr)
    max_number = -1

    for index in range(length - 1, -1, -1):
        temp = arr[index]
        arr[index] = max_number
        max_number = max(temp, max_number)

    return arr
```

## Rotate Array

Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

Example:

Input: `k = 3`, `[1, 2, 3, 4, 5, 6]`
Output: `[4, 5, 6, 1, 2, 3]`

With array:
Time: O(N)
Space: O(N)

```python
def rotate_array_with_array(nums: List[int], k: int) -> List[int]:
    length = len(nums)
    copy = [0] * length

    for index in range(length):
        copy[(index + k) % length] = nums[index]

    return copy
```

```python
def rotate_array_in_place(nums: List[int], k: int) -> List[int]:
    length = len(nums)
    k = k % length

    reverse(nums, 0, length - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, length - 1)
    return nums

def reverse(arr: List, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
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

## Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity.

Example 1:

Input: `[2,2,1]`

Solution using hash table:

Solution: Time: O(N), Space: O(N)  

```python
def single_number(nums: List[int]) -> int:
    if not nums:
        return 0
    
    nums_dict = dict()

    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1

    for num in nums_dict:
        if nums_dict[num] == 1:
            return num

    return 0
```

Solution using bitwise function. Time: O(N), Space: O(1)

```python
def single_number_bitwise(nums: List[int]) -> int:
    if not nums:
        return 0
    current = nums[0]
    
    for index in range(1, len(nums)):
        current ^= nums[index]
        
    return current
```

## Sorted Squares

Given a sorted array of numbers return the squares in ascending order

Example

Input: `[-2, -1, 0, 1, 3]`
Output: `[0, 1, 1, 4, 9]`

```python
def sorted_squares(nums: List[int]) -> List[int]:
    length = len(nums)
    first_positive = None

    for index in range(length):
        if nums[index] >= 0:
            first_positive = index
            break

    # All Negative
    if first_positive is None:
        result = []
        for index in range(length - 1, -1, -1):
            result.append(nums[index] * nums[index])
        return result

    # All Positive
    if first_positive == 0:
        return [x * x for x in nums]

    left = first_positive - 1
    right = first_positive
    squares = []

    while left >= 0 and right < length:
        if abs(nums[left]) < nums[right]:
            squares.append(nums[left] * nums[left])
            left -= 1
        else:
            squares.append(nums[right] * nums[right])
            right += 1

    while right < length:
        squares.append(nums[right] * nums[right])
        right += 1

    while left >= 0:
        squares.append(nums[left] * nums[left])
        left -= 1

    return squares
```

## Valid Mountain Array

Given an array of integers, return true if it is valid mountain array.

A valid mountain array is:

`A.length >= 3`
There exists some i with `0 < i < A.length - 1` such that:
`A[0] < A[1] < ... A[i-1] < A[i]`
`A[i] > A[i+1] > ... > A[A.length - 1]`

Example: `[1, 2, 3, 2, 1]`

```python
def valid_mountain_array(arr: List[int]) -> bool:
    length = len(arr)
    if length <= 2:
        return False

    index = 1

    # Check increasing
    while index < length:
        if arr[index - 1] < arr[index]:
            index += 1
        else:
            break

    # Edge case: only increasing, only decreasing
    if index == length or index == 1:
        return False

    # Check decreasing
    while index < length:
        if arr[index - 1] > arr[index]:
            index += 1
        else:
            return False
    return True
```