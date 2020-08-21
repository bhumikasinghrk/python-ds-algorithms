from arrays.max_consecutive_ones import max_consecutive_ones


def test_max_consecutive_ones():
    assert max_consecutive_ones([1, 1]) == 2
    assert max_consecutive_ones([1, 1, 0, 1, 1, 1]) == 3
    assert max_consecutive_ones([1, 1, 0, 0, 1, 1]) == 2
    assert max_consecutive_ones([0, 1, 1, 1, 1,  0, 1, 1, 1, 0]) == 4
