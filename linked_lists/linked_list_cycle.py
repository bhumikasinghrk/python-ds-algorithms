from typing import Generic, Optional, Set, TypeVar

T = TypeVar('T')


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


class ListNode(Generic[T]):
    def __init__(self, val: T):
        self.val: T = val
        self.next: Optional[ListNode] = None
