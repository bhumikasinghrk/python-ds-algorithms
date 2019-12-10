from algorithm_theory.binary_search import binary_search_iterative, binary_search_recursive


def test_binary_search_iterative():
    arr = [2, 5, 36, 40, 58]
    assert binary_search_iterative(arr, 40) == 3


def test_binary_search_recursive():
    arr = [2, 5, 36, 40, 58]
    assert binary_search_recursive(arr, 0, len(arr) - 1, 5) == 1
