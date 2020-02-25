from data_structures.trie_hash_table import TrieHashTable


def test_trie_hash_table():
    trie = TrieHashTable()
    assert trie.insert('ab') is None
    assert not trie.search('a')
    assert trie.search('ab')
    assert trie.starts_with('a')
