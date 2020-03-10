from typing import Optional
from data_structures.list_node import ListNode


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head

    return head
