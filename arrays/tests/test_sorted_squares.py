from arrays.sorted_squares import sorted_squares


def test_sorted_squares():
    assert sorted_squares([1, 2, 3]) == [1, 4, 9]
    assert sorted_squares([-3, -2, -1]) == [1, 4, 9]
    assert sorted_squares([]) == []
    assert sorted_squares([-1, 1]) == [1, 1]
    assert sorted_squares([-2, -1, 0, 1, 3]) == [0, 1, 1, 4, 9]
