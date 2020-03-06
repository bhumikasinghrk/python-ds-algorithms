from typing import Optional
from singly_linked_lists.find_middle_node import find_middle_node
from singly_linked_lists.list_node import ListNode
from singly_linked_lists.reverse_linked_list import reverse_linked_list


def is_palindrome(head: Optional[ListNode]) -> bool:
    if not head:
        return False

    # Find midway
    first_half_end = find_middle_node(head)

    # reverse second half
    second_half_head = reverse_linked_list(first_half_end.next)

    # first half should match second half
    palindrome = True
    first_pointer = head
    second_pointer = second_half_head

    while palindrome and second_pointer:
        if first_pointer.val != second_pointer.val:
            return False
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    # restore list
    first_half_end.next = reverse_linked_list(second_half_head)
    return palindrome
