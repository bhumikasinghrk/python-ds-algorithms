from arrays.two_sum import two_sum


def test_two_sum():
    assert two_sum([2, 15, 7, 32], 9) == [0, 2]
    assert two_sum([-1, 0], -1) == [0, 1]
