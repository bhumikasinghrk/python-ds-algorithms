# Python Data Structures and Algorithms [![Build Status](https://travis-ci.org/ahcode0919/python-ds-algorithms.svg?branch=master)](https://travis-ci.org/ahcode0919/python-ds-algorithms) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Various Data Structures and Algorithm Solutions in Python (3.x)

* [Algorithm Theory](#algorithm-theory)
    * [Searches](#searches)
        * [Binary Search](#binary-search)
        * [Jump Search](#jump-search)
        * [Linear Search](#linear-search)
    * [Sorts](#sorts)
        * [Bubble Sort](#bubble-sort)
* [Data Structures](#data-structures)
    * [Singly Linked List](#singly-linked-list)
* [Algorithms]()
    * [Arrays](#arrays)
    * [Integers](#integers)
    * [Matrices](#matrices)
    * [Strings](#strings)
    * [Trees](#trees)
* [Resources](#resources)

## Algorithm Theory

### Searches

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
        middle = int((left + right) / 2)

        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
    return None
```

Recursive Approach:

```python

def binarySearchRecursive(array, left, right, target):
    if right >= left:

        mid = int((left + right) / 2)

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
```

#### Jump Search

[Jump Search](https://www.geeksforgeeks.org/jump-search/) is a searching algorithm for sorted arrays. The basic idea is to check fewer elements (than linear search) 
by jumping ahead by fixed steps or skipping some elements in place of searching all elements.

For example, suppose we have an array arr[] of size n and block (to be jumped) size m. Then we search at the indexes
 arr[0], arr[m], arr[2m]…..arr[km] and so on. Once we find the interval (arr[km] < x < arr[(k+1)m]), we perform a linear
  search operation from the index km to find the element x.

What is the optimal block size to be skipped?
In the worst case, we have to do n/m jumps and if the last checked value is greater than the element to be searched for,
 we perform m-1 comparisons more for linear search. Therefore the total number of comparisons in the worst case will be 
 ((n/m) + m-1). The value of the function ((n/m) + m-1) will be minimum when m = √n. Therefore, the best step size is 
 m = √n. (Geeks For Geeks)

```python
def jump_search(array, target):
    length = len(array)
    interval = int(math.sqrt(length))
    index = interval - 1  # 0 Based
    previous = index

    while index <= length - 1:
        if array[index] == target:
            return index
        elif array[index] > target:
            return linear_search(array, previous, index - 1, target)
        else:
            previous = index
            index += interval

    return None
```

#### Linear Search

The most basic search. Start from the leftmost element of the array and one by one compare the target with each element 
of the array. If the target matches with an element, return the index.

```python
def linear_search(array, left, right, target):
    for index in range(left, right + 1):
        if array[index] == target:
            return index
    return None
```

### Sorts

#### Bubble Sort

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in 
wrong order.

Example: `[2, 1, 3] -> [1, 2, 3]`

```python
def bubble_sort(array):
    length = len(array)
    
    # Return if nothing to sort
    if length <= 1:
        return array

    # Reduce the upper limit with each iteration, since the correct value has 'bubbled' to the top
    for i in reversed(range(0, length)):
        swap = False
        # Compare value and switch up to the upper limit 'i'
        for j in range(0, i):
            next = j + 1
            if next < length and array[j] > array[next]:
                temp = array[j]
                array[j] = array[next]
                array[next] = temp
                swap = True

        # Return if no swaps take place
        if not swap:
            return array
    return array
```

## Data Structures

* [Singly Linked List](#singly-linked-list)
    
#### Singly Linked List

Wikipedia: Singly linked lists contain nodes which have a data field as well as 'next' field, which points to the next
node in line of nodes. Operations that can be performed on singly linked lists include insertion, deletion and
traversal.

Benefits:

* Dynamic data structure the can expand or shrink as needed
* Requires no extra space (memory efficient)
* Does not require a continuous block of memory like arrays

Drawbacks:

* Operations take O(N) time (Ex: Search)
* Tracking of pointers takes up additional memory


Node Implementation: 

```python
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
```

Singly Linked List Implementation:

```python
class SinglyLinkedList(object):
    _head = None

    def __init__(self, head: Node = None) -> None:
        if head:
            self._head = head

    def allvalues(self) -> []:
        values = []
        node = self._head

        while node:
            values.append(node.data)
            node = node.next_node

        return values

    # O(N)
    def append(self, node: Node) -> None:
        if not self._head:
            self._head = node
            return

        last_node = self._head

        while last_node:
            next_node = last_node.next_node

            if not next_node:
                break
            last_node = next_node

        last_node.next_node = node

    # O(N)
    def get(self, index: int = None) -> Node:
        if not index and not self._head:  # No index and head is null
            return None
        elif not index and self._head:    # No index but head is present
            return self._head
        elif index:                       # Index provided
            count = 0
            current_node = self._head

            while current_node:
                next_node = current_node.next_node
                count += 1

                if next_node and count == index:
                    return next_node
                if next_node:
                    current_node = next_node
                    continue
                break

        return None                       # Index not valid, return None

    # O(N)
    def insert(self, node: Node, index: int = None) -> bool:
        success = False

        if not index or index == 0:
            if not self._head:
                self._head = node
            else:
                node.next_node = self._head
                self._head = node
            success = True
        else:
            previous_node = self.get(index - 1)
            insert_node = previous_node.next_node

            if previous_node:
                node.next_node = insert_node
                previous_node.next_node = node
                success = True

        return success

    # O(N)
    def remove(self, index: int) -> Node:
        node = None

        if index == 0:
            if self._head:
                node = self._head
                self._head = self._head.next_node
        else:
            previous_node = self.get(index - 1)
            node = previous_node.next_node

            # If node_to_remove is not present the index was invalid and we can return False
            if previous_node and node:
                previous_node.next_node = node.next_node
        return node

    # O(N)
    def size(self) -> int:
        count = 0
        node = self._head

        while node:
            count += 1
            node = node.next_node

        return count
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

First Duplicate w/ Set

```python
def first_duplicate(a):
    uniqueset = set()
    for value in a:
        if value in uniqueset:
            return value
        else:
            uniqueset.add(value)
    return -1
```

First Duplicate (In-Place)

```python
def first_duplicate_in_place(array):
    while len(array) > 0:
        value = array.pop(0)
        if value in array:
            return value
    return -1
```

#### First Not Repeating Character

Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you
would be asked to do during a real interview.

Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character,
return '_'.

With Set:

```python
def first_not_repeating_character(s):
    checkedChars = set() #skip characters we've already checked.
    for char in s:
        if char not in checkedChars and s.index(char) == s.rindex(char):
            return char
        checkedChars.add(char)
    return '_'
```

With Array Slices (less optimal):

```python
def first_not_repeating_character(s):
    length = len(s)
    index = 0
    while index < length:
        if s[index] not in s[:index] and s[index] not in s[index + 1:]:
            return s[index]
        index += 1
    return '_'
```

#### Make Array Consecutive

Find the number of elements that would need to be added so that each array value is separated by one.

`[1,2,3,5] -> 1 #4 needs to be added to the array`

```python
def make_array_consecutive(arr):
    length = len(arr)
    statuesneeded = 0

    if length <= 1:
        return statuesneeded

    sortedstatues = sorted(arr)

    for i in range(1, length):
        statuesneeded += (sortedstatues[i] - sortedstatues[i - 1]) - 1

    return statuesneeded
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
def search_insert(nums, target):
    leftindex = 0
    rightindex = len(nums) - 1

    while leftindex <= rightindex:
        middle = int((leftindex + rightindex) / 2)

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            leftindex = middle + 1
        else:
            rightindex = middle - 1

    return leftindex
```

## Integers

* [Palindrome Number](#palindrome-number)
* [Reverse Number](#reverse-number)
* [Two Sum](#two-sum)

#### Palindrome Number

[Leetcode: Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1: `121` -> `true`

Example 2: `-121` -> `false`

Explanation: From left to right, it reads `-121`. From right to left, it becomes `121-`. Therefore it is not a palindrome.

```python
def isPalindrome(x):
    num = str(x)
    return num == num[::-1]
```

#### Reverse Number

[Leetcode: Reverse Number](https://leetcode.com/problems/reverse-integer/description/)

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: `123`

Output: `321`

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

Because `nums[0] + nums[1] = 2 + 7 = 9`, `return [0, 1]`.

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

## Resources

* [Geeks For Geeks](https://www.geeksforgeeks.org/)
* [Leetcode](https://www.leetcode.com)