from arrays.minimum_subarray_length import minimum_subarray_length


def test_minimum_subarray_length():
    assert minimum_subarray_length(11, [1, 2, 3, 4, 5]) == 3
    assert minimum_subarray_length(3, [1, 2, 3]) == 1
    assert minimum_subarray_length(3, [1, 2]) == 2
    assert minimum_subarray_length(14, [2, 4, 6, 8]) == 2
