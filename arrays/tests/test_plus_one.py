from arrays.plus_one import plus_one


def test_plus_one():
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([0]) == [1]
    assert plus_one([9, 9]) == [1, 0, 0]
