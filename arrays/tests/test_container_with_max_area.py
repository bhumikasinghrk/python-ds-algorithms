from arrays.container_with_max_area import container_with_max_area


def test_container_with_max_area():
    assert container_with_max_area([1, 2, 3, 4]) == 4
    assert container_with_max_area([3, 3]) == 3
    assert container_with_max_area([]) == 0
    assert container_with_max_area([1]) == 0
    assert container_with_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
