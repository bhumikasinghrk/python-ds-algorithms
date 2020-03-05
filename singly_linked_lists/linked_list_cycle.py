from typing import Optional, Set, TypeVar
from singly_linked_lists.list_node import ListNode

T = TypeVar('T')


# Time: O(N + K) -> O(N), Space: O(1)
def has_cycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False

    slow: ListNode = head
    fast: ListNode = head.next.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


# Time: O(N), Space: O(N)
def has_cycle_with_set(head: Optional[ListNode]) -> bool:
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
