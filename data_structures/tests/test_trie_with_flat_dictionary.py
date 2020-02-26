from data_structures.trie_with_flat_dictionary import TrieWithFlatDictionary


def test_trie_with_flat_dictionary():
    trie = TrieWithFlatDictionary()
    assert trie.insert('ab') is None
    assert not trie.search('a')
    assert trie.search('ab')
    assert trie.starts_with('a')
