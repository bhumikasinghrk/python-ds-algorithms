# Python Data Structures and Algorithms

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
