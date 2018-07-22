from algorithm_theory.binary_search import *

def binary_search_iterative():
    a = [2, 5, 36, 40, 58]
    assert binary_search_iterative(a, 40) == 3

def test_binarySearchRecursive():
    a = [2, 5, 36, 40, 58]
    assert binary_search_recursive(a, 0, len(a) - 1, 5) == 1