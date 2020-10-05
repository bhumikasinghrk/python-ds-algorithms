from arrays.sort_by_parity import sort_by_parity


def test_sort_by_parity():
    assert sort_by_parity([1]) == [1]
    assert sort_by_parity([2]) == [2]
    assert sort_by_parity([1, 2]) == [2, 1]
    assert sort_by_parity([2, 4, 3, 1, 5, 6, 7, 8]) == [2, 4, 8, 6, 5, 1, 7, 3]
