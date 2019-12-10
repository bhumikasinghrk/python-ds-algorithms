from arrays.find_pivot_index import find_pivot_index


def test_find_pivot_index():
    assert find_pivot_index([]) == -1
    assert find_pivot_index([1]) == 0
    assert find_pivot_index([1, 1]) == -1
    assert find_pivot_index([1, 2, 3]) == -1
    assert find_pivot_index([1, 7, 3, 6, 5, 6]) == 3
