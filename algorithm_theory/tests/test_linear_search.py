from algorithm_theory.linear_search import linear_search


def test_linear_search():
    a = [1, 2, 3, 4, 5]
    assert linear_search(a, 0, 4, 4) == 3
