from data_structures.list_node import ListNode
from singly_linked_lists.rotate_list import rotate_list
from test_helpers.test_helpers import get_list_values


def test_rotate_list():
    head = None
    assert rotate_list(head, 1) is None

    head = ListNode(1)
    assert get_list_values(rotate_list(head, 1)) == [1]
    assert get_list_values(rotate_list(head, 3)) == [1]

    head.next = ListNode(2)
    assert get_list_values(rotate_list(head, 1)) == [2, 1]

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    assert get_list_values(rotate_list(head, 2)) == [4, 5, 1, 2, 3]
