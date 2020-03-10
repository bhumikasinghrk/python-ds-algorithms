from typing import Optional
from data_structures.list_node import ListNode


def find_middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow
