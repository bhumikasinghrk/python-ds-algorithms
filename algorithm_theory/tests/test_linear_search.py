from algorithm_theory.linear_search import linear_search


def test_linear_search():
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 0, 4, 4) == 3
