# Algorithm Theory

Collection of fundamental CS algorithm approaches

## Searches

### Binary Search

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

        # If element is smaller than mid, then it can only be present in left sub-array
        elif array[mid] > target:
            return binary_search_recursive(array, left, mid - 1, target)

        # Else the element can only be present in the right sub-array
        else:
            return binary_search_recursive(array, mid + 1, right, target)
    else:
        return None
```

### Jump Search

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

### Linear Search

The most basic search. Start from the leftmost element of the array and one by one compare the target with each element 
of the array. If the target matches with an element, return the index.

```python
def linear_search(array: [int], left: int, right: int, target: int) -> Optional[int]:
    for index in range(left, right + 1):
        if array[index] == target:
            return index
    return None
```

## Sorts

### Bubble Sort

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
            next_val = j + 1
            if next_val < length and array[j] > array[next_val]:
                temp = array[j]
                array[j] = array[next_val]
                array[next_val] = temp
                swap = True

        # Return if no swaps take place
        if not swap:
            return array
    return array
```
