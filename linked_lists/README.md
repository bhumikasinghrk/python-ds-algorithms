# Linked Lists

* [Detect Cycle](#detect-cycle)
* [Linked List Cycle](#linked-list-cycle)

## Detect Cycle

Given a linked list, return the node where the cycle begins. If there is no cycle, return `None`.

Solution with slow/fast

Time: O(N), Space: O(1)

```python
def detect_cycle(head: ListNode) -> Optional[ListNode]:
    # detect cycle
    if not head or not head.next:
        return None
    slow: ListNode = head
    fast: ListNode = head
    intersection: Optional[ListNode] = None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            intersection = slow
            break

    if not intersection:
        return intersection

    # detect intersection
    node = head
    while node != intersection:
        node = node.next
        intersection = intersection.next

    return intersection
```

Solution with set

Time: O(N), Space: O(1)

```python
def detect_cycle_with_set(head: ListNode) -> Optional[ListNode]:
    visited_nodes: Set[ListNode] = set()

    node = head

    while node:
        if node and node in visited_nodes:
            return node
        visited_nodes.add(node)
        node = node.next
    return None
```

## Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

```python
# Time: O(N + K) -> O(N), Space: O(1)
def has_cycle(head: Optional['ListNode']) -> bool:
    if not head or not head.next:
        return False

    slow: ListNode = head
    fast: ListNode = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
```

Solution with set (less optimal)

```python
# Time: O(N), Space: O(N)
def has_cycle_with_set(head: Optional['ListNode']) -> bool:
    if not head or not head.next:
        return False

    node_set: Set[ListNode] = set()
    node: ListNode = head

    while node:
        if not node or node in node_set:
            return True
        node_set.add(node)
        node = node.next
    return False
```