from arrays.find_max_consecutive_ones import find_max_consecutive_ones


def test_find_max_consecutive_ones():
    assert find_max_consecutive_ones([1, 0]) == 2
    assert find_max_consecutive_ones([0]) == 1
    assert find_max_consecutive_ones([1]) == 1
    assert find_max_consecutive_ones([1, 0, 1, 1, 0]) == 4
    assert find_max_consecutive_ones([1, 0, 1, 1, 1]) == 5
    assert find_max_consecutive_ones([0, 1, 1, 0, 1, 0]) == 4
