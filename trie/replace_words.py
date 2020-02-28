from typing import Dict, List


def replace_words(dictionary: List[str], sentence: str) -> str:
    words = sentence.split(' ')
    updated_sentence: [str] = []
    prefix_trie = TrieNode()

    for word in dictionary:
        prefix_trie.insert(word)

    for word in words:
        updated_sentence.append(prefix_trie.replace_word(word))

    return ' '.join(updated_sentence)


class TrieNode:
    def __init__(self):
        self.nodes: Dict[str: TrieNode] = dict()

    def insert(self, word: str) -> None:
        current_node = self
        for index in range(1, len(word) + 1):
            if word[:index] in current_node.nodes:
                next_node = current_node.nodes.get(word[:index])
                if len(next_node.nodes) == 0:
                    return
                if index == len(word):
                    current_node.nodes[word[:index]] = TrieNode()
                    return
                current_node = next_node
            else:
                current_node.nodes.setdefault(word[:index], TrieNode())
                current_node = current_node.nodes.get(word[:index])

    def replace_word(self, word: str) -> str:
        current_node = self
        for index in range(1, len(word) + 1):
            if word[:index] in current_node.nodes:
                current_node = current_node.nodes.get(word[:index])
                if len(current_node.nodes) == 0:
                    return word[:index]
            else:
                return word
        return word
