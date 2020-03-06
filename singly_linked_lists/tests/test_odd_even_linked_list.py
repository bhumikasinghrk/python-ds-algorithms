from singly_linked_lists.list_node import ListNode
from singly_linked_lists.odd_even_linked_list import odd_even_list
from test_helpers.test_helpers import get_list_values


def test_odd_even_linked_list():
    head = ListNode(1)
    assert odd_even_list(head) == head

    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    assert get_list_values(odd_even_list(head)) == [1, 3, 5, 2, 4]
