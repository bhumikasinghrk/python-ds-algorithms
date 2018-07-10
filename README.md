# Python Data Structures and Algorithms [![Build Status](https://travis-ci.org/ahcode0919/python-ds-algorithms.svg?branch=master)](https://travis-ci.org/ahcode0919/python-ds-algorithms) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Various Data Structures and Algorithm Solutions in Python (3.x)

[Arrays](#arrays)

## Arrays

* [First Duplicate](#firstduplicate)

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
