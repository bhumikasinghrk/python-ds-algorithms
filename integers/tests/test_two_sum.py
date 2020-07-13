from integers.two_sum import two_sum, two_sum_sorted


def test_two_sum():
    arr = [2, 15, 7, 32]
    assert two_sum(arr, 9) == [0, 2]


def test_two_sum_sorted():
    arr = [2, 7, 11, 15]
    assert two_sum_sorted(arr, 9) == [0, 1]
