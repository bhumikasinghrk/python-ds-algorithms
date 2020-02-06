from multi_dimensional_arrays.pascals_triangle import pascals_triangle


def test_pascals_triangle():
    assert pascals_triangle(0) == []

    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascals_triangle(5) == expected
