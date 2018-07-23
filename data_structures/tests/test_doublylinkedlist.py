from data_structures.doublylinkedlist import *

empty_list = DoublyLinkedList()
one_node_list = DoublyLinkedList()
one_node_list.append(Node(5))


def test_init():
    assert one_node_list.size() == 1
    assert one_node_list.get_value(0) == 5


def test_init_none():
    assert not empty_list.get_value(0)
    assert empty_list.size() == 0


def test_allvalues():
    doubly_linked_list = get_multi_node_list()
    assert doubly_linked_list.allvalues() == [5, 2, 4, 1]


def test_append_empty():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(Node(1))
    assert doubly_linked_list.size() == 1
    assert doubly_linked_list.get_value(0) == 1


def test_append():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(Node(3))
    doubly_linked_list.append(Node(4))
    assert doubly_linked_list.size() == 2
    assert doubly_linked_list.get_value(0) == 3
    assert doubly_linked_list.get_value(1) == 4


def test_get_empty():
    assert not empty_list.get_value(0)


def test_get_invalid():
    assert not get_multi_node_list().get_value(10)


def test_get_valid():
    assert get_multi_node_list().get_value(3) == 1


def test_get_node():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(Node(3), 0)
    assert doubly_linked_list.get_node(0).data == 3


def test_insert_empty():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(Node(3), 0)
    assert doubly_linked_list.size() == 1
    assert doubly_linked_list.get_value(0) == 3


def test_insert_head():
    doubly_linked_list = get_multi_node_list()
    doubly_linked_list.insert(Node(32), 0)
    assert doubly_linked_list.size() == 5
    assert doubly_linked_list.get_value(0) == 32
    assert doubly_linked_list.get_value(1) == 5


def test_insert_middle():
    doubly_linked_list = get_multi_node_list()
    doubly_linked_list.insert(Node(11), 1)
    assert doubly_linked_list.size() == 5
    assert doubly_linked_list.get_value(0) == 5
    assert doubly_linked_list.get_value(1) == 11
    assert doubly_linked_list.get_value(2) == 2


def test_insert_tail():
    doubly_linked_list = get_multi_node_list()
    doubly_linked_list.insert(Node(22), 3)
    assert doubly_linked_list.size() == 5
    assert doubly_linked_list.get_value(3) == 22
    assert doubly_linked_list.get_value(4) == 1


def test_remove_empty():
    doubly_linked_list = DoublyLinkedList()
    assert not doubly_linked_list.remove(0)


def test_remove():
    doubly_linked_list = get_multi_node_list()
    assert doubly_linked_list.remove(0) == 5
    assert doubly_linked_list.size() == 3

    assert doubly_linked_list.remove(2) == 1
    assert doubly_linked_list.size() == 2


def test_size():
    assert empty_list.size() == 0
    assert one_node_list.size() == 1
    assert get_multi_node_list().size() == 4


# Helpers


def get_multi_node_list() -> DoublyLinkedList:
    multi_node_list = DoublyLinkedList()
    multi_node_list.append(Node(5))
    multi_node_list.append(Node(2))
    multi_node_list.append(Node(4))
    multi_node_list.append(Node(1))
    return multi_node_list
