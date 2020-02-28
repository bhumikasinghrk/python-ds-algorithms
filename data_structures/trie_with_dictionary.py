from typing import Dict


class TrieWithDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_trie = self.head
        for index in range(1, len(word) + 1):
            if word[:index] in current_trie.child_nodes:
                current_trie = current_trie.child_nodes.get(word[:index])
            else:
                child_node = TrieNode()
                current_trie.child_nodes.setdefault(word[:index], child_node)
                current_trie = child_node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_trie = self.head
        for index in range(1, len(word) + 1):
            if word[:index] in current_trie.child_nodes:
                current_trie = current_trie.child_nodes.get(word[:index])
            else:
                return False
        return len(current_trie.child_nodes) == 0

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_trie = self.head
        for index in range(1, len(prefix) + 1):
            if prefix[:index] in current_trie.child_nodes:
                current_trie = current_trie.child_nodes.get(prefix[:index])
            else:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.child_nodes: Dict[str: TrieNode] = dict()
