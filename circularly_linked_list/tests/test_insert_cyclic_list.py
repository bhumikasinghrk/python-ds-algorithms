from circularly_linked_list.insert_cyclic_list import insert
from data_structures.list_node import ListNode
from test_helpers.test_helpers import get_cyclic_list_values


def test_insert():
    head = None
    assert get_cyclic_list_values(insert(head, 1)) == [1]

    head = ListNode(1)
    head.next = head
    assert get_cyclic_list_values(insert(head, 2)) == [1, 2]

    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    head.next.next.next = head
    assert get_cyclic_list_values(insert(head, 2)) == [3, 4, 1, 2]
