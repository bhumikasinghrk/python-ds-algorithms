#  Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which
#  the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the
#  number for which the second occurrence has a smaller index than the second occurrence of the other number does. If
#  there are no such elements, return -1.
def firstDuplicate(array):
    uniqueSet = set()
    for value in array:
        if value in uniqueSet:
            return value
        else:
            uniqueSet.add(value)
    return -1

def test_first_duplicate():
    assert firstDuplicate([1,2,3]) == -1
    assert firstDuplicate([1,2,3,4,5,1]) == 1