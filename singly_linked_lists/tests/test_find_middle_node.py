from singly_linked_lists.find_middle_node import find_middle_node
from data_structures.list_node import ListNode


def test_find_middle_node():
    head = ListNode(1)
    assert find_middle_node(head) == head

    head.next = ListNode(2)
    assert find_middle_node(head) == head

    # 1, 2, 3
    head.next.next = ListNode(3)
    assert find_middle_node(head) == head.next

    head.next.next.next = ListNode(4)
    assert find_middle_node(head) == head.next
