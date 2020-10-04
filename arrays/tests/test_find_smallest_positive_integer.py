from arrays.find_smallest_positive_integer import find_smallest_positive_integer


def test_find_smallest_positive_integer():
    assert find_smallest_positive_integer([1, 2, 3]) == 1
    assert find_smallest_positive_integer([-1, -2, -3]) == 0
    assert find_smallest_positive_integer([1, 1, 1]) == 1
    assert find_smallest_positive_integer([3, 2, 1]) == 1
    assert find_smallest_positive_integer([1, -2, 3]) == 1
    assert find_smallest_positive_integer([4, 0, 1, 2, 3]) == 1
