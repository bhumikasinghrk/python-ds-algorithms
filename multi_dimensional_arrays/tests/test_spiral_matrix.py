from multi_dimensional_arrays.spiral_matrix import spiral_matrix


def test_spiral_matrix():
    matrix = [[2, 5, 8], [4, 0, -1]]
    assert spiral_matrix(matrix) == [2, 5, 8, -1, 0, 4]

    matrix = [[6], [9], [7]]
    assert spiral_matrix(matrix) == [6, 9, 7]

    matrix = [[6, 9, 7]]
    assert spiral_matrix(matrix) == [6, 9, 7]

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert spiral_matrix(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert spiral_matrix(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
