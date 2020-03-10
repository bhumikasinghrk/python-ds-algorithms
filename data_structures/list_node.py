from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class ListNode(Generic[T]):
    def __init__(self, val: T):
        self.val: T = val
        self.next: Optional[ListNode] = None
