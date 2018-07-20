# Python Data Structures and Algorithms [![Build Status](https://travis-ci.org/ahcode0919/python-ds-algorithms.svg?branch=master)](https://travis-ci.org/ahcode0919/python-ds-algorithms) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Various Data Structures and Algorithm Solutions in Python (3.x)

* [Algorithm Theory](#algorithm-theory)
* [Arrays](#arrays)
* [Binary Search](#binary-search)
* [Integers](#integers)
* [Matrices](#matrices)
* [Strings](#strings)
* [Trees](#trees)

## Algorithm Theory

* [Binary Search](#binary-search)
* [Linear Search](#linear-search)

#### Binary Search

Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval
covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow
the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or
the interval is empty.

Iterative Approach:

```python
def binarySearchIterative(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = int(left + right / 2)

        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
    return None
```

Recursive Approach:

````python

def binarySearchRecursive(array, left, right, target):
    if right >= left:

        mid = int(left + right / 2)

        # If element is present at the middle
        if array[mid] == target:
            return mid

        # If element is smaller than mid, then it can only be present in left subarray
        elif array[mid] > target:
            return binarySearchRecursive(array, left, mid - 1, target)

        # Else the element can only be present in the right subarray
        else:
            return binarySearchRecursive(array, mid + 1, right, target)
    else:
        return None
````

#### Linear Search

The most basic search. Start from the leftmost element of the array and one by one compare the target with each element 
of the array. If the target matches with an element, return the index.

```python
def linear_search(array, length, target):
    for index in range(0, length):
        if array[index] == target:
            return index
    return None
```

## Arrays

* [First Duplicate](#first-duplicate)
* [First Not Repeating Character](#first-not-repeating-character)
* [Make Array Consecutive](#make-array-consecutive)
* [Search Insert Position](#search-insert-position)

#### First Duplicate

Given an array a that contains only numbers in the range from 1 to a.length, find
the first duplicate number for which the second occurrence has the minimal index.
In other words, if there are more than 1 duplicated numbers, return the number for
which the second occurrence has a smaller index than the second occurrence of
the other number does. If there are no such elements, return -1.

```python
def firstDuplicate(a):
    uniqueSet = set()
    for value in a:
        if value in uniqueSet:
            return value
        else:
            uniqueSet.add(value)
    return -1
```

#### First Not Repeating Character

Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you
would be asked to do during a real interview.

Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character,
return '_'.


```python
def firstNotRepeatingCharacter(s):
    checkedChars = set() #skip characters we've already checked.
    for char in s:
        if char not in checkedChars and s.index(char) == s.rindex(char):
            return char
        checkedChars.add(char)
    return '_'
```

#### Make Array Consecutive

Find the number of elements that would need to be added so that each array value is separated by one.
`[1,2,3,5] -> 1 #4 needs to be added to the array`

```python
def makeArrayConsecutive(arr):
    length = len(arr)
    statuesNeeded = 0

    if length <= 1:
        return statuesNeeded

    sortedStatues = sorted(arr)
    print(sortedStatues)

    for i in range(1, length):
        statuesNeeded += (sortedStatues[i] - sortedStatues[i - 1]) - 1

    return statuesNeeded
``` 

#### Search Insert Position

[Leetcode: Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it 
would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: `[1,3,5,6], 5`
Output: `2`

```python
def searchInsert(nums, target):
    leftIndex = 0
    rightIndex = len(nums) - 1

    while leftIndex <= rightIndex:
        middle = int((leftIndex + rightIndex) / 2)

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            leftIndex = middle + 1
        else:
            rightIndex = middle - 1

    return leftIndex
```

## Integers

* [Palindrome Number](#palindrome-number)
* [Reverse Number](#reverse-number)
* [Two Sum](#two-sum)

#### Palindrome Number

[Leetcode: Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```python
def isPalindrome(x):
    num = str(x)
    return num == num[::-1]
```

#### Reverse Number

[Leetcode: Reverse Number](https://leetcode.com/problems/reverse-integer/description/)

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

```python
def reverse_number(number):
    reversed = int(str(abs(number))[::-1])

    if reversed > 2**31 - 1:
        return 0

    if number < 0:
        return -reversed
    return reversed
```

#### Two Sum

[Leetcode: Two Sum](https://leetcode.com/problems/two-sum/description/)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given `nums = [2, 7, 11, 15], target = 9`,

Because `nums[0] + nums[1] = 2 + 7 = 9`,
`return [0, 1]`.

Solution - O(N)
```python

def two_sum(array, target):
    complements = dict()

    for index, num in enumerate(array):
        complement = str(target - num)
        if complement in complements:
            return [index, complements[complement]]
        else:
            complements[str(num)] = index
    return [-1, -1]
```

Solution for sorted arrays - O(N)

```python

def two_sum_sorted(array, target):
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
 

## Matrices

* [Rotate Image 90 Degrees Clockwise](#rotate-image-90-degrees-clockwise)

#### Rotate Image 90 Degrees Clockwise

Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during
an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
```python
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
     
rotateImage(a) ==
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
``` 

```python
def rotateImage90degrees(a):
    size = len(a)
    layer_count = int(size / 2)

    for layer in range(0, layer_count):
        first = layer
        last = size - first - 1

        for element in range(first, last):
            offset = element - first

            top = a[first][element]
            right_side = a[element][last]
            bottom = a[last][last - offset]
            left_side = a[last - offset][first]

            a[first][element] = left_side
            a[element][last] = top
            a[last][last - offset] = right_side
            a[last - offset][first] = bottom
```

## Strings

* [Jewels and Stones](#jewels-and-stones)

#### Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have. You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so 
"a" is considered a different type of stone from "A".

Example 1:

Input: `J = "aA"`, `S = "aAAbbbb"`
Output: `3`

```python

def numJewelsInStones(J, S):
    stoneCount = dict()
    for stone in S:
        if stone in stoneCount:
            stoneCount[stone] += 1
        else:
            stoneCount[stone] = 1

    count = 0
    jSet = set(J)

    for jewel in jSet:
        if jewel in stoneCount:
            count += stoneCount[jewel]

    return count
```

## Trees

* [Binary Tree Path](#binary-tree-path)

#### Binary Tree Path

[Leetcode: Binary Tree Path](https://leetcode.com/problems/binary-tree-paths/description/)

Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:

Input:
```
   1
 /   \
2     3
 \
  5
```
Output: `["1->2->5", "1->3"]`

Explanation: All root-to-leaf paths are: `1->2->5`, `1->3`

```python
def binaryTreePaths(root):
    paths = []
    if not root:
        return paths
    getPath(root, '', paths)
    return paths

def getPath(node, path, paths):
    if not node.left and not node.right:
        paths.append(path + str(node.val))
    if node.left:
        getPath(node.left, path + str(node.val) + '->', paths)
    if node.right:
        getPath(node.right, path + str(node.val) + '->', paths)
```