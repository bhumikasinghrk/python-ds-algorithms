from arrays.check_double import check_double


def test_check_double():
    assert check_double([10, 3, 5, 2, 1])
    assert check_double([0, 0])
    assert not check_double([1, 1])
