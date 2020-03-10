from singly_linked_lists.reverse_linked_list_recursive import reverse_linked_list_recursive
from data_structures.list_node import ListNode


def test_reverse_linked_list():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert get_list_values(reverse_linked_list_recursive(head)) == [3, 2, 1]

    head = ListNode(1)
    head.next = ListNode(2)
    assert get_list_values(reverse_linked_list_recursive(head)) == [2, 1]

    head = ListNode(1)
    assert get_list_values(reverse_linked_list_recursive(head)) == [1]


def get_list_values(head: ListNode):
    node = head
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values
