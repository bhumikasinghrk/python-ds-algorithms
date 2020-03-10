from doubly_linked_list.flatten_doubly_linked_lists import flatten, flatten_iterative
from doubly_linked_list.flatten_doubly_linked_lists import Node
from test_helpers.test_helpers import get_list_values


def test_flatten():
    head = Node(1, None, None, None)
    child = Node(3, None, None, None)
    child.next = Node(4, child, None, None)
    head.next = Node(2, head, None, child)
    head.next.next = Node(5, head.next, None, None)

    assert get_list_values(flatten(head)) == [1, 2, 3, 4, 5]
    assert get_list_values(flatten_iterative(head)) == [1, 2, 3, 4, 5]
