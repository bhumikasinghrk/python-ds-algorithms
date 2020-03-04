from typing import Optional, Set
from linked_lists.list_node import ListNode


def get_intersection_node_with_set(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    nodes: Set[ListNode] = set()
    node_a: ListNode = head_a
    node_b: ListNode = head_b

    while node_a or node_b:
        if node_a:
            if node_a in nodes:
                return node_a
            nodes.add(node_a)
            node_a = node_a.next

        if node_b:
            if node_b in nodes:
                return node_b
            nodes.add(node_b)
            node_b = node_b.next

    return None
