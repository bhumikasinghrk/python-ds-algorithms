from typing import Optional
from data_structures.list_node import ListNode


def reverse_linked_list_recursive(head: ListNode) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
