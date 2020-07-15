from arrays.rotate_array import rotate_array_with_array


def test_rotate_array_with_array():
    nums = [1, 2, 3, 4, 5, 6, 7]
    assert rotate_array_with_array(nums, 3) == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    assert rotate_array_with_array(nums, 2) == [3, 99, -1, -100]
