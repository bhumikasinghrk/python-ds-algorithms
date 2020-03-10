from singly_linked_lists.copy_list_with_random_pointer import Node, copy_random_list


def test_copy_random_list():
    head = Node(1)
    head.next = Node(2)
    head.next.random = head
    head.next.next = Node(3)
    head.next.next.random = head
    new_head = copy_random_list(head)
    assert new_head.value == 1
    assert new_head.next.value == 2
    assert new_head.next.next.value == 3
    assert new_head.next.random == new_head
    assert new_head.next.next.random == new_head

