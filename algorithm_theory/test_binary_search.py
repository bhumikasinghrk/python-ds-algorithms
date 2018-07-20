# Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval
# covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow
# the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or
# the interval is empty.


def binarySearchIterative(array, target):
    start = 0
    end = len(array)

    while start <= end:
        middle = int((end - start) / 2)
        if array[middle] < target:
            start += 1
        elif array[middle] > target:
            end -= 1
        else:
            return None

def binarySearchRecursive(array, left, right, target):
    if right >= left:

        mid = int((right - left) / 2)

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

def test_binarySearchIterative():
    a = [9,8,7,6,5,4,3,2,1]
    assert binarySearchIterative(a, 3) == 6

def test_binarySearchRecursive():
    a = [9,8,7,6,5,4,3,2,1]
    assert binarySearchRecursive(a, 0, len(a), 3) == 6