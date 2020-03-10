from singly_linked_lists.add_two_numbers import add_two_numbers
from data_structures.list_node import ListNode
from test_helpers.test_helpers import get_list_values


def test_add_two_numbers():
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)

    head2 = None

    assert get_list_values(add_two_numbers(head1, head2)) == [1, 2, 3]

    head1 = ListNode(5)
    head2 = ListNode(5)
    assert get_list_values(add_two_numbers(head1, head2)) == [0, 1]

    head1.next = ListNode(2)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)
    assert get_list_values(add_two_numbers(head1, head2)) == [0, 6, 4]
