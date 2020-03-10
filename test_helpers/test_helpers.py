from typing import TypeVar
from data_structures.list_node import ListNode

T = TypeVar('T')


def get_list_values(head: T):
    node = head
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def get_cyclic_list_values(head: ListNode):
    if not head:
        return []

    values = [head.val]
    node = head.next

    while node is not head:
        values.append(node.val)
        node = node.next
    return values
