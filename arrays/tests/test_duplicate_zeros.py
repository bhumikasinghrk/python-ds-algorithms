from arrays.duplicate_zeros import duplicate_zeros


def test_duplicate_zeros():
    assert duplicate_zeros([1, 2, 3]) == [1, 2, 3]
    assert duplicate_zeros([1, 0]) == [1, 0]
    assert duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 6]) == [1, 0, 0, 2, 3, 0, 0, 4]
    assert duplicate_zeros([0]) == [0]
