from data_structures.list_node import ListNode
from singly_linked_lists.palindrome_linked_list import is_palindrome


def test_is_palindrome():
    head = ListNode(1)
    assert is_palindrome(head)

    head.next = ListNode(2)
    assert not is_palindrome(head)

    head.next.next = ListNode(1)
    assert is_palindrome(head)
