from typing import Optional
from singly_linked_lists.list_node import ListNode


def add_two_numbers(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
    node1 = head1
    node2 = head2
    dummy_node = ListNode(0)
    result = dummy_node
    carry = 0
    while node1 or node2:
        val1 = 0
        val2 = 0
        if node1:
            val1 = node1.val
            node1 = node1.next
        if node2:
            val2 = node2.val
            node2 = node2.next

        total = val1 + val2 + carry
        carry = int(total / 10)
        result.next = ListNode(total % 10)
        result = result.next

    if carry > 0:
        result.next = ListNode(carry)

    return dummy_node.next
