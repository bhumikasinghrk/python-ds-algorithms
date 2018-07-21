from algorithm_theory.jump_search import jump_search

def test_jump_search():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert jump_search(a, 8) == 7

    a = [1]
    assert jump_search(a, 5) == None

    a = [1, 2, 3, 4, 5]
    assert jump_search(a, 2) == 1