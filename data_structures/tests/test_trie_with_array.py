from data_structures.trie_with_array import TrieWithArray


def test_trie_with_array():
    trie = TrieWithArray()
    assert trie.insert('ab') is None
    assert not trie.search('a')
    assert trie.search('ab')
    assert trie.starts_with('a')
