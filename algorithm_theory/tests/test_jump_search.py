from algorithm_theory.jump_search import jump_search


def test_jump_search():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert jump_search(arr, 8) == 7

    arr = [1]
    assert jump_search(arr, 5) is None

    arr = [1, 2, 3, 4, 5]
    assert jump_search(arr, 2) == 1
