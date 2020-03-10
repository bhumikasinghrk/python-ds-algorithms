from typing import Optional
from data_structures.list_node import ListNode


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    if not head_a or not head_b:
        return None

    node_a: ListNode = head_a
    node_b: ListNode = head_b

    while node_a != node_b:
        node_a = node_a.next
        node_b = node_b.next

        if node_a is None and node_b is None:
            return None

        if node_a is None:
            node_a = head_b

        if node_b is None:
            node_b = head_a

    return node_a
