from multi_dimensional_arrays.diagonal_traverse import diagonal_traverse


def test_diagonal_traverse():
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert diagonal_traverse(arr) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
    assert diagonal_traverse([]) == []
