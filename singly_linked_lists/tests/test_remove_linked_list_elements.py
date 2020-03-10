from singly_linked_lists.remove_linked_list_elements import remove_elements
from data_structures.list_node import ListNode
from test_helpers.test_helpers import get_list_values


def test_remove_elements():
    assert remove_elements(None, 1) is None

    head = ListNode(1)
    assert remove_elements(head, 1) is None
    assert remove_elements(head, 2) is head

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    assert get_list_values(remove_elements(head, 2)) == [1, 3]
