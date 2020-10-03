from arrays.valid_mountain_array import valid_mountain_array


def test_valid_mountain_array():
    assert valid_mountain_array([1, 2, 1])
    assert valid_mountain_array([1, 2, 3, 4, 3])
    assert not valid_mountain_array([5, 2])
    assert not valid_mountain_array([1, 2, 3, 4])
    assert not valid_mountain_array([3, 2, 1, 0])
    assert not valid_mountain_array([1])
