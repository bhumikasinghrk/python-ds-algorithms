from typing import Generic, TypeVar

T = TypeVar('T')


class TrieHashTable(Generic[T]):
    """
    O(1) for accessing elements
    O(M * N) - Because multiple values of a key must be tracked (plus their associated True/False values)
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        for index in range(1, len(word)):
            if self.nodes.get(word[0:index]) is None:
                self.nodes[word[0:index]] = False
        self.nodes[word] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.nodes.get(word) is True

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.nodes.get(prefix) is not None
