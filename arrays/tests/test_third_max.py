from arrays.third_max import third_max


def test_third_max():
    assert third_max([3, 2, 1]) == 1
    assert third_max([3, 20]) == 20
    assert third_max([2, 3, 3, 5, 7, 9]) == 5
    assert third_max([2, 2, 3, 4]) == 2
