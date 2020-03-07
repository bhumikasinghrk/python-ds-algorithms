from singly_linked_lists.merge_two_sorted_lists import merge_two_lists
from singly_linked_lists.list_node import ListNode
from test_helpers.test_helpers import get_list_values


def test_merge_two_lists():

    list1 = ListNode(1)
    assert get_list_values(merge_two_lists(list1, None)) == [1]

    list2 = ListNode(1)
    assert get_list_values(merge_two_lists(list1, list2)) == [1, 1]

    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    assert get_list_values(merge_two_lists(list1, list2)) == [1, 1, 2, 3, 4, 4]