# Trie

* [Map Sum](#map-sum)
* [Replace Words](#replace-words)

## Map Sum

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer
represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs'
value whose key starts with the prefix.

Example 1:

```text
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
```

```python
class MapSum:
    def __init__(self):
        self.value = 0
        self.head: MapSumNode = MapSumNode()

    def insert(self, key: str, val: int) -> None:
        current_node = self.head
        for index in range(1, len(key) + 1):
            if key[:index] in current_node.nodes:
                current_node = current_node.nodes.get(key[:index])
            else:
                current_node.nodes.setdefault(key[:index], MapSumNode())
                current_node = current_node.nodes.get(key[:index])
        current_node.value = val

    def sum(self, prefix: str) -> int:
        current_node = self.head
        # Find target node
        for index in range(1, len(prefix) + 1):
            if prefix[:index] in current_node.nodes:
                current_node = current_node.nodes.get(prefix[:index])
            else:
                return 0

        # sum child nodes
        return self.__recursive_sum(current_node)

    def __recursive_sum(self, parent_node) -> int:
        if len(parent_node.nodes) == 0:
            return parent_node.value

        total = parent_node.value

        for node in parent_node.nodes:
            total += self.__recursive_sum(parent_node.nodes.get(node))
        return total


class MapSumNode:
    def __init__(self, value: int = 0):
        self.value = value
        self.nodes: Dict[str: MapSumNode] = dict()
```

## Replace Words

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's
call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence
with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input:  `dict = ["cat", "bat", "rat"]`
        `sentence = "the cattle was rattled by the battery"`
Output: `"the cat was rat by the bat"`

```python
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
```