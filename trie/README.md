# Trie

* [Design Search Autocomplete System](#design-search-autocomplete-system)
* [Map Sum](#map-sum)
* [Replace Words](#replace-words)

## Design Search Autocomplete System

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a
special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences
that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences
have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is
a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your
system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case
letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be
recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of
sentence already typed.

 
Example:


Operation: `AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])`
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times

Now, the user begins another search:

Operation: `input('i')`
Output: `["i love you", "island","i love leetcode"]`
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since
`' '` has ASCII code 32 and `'r'` has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only
need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: `input(' ')`
Output: `["i love you","i love leetcode"]`
Explanation: There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation: There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation: The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the
following input will be counted as a new search.

 
Note:

The input sentence will always start with a letter and end with '#', and only one blank space will exist between two
words. The number of complete sentences that to be searched won't exceed 100. The length of each sentence including
those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are
persisted across multiple test cases. Please see here for more details.

```python

```

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
