from typing import Optional
from singly_linked_lists.list_node import ListNode


def reverse_linked_list(head: ListNode) -> Optional[ListNode]:
    if not head:
        return None
    current_node: ListNode = head.next
    end = head
    new_list = head

    while current_node:
        next_node = current_node.next
        current_node.next = new_list
        new_list = current_node
        current_node = next_node
    end.next = None
    return new_list
