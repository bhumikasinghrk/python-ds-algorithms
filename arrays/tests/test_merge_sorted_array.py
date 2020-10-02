from arrays.merge_sorted_array import merge_sorted_array


def test_merge_sorted_array():
    assert merge_sorted_array([2, 0], 1, [1], 1) == [1, 2]
    assert merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 4, 5], 3) == [1, 2, 2, 3, 4, 5]
    assert merge_sorted_array([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3) == [1, 2, 3, 4, 5, 6]
