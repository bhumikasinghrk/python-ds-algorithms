from singly_linked_lists.reverse_linked_list import reverse_linked_list
from data_structures.list_node import ListNode
from test_helpers.test_helpers import get_list_values


def test_reverse_linked_list():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert get_list_values(reverse_linked_list(head)) == [3, 2, 1]

    head = ListNode(1)
    head.next = ListNode(2)
    assert get_list_values(reverse_linked_list(head)) == [2, 1]

    head = ListNode(1)
    assert get_list_values(reverse_linked_list(head)) == [1]
