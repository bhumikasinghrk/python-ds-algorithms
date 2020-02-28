from trie.map_sum import MapSum


def test_map_sum():
    map_sum = MapSum()
    assert map_sum.insert('apple', 3) is None
    assert map_sum.sum('ap') == 3
    assert map_sum.sum('apples') == 0
    assert map_sum.insert('app', 2) is None
    assert map_sum.sum('ap') == 5
