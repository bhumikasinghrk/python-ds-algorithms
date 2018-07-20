from algorithm_theory.binary_search import *

def test_binarySearchIterative():
    a = [2, 5, 36, 40, 58]
    assert binarySearchIterative(a, 40) == 3

def test_binarySearchRecursive():
    a = [2, 5, 36, 40, 58]
    assert binarySearchRecursive(a, 0, len(a) - 1, 5) == 1

test_binarySearchIterative()
test_binarySearchRecursive()