from linked_lists.intersection_two_linked_lists import get_intersection_node
from linked_lists.list_node import ListNode


def test_get_intersection_node():
    head1 = ListNode(1)
    head1.next = ListNode(2)

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    assert get_intersection_node(head1, head2) is None

    head1 = ListNode(1)
    head2 = head1
    assert get_intersection_node(head1, head2) is head1

    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head2 = ListNode(1)
    head2.next = head1.next.next
    assert get_intersection_node(head1, head2) is head1.next.next
