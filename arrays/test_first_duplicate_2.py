#  Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number.
#  In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has
#  a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

def firstDuplicateInPlace(array):
    while len(array) > 0:
        value = array.pop(0)
        if value in array:
            return value
    return -1


def test_first_duplicate_in_place():
    assert firstDuplicateInPlace([1, 2, 3]) == -1
    assert firstDuplicateInPlace([1, 2, 3, 4, 5, 1]) == 1