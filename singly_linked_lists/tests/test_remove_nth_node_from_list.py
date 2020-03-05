from singly_linked_lists.remove_nth_node_from_list import remove_nth_from_end
from singly_linked_lists.list_node import ListNode


def test_remove_nth_from_end():
    head = ListNode(1)
    assert remove_nth_from_end(head, 1) is None

    head = ListNode(1)
    head.next = ListNode(2)
    assert remove_nth_from_end(head, 2).val == 2
    assert remove_nth_from_end(head, 1).val == 1

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    assert remove_nth_from_end(head, 2).next.next.val == 4
