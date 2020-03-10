from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class ListNode(Generic[T]):
    def __init__(self, val: T, previous_node: Optional['ListNode'] = None, next_node: Optional['ListNode'] = None):
        self.value: T = val
        self.previous: Optional[ListNode] = previous_node
        self.next: Optional[ListNode] = next_node
