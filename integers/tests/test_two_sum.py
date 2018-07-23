from integers.two_sum import two_sum, two_sum_sorted


def test_two_sum():
    a = [2, 15, 7, 32]
    assert two_sum(a, 9) == [2, 0]


def test_two_sum_sorted():
    a = [2, 7, 11, 15]
    assert two_sum_sorted(a, 9) == [0, 1]
