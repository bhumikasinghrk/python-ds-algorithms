# Data Structures

* [Singly Linked List](#singly-linked-list)
* [Doubly Linked List](#doubly-linked-list)
* [Circularly Linked List](#circularly-linked-list)
* [Binary Tree](#binary-tree)
* [Queues](#queue)
* [Stack](#stack)
* [Trie](#trie)

## Singly Linked List

[Wikipedia - Linked Lists](https://en.wikipedia.org/wiki/Linked_list): Singly linked lists contain nodes which have a 
data field as well as 'next' field, which points to the next node in line of nodes. Operations that can be performed on 
singly linked lists include insertion, deletion and traversal.

Benefits:

* Dynamic data structure the can expand or shrink as needed
* Requires no extra space (memory efficient)
* Does not require a continuous block of memory like arrays

Drawbacks:

* Operations take O(N) time (Ex: Search)
* Tracking of pointers takes up additional memory


Node Implementation: 

```python
class Node(Generic[T]):
    def __init__(self, data: T = None, next_node: 'Node' = None):
        self.data = data
        self.next_node = next_node
```

Singly Linked List Implementation:

```python
from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T = None, next_node: 'Node' = None):
        self.data = data
        self.next_node = next_node


# Wikipedia: Singly linked lists contain nodes which have a data field as well as 'next' field, which points to the next
# node in line of nodes. Operations that can be performed on singly linked lists include insertion, deletion and
# traversal.


class SinglyLinkedList(Generic[T]):

    def __init__(self):
        self.__head = Node()

    def all_values(self) -> [T]:
        values = []
        node = self.__head.next_node

        while node:
            values.append(node.data)
            node = node.next_node

        return values

    # O(N)
    def append(self, data: T) -> None:
        node = Node(data)
        last_node = self.__head

        while last_node:
            if not last_node.next_node:
                break
            last_node = last_node.next_node
        last_node.next_node = node

    # O(N)
    def get(self, index: int) -> Optional[T]:
        current_node = self.__head.next_node
        count = 0

        while current_node:
            if count == index:
                break
            current_node = current_node.next_node
            count += 1
        if current_node is None or count != index:
            return None
        return current_node.data

    def insert(self, data: T, index: int) -> None:
        node = Node(data)
        current_node = self.__head
        count = 0
        while current_node:
            if count == index:
                next_node = current_node.next_node
                node.next_node = next_node
                current_node.next_node = node
                return
            current_node = current_node.next_node
            count += 1
        if count < index:
            IndexError('Index out of bounds')

    def remove(self, index: int) -> None:
        count = 0
        current_node = self.__head

        while current_node:
            if count == index:
                remove_node = current_node.next_node
                if remove_node and remove_node.next_node:
                    current_node.next_node = remove_node.next_node
                    return
                current_node.next_node = None
            current_node = current_node.next_node
            count += 1

    # O(N)
    def size(self) -> int:
        count = 0
        current_node = self.__head.next_node

        while current_node:
            count += 1
            current_node = current_node.next_node
        return count
```

## Doubly Linked List

[Wikipedia: Doubly Linked List](https://en.wikipedia.org/wiki/Doubly_linked_list): In a 'doubly linked list', each node 
contains, besides the next-node link, a second link field pointing to the 'previous' node in the sequence.

Doubly Linked List Node:

```python
class Node(Generic[T]):
    def __init__(self, data: T = None, previous_node: 'Node' = None, next_node: 'Node' = None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node
```

Implementation:

```python
class DoublyLinkedList(Generic[T]):

    def __init__(self):
        self.__head = Node()
        self.__tail = Node()

        self.__head.next_node = self.__tail
        self.__tail.previous_node = self.__head

    # O(N)
    def all_values(self) -> [T]:
        values = []
        node = self.__head.next_node

        while node is not self.__tail:
            values.append(node.data)
            node = node.next_node

        return values

    # O(1)
    def append(self, data: T):
        # Last <-> Tail --> Last <-> New <-> Tail
        node = Node(data)
        last_node = self.__tail.previous_node

        last_node.next_node = node
        node.previous_node = last_node

        node.next_node = self.__tail
        self.__tail.previous_node = node

    # O(N)
    def get_node(self, index: int) -> Optional[Node]:
        current_node = self.__head.next_node
        count = 0

        while current_node is not self.__tail:
            if count == index:
                return current_node
            current_node = current_node.next_node
            count += 1
        return None

    # O(N)
    def get(self, index: int) -> Optional[T]:
        node = self.get_node(index)
        if node:
            return node.data
        return None

    # O(N)
    def insert(self, data: T, index: int):
        node = Node(data)
        current_node: Node = self.get_node(index)
        
        if not current_node and index == 0:
            self.__head.next_node = node
            node.previous_node = self.__head
            node.next_node = self.__tail
            self.__tail.previous_node = node
            return

        if not current_node:
            raise IndexError("Index out of bounds")

        # Previous <-> Original --> Previous <-> New <-> Original
        current_node.previous_node.next_node = node
        node.previous_node = current_node.previous_node
        node.next_node = current_node
        current_node.previous_node = node

    # O(N)
    def remove(self, index: int) -> Optional[T]:
        node = self.get_node(index)
        if not node:
            return None

        # Previous <-> Node <-> Next --> Previous <-> Next
        node.previous_node.next_node = node.next_node
        node.next_node.previous_node = node.previous_node

        return node.data

    # O(N)
    def size(self) -> int:
        count = 0
        node = self.__head.next_node

        while node != self.__tail:
            count += 1
            node = node.next_node
        return count
```

## Circularly Linked List

In the last node of a list, the link field often contains a null reference, a special value used to indicate the lack of
further nodes. A less common convention is to make it point to the first node of the list; in that case the list is said
to be 'circular' or 'circularly linked'; otherwise it is said to be 'open' or 'linear'. It is a list where the last
pointer points to the first node.

This is more of an example. It can be optimized in a variety of ways depending on its intended usage.

```python
class CircularlyLinkedList(object):
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next_node = self._head

    @property
    def head(self) -> Node:
        return self._head

    @head.setter
    def head(self, node: Node):
        self._head = node
        if node:
            node.next_node = self._head

    def all_values(self) -> []:
        values = []
        node = self.head

        while node:
            values.append(node.data)
            node = node.next_node
            if node == self.head:
                break
        return values

    def append(self, node: Node):
        previous_node = self.head

        if not previous_node:
            self.head = node
            node.next_node = self.head
            return

        while previous_node.next_node != self.head:
            previous_node = previous_node.next_node

        next_node = previous_node.next_node
        previous_node.next_node = node
        node.next_node = next_node

    def remove(self, index: int):
        previous_node = self.head

        if not previous_node:
            raise IndexError("List is empty")

        if previous_node.next_node == self.head:
            self.head = None
            return

        if index == 0:
            previous_node.next_node = self.head.next_node
            self.head = previous_node.next_node
            return

        list_index = 1
        while previous_node.next_node is not self.head and list_index < index:
            previous_node = previous_node.next_node
            list_index += 1

        if list_index == index:
            next_node = previous_node.next_node
            previous_node.next_node = next_node.next_node
        else:
            raise IndexError

    def size(self) -> int:
        count = 0
        if not self.head:
            return count

        count += 1
        node = self.head.next_node

        while node and node != self.head:
            count += 1
            node = node.next_node
        return count
```

## Binary Tree

A Binary tree is a non-linear tree data structure with one "root" node. Each node has only two child nodes. These are
donated "left" and "right".

Further Reading - [Wikipedia: Binary Tree](https://en.wikipedia.org/wiki/Binary_tree)

```text
     Root
      / \
     L   R
    / \
   L   R
```

Binary Tree Node

```python
class BinaryTreeNode:

    def __init__(self, data, left_node=None, right_node=None):
        self._data = data
        self._left_node = left_node
        self._right_node = right_node
        
     # ... Getters and Setters #
```

Binary Tree

```python
class BinaryTree(object):

    def __init__(self, root: BinaryTreeNode = None):
        self._root = root

    @property
    def root(self) -> BinaryTreeNode:
        return self._root

    @root.setter
    def root(self, root: BinaryTreeNode):
        self._root = root
```

## Queue

A Queue is a FIFO (first in first out) data structure. The simplest analogy would be waiting in line.  

```text

Front             Back
    [1, 2, 3, 4] 
Remove values from the front and add new values to the back
Enqueue - Add new value to the back
Dequeue - Remove value from the front
```

Basic queue backed with a list. Not optimal since list has O(N) complexity for inserting and removing elements at the
beginning of the list

```python
class QueueList:

    T = TypeVar('T')

    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def dequeue(self) -> T:
        return self.queue.pop(0)

    def enqueue(self, element: T):
        self.queue.append(element)
```

Queue with Linked List

```python
class QueueLinkList(Generic[T]):
    """
    Queue backed by a doubly linked list
    """

    def __init__(self):
        self.linked_list = DoublyLinkedList()

    def __len__(self):
        return self.linked_list.size()

    # O(1)
    def dequeue(self) -> T:
        return self.linked_list.remove(0)

    # O(1)
    def enqueue(self, element: T):
        self.linked_list.append(element)
```

Circular Queue - Similar to linked-list in time complexity but uses an array to mimic the same functionality

```python
class CircularQueue(Generic[T]):

    def __init__(self, k: int):
        self.queue = [0] * k
        self.count = 0
        self.size = k
        self.head = 0

    def enqueue(self, value: T) -> bool:
        if self.isfull():
            return False
        tail = (self.head + self.count) % self.size
        self.queue[tail] = value
        self.count += 1
        return True

    def dequeue(self) -> bool:
        if self.isempty():
            return False
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def front(self) -> T:
        """
        Get the front item from the queue.
        """
        if self.isempty():
            return -1
        return self.queue[self.head]

    def rear(self) -> T:
        """
        Get the last item from the queue.
        """
        if self.isempty():
            return -1
        tail = (self.head + self.count - 1) % self.size
        return self.queue[tail]

    def isempty(self) -> bool:
        return self.count == 0

    def isfull(self) -> bool:
        return self.count == self.size
```

Deque (Built-in)

```python
from collections import deque

queue = deque()
queue.append(1)
queue.popleft() # 1
```

## Stack

A stack is a FIFO (first in first out) data structure. It can be backed by a list since append and pop are O(1)

```python
class StackList(Generic[T]):

    def __init__(self):
        self.__list = []

    def __len__(self):
        return len(self.__list)

    def push(self, data: T):
        self.__list.append(data)

    def pop(self, data: T):
        self.__list.pop(data)
```


## Trie

A Trie is a special form of a Nary tree. Typically, a trie is used to store strings. Each Trie node represents a string 
(a prefix). Each node might have several children nodes while the paths to different children nodes represent different 
characters. And the strings the child nodes represent will be the origin string represented by the node itself plus the 
character on the path. - Leetcode

Leetcode - Prefix Trie

```text
     head
     /  \
    a    b
   /    /  \
 am    ba  be
      /
    bad
```

Trie with arrays

```python
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
```

Trie with dictionary (Hash table)

```python
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
```

Trie like implementation with a flat dictionary (Hash table)

```python
class TrieWithFlatDictionary:
    """
    O(1) for accessing elements
    O(M * N) - Because multiple values of a key must be tracked (plus their associated True/False values)
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes: Dict[str: bool] = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        for index in range(1, len(word)):
            if self.nodes.get(word[:index]) is None:
                self.nodes[word[:index]] = False
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
```
