# Python Data Structures and Algorithms [![Build Status](https://travis-ci.org/ahcode0919/python-ds-algorithms.svg?branch=master)](https://travis-ci.org/ahcode0919/python-ds-algorithms) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Various Data Structures and Algorithm Solutions in Python (3.x)

* [Arrays](#arrays)
* [Matrices](#matrices)

## Arrays

* [First Duplicate](#first-duplicate)
* [First Not Repeating Character](#first-not-repeating-character)
* [Make Array Consecutive](#make-array-consecutive)

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
