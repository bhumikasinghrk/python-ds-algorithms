from typing import Optional, Set
from data_structures.list_node import ListNode


def detect_cycle(head: ListNode) -> Optional[ListNode]:
    # detect cycle
    if not head or not head.next:
        return None
    slow: ListNode = head
    fast: ListNode = head
    intersection: Optional[ListNode] = None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            intersection = slow
            break

    if not intersection:
        return intersection

    # detect intersection
    node = head
    while node != intersection:
        node = node.next
        intersection = intersection.next

    return intersection


def detect_cycle_with_set(head: ListNode) -> Optional[ListNode]:
    visited_nodes: Set[ListNode] = set()

    node = head

    while node:
        if node and node in visited_nodes:
            return node
        visited_nodes.add(node)
        node = node.next
    return None
