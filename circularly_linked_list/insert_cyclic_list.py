from typing import Optional
from data_structures.list_node import ListNode


def insert(head: Optional[ListNode], value: int) -> Optional[ListNode]:
    if not head:
        cyclic_list = ListNode(value)
        cyclic_list.next = cyclic_list
        return cyclic_list

    previous = head
    node = head.next

    while node:
        if previous.val <= value <= node.val:
            new_node = ListNode(value)
            previous.next = new_node
            new_node.next = node
            return head
        if previous.val > node.val:
            if value >= previous.val or value <= node.val:
                new_node = ListNode(value)
                previous.next = new_node
                new_node.next = node
                return head

        previous = node
        node = node.next

        if previous == head:
            break

    new_node = ListNode(value)
    previous.next = new_node
    new_node.next = node

    return head
