from singly_linked_lists.linked_list_cycle import ListNode, has_cycle, has_cycle_with_set


def test_has_cycle():
    assert not has_cycle(None)
    assert not has_cycle(ListNode(1))

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    assert has_cycle(head)

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    assert not has_cycle(head2)


def test_has_cycle_with_set():
    assert not has_cycle_with_set(None)
    assert not has_cycle_with_set(ListNode(1))

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    assert has_cycle_with_set(head)

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    assert not has_cycle_with_set(head2)
