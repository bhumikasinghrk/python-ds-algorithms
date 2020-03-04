# Linked Lists

* [Linked List Cycle](#linked-list-cycle)

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