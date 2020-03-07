from typing import Optional
from singly_linked_lists.list_node import ListNode


def merge_two_lists(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
    if not head1 and not head2:
        return None

    node1 = head1
    node2 = head2
    dummy_node = ListNode(0)
    current_node = dummy_node

    while node1 and node2:
        if node1.val <= node2.val:
            current_node.next = node1
            node1 = node1.next
        else:
            current_node.next = node2
            node2 = node2.next
        current_node = current_node.next

    if node1:
        current_node.next = node1
    if node2:
        current_node.next = node2

    return dummy_node.next
