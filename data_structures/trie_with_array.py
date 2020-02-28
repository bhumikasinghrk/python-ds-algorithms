from typing import List, Optional


class TrieWithArray:
    def __init__(self):
        self.head: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_trie = self.head
        for index in range(1, len(word) + 1):
            node_index = ord(word[:index][-1]) - ord('a')
            if current_trie.child_nodes[node_index]:
                current_trie = current_trie.child_nodes[node_index]
            else:
                current_trie.child_nodes[node_index] = TrieNode()
                current_trie = current_trie.child_nodes[node_index]

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        """
        current_trie = self.head
        for index in range(1, len(word) + 1):
            node_index = ord(word[:index][-1]) - ord('a')
            if current_trie.child_nodes[node_index]:
                current_trie = current_trie.child_nodes[node_index]
            else:
                return False
        return current_trie.child_nodes == [None] * 26

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        current_trie = self.head
        for index in range(1, len(prefix) + 1):
            node_index = ord(prefix[:index][-1]) - ord('a')
            if current_trie.child_nodes[node_index]:
                current_trie = current_trie.child_nodes[node_index]
            else:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.child_nodes: List[Optional[TrieNode]] = [None] * 26
