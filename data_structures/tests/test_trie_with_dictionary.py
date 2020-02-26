from data_structures.trie_with_dictionary import TrieWithDictionary


def test_trie_with_dictionary():
    trie = TrieWithDictionary()
    assert trie.insert('ab') is None
    assert not trie.search('a')
    assert trie.search('ab')
    assert trie.starts_with('a')
