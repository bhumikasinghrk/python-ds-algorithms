from singly_linked_lists.detect_cycle import detect_cycle, detect_cycle_with_set
from singly_linked_lists.list_node import ListNode


def test_detect_cycle():
    assert detect_cycle(ListNode(1)) is None

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert detect_cycle(head) is None

    head = ListNode(1)
    head.next = head
    assert detect_cycle(head) == head

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    assert detect_cycle(head) is head.next


def test_detect_cycle_with_set():
    assert detect_cycle_with_set(ListNode(1)) is None

    head = ListNode(1)
    head.next = head
    assert detect_cycle_with_set(head) == head

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    assert detect_cycle_with_set(head) == head.next
