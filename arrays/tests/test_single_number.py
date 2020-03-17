from arrays.single_number import single_number, single_number_bitwise


def test_single_number():
    assert single_number([1, 2, 2, 3, 3]) == 1
    assert single_number([1, 1]) == 0


def test_single_number_bitwise():
    assert single_number_bitwise([1, 2, 2, 3, 3]) == 1
    assert single_number_bitwise([1, 1]) == 0
