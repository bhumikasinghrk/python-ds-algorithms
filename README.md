# Python Data Structures and Algorithms [![Build Status](https://travis-ci.org/ahcode0919/python-ds-algorithms.svg?branch=master)](https://travis-ci.org/ahcode0919/python-ds-algorithms) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Various Data Structures and Algorithm Solutions in Python (3.x). Succint Python one-liners are avoided in most solutions
prevent obscuring the function and logic of the algorithms / data-structures.  

* [Algorithm Theory](#algorithm-theory)
    * [Searches](#searches)
        * [Binary Search](#binary-search)
        * [Jump Search](#jump-search)
        * [Linear Search](#linear-search)
    * [Sorts](#sorts)
        * [Bubble Sort](#bubble-sort)
* [Data Structures](#data-structures)
    * [Singly Linked List](#singly-linked-list)
    * [Doubly Linked List](#doubly-linked-list)
    * [Circularly Linked List (WIP)](#)
* [Algorithms](#algorithms)
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
def binary_search_iterative(array: [int], target: int) -> Optional[int]:
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

def binary_search_recursive(array: [int], left: int, right: int, target: int) -> Optional[int]:
    if right >= left:

        mid = int((left + right) / 2)

        # If element is present at the middle
        if array[mid] == target:
            return mid

        # If element is smaller than mid, then it can only be present in left subarray
        elif array[mid] > target:
            return binary_search_recursive(array, left, mid - 1, target)

        # Else the element can only be present in the right subarray
        else:
            return binary_search_recursive(array, mid + 1, right, target)
    else:
        return None
```

#### Jump Search

[Jump Search](https://www.geeksforgeeks.org/jump-search/) is a searching algorithm for sorted arrays. The basic idea is 
to check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of 
searching all elements.

For example, suppose we have an array arr[] of size n and block (to be jumped) size `m`. Then we search at the indexes
`arr[0]`, `arr[m]`, `arr[2m]…..arr[km]`, and so on. Once we find the interval (`arr[km] < x < arr[(k+1)m]`), we perform
a linear search operation from the index `km` to find the element `x`.

What is the optimal block size to be skipped?
In the worst case, we have to do `n/m` jumps and if the last checked value is greater than the element to be searched 
for, we perform `m-1` comparisons more for linear search. Therefore the total number of comparisons in the worst case 
will be `((n/m) + m-1)`. The value of the function `((n/m) + m-1)` will be minimum when `m = √n`. Therefore, the best 
step size is `m = √n`. (Geeks For Geeks)

```python
def jump_search(array: [int], target: int) -> Optional[int]:
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
def linear_search(array: [int], left: int, right: int, target: int) -> Optional[int]:
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
def bubble_sort(array: [int]) -> [int]:
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
* [Doubly Linked List](#doubly-linked-list)
* [Circularly Linked List](#circularly-linked-list)

#### Singly Linked List

[Wikipedia - Linked Lists](https://en.wikipedia.org/wiki/Linked_list): Singly linked lists contain nodes which have a 
data field as well as 'next' field, which points to the next node in line of nodes. Operations that can be performed on 
singly linked lists include insertion, deletion and traversal.

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
    def get(self, index: int) -> Optional[int]:
        if not self._head:  # No index and head is null
            return None
        node = self.get_node(index)
        if node:
            return node.data
        return None

    # O(N)
    def get_node(self, index: int) -> Optional[Node]:
        if not self._head:  # No index and head is null
            return None
        count = 0
        current_node = self._head

        while current_node:
            if count == index:
                return current_node
            current_node = current_node.next_node
            count += 1
        return None

    # O(N)
    def insert(self, node: Node, index: int) -> None:
        # None --> Node
        if not self._head:
            self._head = node
        # Head -> .... --> Node -> Head -> ....
        elif index == 0:
            node.next_node = self._head
            self._head = node
        # Previous -> Next --> Previous -> Node -> Next
        else:
            previous_node = self.get_node(index - 1)
            if not previous_node:
                raise IndexError("Index out of bounds")
            node.next_node = previous_node.next_node
            previous_node.next_node = node

    # O(N)
    def remove(self, index: int) -> Optional[int]:
        value = None

        if index == 0 and self._head:
            value = self._head.data
            self._head = self._head.next_node
        else:
            previous_node = self.get_node(index - 1)
            if previous_node and previous_node.next_node:
                value = previous_node.next_node.data
                previous_node.next_node = previous_node.next_node.next_node
        return value

    # O(N)
    def size(self) -> int:
        count = 0
        node = self._head

        while node:
            count += 1
            node = node.next_node
        return count
```

#### Doubly Linked List

[Wikipedia: Doubly Linked List](https://en.wikipedia.org/wiki/Doubly_linked_list): In a 'doubly linked list', each node 
contains, besides the next-node link, a second link field pointing to the 'previous' node in the sequence.

Doubly Linked List Node:

```python
class Node:
    def __init__(self, data=None, previous_node=None, next_node=None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node
```

Implementation:

```python
class DoublyLinkedList(object):

    def __init__(self) -> None:
        self._head = Node()
        self._tail = Node()

        self._head.next_node = self._tail
        self._tail.previous_node = self._head

    # O(1)
    def append(self, node: Node) -> None:
        last_node = self._tail.previous_node
        # Last <-> Tail --> Last <-> New <-> Tail

        # Link the new node to the original last node and the tail
        last_node.next_node = node
        node.previous_node = last_node

        # Point the tail to the new last node
        node.next_node = self._tail
        self._tail.previous_node = node

    # O(N)
    def get_node(self, index: int) -> Optional[Node]:
        current_node = self._head.next_node
        if current_node == self._tail:  # empty list
            return None

        count = 0

        while current_node:
            if count == index:
                return current_node
            current_node = current_node.next_node
            count += 1
        return None

    # O(N)
    def get_value(self, index: int) -> Optional[int]:
        node = self.get_node(index)
        if node:
            return node.data
        return None

    # O(N)
    def insert(self, node: Node, index: int) -> None:
        original_node = self._tail

        if index != 0 or self._head.next_node != self._tail:  # empty list
            original_node = self.get_node(index)

        if not original_node:
            raise IndexError("Node not present at index")

        previous_node = original_node.previous_node
        # Previous <-> Original --> Previous <-> New <-> Original
        previous_node.next_node = node      # previous node points to the new node
        node.previous_node = previous_node  # previous node is new node's previous node
        node.next_node = original_node      # new node's next node is the original node
        original_node.previous = node       # original node's previous node is the new node

    # O(N)
    def remove(self, index: int) -> Optional[int]:
        node = self.get_node(index)
        if not node:
            return None  # Could also raise an exception

        previous_node = node.previous_node
        next_node = node.next_node

        # Previous <-> Node <-> Next --> Previous <-> Next
        previous_node.next_node = next_node
        next_node.previous_node = previous_node

        return node.data

    # O(N)
    def size(self) -> int:
        count = 0
        node = self._head.next_node

        while node != self._tail:
            count += 1
            node = node.next_node
        return count
```

#### Circularly Linked List

[Wikipedia: Doubly Linked List](https://en.wikipedia.org/wiki/Doubly_linked_list) In the last node of a list, the link 
field often contains a null reference, a special value used to indicate the lack of further nodes. A less common 
convention is to make it point to the first node of the list; in that case the list is said to be 'circular' or 
'circularly linked'; otherwise it is said to be 'open' or 'linear'. It is a list where the last pointer points 
to the first node.

This is more of an example. It can be optimized in a variety of ways depending on its intended usage.

```python
from data_structures.singlylinkedlist import Node


class CircularlyLinkedList(object):
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next_node = self._head

    @property
    def head(self) -> Node:
        return self._head

    @head.setter
    def head(self, node: Node):
        self._head = node
        if node:
            node.next_node = self._head

    def all_values(self) -> []:
        values = []
        node = self.head

        while node:
            values.append(node.data)
            node = node.next_node
            if node == self.head:
                break
        return values

    def append(self, node: Node):
        previous_node = self.head

        if not previous_node:
            self.head = node
            node.next_node = self.head
            return

        while previous_node.next_node != self.head:
            previous_node = previous_node.next_node

        next_node = previous_node.next_node
        previous_node.next_node = node
        node.next_node = next_node

    def remove(self, index: int):
        previous_node = self.head

        if not previous_node:
            raise IndexError("List is empty")

        if previous_node.next_node == self.head:
            self.head = None
            return

        if index == 0:
            previous_node.next_node = self.head.next_node
            self.head = previous_node.next_node
            return

        list_index = 1
        while previous_node.next_node is not self.head and list_index < index:
            previous_node = previous_node.next_node
            list_index += 1

        if list_index == index:
            next_node = previous_node.next_node
            previous_node.next_node = next_node.next_node
        else:
            raise IndexError

    def size(self) -> int:
        count = 0
        if not self.head:
            return count

        count += 1
        node = self.head.next_node

        while node and node != self.head:
            count += 1
            node = node.next_node
        return count
```

#### Binary Tree

A Binary tree is a non-linear tree data structure with one "root" node. Each node has only two child nodes. These are
donated "left" and "right".

Further Reading - [Wikipedia: Binary Tree](https://en.wikipedia.org/wiki/Binary_tree)

```text
     Root
      / \
     L   R
    / \
   L   R
```

Binary Tree Node

```python
class BinaryTreeNode:

    def __init__(self, data, left_node=None, right_node=None):
        self._data = data
        self._left_node = left_node
        self._right_node = right_node
        
     # ... Getters and Setters #
```

Binary Tree

```python
class BinaryTree(object):

    def __init__(self, root: BinaryTreeNode = None):
        self._root = root

    @property
    def root(self) -> BinaryTreeNode:
        return self._root

    @root.setter
    def root(self, root: BinaryTreeNode):
        self._root = root
```
 
## Algorithms

### Arrays

* [First Duplicate](#first-duplicate)
* [First Not Repeating Character](#first-not-repeating-character)
* [Make Array Consecutive](#make-array-consecutive)
* [Search Insert Position](#search-insert-position)

#### First Duplicate

Given an array a that contains only numbers in the range from `1` to `a.length`, find
the first duplicate number for which the second occurrence has the minimal index.
In other words, if there are more than 1 duplicated numbers, return the number for
which the second occurrence has a smaller index than the second occurrence of
the other number does. If there are no such elements, return `-1`.

First Duplicate w/ Set

```python
def first_duplicate(a: [int]) -> int:
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
def first_duplicate_in_place(array: [int]) -> int:
    while len(array) > 0:
        value = array.pop(0)
        if value in array:
            return value
    return -1
```

#### First Not Repeating Character

Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you
would be asked to do during a real interview.

Given a string `s`, find and return the first instance of a non-repeating character in it. If there is no such 
character, return `_`.

With Set:

```python
def first_not_repeating_character(s: str) -> str:
    checkedChars = set() #skip characters we've already checked.
    for char in s:
        if char not in checkedChars and s.index(char) == s.rindex(char):
            return char
        checkedChars.add(char)
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

#### Make Array Consecutive

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

#### Search Insert Position

[Leetcode: Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it 
would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: `[1,3,5,6], 5`
Output: `2`

```python
def search_insert(nums: [int], target: int) -> int:
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

### Integers

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
def is_palindrome(x: int) -> bool:
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
def reverse_number(number: int) -> int:
    reversed_number = int(str(abs(number))[::-1])

    if reversed_number > 2**31 - 1:  # Check for integer overflow (per question)
        return 0

    if number < 0:
        return -reversed_number
    return reversed_number
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
def two_sum(array: [], target: int) -> []:
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
 

###Matrices

* [Rotate Image 90 Degrees Clockwise](#rotate-image-90-degrees-clockwise)

#### Rotate Image 90 Degrees Clockwise

Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during
an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Input:
```python
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
```

Output:
```python
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
```     

```python
def rotate_image_90_degrees(a: [[int]]) -> [[int]]:
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
    return a
```

### Strings

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
def jewels_and_stones(jewels: str, stones: str) -> int:
    stonecount = dict()
    
    for stone in stones:
        if stone in stonecount:
            stonecount[stone] += 1
        else:
            stonecount[stone] = 1

    count = 0
    jset = set(jewels)

    for jewel in jset:
        if jewel in stonecount:
            count += stonecount[jewel]

    return count
```

### Trees

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
def binary_tree_paths(root_node: TreeNode) -> str:
    paths = []
    if not root_node:
        return paths
    get_path(root_node, '', paths)
    return paths

def get_path(node: TreeNode, path: str, paths: []) -> str:
    if not node.left and not node.right:
        paths.append(path + str(node.val))
        return
    if node.left:
        get_path(node.left, path + str(node.val) + '->', paths)
    if node.right:
        get_path(node.right, path + str(node.val) + '->', paths)
```

## Resources

* [Code Signal](https://codesignal.com)
* [Geeks For Geeks](https://www.geeksforgeeks.org/)
* [Hackerrank](https://www.hackerrank.com/)
* [Leetcode](https://www.leetcode.com)