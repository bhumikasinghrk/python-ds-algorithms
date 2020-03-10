from typing import Optional
from data_structures.list_node import ListNode


def reverse_linked_list(head: ListNode) -> Optional[ListNode]:
    if not head:
        return None
    previous: Optional[ListNode] = None
    current: Optional[ListNode] = head

    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp

    return previous
