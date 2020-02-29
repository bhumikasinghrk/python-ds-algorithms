from typing import Dict, List

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.ranks: Dict[str: int] = dict()
        self.head = TrieNode()

        for index, sentence in enumerate(sentences):
            self.head.insert(sentence)
            self.ranks.setdefault(sentence, times[index])

    def input(self, search: str) -> List[str]:
        # find all matching strings
        matches = []
        parent_node = self.head

        # find parent node
        for index in range(1, len(search) + 1):
            if search[:index] in parent_node.nodes:
                parent_node = parent_node.nodes.get(search[:index])

        matches.extend(self.__child_strings(parent_node))

        # find top 3 by times
        # update times
        return matches

    def __child_strings(self, parent_node: TrieNode) -> List[str]:
        child_strings = []
        if len(parent_node.nodes) == 0:
            child_strings.append(parent_node)

        for key in parent_node.nodes:
            child_strings.append(self.__child_strings(parent_node.nodes.get(key)))

        return child_strings


class TrieNode:
    def __init__(self):
        self.nodes: Dict[str: TrieNode] = dict()
        self.times = 0

    def insert(self, sentence, times):
        node = self
        for index in range(1, len(sentence) + 1):
            if sentence[:index] in node.nodes:
                node = node.nodes.get(sentence[:index])
            else:
                node.nodes.setdefault(sentence[:index], TrieNode())
                node = node.nodes.get(sentence[:index])
        node.times = times

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)