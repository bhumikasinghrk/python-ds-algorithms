from typing import Optional
from data_structures.list_node import ListNode


def rotate_list(head: Optional[ListNode], amount: int) -> Optional[ListNode]:
    if not head:
        return None

    if not head.next:
        return head

    current = head
    number = 1

    while current.next:
        number += 1
        current = current.next
    current.next = head
    current = head

    for _ in range((number - amount) % number - 1):
        current = current.next

    new_head = current.next
    current.next = None
    return new_head
