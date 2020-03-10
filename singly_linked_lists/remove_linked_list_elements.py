from typing import Optional
from data_structures.list_node import ListNode


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy_node: ListNode = ListNode(0)
    dummy_node.next = head

    previous: ListNode = dummy_node
    current: Optional[ListNode] = head

    while current:
        if current.val == val:
            previous.next = current.next
            current = current.next
        else:
            previous = current
            current = current.next

    return dummy_node.next
