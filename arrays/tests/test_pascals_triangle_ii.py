from arrays.pascals_triangle_ii import pascals_triangle_ii


def test_pascals_triangle_ii():
    assert pascals_triangle_ii(0) == [1]
    assert pascals_triangle_ii(1) == [1, 1]
    assert pascals_triangle_ii(2) == [1, 2, 1]
    assert pascals_triangle_ii(3) == [1, 3, 3, 1]
    assert pascals_triangle_ii(4) == [1, 4, 6, 4, 1]
