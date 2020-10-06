from arrays.find_disappeared_numbers import find_disappeared_numbers, find_disappeared_numbers_ii


def test_find_disappeared_numbers():
    assert find_disappeared_numbers([1, 2, 3]) == []
    assert find_disappeared_numbers([1, 2, 2, 4, 4]) == [3, 5]
    assert find_disappeared_numbers([5, 2, 4, 4, 3, 6, 8, 8]) == [1, 7]


def test_find_disappeared_numbers_ii():
    assert find_disappeared_numbers_ii([1, 2, 3]) == []
    assert find_disappeared_numbers_ii([1, 2, 2, 4, 4]) == [3, 5]
    assert find_disappeared_numbers_ii([5, 2, 4, 4, 3, 6, 8, 8]) == [1, 7]
