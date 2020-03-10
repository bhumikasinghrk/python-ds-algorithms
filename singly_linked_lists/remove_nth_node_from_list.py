from typing import Optional
from data_structures.list_node import ListNode


def remove_nth_from_end(head: ListNode, nth: int) -> Optional[ListNode]:
    dummy: ListNode = ListNode(0)
    dummy.next = head
    previous: ListNode = dummy
    lead: ListNode = dummy

    # Move lead forward
    for _ in range(nth + 1):
        lead = lead.next

    # Move through list until lead is None
    while lead:
        previous = previous.next
        lead = lead.next

    # Delete Node by relinking nodes or reassigning head
    previous.next = previous.next.next
    return dummy.next
